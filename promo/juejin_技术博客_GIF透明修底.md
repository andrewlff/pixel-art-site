# 用 Python 修 AI 生成 GIF 的后段帧露底：三次尝试，两端代码

> 掘金技术博客草稿 · 2026-11-21 · 未发布（掘金发文需本人登录扫码）

## 背景

用 AI 生成一套 6 帧像素攻击动画，导出成 GIF。第一帧干净，往后几帧画布边缘和角色周围就开始出现底色残留——浅绿色的一圈、偶尔一块纯黑底板，透明区变成不透明。肉眼看着"只是有点脏"，丢进 Godot / Unity 里就是一圈白边加一张黑底。

这类问题的根源不在生成模型，而在整条链路的透明天真假设：**模型按 RGB 图生成，谁也没告诉它"这一块应该 alpha=0"**。所以修底不是调参，是一次图像分割。

下面是我在这套 8 角色 × 6 帧（48 帧）素材上做的三次尝试，以及最后跑通的做法。数据都是脚本实测，可复现。

## 第一版：边框中位色估底色 —— 错得最干脆

最直觉的做法：取画布四条边的像素中位色，当作"背景色"，然后把全图等于这个色的像素打成透明。

问题一眼可见：**GIF 帧的四角本来就是 `(0,0,0,0)`**，中位色估出来是纯黑。于是一套浅绿底的素材被"识别"成黑底，一个像素都不动；再叠上容差，角色暗部反而被一起吃掉。

教训：透明 GIF 的边缘像素值没有语义，拿它当底色基准属于用错数据源。

## 第二版：浅色 + 与画布边界连通

换成两条判据同时成立：像素是"浅色低饱和"（浅绿、浅蓝、近白都覆盖），**并且**从画布边界能连通到它。

```python
def pale_mask(rgb):
    r, g, b = rgb[...,0].astype(np.int16), rgb[...,1].astype(np.int16), rgb[...,2].astype(np.int16)
    mn = np.minimum(np.minimum(r, g), b)
    mx = np.maximum(np.maximum(r, g), b)
    return (mn >= 185) & ((mx - mn) <= 52) & (g >= r) & (g >= b - 45)
```

这一版在 6 个角色上直接成功了，但 `sword_boy` 翻车：角色身上有约 1800 个浅色像素块被非浅色像素（深色描边）完整包住，从边界根本够不到。它们不算背景，可也没被算进角色——判据本身是死的，连通性只是让它更保守。

## 第三版：把"角色"定义为最大的非浅色连通体

换思路：不猜背景，直接找角色。

1. 非浅色、非纯黑、`alpha>10` 的像素构成候选网格；
2. 在 1/4 降采样后的网格上，按 8×8 块统计候选密度，取密度最高的 5 块**分别**当种子做连通生长，谁长出来的面积最大，谁就是角色轮廓；
3. 被轮廓包住、够不到画布边界的透明区当作"角色内部洞"补回来——否则衣服高光、围巾会被挖空；
4. 紧贴角色轮廓的纯黑描边保留 2px，避免角色被削掉一圈。

降采样 + 多次种子是这一版的关键。少了它，种子很容易落在火球的零散光效像素上，角色只被认出一小块；只用一个种子，遇到 `mage_fireball` 那种"炸开的特效比角色本体还亮"的帧就会跑偏。

```python
# 种子：8×8 块密度前 5 名各试一次，取连通体最大者
dens = small[:h8*blk, :w8*blk].reshape(h8, blk, w8, blk).sum(axis=(1, 3))
cand = np.argsort(dens.ravel())[::-1][:5]
best_comp, best_size = None, -1
for idx in cand:
    sy, sx = divmod(int(idx), w8)
    seedmask = np.zeros_like(small); seedmask[sy*blk + blk//2, sx*blk + blk//2] = True
    comp = grow(small, seedmask)          # 8 邻域生长，mask 限界
    if int(comp.sum()) > best_size:
        best_comp, best_size = comp, int(comp.sum())
```

纯黑底板（`alchemist` 后段帧出现过）在这一版里被单独处理：`near_black = rgb.max(axis=2) <= 6`，先排除出候选，再只在角色轮廓 2px 范围内回补——这样黑底不会被认成角色，描边又不会丢。

## 另一个坑：RGBA 直接存 GIF，透明区会变黑

分割做对了，写出文件还有第二道坎。`Image.save(..., save_all=True)` 直接吃 RGBA 帧，Pillow 会给透明区填黑、写成不透明。

正确做法是显式调色板 + 透明索引：

```python
def save_alpha_gif(frames, path, durs, loop):
    pal = frames[0].convert("RGB").quantize(colors=255, method=Image.MEDIANCUT)
    pal_bytes = pal.getpalette()
    while len(pal_bytes) < 768:
        pal_bytes += [0, 0, 0]
    pf = []
    for fr in frames:
        p = fr.convert("RGB").quantize(palette=pal, dither=Image.Dither.NONE)
        arr = np.array(p).copy()
        arr[np.array(fr)[..., 3] < 10] = 255          # alpha<10 → 索引 255
        img = Image.fromarray(arr, "P")
        img.putpalette(pal_bytes[:765] + [0, 0, 0])
        pf.append(img)
    pf[0].save(path, save_all=True, append_images=pf[1:], duration=durs, loop=loop,
               transparency=255, disposal=2, optimize=False)
```

要点三条：**所有帧共用一个调色板**（否则帧间颜色跳变）、**`transparency=255` 指向预留的透明索引**、**`disposal=2`** 保证每帧重绘前清背景。`dither=NONE` 也别省，像素画被抖动噪点毁掉是常事。

## 结果

48 帧（8 角色 × 6 帧），残留率口径＝不透明区里"偏绿"像素占比（`G>200 且 G−R>12 且 G−B>12`，抽样步长 6）：**平均 8.25% → 0.36%，最坏一帧 49.6% → 0.4%**。所有数字以"重新读回修复后的 GIF"为准，不是内存里的中间结果——分割对了、写出错了的情况，只有回读才看得出来。

踩坑留下的两个已知瑕疵，一并记在这：`dragon_baby` 第 5 帧仍有 9.1% 边缘抗锯齿残留（再放宽阈值会吃掉角色浅色部位，暂时留着）；`sword_boy` 本身是深色剪影，暗底上几乎不可见——这是素材特性，不是修底的错。

## 小结

- 别拿画布边缘像素当底色基准，透明 GIF 的四角是 `(0,0,0,0)`
- 判据式分割（"什么是背景"）会在被包围的浅色块上失败；连通体式分割（"什么是角色"）更稳
- 种子一定要多点试，特效爆开的帧上单种子必偏移
- 写 GIF 的透明是调色板 + 索引 + disposal 三件事，不是打个 `RGBA` 就完事

脚本在 `D:\pixel-art-dashboard\xiaohongshu_20261118\fix_gifs.py`，依赖只有 Pillow + numpy；主仓那条零依赖管线还没并入这套逻辑，是下一步的事。

仓库：

- github.com/andrewlff/pixel-art-action-frames
- github.com/andrewlff/godot-pixel-batch-tool
- github.com/andrewlff/unity-pixel-batch-tool

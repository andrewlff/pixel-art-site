"""修 GIF 后段帧露底（第三版 · 连通体法）

为什么前两版不行：
- v1 用边框中位色估底色 → 四角是 (0,0,0,0)，估出黑色，完全错；
- v2 用“浅色像素 + 与画布边界连通” → sword_boy 有约 1800 个浅色块被非浅色像素包住，够不到边界。
本版改为：把“非浅色连通体”里最大的那块当角色轮廓，其余一律透明；
角色内部被包住的透明洞再补回来（避免衣服/高光被挖空）。

原素材只读；输出 fixed_gifs\<role>\<role>_attack_alpha.gif
"""
import os
import numpy as np
from PIL import Image, ImageSequence

BASE = r"C:\Users\SHAN\Doubao\chats\2026-09-17\new-chat-9\attack_frames"
OUT = r"D:\pixel-art-dashboard\xiaohongshu_20261118\fixed_gifs"
os.makedirs(OUT, exist_ok=True)

ROLES = ["fox_girl", "elf_archer", "dragon_baby", "mage_fireball",
         "sword_boy", "alchemist", "rogue_dagger", "dwarf_warrior"]
DS = 4
MAX_IT = 400


def green_pct(rgb, alpha):
    r = rgb[..., 0].astype(np.int16); g = rgb[..., 1].astype(np.int16); b = rgb[..., 2].astype(np.int16)
    green = (g > 200) & (g - r > 12) & (g - b > 12)
    sub_g = green[::6, ::6]; sub_o = (alpha > 10)[::6, ::6]
    tot = sub_o.sum()
    return 0.0 if tot == 0 else float((sub_g & sub_o).sum()) / float(tot) * 100


def pale_mask(rgb):
    """浅色低饱和（浅绿、浅蓝、近白四种底板都覆盖）"""
    r, g, b = rgb[..., 0].astype(np.int16), rgb[..., 1].astype(np.int16), rgb[..., 2].astype(np.int16)
    mn = np.minimum(np.minimum(r, g), b)
    mx = np.maximum(np.maximum(r, g), b)
    return (mn >= 185) & ((mx - mn) <= 52) & (g >= r) & (g >= b - 45)


def pool(mask, ds=DS):
    h, w = mask.shape
    hh, ww = h // ds, w // ds
    return mask[:hh * ds, :ww * ds].reshape(hh, ds, ww, ds).any(axis=(1, 3))


def unpool(small, shape, ds=DS):
    h, w = shape
    hh, ww = small.shape
    up = np.kron(small, np.ones((ds, ds), bool))
    full = np.zeros(shape, bool)
    full[:hh * ds, :ww * ds] = up
    return full


def grow(grid, seeds, limit=MAX_IT, conn8=True):
    cur = seeds & grid
    if not cur.any():
        return cur
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if conn8:
        steps += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for _ in range(limit):
        nxt = cur.copy()
        for dy, dx in steps:
            nxt |= np.roll(np.roll(cur, dy, 0), dx, 1)
        nxt &= grid
        if nxt.sum() == cur.sum():
            break
        cur = nxt
    return cur


def character_mask(rgba):
    rgb = rgba[..., :3]
    alpha = rgba[..., 3]
    near_black = rgb.max(axis=2) <= 6          # 纯黑底板（alchemist 后段帧出现）
    nonpale = (~pale_mask(rgb)) & (~near_black) & (alpha > 10)
    if not nonpale.any():
        return np.zeros_like(alpha, bool), np.zeros_like(alpha, bool)
    small = pool(nonpale)
    if not small.any():
        return np.zeros_like(alpha, bool), np.zeros_like(alpha, bool)

    # 种子：在 1/4 网格上再按 8×8 块统计“非浅色密度”，取密度最高的几块分别试，
    # 防止种子落在零散特效像素上把角色只认出一小块
    blk = 8
    hh, ww = small.shape
    h8, w8 = hh // blk, ww // blk
    dens = small[:h8 * blk, :w8 * blk].reshape(h8, blk, w8, blk).sum(axis=(1, 3))
    flat = dens.ravel()
    cand = np.argsort(flat)[::-1][:5]
    best_comp, best_size = None, -1
    for idx in cand:
        sy, sx = divmod(int(idx), w8)
        seedmask = np.zeros_like(small)
        seedmask[sy * blk + blk // 2, sx * blk + blk // 2] = True
        comp = grow(small, seedmask)
        size = int(comp.sum())
        if size > best_size:
            best_comp, best_size = comp, size
    comp = best_comp
    char = unpool(comp, alpha.shape) & nonpale

    # 角色内部封闭的浅色洞（衣服/高光/围巾）补回来：只看“够不到画布边界”的透明区
    outside_grid = ~comp
    border = np.zeros_like(small, bool)
    border[0, :] = outside_grid[0, :]
    border[-1, :] = outside_grid[-1, :]
    border[:, 0] = outside_grid[:, 0]
    border[:, -1] = outside_grid[:, -1]
    outside = grow(outside_grid, border)
    holes = unpool(~outside & ~comp, alpha.shape)

    # 轮廓回补：紧贴角色的纯黑像素（描边）留 2px，避免角色被削掉一圈
    core = char | holes
    rim = core.copy()
    for _ in range(2):
        rim = rim | np.roll(rim, 1, 0) | np.roll(rim, -1, 0) | np.roll(rim, 1, 1) | np.roll(rim, -1, 1)
    rim = (rim & near_black & (alpha > 10)) | core
    return core, holes | (rim & ~core)


def save_alpha_gif(frames, path, durs, loop):
    """显式调色板 + 透明索引写 GIF：直接存 RGBA 会把透明区变成不透明黑"""
    pal = frames[0].convert("RGB").quantize(colors=255, method=Image.MEDIANCUT)
    pal_bytes = pal.getpalette()
    while len(pal_bytes) < 768:
        pal_bytes += [0, 0, 0]
    pf = []
    for fr in frames:
        p = fr.convert("RGB").quantize(palette=pal, dither=Image.Dither.NONE)
        arr = np.array(p).copy()
        arr[np.array(fr)[..., 3] < 10] = 255
        img = Image.fromarray(arr, "P")
        img.putpalette(pal_bytes[:765] + [0, 0, 0])
        pf.append(img)
    pf[0].save(path, save_all=True, append_images=pf[1:], duration=durs, loop=loop,
               transparency=255, disposal=2, optimize=False)


rows = []
for role in ROLES:
    src = os.path.join(BASE, role, f"{role}_attack.gif")
    gif = Image.open(src)
    frames, durs = [], []
    for fr in ImageSequence.Iterator(gif):
        frames.append(fr.convert("RGBA").copy())
        durs.append(fr.info.get("duration", gif.info.get("duration", 130)))
    loop = gif.info.get("loop", 0)

    fixed, before = [], []
    for fr in frames:
        rgba = np.array(fr)
        alpha_old = rgba[..., 3].copy()
        before.append(green_pct(rgba[..., :3], alpha_old))
        char, holes = character_mask(rgba)
        keep = char | holes
        rgba2 = rgba.copy()
        rgba2[..., 3] = np.where(keep, alpha_old, 0)
        fixed.append(Image.fromarray(rgba2, "RGBA"))

    dst_dir = os.path.join(OUT, role)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, f"{role}_attack_alpha.gif")
    save_alpha_gif(fixed, dst, durs, loop)

    # 一律以“重新读回文件”为准
    back = Image.open(dst)
    after, removed = [], []
    for fr in ImageSequence.Iterator(back):
        rgba = np.array(fr.convert("RGBA"))
        after.append(green_pct(rgba[..., :3], rgba[..., 3]))
        removed.append(100.0 * float((rgba[..., 3] < 10).mean()))

    rows.append((role, before, after, removed, os.path.getsize(dst)))

print(f"{'role':<15}{'修复前 每帧%':<32}{'修复后 每帧%':<28}{'清掉面积%':<26}size")
for role, before, after, removed, size in rows:
    print(f"{role:<15}{str([round(v,1) for v in before]):<32}{str([round(v,1) for v in after]):<28}"
          f"{str([round(v,1) for v in removed]):<26}{size}")

all_before = np.array([v for r in rows for v in r[1]])
all_after = np.array([v for r in rows for v in r[2]])
print("\n汇总：48 帧 · 修复前平均残留 %.2f%%、最高 %.1f%% → 修复后平均 %.2f%%、最高 %.1f%%"
      % (all_before.mean(), all_before.max(), all_after.mean(), all_after.max()))

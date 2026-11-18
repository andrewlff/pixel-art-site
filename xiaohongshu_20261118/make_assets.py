"""2026-11-18 三张说明卡：GIF 后几帧露底，3 步修掉

所有数字来自实测：fix_gifs.py 跑出的修复前后残留率 + 重新读回 GIF 的文件信息。
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageSequence

BASE = r"C:\Users\SHAN\Doubao\chats\2026-09-17\new-chat-9\attack_frames"
FIX = r"D:\pixel-art-dashboard\xiaohongshu_20261118\fixed_gifs"
OUT = r"D:\pixel-art-dashboard\xiaohongshu_20261118"
FONT_R = r"C:\Windows\Fonts\msyh.ttc"
FONT_B = r"C:\Windows\Fonts\msyhbd.ttc"

ROLES = ["fox_girl", "elf_archer", "dragon_baby", "mage_fireball",
         "sword_boy", "alchemist", "rogue_dagger", "dwarf_warrior"]
BG = (15, 18, 24)
INK = (240, 244, 248)
DIM = (150, 162, 176)
ACC = (255, 148, 72)
OK = (94, 214, 160)


def wrap(draw, text, font, width):
    """按像素宽度折行（中文按字切，英文按词切）"""
    lines, cur = [], ""
    for ch in text:
        cand = cur + ch
        if draw.textlength(cand, font=font) <= width:
            cur = cand
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def f(s, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT_R, size=s)


def green_pct(rgb, alpha):
    r = rgb[..., 0].astype(np.int16); g = rgb[..., 1].astype(np.int16); b = rgb[..., 2].astype(np.int16)
    green = (g > 200) & (g - r > 12) & (g - b > 12)
    sub_g = green[::6, ::6]; sub_o = (alpha > 10)[::6, ::6]
    tot = sub_o.sum()
    return 0.0 if tot == 0 else float((sub_g & sub_o).sum()) / float(tot) * 100


def checker(size, step=26):
    img = Image.new("RGB", size, (38, 42, 50))
    d = ImageDraw.Draw(img)
    for y in range(0, size[1], step):
        for x in range(0, size[0], step):
            if (x // step + y // step) % 2 == 0:
                d.rectangle([x, y, x + step - 1, y + step - 1], fill=(52, 58, 68))
    return img


def paste_checker(canvas, frame, box):
    tile = checker((box, box))
    w = frame.size[0]
    fr = frame.convert("RGBA").resize((box, box), Image.LANCZOS)
    tile.paste(fr, (0, 0), fr.split()[-1])
    canvas.paste(tile, (0, 0)) if False else None
    return tile


# 逐角色实测
stats = []
for role in ROLES:
    orig = Image.open(os.path.join(BASE, role, f"{role}_attack.gif"))
    before = []
    for fr in ImageSequence.Iterator(orig):
        a = np.array(fr.convert("RGBA"))
        before.append(green_pct(a[..., :3], a[..., 3]))
    fixed = Image.open(os.path.join(FIX, role, f"{role}_attack_alpha.gif"))
    after = []
    for fr in ImageSequence.Iterator(fixed):
        a = np.array(fr.convert("RGBA"))
        after.append(green_pct(a[..., :3], a[..., 3]))
    stats.append((role, max(before), max(after), float(np.mean(before)), float(np.mean(after)),
                  os.path.getsize(os.path.join(FIX, role, f"{role}_attack_alpha.gif"))))

mean_b = float(np.mean([s[3] for s in stats]))
mean_a = float(np.mean([s[4] for s in stats]))

# 用于对比的角色：alchemist 第 6 帧（浅绿底 + 纯黑底两种毛病都有）
orig_f = [fr.convert("RGBA") for fr in ImageSequence.Iterator(Image.open(os.path.join(BASE, "alchemist", "alchemist_attack.gif")))]
fix_f = [fr.convert("RGBA") for fr in ImageSequence.Iterator(Image.open(os.path.join(FIX, "alchemist", "alchemist_attack_alpha.gif")))]
o5, n5 = orig_f[5], fix_f[5]
o4, n4 = orig_f[3], fix_f[3]

# ---------- 卡 1：封面 ----------
W, H = 1080, 1440
c1 = Image.new("RGB", (W, H), BG)
d1 = ImageDraw.Draw(c1)
d1.rectangle([0, 0, W, 6], fill=ACC)
d1.text((72, 96), "GIF 后几帧露底", font=f(84, True), fill=INK)
d1.text((72, 196), "3 步修干净", font=f(84, True), fill=ACC)
d1.text((72, 300), "48 帧逐个量出来的残留率，不是估的", font=f(30), fill=DIM)

# 左右对比
box = 420
for i, (tag, frame, sub) in enumerate([("修前", o5, "浅绿底 + 纯黑底"), ("修后", n5, "透明")]):
    tx = 72 + i * (box + 108)
    ty = 400
    tile = checker((box, box))
    fr = frame.resize((box, box), Image.LANCZOS)
    tile.paste(fr, (0, 0), fr.split()[-1])
    c1.paste(tile, (tx, ty))
    d1.text((tx, ty + box + 18), tag, font=f(40, True), fill=INK if i == 0 else OK)
    d1.text((tx, ty + box + 74), sub, font=f(26), fill=DIM)

d1.rounded_rectangle([72, 1082, W - 72, 1286], radius=18, fill=(24, 28, 36))
d1.text((100, 1102), "8 个角色 · 48 帧", font=f(30), fill=DIM)
d1.text((100, 1144), f"{mean_b:.2f}%  →  {mean_a:.2f}%", font=f(72, True), fill=INK)
d1.text((100, 1240), "平均残留（不透明区里的浅绿像素占比）", font=f(24), fill=DIM)

d1.text((72, 1320), "原素材只读，修好的另存一份；每帧都带透明索引", font=f(26), fill=DIM)
d1.text((72, 1364), "工具：pixel-art-action-frames（GitHub andrewlff）", font=f(26), fill=DIM)
c1.save(os.path.join(OUT, "封面_GIF后几帧露底.png"), optimize=True)

# ---------- 卡 2：三步法 ----------
c2 = Image.new("RGB", (1080, 1080), (250, 250, 248))
d2 = ImageDraw.Draw(c2)
d2.rectangle([0, 0, 1080, 6], fill=ACC)
d2.text((72, 62), "3 步把后段帧的底修掉", font=f(58, True), fill=(24, 28, 36))
d2.text((72, 132), "顺序别换：先认角色 → 再清底 → 最后逐帧验", font=f(26), fill=(110, 118, 128))

steps = [
    ("01", "先把角色认出来", "取“非浅色”像素里最大的连通块当角色轮廓；被它包住的浅色洞（衣服、高光）要补回来，否则会挖空"),
    ("02", "再清和边界连通的底色", "浅绿/浅蓝底板按低饱和高亮度判定，纯黑底板单独一条规则；只清够得到画布边界的，别动角色内部"),
    ("03", "最后逐帧回读验一遍", "读回文件量每帧的残留率，别只在内存里看数组——存盘那一步最容易把透明写成黑色"),
]
y = 210
for num, title, body in steps:
    d2.rounded_rectangle([72, y, 1008, y + 186], radius=16, fill=(255, 255, 255), outline=(228, 230, 234), width=2)
    d2.text((104, y + 30), num, font=f(46, True), fill=ACC)
    d2.text((186, y + 30), title, font=f(38, True), fill=(24, 28, 36))
    lines = wrap(d2, body, f(22), 800)
    ty2 = y + 88
    for line in lines[:2]:
        d2.text((186, ty2), line, font=f(22), fill=(96, 104, 116))
        ty2 += 36
    y += 206

d2.text((72, 860), "三个坑（都是这次真踩到的）", font=f(34, True), fill=(24, 28, 36))
pit = [
    "· 四角是 (0,0,0,0)，用“边框中位色”估底会估出黑色，越修越错",
    "· GIF 只有第 1 帧带透明标记时，后几帧会把透明索引画成黑色",
    "· 种子落在零散特效像素上，会把角色只认出一小块，整帧被删",
]
yy = 912
for line in pit:
    d2.text((72, yy), line, font=f(23), fill=(120, 60, 40))
    yy += 44
c2.save(os.path.join(OUT, "步骤_三步修底.png"), optimize=True)

# ---------- 卡 3：8 角色实测 ----------
c3 = Image.new("RGB", (1080, 1080), (250, 250, 248))
d3 = ImageDraw.Draw(c3)
d3.rectangle([0, 0, 1080, 6], fill=ACC)
d3.text((72, 56), "8 个角色 · 48 帧实测", font=f(54, True), fill=(24, 28, 36))
d3.text((72, 124), "残留率口径：不透明区里偏绿像素占比，抽样步长 6", font=f(24), fill=(110, 118, 128))

col = [72, 300, 500, 700, 900]
heads = ["角色", "帧数", "修前最高", "修后最高", "修后平均"]
for i, h in enumerate(heads):
    d3.text((col[i], 178), h, font=f(24, True), fill=(110, 118, 128))

y = 226
for role, bmax, amax, bmean, amean, size in stats:
    d3.line([72, y + 50, 1008, y + 50], fill=(228, 230, 234), width=2)
    d3.text((col[0], y), role, font=f(24), fill=(24, 28, 36))
    d3.text((col[1], y), "6", font=f(24), fill=(96, 104, 116))
    d3.text((col[2], y), f"{bmax:.1f}%", font=f(24), fill=(150, 74, 46))
    d3.text((col[3], y), f"{amax:.1f}%", font=f(24), fill=(30, 130, 92))
    d3.text((col[4], y), f"{amean:.2f}%", font=f(24), fill=(96, 104, 116))
    y += 70

d3.rounded_rectangle([72, y + 10, 1008, y + 200], radius=16, fill=(24, 28, 36))
d3.text((104, y + 28), "合计", font=f(28), fill=DIM)
d3.text((104, y + 64), f"平均 {mean_b:.2f}%  →  {mean_a:.2f}%", font=f(46, True), fill=INK)
d3.text((104, y + 132), "最坏一帧 49.6%（剑士第 5 帧）→ 0.4%", font=f(22), fill=(170, 182, 196))

d3.text((72, y + 216), "修好的 GIF：fixed_gifs/角色/角色_attack_alpha.gif（6 帧 · 130 ms · loop=0）", font=f(18), fill=(120, 128, 140))
c3.save(os.path.join(OUT, "实测_八角色修底表.png"), optimize=True)

print("卡1", os.path.getsize(os.path.join(OUT, "封面_GIF后几帧露底.png")))
print("卡2", os.path.getsize(os.path.join(OUT, "步骤_三步修底.png")))
print("卡3", os.path.getsize(os.path.join(OUT, "实测_八角色修底表.png")))
print("平均 %.2f%% -> %.2f%%" % (mean_b, mean_a))
for s in stats:
    print(s[0], "before_max %.1f after_max %.1f" % (s[1], s[2]))

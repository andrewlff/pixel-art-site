# -*- coding: utf-8 -*-
"""生成 B站 演示视频（16:9 1080p，约 60s）：卡片由 PIL 绘制，GIF 循环与合成交给 ffmpeg。
输出：D:\pixel-art-dashboard\promo\bilibili_demo\pixel-pipeline-demo-60s.mp4
"""
import os, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\pixel-art-dashboard\promo\bilibili_demo"
CARDS = os.path.join(OUT, "cards")
SEGS = os.path.join(OUT, "segs")
FIXED = r"D:\pixel-art-dashboard\xiaohongshu_20261118\fixed_gifs"
ORIG = r"C:\Users\SHAN\Doubao\chats\2026-09-17\new-chat-9\attack_frames"
FF = r"D:\dev\ffmpeg.exe"
W, H, FPS = 1920, 1080, 30
BG = (16, 17, 24)
FG = (238, 238, 245)
MUTED = (150, 158, 178)
ACCENT = (240, 170, 150)   # 低饱和暖粉，配合像素素材
ACCENT2 = (150, 190, 220)

ROLES = [
    ("fox_girl", "FOX GIRL", "狐耳少女"),
    ("elf_archer", "ELF ARCHER", "精灵弓手"),
    ("dragon_baby", "DRAGON BABY", "幼龙"),
    ("mage_fireball", "MAGE", "火球法师"),
    ("sword_boy", "SWORD BOY", "剑士"),
    ("alchemist", "ALCHEMIST", "炼金术士"),
    ("rogue_dagger", "ROGUE", "刺客"),
    ("dwarf_warrior", "DWARF", "矮人战士"),
]

F_TITLE = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 86)
F_BIG = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 60)
F_ASS = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 40)
F_40 = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 34)
F_SMALL = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 27)
F_MONO = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 40)


def canvas():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    return im, ImageDraw.Draw(im)


def text_c(d, y, s, font, fill=FG, spacing=14):
    w = d.textlength(s, font=font)
    d.text(((W - w) / 2, y), s, font=font, fill=fill)
    return y + font.size + spacing


def checker_bg(size, cell=24):
    im = Image.new("RGB", size, (44, 46, 58))
    d = ImageDraw.Draw(im)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2 == 0:
                d.rectangle([x, y, x + cell - 1, y + cell - 1], fill=(56, 58, 72))
    return im


def card_title():
    im, d = canvas()
    d.rectangle([0, 0, 12, H], fill=ACCENT)
    text_c(d, 250, "角色立绘 / 6 帧动作", F_ASS, MUTED)
    text_c(d, 310, "一键变透明底像素资产", F_TITLE)
    text_c(d, 430, "透明单帧 · 横排图集 · JSON 清单 · 循环 GIF", F_ASS, ACCENT2)
    d.line([(660, 530), (1260, 530)], fill=(70, 74, 92))
    text_c(d, 560, "纯 Python 标准库 · 零依赖", F_40, MUTED)
    text_c(d, 930, "github.com/andrewlff/pixel-art-action-frames", F_SMALL, MUTED)
    im.save(os.path.join(CARDS, "c1_title.png"))


def card_flow():
    im, d = canvas()
    d.rectangle([0, 0, 12, H], fill=ACCENT)
    y = 170
    y = text_c(d, y, "一条命令跑完的四步", F_BIG, FG, 40)
    rows = [
        ("01", "去背景", "flood-fill 从边界清底，保住角色内部的同色区域"),
        ("02", "统一裁剪 + 像素化", "最近邻缩格、32 色量化、深棕描边，整数倍放大"),
        ("03", "打包", "透明单帧 + 横排图集 + JSON 帧清单（rect 可直接切）"),
        ("04", "合成 GIF", "自写 GIF89a 编码器：全局色表 + 透明索引 + disposal=2，不叠残影"),
    ]
    for no, k, desc in rows:
        d.text((200, y), no, font=F_MONO, fill=ACCENT)
        d.text((300, y), k, font=F_ASS, fill=FG)
        d.text((300, y + 52), desc, font=F_SMALL, fill=MUTED)
        y += 150
    text_c(d, y + 40, "输出可直接拖进 Godot / Unity", F_40, ACCENT2)
    im.save(os.path.join(CARDS, "c2_flow.png"))


def card_role(i, key, en, cn):
    im, d = canvas()
    d.rectangle([0, 0, 12, H], fill=ACCENT2)
    d.text((90, 70), "06 FRAMES · 130ms · LOOP", font=F_SMALL, fill=MUTED)
    d.text((90, 110), "%s  %s" % (en, cn), font=F_BIG, fill=FG)
    d.text((1230, 70), "%02d / 08" % (i + 1), font=F_MONO, fill=MUTED)
    # 帧进度点
    for k in range(6):
        x = 1230 + k * 34
        d.ellipse([x, 130, x + 18, 148], outline=ACCENT2 if k == 0 else (70, 76, 96))
    im.save(os.path.join(CARDS, "role_%d.png" % i))


def card_before_after():
    im, d = canvas()
    text_c(d, 70, "后段帧露底 → 逐帧清理", F_BIG, FG, 40)
    text_c(d, 150, "8 个角色 · 48 帧 · 残留 8.25% → 0.36%", F_40, MUTED)
    box = 480
    y0 = 250
    for idx, (title, path, frame) in enumerate([
        ("修前", os.path.join(ORIG, "alchemist", "alchemist_attack.gif"), 4),
        ("修后", os.path.join(FIXED, "alchemist", "alchemist_attack_alpha.gif"), 4),
    ]):
        x0 = 330 + idx * 620
        card = checker_bg((box, box), 30)
        gi = Image.open(path)
        gi.seek(frame)
        fr = gi.convert("RGBA").resize((box, box), Image.LANCZOS)
        card.paste(fr, (0, 0), fr)
        im.paste(card, (x0, y0))
        d.rectangle([x0, y0, x0 + box, y0 + box], outline=(90, 96, 118))
        tw = d.textlength(title, font=F_ASS)
        d.text((x0 + (box - tw) / 2, y0 + box + 24), title, font=F_ASS, fill=FG if idx else MUTED)
    text_c(d, y0 + box + 110, "四角常是 (0,0,0,0)，用边框中位色估底会估成黑色", F_SMALL, MUTED)
    text_c(d, y0 + box + 156, "RGBA 直存 GIF 会把透明区写成不透明黑，须显式调色板 + 透明索引", F_SMALL, MUTED)
    im.save(os.path.join(CARDS, "c3_ba.png"))


def card_outro():
    im, d = canvas()
    d.rectangle([0, 0, 12, H], fill=ACCENT)
    text_c(d, 300, "仓库都在 GitHub", F_TITLE)
    y = 470
    for s in [
        "主仓   github.com/andrewlff/pixel-art-action-frames",
        "Godot  github.com/andrewlff/godot-pixel-batch-tool",
        "Unity  github.com/andrewlff/unity-pixel-batch-tool",
    ]:
        w = d.textlength(s, font=F_40)
        d.text(((W - w) / 2, y), s, font=F_40, fill=MUTED)
        y += 78
    text_c(d, 760, "零依赖 · MIT · 觉得有用点个 star", F_ASS, ACCENT2)
    im.save(os.path.join(CARDS, "c4_outro.png"))


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("FFMPEG FAIL:", " ".join(args))
        print((r.stderr or "")[-1200:])
        raise SystemExit(1)


def seg_image(card, secs, out):
    run([FF, "-y", "-loop", "1", "-i", card, "-t", str(secs),
         "-vf", "scale=%d:%d,fps=%d,format=yuv420p" % (W, H, FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])


def seg_role(i, key, secs, out):
    gif = os.path.join(FIXED, key, "%s_attack_alpha.gif" % key)
    card = os.path.join(CARDS, "role_%d.png" % i)
    run([FF, "-y", "-loop", "1", "-t", str(secs), "-i", card,
         "-t", str(secs), "-i", gif,
         "-filter_complex",
         "[0:v]scale=%d:%d,fps=%d[bg];[1:v]scale=-1:740,format=rgba,fps=%d[g];"
         "[bg][g]overlay=(W-w)/2:(H-h)/2-10:format=auto,format=yuv420p[v]" % (W, H, FPS, FPS),
         "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out])


def main():
    os.makedirs(CARDS, exist_ok=True)
    os.makedirs(SEGS, exist_ok=True)
    card_title(); card_flow(); card_before_after(); card_outro()
    for i, (k, en, cn) in enumerate(ROLES):
        card_role(i, k, en, cn)

    segs = []
    p1 = os.path.join(SEGS, "01_title.mp4")
    seg_image(os.path.join(CARDS, "c1_title.png"), 4, p1); segs.append(p1)
    p2 = os.path.join(SEGS, "02_flow.mp4")
    seg_image(os.path.join(CARDS, "c2_flow.png"), 8, p2); segs.append(p2)
    for idx, (k, en, cn) in enumerate(ROLES):
        pr = os.path.join(SEGS, "r%02d.mp4" % idx)
        seg_role(idx, k, 5, pr); segs.append(pr)
    p3 = os.path.join(SEGS, "03_ba.mp4")
    seg_image(os.path.join(CARDS, "c3_ba.png"), 6, p3); segs.append(p3)
    p4 = os.path.join(SEGS, "04_outro.mp4")
    seg_image(os.path.join(CARDS, "c4_outro.png"), 6, p4); segs.append(p4)

    lst = os.path.join(OUT, "concat.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for p in segs:
            f.write("file '%s'\n" % p.replace("\\", "/"))

    final = os.path.join(OUT, "pixel-pipeline-demo-60s.mp4")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", "-movflags", "+faststart", final])
    print("OK", final, os.path.getsize(final))


if __name__ == "__main__":
    main()

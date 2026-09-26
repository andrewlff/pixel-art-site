#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""跑 4 组不同画风的场景配置，输出 environment sheet prompt。"""
import sys, os, json
SKILL_DIR = r"C:\Users\SHAN\AppData\Local\DoubaoWork\User Data\Default\.doubaowork\agent_mode\workspace\.user_skills\scene-batch-generator\scripts"
sys.path.insert(0, SKILL_DIR)
import scene_pipeline as sp

GROUPS = [
    {
        "name": "g1_handpaint_fantasy",
        "BACKGROUND": "异世界冒险大陆：魔法森林、浮空岛、古代遗迹与水晶矿脉，冒险者穿行其间。",
        "STYLE": sp.STYLE_PRESETS["handpaint"],
        "COUNT": 6, "GRID_COLS": 3, "pool": sp.FANTASY_SCENES, "offset": 0,
    },
    {
        "name": "g2_ghibli_coast",
        "BACKGROUND": "温暖治愈的海滨与山谷世界：港口小镇、沙漠绿洲、浮空群岛与雪山隘口。",
        "STYLE": sp.STYLE_PRESETS["ghibli"],
        "COUNT": 6, "GRID_COLS": 3, "pool": sp.FANTASY_SCENES, "offset": 6,
    },
    {
        "name": "g3_dark_ominous",
        "BACKGROUND": "暗黑奇幻废土：迷雾沼泽、火山熔岩、地下神殿与被遗忘的古代遗迹。",
        "STYLE": sp.STYLE_PRESETS["dark"],
        "COUNT": 6, "GRID_COLS": 3, "pool": sp.FANTASY_SCENES, "offset": 2,
    },
    {
        "name": "g4_pixel_neon",
        "BACKGROUND": "赛博朋克都市夜景：霓虹街口、地铁、深夜便利店、天台、废弃工厂与立交桥。",
        "STYLE": sp.STYLE_PRESETS["pixel"],
        "COUNT": 6, "GRID_COLS": 3, "pool": sp.MODERN_SCENES, "offset": 0,
    },
]

out = {}
for g in GROUPS:
    sp.BACKGROUND = g["BACKGROUND"]
    sp.STYLE = g["STYLE"]
    sp.GRID_COLS = g["GRID_COLS"]
    pool = g["pool"][g["offset"]:g["offset"]+g["COUNT"]]
    # 临时替换 pool：复制 build 逻辑但用切片后的 pool
    scenes = []
    TIMES = ["清晨","正午","黄昏","夜晚","午后","黎明"]
    WEATHERS = ["晴朗","薄雾","小雨","多云","晴朗","风雪"]
    LIGHT = sp.LIGHT
    for i,(place,elems) in enumerate(pool,1):
        t,w = TIMES[(i-1)%len(TIMES)], WEATHERS[(i-1)%len(WEATHERS)]
        light,tone = LIGHT[t]
        scenes.append({"id":i,"place":place,"time":t,"weather":w,"light":light,"tone":tone,"elems":elems,
                       "cn":f"场景{i}：{place}，{t}，{w}，{light}，{tone}色调，含{elems}"})
    seg = "；".join(s["cn"] for s in scenes)
    rows = (len(scenes)+g["GRID_COLS"]-1)//g["GRID_COLS"]
    prompt = (f"游戏场景概念设定图（environment sheet），{g['STYLE']}。背景世界观：{g['BACKGROUND']} "
              f"请在同一张图中按{rows}行{g['GRID_COLS']}列网格排列{len(scenes)}个不同场景的概念图，"
              f"每格一个完整横构图场景、彼此内容与色调差异明显：{seg}。"
              f"不画角色或仅放极小人物剪影作比例参考，每格下方标注编号1到{len(scenes)}，无多余文字，无水印。")
    out[g["name"]] = {"prompt": prompt, "scenes": scenes}

print(json.dumps(out, ensure_ascii=False, indent=2))

# B站 演示视频 · 发布文案（2026-11-20）

> 状态：视频与封面已产出，**未上传**。B站上传需本人登录账号操作（扫码/短信验证一律不能代办）。

## 视频文件

- 视频：`D:\pixel-art-dashboard\promo\bilibili_demo\pixel-pipeline-demo-60s.mp4`
  - 1920×1080 / 30 fps / 时长 1:04 / H.264 / 无音轨（B站允许静音上传，需要 BGM 请在投稿页选平台音乐库）
- 封面：`D:\pixel-art-dashboard\promo\bilibili_demo\封面_1466x917.png`（1466×917，符合 B 站封面比例）
- 分段素材：`segs\` 与卡片 `cards\`（要改文案重出，跑 `build_demo.py`）

## 标题（82 字以内，B 站上限 80）

【开源】立绘+6帧动作，一键出透明底像素动画｜零依赖 Python

## 简介

自己写的一套像素美术资产管线，做独立游戏时不用再手工抠图对齐。

输入角色立绘或 6 帧攻击动作，一条命令输出：透明单帧 + 横排图集 + JSON 帧清单 + 循环 GIF，直接拖进 Godot / Unity。

全部脚本只用 Python 标准库，不装 Pillow 也能跑。

这期演示了 8 个角色，顺手把 GIF 后段帧露底的问题修了——48 帧平均残留 8.25% 降到 0.36%，修前修后对比在 0:52。

仓库：
主仓 github.com/andrewlff/pixel-art-action-frames
Godot github.com/andrewlff/godot-pixel-batch-tool
Unity github.com/andrewlff/unity-pixel-batch-tool

觉得有用点个 star，后面会继续更。

## 标签

像素画、独立游戏、Godot、Unity、开源、AI绘画、游戏开发、像素艺术

## 分区

科技 → 计算机技术（或「游戏 → 游戏开发」）

## 时间轴（用于简介置顶评论）

- 0:00 它能做什么
- 0:04 一条命令跑完的四步
- 0:12 八个角色逐个播放（6 帧 / 130ms / 循环）
- 0:52 后段帧露底：修前 vs 修后
- 0:58 仓库地址

## 上传步骤（本人操作）

1. 打开 bilibili.com → 投稿 → 上传视频，选上面那个 mp4
2. 封面手动上传 `封面_1466x917.png`
3. 标题 / 简介 / 标签 直接复制本文
4. 分区选「科技 → 计算机技术」，勾选原创
5. 发布后把链接记到 `发布记录.md`

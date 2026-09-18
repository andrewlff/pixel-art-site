# Changelog

All notable changes to Pixel Art Action Frames & Pixelizer Web Tool.

## [Unreleased] — 2026-09-18

### Added
- Web 端 Pixelizer 工具（浏览器纯 Canvas，无需后端）
  - Single Image 模式：上传单图实时像素化
  - Animation Frames 模式：多帧批量处理 + 循环播放 + FPS 调节
  - Grid Size / Colors / Scale 三参数滑块
  - Outline 描边开关（深棕边缘暗化）
  - Transparent BG 去背景开关 + BG Tolerance 容差滑块
  - Download PNG / Download All Frames 导出
  - Compare Original 原图对比
- 项目运营看板（index.html）：GitHub 仓库状态、小红书发布日历、定时任务、资产清单、OSS 进度
- 4 角色像素攻击帧管线（orbs / bone / palm / ghost）
  - 6 帧攻击动作序列
  - 透明底像素图集 + JSON 帧清单 + 动画 GIF
  - 可直接导入 Godot / Unity

### Fixed
- Transparent BG toggle 变量名 typo 导致开关无效
- 背景采样从四角平均改为整条边缘众数
- GIF 帧叠加问题（disposal=2）

### Tech
- 前端：原生 HTML + Canvas 2D + ECharts
- 算法：median-cut 量化 + nearest-neighbor 缩放 + flood-fill 去背景
- 引擎插件：Godot 4 / Unity Editor C#

---

## [1.0.0] — 2026-09-17

### Added
- Python 像素化管线（pixel_core.py）
- 批量去背景脚本（transparent_frames.py）
- GIF 构建脚本（build_gif.py）
- GitHub 三仓库发布：
  - pixel-art-action-frames（核心管线）
  - godot-pixel-batch-tool（Godot 编辑器插件）
  - unity-pixel-batch-tool（Unity 编辑器插件）
- 每日小红书引流定时任务
- 评论回复与工具分发定时任务

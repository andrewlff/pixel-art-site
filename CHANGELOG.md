# Changelog

All notable changes to Pixel Art Action Frames & Pixelizer Web Tool.

## [Unreleased] — 2026-09-21

### Added
- Split Sheet：上传大网格图，按 Cols×Rows 自动切帧
- 视频抽帧：直接拖 mp4 上传，Sample FPS 控制采样率
- Lock Palette：首帧色板固化，后续帧复用，导出 .gpl
- 标准尺寸预设：16/32/48/64 一键设置
- Export JSON：帧清单（cols/rows/cell_w/cell_h/frame_ms/frames[i].rect），直导 Godot/Unity
- 去背模式：Auto / Green Screen（含溢色抑制）/ White / Black
- 帧拖拽排序：底部帧条直接拖动换顺序
- AI Generate tab：角色+动作+方向+网格 → 标准提示词一键复制

### Fixed
- 暂停不可用：多次 processAll 叠加 setInterval，startPlay 开头先 stopPlay 清旧定时器
- 加帧/减帧/拖帧后不自动播放，且保持当前帧位置
- frame-edit-row 重复 style 属性导致 Single 模式误显示 +Frame/−Frame

## [Unreleased] — 2026-09-19

### Added
- Pixelizer Web 工具上线 GitHub Pages：https://andrewlff.github.io/pixel-art-site/
- Animation Frames 模式：多帧批量像素化 + 循环播放 + FPS 调节
- BG Tolerance 容差滑块，背景去除可调
- 项目看板 dashboard.html（GitHub 仓库/小红书日历/定时任务/OSS 进度）

### Fixed
- Transparent BG toggle 变量名 typo（!transparentToggle → !transparentEnabled）
- 背景采样从四角平均改为整条边缘众数
- GitHub Pages 首页改为 Pixelizer 工具本体

### Deploy
- pixel-art-site repo 创建并启用 GitHub Pages
- 每次 push 自动部署

---

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
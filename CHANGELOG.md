# Changelog

All notable changes to Pixel Art Action Frames & Pixelizer Web Tool.


## [Unreleased] — 2026-10-04

### Added
- Pixelizer 素材库编辑模式（Library Edit）：新增「素材库编辑」Tab，白底素材缩略图网格（lib-grid）+ 选中预览，支持从素材库直接载入编辑
- 帧定位编辑器：动画帧模式下逐帧走查（上一帧/下一帧）、X/Y 偏移滑块（-64~64px）、画布直接拖动移动当前帧、重置本帧（09-28 开发，本次提交入库）

### Notes
- 10-02/10-03 无新增功能迭代（国庆假期，无产出）

---

## [Unreleased] — 2026-10-01

### Added
- 白底可抠图素材库扩展（Pixel-assets-white-bg v2）：新增 4 个高辨识度像素主体（机甲骑士、烈焰魔龙、猫耳剑士、水晶魔像），1:1 白底独立主体，亮眼撞色 + 强记忆点造型，可直接抠图进游戏与社媒封面（生成规则：白底可抠图 + 吸引眼球 + 不重复往期）
- 小红书 10-01 笔记配图使用自主生成新素材（四宫格拼图 1 张），封面与 09-30 期完全不重复
## [Unreleased] — 2026-09-30

### Added
- 白底可抠图素材库（Pixel-assets-white-bg）：像素角色/道具系列（骑士、长剑、橘白猫咪等），纯白背景独立主体，可直接抠图用于游戏素材与社媒配图（生成规则：白底可抠图 + 亮眼配色 + 不重复）
- 素材生成规则落地：小红书配图统一走"自主生成白底可抠图素材"流程，避免往期雷同

---

## [Unreleased] — 2026-09-29

### Added
- Pixelizer 演示视频系列：最终版 10 支（字幕/旁白/BGM 多版本，Pixelizer-demo-*.mp4），用于小红书/B站推广物料
- 场景风格化测试扩展：新增厚涂（g5_thick）/ 水墨（g6_ink）/ 低多边形（g7_lowpoly）3 种风格场景测试图，累计 7 种风格

---

## [Unreleased] — 2026-09-27

### Added
- 射手（archer）角色像素化管线验证：立绘 → 6 帧动作序列 → 透明图集（archer_sheet.png）+ 帧清单（archer_sheet.json）+ 动画 GIF（archer_sheet.gif），产物入 scenes/archer_frames/out
- README 增加 star badge 与 demo GIF（推广计划落地）

---

## [Unreleased] — 2026-09-26

### Added
- 作品集看板升级：dashboard.html 改为「AI 游戏美术 Skill 工具箱」，新增场景画廊（scenes-gallery）模块
- 场景设定图资产 4 套 24 格：手绘（g1_handpaint）/ 吉卜力（g2_ghibli）/ 暗黑（g3_dark）/ 像素赛博（g4_pixel_neon），附 prompts.json 与批量生成脚本 _gen_prompts.py
- 看板统计更新：Skill 工具 9 项、场景设定图 4 套 · 24 格、GitHub Repos 3 个

### Improved
- 作品集看板移动端适配：scenes-gallery 单列布局

---

## [Unreleased] — 2026-09-24

### Added
- 批量导出文件名模板：支持{character}/{action}/{frame_num}占位符
- README补充Godot/Unity插件3步快速安装说明

### Improved
- 像素化预设新增"16-bit复古"：更细颗粒+更高饱和度
- 透明GIF导出速度提升约30%（worker内缓存色表）

---

## [Unreleased] — 2026-09-23

### Added
- 黑猫角色3套动作帧生成管线验证：出拳攻击(120ms)、挥剑攻击(140ms)、跳跃(150ms)
- 优化后提示词模板：锚点固定+6帧动作细化+头尾帧呼应，解决帧间漂移
- 透明GIF编码器修复：disposal=2全局色表+专用透明索引，彻底消除帧叠加残影

### Improved
- 像素化质量提升：RGBA分离量化（RGB中位切分+alpha通道保留）
- 动作帧一致性：同一角色6帧外观锚点统一（发色/服装/武器/瞳色）

---

## [Unreleased] — 2026-09-22

### Added
- 众生之门风格战斗HUD复刻：深青#00353F + 青绿#4F948B + 金黄#EBC407 配色
- Q版黑猫玩家模型（圆头+竖耳+大眼）
- 圆形小地图 + 摇杆装饰 + 技能按钮组（带快捷键角标）
- 顶部怪物血条 + 玩家血条/灵能条双层条

### Fixed
- GIF帧叠加残影问题：disposal=2 每帧清屏后重绘
- 鼠标灵敏度过高：从0.002降到0.0015，pitch限制±0.7弧度

---

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

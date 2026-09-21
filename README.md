# Pixelizer 🎮

在线像素化 + 动作帧工具，纯前端，零依赖，免费开源。

**在线使用**：https://pixel-art-site.pages.dev/

---

## ✨ 功能

### 单图像素化
- 网格大小 8-128，颜色数 2-64，缩放 1-16
- 深棕描边 / 透明背景开关
- 标准尺寸预设（16/32/48/64）

### 动画帧模式
- 多帧上传 / 视频抽帧（mp4/webm）
- Sprite Sheet 一键拆分（cols×rows）
- 色板锁定（多帧色调统一，导出 .gpl）
- 绿幕/白地/黑地一键去背
- 帧拖拽排序 / 右键翻转 / 每帧单独时长
- 洋葱皮预览
- 导出：单帧 PNG / 透明 GIF / Sprite Sheet 大图集 / JSON 帧清单

### AI Generate
- 填角色+动作+方向+网格大小，自动生成标准提示词
- 复制到豆包/即梦/Nano Banana 出图，回来直接切帧

---

## 🚀 使用

直接打开 https://pixel-art-site.pages.dev/ 就能用，不用下载不用注册。

本地运行：
```bash
git clone https://github.com/andrewlff/pixel-art-site.git
cd pixel-art-site
# 直接用浏览器打开 index.html
```

---

## 📦 导出格式

- **PNG**：单帧透明底像素画
- **GIF**：透明循环动画
- **Sprite Sheet**：cols×rows 大图集 PNG
- **JSON**：帧清单（cell_w/cell_h/frame_ms/frames[i].rect），直接导入 Godot/Unity
- **.gpl**：色板文件，导入 Aseprite

---

## 🛠️ 技术栈

- 纯 HTML/CSS/JS，零依赖
- Canvas 2D 像素化算法（median-cut 量化 + flood-fill 去背景）
- gif.js（CDN）导出 GIF
- Cloudflare Pages 部署

---

## 📄 License

MIT

---

## ❤️ 赞助

如果这个工具帮到你，可以赞助我一杯咖啡：
USDT (TRC20): `TFtHDFWCMFMxLCtsBQpPudToiKry6ETTQ1`

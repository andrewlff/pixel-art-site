# Changelog

All notable changes to Pixel Art Action Frames & Pixelizer Web Tool.

## [Unreleased] — 2026-11-14

### Notes
- 11-14 无代码功能迭代（四仓无新提交；当日为运营日，内容侧仅产出文案草稿与核查记录）
- 小红书登录态中断（连续第 40 天可用记录就此中断）：本机内置浏览器进程退出，`aha_browser_use` 返回 `CDP session is disconnected` / `no browser tab is available`，`list_tabs()` 为空，`Get-Process chrome` 计数为 0；尝试重启 `DoubaoWork_browser_proxy.exe` 后 9222 端口有监听但 `http://127.0.0.1:9222/json/version` 返回 404（无 CDP 端点），`bu` 仍取不到标签页；本机 Chrome 打开 `xiaohongshu.com/notification` 被重定向至 `/login`，该浏览器无小红书登录态
- 11-14 评论核查：未执行（浏览器不可用），当日新评论 0 / 已回复 0 / 待回复 0 均为「未核查」而非「确认无」
- 11-14 发布小红书笔记：未执行（同上，创作平台不可达），当日 0 篇；已在 `发布记录.md` 落一份 D8 草稿（标题/正文/8 标签/配图方案）待登录恢复后直接发布
- 11-14 数据核查：GitHub 四仓 `api.github.com` 读数 — pixel-art-action-frames 0 star、godot-pixel-batch-tool 0 star、unity-pixel-batch-tool 0 star、pixel-art-site 0 star（最新 push 2026-11-13 06:39 UTC，对应 commit `92bd5aa`）；站点 https://pixel-art-site.pages.dev 返回 200（server: cloudflare），线上正常；Cloudflare Pages 昨日 UV/访问量与小红书创作者中心笔记数据**未取到**（无可用 API token，且浏览器分支不可用）
- 11-14 本周推广待办盘点：小红书周更（11-11、11-13 已发 2 篇，达标）；V2EX 首帖未发；B 站 1 分钟演示视频未录（本地已有 `Pixelizer-demo-final-subtitled.mp4` 等竖屏成品可直接上传）；GitHub README demo GIF + star badge 未加；掘金技术博客未写
## [Unreleased] — 2026-11-13

### Notes
- 11-13 无代码功能迭代（当日为运营与发布日，四仓无代码提交）
- 小红书登录态正常（连续第 39 天可用）：通知页「评论和@」、图文发布页、笔记管理页均可直接访问，无登录重定向
- 11-13 评论核查：通知页「评论和@」全量读取，最新仍为「洛笙喔 / 2 天前 / 回复了你的评论 · 私 · 报名」与「Spark / 4 天前」两条，后者下方挂着 11-09 我方回复（内容含仓库名与网页版入口）；往后 Momo 09-25、奶芙饼饼 09-21、一颗小布丁 09-19 等均为旧条目。当日新评论 0、已回复 0、待回复 0
- 11-13 发布小红书图文笔记（D 开源更新型，对应 7 天日历 D7「三件套合集」）：标题《像素化三件套⚔️三端同一套参数》（15/20 字），3 图，原创声明已开启并完成《原创声明须知》勾选与「声明原创」确认（内层 checkbox=true、权益弹层已关闭），正文 680 字，含 8 个固定话题标签（独立游戏 / 像素画 / 游戏开发 / Godot / Unity / 开源项目 / AI绘画 / 设计工具，均已转为 `[话题]#` 蓝色话题 chip）
- 11-13 发布结果：创作平台返回 `published=true`；笔记管理页首条「审核中 / 像素化三件套⚔️三端同一套参数 / 2026-11-13 14:38 / 曝光 0·评论 0·赞 0·收藏 0·分享 0」，全部 23 篇；noteId 与公开链接待过审后补
- 11-13 新素材目录 xiaohongshu_20261113：`封面_三件套合集.png`（1080×1440，kicker「开源 · 三件套」+ 四张真实成品 2×2 白卡 + 参数带「48 网格 · 24 色 · 6 倍放大 · 描边可关」）、`工作流_三端同一套参数.png`（1080×980，四列 ①输入 ②参数 ③入口 ④输出，无箭头、单列 225 宽 30 号字，文案压到不溢出）；配图第三张沿用 11-10 的 `xiaohongshu_20261110\对比_四角色批量.png`（1080×1300）
- 11-13 生图脚本：`make_cover_v3.py`、`make_flow_v4.py` 为最终采用版本；`make_assets_1113.py`、`make_assets_v2.py` 为废弃版本。返工记录两处：① v1 封面把 `godot_preview.png` / `unity_preview.png`（实为配色测试条）误标为"编辑器面板"，属失实，整版废弃；② v3 封面曾给四张成品硬起角色名（与实际图像不符），已删标签，副行改为「同一套参数，同一批输出（四张成品）」。另删除一张 `对比_立绘与像素版.png`（原图本身即像素风，前后无差异，无说服力）
- 11-13 发布页踩坑与修法（计入操作手册）：正文 TipTap/ProseMirror 编辑器里 `Ctrl+End` 不移动光标、`bu.click` 会把光标落在段落中间，导致话题被插进句子内部（"参数还各 #独立游戏 记各的"）；`Ctrl+A` 后 `Backspace` 清空（JS 校验 `.ProseMirror` innerText 长度≈1）再整体写回是可靠路径；话题必须"输入 # 词 + 点候选行 `box "#xx N浏览"`"才会转成 chip，纯文本不会；原创开关 JS `.click()` 无效、`find` 报 not-visible、`bu.scroll` 报 `kScrollTargetNotUserScrollable`，实际可用路径是 JS 改内部容器 `scrollTop` 后 `click_xy` 点归一化坐标（451,115），弹层内勾选 checkbox 再点「声明原创」
- 11-13 数据核查（真值）：Cloudflare Pages 项目 `pixel-art-site` Metrics「Last 24 hours」Requests 0 / Subrequests 0 / No data；Web Analytics `siteTag~in=194ff5b1d471470b88fa35908717e500` Visits 0 / Page views 0。GitHub 四仓（pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-site）star 均 0，与 11-12 基线一致；API 未认证 403，改用仓库页 `"stargazerCount"` 解析
- 11-13 小红书笔记数据（截至核查时）：11-11 笔记 59 曝光 / 0 评论 / 0 赞 / 1 收藏 / 0 分享；11-10 笔记 161 / 0 / 5 / 4 / 0；11-09 笔记 150 / 0 / 9 / 12 / 2
- 11-12 缺口记录：`发布记录.md` 末条仍为 11-11 D6（noteId `6af40b0d000000002b038a91`），11-12 无发布记录，当日运营线在云主机环境受阻未执行
## [Unreleased] — 2026-11-11

### Notes
- 11-11 无代码功能迭代（当日为运营与发布日，四仓无代码提交）
- 小红书登录态正常（连续第 37 天可用）：通知页、图文发布页、笔记管理页、创作者数据页、粉丝数据页均可直接访问，无登录重定向
- 11-11 评论核查：通知页「评论和@」当日新增 1 条系统通知——小红薯6AF584EC 作者「回复了你的评论 / 1小时前 / 该评论已删除」，无正文，无回复义务；历史 3 条（Spark 追问已回复、Spark「原评论已删除」、Spark 7 天前原评论）与「一面千识 10-08」旧通知状态不变；当日新评论 0、需回复 0、已回复 0
- 11-11 发布小红书图文笔记（B 教程干货型，对应 7 天日历 D6「透明 GIF 无残影叠加的编码要点」）：标题《透明GIF拖影子？改1个字节就好》（16 字），3 图，原创声明已开启（内层 checkbox=true、弹层已关闭），正文 695/1000 字，含 8 个固定话题标签
- 11-11 发布结果：创作平台返回 `published=true`；笔记管理页首条「审核中 / 透明GIF拖影子？改1个字节就好 / 2026-11-11 14:28 / 曝光 0·评论 0·赞 0·收藏 0·分享 0」，全部 22 篇；noteId `6af40b0d000000002b038a91`（从首条卡片 `data-impression` 的 noteTarget 取到）
- 11-11 新增素材目录 xiaohongshu_20261111：make_assets.py（PIL）内含 disposal 对照实验 + 三图生成；成图 1080×1440 封面、1080×1300「残影 vs 正确」上下对照、1080×900 六帧棋盘格预览
- 11-11 对照实验（真值，非示意）：取仓库 `examples/orbs/orbs_sheet.gif`（512×504 / 6 帧 / 120ms / loop=0）解成 RGBA 帧，用同一批帧分别按 disposal=2 与 disposal=1 重新编码，再逐帧解回统计「正确版 alpha=0 却被上一帧占住」的像素：合计 57,856 px，帧 1→6 依次 0 / 5,760 / 6,208 / 10,368 / 17,472 / 18,048，残影随帧号累积，正是"拖影子"的可复现来源
- 11-11 文案技术要点（与 scripts/build_gif.py 自述一致）：全局色表 + 专用透明索引、LSD 背景索引指向透明色；每帧 GCE disposal=2（绘帧前恢复背景=透明）；全尺寸帧 + LZW 子块；帧延迟与循环次数须与 JSON 清单对齐（120ms / loop=0）
- 11-11 文案合规：正文无任何裸域名（no-http 校验通过），无 GitHub 界面截图，仓库引用只写 pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool 三个仓库名并要求「按仓库名搜同名项目」
- 11-10 笔记已过审并开始有数据：143 曝光 / 评论 0 / 赞 5 / 收藏 4 / 分享 0；11-09 笔记 137 / 0 / 9 / 12 / 2（较昨日 +9 曝光、+1 赞）
- 11-11 推广数据（Cloudflare 账号级，未触发 Turnstile）：近 24 小时 Requests 48（环比 -87.0%）、Visits 6（0.0%）、Bandwidth 219.08 kB（-82.0%）；国家 NL 98 / US 16 / FI 7 / TW 2；加密请求 46（95.83%）、加密带宽 183.23 kB（83.64%）；缓存命中 2（4.17%）
- 11-11 推广数据（Cloudflare 近 7 天）：Requests 482（-3.8%）、Visits 39（-39.1%）、Bandwidth 2.33 MB（-15.9%）；国家 US 691 / NL 175 / DE 22 / FI 19 / PL 12 / UK 11 / SE 10 / SG 7 / TW 7 / CH 7 / UA 5 / FR 2；加密请求 379（78.63%）、加密带宽 2.22 MB（95.20%）；24h 跌幅主要来自 11-10 的 US 抓取高峰回落，访客数仍在个位数
- 11-11 GitHub 四仓（pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-site）star 均 0，与 11-10 持平；pixel-art-site 页面直连 SSL 失败，改用 `api.github.com/repos/...` 取到 stars=0 / forks=0
- 11-11 小红书创作者中心（统计周期 11-04~11-10）：曝光 5,273（环比 +245%）、观看 496（+197%）、封面点击率 10%（-13%）、平均观看时长 18 秒（+63%）、观看总时长 2.2 小时（+377%）、视频完播率 0%；发布数 4、互动数 52、主页访客 22、涨粉 1；总粉丝 94（新增 0、流失 0），男 47% / 女 53%
- 11-11 推广待办（本周四项）仍全部未执行：V2EX 首帖、B站 1 分钟演示视频、GitHub README demo GIF + star badge、掘金技术博客
- 11-11 环境风险：C 盘仅剩 425 MB（已用 96.5 GB），当日按 L1 白名单清理 %TEMP% / Windows\Temp / D3DSCache / NVIDIA 着色器缓存仅释放约 5 MB（浏览器占用导致大部分临时文件删不掉）；大占用仍为 DoubaoWork 5.33 GB、Chrome User Data 1.04 GB、Edge 290 MB，只报告未动
- 11-11 磁盘不足已实际打断执行一次：11-10 收尾的 `Remove-Item` 报 `no space on device (system_error=28)` 致设备离线；本日复核遗留项——`_block_1110.md` / `_append_1110.md` 两个临时草稿已删净（Test-Path=false），`今日运营简报_20261110.md` 7,167 B 在位
- git 状态：本区块单独提交 CHANGELOG.md 后推送 origin/main（scenes/* 删除、.wrangler/、*.mp4 等既有改动均非本次产物，不纳入提交）

---

## [Unreleased] — 2026-11-10

### Notes
- 11-10 无代码功能迭代（当日为运营与发布日，四仓无代码提交）
- 小红书登录态正常（连续第 36 天可用）：通知页、图文发布页、笔记管理页、创作者数据页、粉丝数据页均可直接访问，无登录重定向
- 11-10 评论核查：通知页「评论和@」仍为原 3 条——Spark 追问「哪里可以选择动作模板呢」（昨天 09:17，11-09 已回复并确认为我方第 4 条评论）、Spark「原评论已删除」系统提示、Spark 6 天前原评论；同页另有旧通知「一面千识 10-08 私信哈」「大话游 09-29 后台dd」；当日新评论 0、已回复 0、待回复 0
- 11-09 整改版笔记已过审：`6af134100000000034018f2c`（《Godot/Unity都能批量像素化⚔️》）在笔记管理页已无「审核中」标记，数据 曝光 128 / 评论 0 / 赞 8 / 收藏 12 / 分享 2（重投后恢复展示，正文「仅写仓库名」的改写通过了审核）
- 11-10 发布小红书图文笔记（A 效果展示型，对应 7 天日历 D5「Unity 编辑器窗口批量导出演示」）：标题《Unity编辑器一键批量像素化⚔️》（17 字），4 图，原创声明已开启，正文 659 字（含 8 个话题标签）
- 11-10 发布结果：创作平台返回「发布成功」页；笔记管理页首条「审核中 / Unity编辑器一键批量像素化⚔️ / 2026-11-10 14:34 / 曝光 0·评论 0·赞 0·收藏 0·分享 0」，全部 21 篇；noteId `6af2bae10000000026024ea6`（从修改页 URL publish/update?id=... 取到）
- 11-10 新增素材目录 xiaohongshu_20261110：build_images.py（PIL）生成 4 张成图——1080×1440 封面、1080×1300 四角色上下对比、1080×1000 单角色前后对比、1600×416 工具窗口 2 倍图；版式为暖白纸底（BG 242,238,227）＋ 与素材底色一致的卡片（PANEL 184,185,168），消除深色卡片与米白素材的拼接硬边
- 11-10 配图为真实跑批产物，非示意图：`python scripts/pixelate.py examples/characters/{bone,palm,orbs,ghost}.png batch_final --grid 48 --colors 24 --scale 6 --no-outline`，输出 288×456 / 288×396 / 288×318 / 288×330 RGBA；四张成图与 batch_final 全部逐张目视通过
- 11-10 参数试错记录（同一批暗色角色素材的可用区间）：32 格 / 16 色 → 脸部糊成一块；64 格 / 32 色（带描边）→ 描边过重；96 格 / 48 色（带描边）→ 颗粒偏细、不像像素画；48 格 / 24 色 / 6 倍 / 关描边 → 颗粒度与角色辨识度平衡最好，最终采用
- 11-10 死路复核：`chroma_key.py --mode white --tolerance 25`（阈值 255-25*4=155）对 examples/characters 的 184-185 灰白底无效，整幅被误删只剩碎片，该批素材做透明底不可行，改走「保留原底 + 卡片同色」的版式
- 11-10 图文发布流程踩坑：①「上传图文」点 box ref 报 `BU_TARGET_OBSCURED`，报错信息直接给出遮挡元素为 span（本次 ref n153），改点 span 才切换成功（URL 变为 &from=tab_switch）；② `input[type="file"]` + upload_file 逐张传 4 图，间隔 3s，页面计数 4/18；③ 标题 `textbox "填写标题会有更多赞哦"`，正文 `.tiptap.ProseMirror` 须 click → ctrl+a → Backspace 清空后一次性 type，回读 659 字；④ 原创声明：点 `.original-wrapper .d-switch` 后弹《原创声明须知》→ 勾「我已阅读并同意」→ 点「声明原创」→ 弹层关闭；开关真值看内层 `input[type=checkbox][checked]` 与 `.d-switch-simulator.checked`（`d-switch` 外层 class 不反映状态）；⑤ 笔记管理页卡片默认无链接，须 hover 才出现操作图标，点第 2 个 `.note-card__action-btn`（编辑）才会跳到 publish/update 并暴露 noteId
- 11-10 文案合规：严格遵守 11-09 判罚结论——正文无任何裸域名（no-http 校验通过）、无 GitHub 界面/logo 截图，仓库引用只写三个仓库名并要求「按仓库名搜同名项目」，可点入口留在个人主页
- 11-10 推广数据（Cloudflare 账号级，本次未触发 Turnstile）：近 24 小时 Requests 369（+12200%）、Visits 6（+500%）、Bandwidth 1.22 MB；近 7 天 Requests 450（-23.2%）、Visits 43（-27.1%）、Bandwidth 2.32 MB（7 天请求集中在 United States 710 次量级，属爬虫/扫描流量，非真实读者）
- 11-10 GitHub 四仓（pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-site）star 均 0，与 11-09 持平，无新增
- 11-10 小红书创作者中心（统计周期 11-03~11-09）：曝光 5,149（环比 +3714%）、观看 503（+7085%）、封面点击率 10.3%（+128%）、平均观看时长 15 秒（+28%）、观看总时长 2 小时、视频完播率 0%；发布数 4、互动数 48、主页访客 20；总粉丝 93（新增 0、流失 0）
- 11-10 推广待办（本周四项）仍全部未执行：V2EX 首帖、B站 1 分钟演示视频、GitHub README demo GIF + star badge、掘金技术博客
- git 状态：本区块单独提交 CHANGELOG.md 后推送 origin/main（未跟踪的 .wrangler/、各类 mp4 与 _check/ 目录均非本次产物，不纳入提交）

---
## [Unreleased] — 2026-11-09

### Notes
- 11-09 无代码功能迭代（当日为运营与发布日，代码仓库无变更）
- 小红书登录态正常（连续第 35 天可用）：通知页、图文发布页、笔记管理页、创作者数据页均可直接访问，无登录重定向
- 11-09 评论核查：通知页「评论和@」新增 1 条——Spark 追问「哦 那可能是我没有注意到 在哪里可以选择动作模板呢？」（1 小时前，福建），针对 11-03 笔记《3步把立绘变成像素攻击动画⚔️全开源》（noteId 6ae988fb000000000f01e11e）的动作模板入口
- 11-09 已用评论级回复控件回复（非笔记级评论框）：说明网页版顶部「动画」标签 → 上传立绘 → 动作模板列表，并给出 README「Action templates」章节与网页版入口 https://andrewlff.github.io/pixel-art-site/ ；回复已在笔记详情页确认为第 4 条评论（共 4 条：Spark 原评论 / 我方 11-07 澄清 / Spark 追问 / 我方本次回复），站内状态「刚刚·广东」
- 11-09 当日互动：新评论 1、已回复 1、待回复 0；同页另有 1 条「评论了你的笔记 / 原评论已删除」系统提示，无正文，记录不回复
- 11-09 发布小红书图文笔记（D 开源更新型，对应 7 天日历 D4「引擎原生插件·批量像素化」）：标题《Godot/Unity都能批量像素化⚔️》（18 字），6 图（封面 1080×1440 + godot/unity 两仓 docs/preview.png + 三张 README 截图），正文 839/1000 字，原创声明已开启
- 11-09 发布结果：创作平台返回 `published=true`；笔记管理页首条「审核中 / Godot/Unity都能批量像素化⚔️ / 2026-11-09 10:46 / 曝光 5·评论 0·赞 0·收藏 0·分享 1」，全部 20 篇。noteId 尚未取到（审核中卡片无 noteId 链接，列表页 HTML 无内嵌 noteId），待过审后补录
- 11-09 新增素材目录 xiaohongshu_20261109：build_cover.py（PIL）生成 1080×1440 3:4 封面（深底 #11131C + 青绿标题 + 960 宽 preview 三联图 + sample 8 倍最近邻放大），素材取自两仓 docs/preview.png（800×208、8,977 B）与 tests/sample.png（64×48、3,411 B）
- 11-09 图文页发布流程记录（与视频页的差异）：① 图片走 `input[type="file"]` + `upload_file` 一次传 6 张，页面计数 6/18；② 标题 `textbox "填写标题会有更多赞哦"` 直接 type；③ 正文 `.tiptap.ProseMirror` 首次写入超限（1,134 字 / 计数 1,066），须 click 正文 → ctrl+a → Backspace 清空 → 一次性 type 精简版（909 字 / 计数 839）；④ 原创声明入口是 `.original-wrapper .d-switch`（点外层 box 无效，会先被「图片可以编辑啦」新手引导遮挡，需先点「我知道了」），拨开后弹《原创声明须知》→ 勾「我已阅读并同意」→「声明原创」按钮由 disabled 变可用 → 关闭弹层；开关真值看内层 `input[type=checkbox][checked]`
- 11-09 推广数据（小红书创作者中心，统计周期 11-02~11-08）：曝光 3,909（环比 +3299%）、观看 365（+4462%）、封面点击率 9.8%（+38%）、平均观看时长 12 秒（+15%）、观看总时长 1.3 小时（+4416%）、视频完播率 0%；互动 点赞 11 / 评论 3 / 收藏 12 / 分享 2；总粉丝 93（新增 0、流失 0）；主页访客 16；发布数 3；互动数 26
- 11-09 GitHub 四仓（pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-site）star 均 0，与 11-08 持平，无新增
- 11-09 Cloudflare 数据未取到：dash.cloudflare.com 连续两次进入「正在进行安全验证」Turnstile 页（Ray ID a5797efc98f3fcba / a57983f5ff23fcba），已按登录/验证交接流程请求人工验证，用户本轮跳过，24h / 7d UV 与请求量为空档
- git 状态：本区块单独提交 CHANGELOG.md 后推送 origin/main
- **11-09 复核（当日第二轮）**：今日笔记在 10:57 被判定「未通过」，处置为「限制推荐和搜索展示，广告投放与蒲公英流量不受影响」；存在问题类型为「笔记存在外部平台信息或联系方式 / 文本违规」，违规内容直接点名正文里三行 github.com/andrewlff/... 仓库地址，另提示图6 为仓库首页截图
- **11-09 整改并重新送审**：删除图5（Unity 仓库首页）、图6（Godot 仓库首页）两张 GitHub 界面截图，保留封面 + godot_preview + unity_preview 共 3 图；正文去掉全部站外 URL，仓库引用改为「按仓库名搜同名项目」的纯文本（godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-action-frames），字数 829；原创声明仍开启；提交后状态回到「审核中」，数据保留 曝光 37 / 评论 0 / 赞 3 / 收藏 2 / 分享 1
- **11-09 noteId 已补**：6af134100000000034018f2c（从修改页 URL publish/update?id=... 取到，此前记为「待补」）
- **经验**：小红书正文不接受裸 github.com 域名（即使不带 http:// 前缀），也不接受含 GitHub 界面/logo 的截图；开源项目引流只能写「仓库名/项目名」纯文本，把可点击入口留在个人主页与评论区
- **11-09 二轮评论核查**：通知页仍为原 3 条（Spark 追问 5 小时前、原评论已删除、5 天前的原评论），无新增评论，已回复状态保持

---
## [Unreleased] — 2026-11-08

### Notes
- 11-08 无代码功能迭代（当日为运营与发布日，代码仓库无变更）
- 小红书登录态正常（连续第 34 天可用）：通知页、视频发布页、笔记管理页、创作者中心均可直接访问，无 401 / 登录重定向
- 11-08 评论核查：通知页「评论和@」无新增评论，最新一条仍是 Spark（4 天前，11-07 已回复澄清）；当日新评论 0、已回复 0、待回复 0
- 11-08 发布小红书视频笔记（C 演示视频型，对应 7 天日历 D3「角色图→图集→GIF 全流程」）：标题《立绘3步变像素攻击动画⚔️开源》（15 字），视频 demo_video.mp4（1080×1920、00:00:36、1,295,759 B），原创声明已开启
- 11-08 发布结果：note ID 6af015e4000000001a01776b，发布时间 2026-11-08 14:25，状态「审核中」，封面待 PK；公开链接 https://www.xiaohongshu.com/explore/6af015e4000000001a01776b?xsec_token=ABqm5cts0QUkfaSwhMgYkjPneRNa_ZFCxBuT9aLCx7naA=&xsec_source=pc_user
- 11-08 发布流程（视频页与图文页差异，踩坑）：视频页标题是 `input[placeholder="填写标题会有更多赞哦"]`（ref n54），正文是 `.tiptap.ProseMirror` contenteditable；点正文后直接 type 全文会把追加的标签插到光标落点（本次曾插进主仓库 URL 中间，造成 `https://github.com/andrew` + 标签 + `lff/...` 断链）。正确做法：click 正文 → ctrl+a → Backspace 清空（innerText 长度归 1）→ 一次性 type 完整正文（含末尾 8 个标签）→ press Escape 关闭话题联想，回读 innerText=612 字并逐行校验 URL 完整
- 11-08 推广数据（Cloudflare）：账号级近 24 小时 Requests 14（-22.2%）、Visits 6（-33.3%）、Bandwidth 235.14 kB；近 7 天 Requests 126（-84.1%）、Visits 38（-56.3%）、Bandwidth 1.23 MB。Pages 项目页 `/pages/view/pixel-art-site` 仍停在 Loading，单项目 UV 无法读取，只能用账号级口径
- 11-08 GitHub 四仓（pixel-art-action-frames / godot-pixel-batch-tool / unity-pixel-batch-tool / pixel-art-site）star 均 0，与 11-07 持平，无新增
- 11-08 小红书创作者中心（统计周期 11-01~11-07）：关注 247 / 粉丝 93 / 获赞收藏 188；曝光 3,713（环比 +2610%）、观看 354（+4957%）、封面点击率 9.9%、视频完播率 0%、点赞 11、评论 3、收藏 12、分享 2、净涨粉 0、主页访客 14
- git 状态：本区块单独提交 CHANGELOG.md 后推送 origin/main

---
## [Unreleased] — 2026-11-07

### Notes
- 11-07 无新增功能迭代（当日为运营与发布日，代码仓库无变更）
- 小红书登录态正常：通知页、笔记详情页均可直接访问，无 401 / 登录重定向
- 11-07 评论回复：Spark 反馈「该项目包含切图、抽帧、去背景，但不包含生成系列动作帧」属对工具范围的误解，已回复澄清——动作帧生成是主功能，单图模式里的切图/抽帧/去背景是其它工具，动作帧在同一页的动画标签；附主仓库与网页版链接。回复已在笔记详情页确认可见（共 2 条评论）
- 11-07 发布小红书图文笔记（A 效果展示型）：《一张图4种像素风⚔️参数全公开》，5 图（1 张 3:4 参数对比封面 + 4 张裁切图）
- 新增配图构建脚本 xiaohongshu_20261107/build_cover.py：从 demo_shots 整页截图自动裁出像素画布，最近邻缩放拼成 3:4 对比封面，避免黑边过多
- 11-07 发布结果：笔记 note ID 6aeec5a90000000015009ad3，发布成功（创作平台 `published=true`，随后个人主页可见），公开链接 https://www.xiaohongshu.com/explore/6aeec5a90000000015009ad3?xsec_token=ABd2D0gI8k4p0-asMICxkd2xWx37n32UyGG27VoCvFOHs=&xsec_source=pc_user
- 11-07 发布流程记录（踩坑）：原创开关拨开后必须先过《原创声明须知》确认弹层（勾"我已阅读并同意"→"声明原创"按钮才从 disabled 变 enabled），否则点"发布"会被弹层遮挡（BU_TARGET_OBSCURED）

---
## [Unreleased] — 2026-11-03

### Notes
- 小红书登录态恢复（10-04 起失效 30 天后，11-03 确认通知页/消息页正常），评论回复与笔记发布恢复执行
- 11-03 评论回复：世界有点灵（"这是什么软件呀～急需"）、奶芙饼饼（"哪里"）均已回复 Pixelizer 网页版+仓库链接
- 11-03 发布小红书图文笔记（B 教程干货型：3 步立绘→像素攻击动画）
- git 状态：补推 11-01（f09c83b）/10-31（cde9837）两个滞留区块

---
## [Unreleased] — 2026-11-01

### Notes
- 11-01 无新增功能迭代
- 小红书登录态自 10-04 起连续 29 天失效（11-01 复核确认 401），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：10-31 区块（cde9837）滞留本地 ahead 1（push Connection reset）；10-30 区块（0df4b54）已同步远程

---
## [Unreleased] — 2026-10-31

### Notes
- 10-31 无新增功能迭代
- 小红书登录态自 10-04 起连续 28 天失效（10-31 复核确认 401），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：10-30 区块（0df4b54）已推送成功，origin/main 同步，ahead 0

---
## [Unreleased] — 2026-10-30

### Notes
- 10-30 无新增功能迭代
- 小红书登录态自 10-04 起连续 27 天失效（10-30 复核确认 401），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：10-24/10-25/10-26 区块（e3029b8、e2b48ab、da7a4e0）滞留本地 ahead 3（github.com:443 连续超时/被重置）；10-23 区块与用户 1f4d0d2 已同步远程

---
## [Unreleased] — 2026-10-26

### Notes
- 10-26 无新增功能迭代
- 小红书登录态自 10-04 起连续 23 天失效（10-26 复核确认 401），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：10-24/10-25 区块（e3029b8、e2b48ab）滞留本地 ahead 2（push 连接超时/被重置）；10-23 区块与用户 1f4d0d2 已同步远程

---
## [Unreleased] — 2026-10-25

### Notes
- 10-25 无新增功能迭代
- 小红书登录态自 10-04 起连续 22 天失效（10-25 复核确认 401），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：10-24 区块（e3029b8）滞留本地 ahead 1（push 连接被重置）；10-23 区块与用户 1f4d0d2 已同步远程

---
## [Unreleased] — 2026-10-24

### Notes
- 10-24 无新增功能迭代（10-23 已由用户提交 dithering/调色板预设等 v2.2 功能）
- 小红书登录态自 10-04 起连续 21 天失效（10-24 复核），评论回复、笔记发布、求职私信核查继续暂停
- git 状态：用户深夜已推送 1f4d0d2（About 面板合并 sponsor 入口 + 点击复制钱包地址），本地与 origin/main 同步

---
## [Unreleased] — 2026-10-23

### Added
- 抖动（Dithering）：Floyd–Steinberg 误差扩散、Bayer 4×4、Bayer 8×8 有序抖动，可在侧栏切换
- 调色板预设：1-Bit、Game Boy、PICO-8、Sweetie 16、DawnBringer 16、Commodore 64
- 色板导入：解析 GIMP/Aseprite `.gpl` 与 Lospec `.hex`，导入后可直接应用到多帧
- 色板预览色块与颜色数显示；`Export .gpl` 在自动取色时也可导出当前首帧色板
- 404 页面：未知路径不再由 SPA fallback 返回 200/index.html

### Changed
- 顶栏「❤ 赞助我」的 prompt 弹窗入口并入 About 面板，钱包地址改为点击即复制（带已复制反馈）
- 多帧色板统一：`Auto · lock to first frame` 用首帧色板预先锁定，处理当次即生效（此前需再触发一次渲染）
- 抖动的背景处理改为先去背再量化，避免误差扩散把背景色带进角色边缘
- 更新日志弹窗与 About 版本号升至 v2.2

### Notes
- 2026-10-22 深夜 Cloudflare Web Traffic 中的 597 次请求经核查为自动化漏洞扫描（SG/DE/NL 云 IP、空 UA、随机路径、`.env`/`phpinfo` 探测），不是真实访客；已启用 Cloudflare Web Analytics 开始积累可用的 PV/UV
- 真实人类访问量此前没有统计口径，后续以 Web Analytics 为准；GitHub Pages 域名（小红书笔记中使用）目前未被 beacon 覆盖
- 小红书登录态自 10-04 起连续 20 天失效（10-23 复核），评论回复、笔记发布、求职私信核查继续暂停

---
## [Unreleased] — 2026-10-22

### Notes
- 10-22 无新增功能迭代（10-21 无本轮记录）
- 小红书登录态自 10-04 起连续 19 天失效，评论回复、笔记发布、求职私信核查继续暂停
- git 10-20 commit a382a2f 仍滞留本地（github.com:443 push 超时），10-22 本轮将尝试补推

---## [Unreleased] — 2026-10-20

### Notes
- 10-20 无新增功能迭代（10-18、10-19 无本轮记录）
- 小红书登录态自 10-04 起连续 17 天失效，评论回复、笔记发布、求职私信核查继续暂停
- git 自 10-17 网络恢复后与 origin/main 同步，本次仅追加日志

---## [Unreleased] — 2026-10-17

### Notes
- 10-17 无新增功能迭代
- 小红书登录态自 10-04 起连续 14 天失效，评论回复、笔记发布、求职私信核查继续暂停
- git push 仍失败（github.com:443 连接超时），c1594db 区块滞留本地（ahead 4），等网络恢复一并推送

---## [Unreleased] — 2026-10-16

### Notes
- 10-16 无新增功能迭代
- 小红书登录态自 10-04 起连续 13 天失效，评论回复、笔记发布、求职私信核查继续暂停
- git push 仍失败（github.com:443 连接超时，第 4 次），29497fa 区块滞留本地（ahead 3），等网络恢复一并推送

---## [Unreleased] — 2026-10-15

### Notes
- 10-15 无新增功能迭代
- 小红书登录态自 10-04 起连续 12 天失效，评论回复、笔记发布、求职私信核查继续暂停
- git push 第 4 次失败（github.com:443 连接超时），e5580fb + 06ce9d4 两个区块仍滞留本地（ahead 2），等网络恢复一并推送

---## [Unreleased] — 2026-10-14

### Notes
- 10-11~10-14 无新增功能迭代
- 小红书登录态自 10-04 起连续 11 天失效，评论回复、笔记发布、求职私信核查全部暂停
- 10-10 区块 commit e5580fb 此前因 GitHub 网络不通未能 push，10-14 复核仍待推送（本次一并推送）

---
## [Unreleased] — 2026-10-10

### Notes
- 10-09/10-10 无新增功能迭代
- 小红书登录态自 10-04 起连续 7 天失效，评论回复与笔记发布暂停中
- GitHub 仓库与远端同步正常（最近 commit fab2233 已推送）

---
## [Unreleased] — 2026-10-08

### Notes
- 国庆假期结束（10-01~10-07），期间无新功能迭代
- 小红书登录态自 10-04 起持续失效，评论回复与笔记发布暂停中
- GitHub 仓库与远端同步正常（最近 commit 36124c1 已推送）

---
## [Unreleased] — 2026-10-07

### Notes
- 10-05/10-06 无新增功能迭代（国庆假期，无产出）
- 补推积压 commit：09-30 / 10-01 / 10-04 三次提交此前因 GitHub 网络不通未能 push，10-07 网络恢复后全部推送成功（86b9b02..9f4e124）

---
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

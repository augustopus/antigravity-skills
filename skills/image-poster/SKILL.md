---
name: image-poster
description: >-
  Use when the user asks to generate, create, design, edit, or iterate on images,
  illustrations, UI mockups, icons, wallpapers, concept art, logos, or visual assets.
  Specifically excels at converting real photos (cityscapes, landscapes, architecture, street scenes)
  into minimalist editorial art posters with Japanese-Scandinavian design, soft gouache texture,
  painterly feathered edges, and integrated Swiss typography.
---

# 艺术海报与图像生成技能 (Image Poster Skill)

本技能指导如何利用 `generate_image` 工具将现实照片（城市、建筑、街头、风景）转化为顶级艺术出版物级别的极简艺术海报，并自动归档至本地。

---

## 核心标准：照片转高级艺术海报 (Photo to Editorial Art Poster)

任何时候用户提供照片转海报，均**默认且严格遵循**以下沉淀的标准范式：

### 1. 整体风格定位 (Aesthetic Definition)
- **风格关键词**: `minimal editorial poster, poetic City illustration, contemporary art book aesthetic, Scandinavian minimalism, Japanese editorial design, soft gouache illustration, abstract cityscape, quiet luxury poster, refined print design`
- **视觉氛围**: 独立艺术杂志内页、城市旅行摄影集、当代艺术书籍封面、博物馆商店精品画作。整体克制、宁静、诗意、高级，充满高品质纸张与哑光印刷质感。

### 2. 画面边缘处理：自然手绘晕染 (Painterly Feathered Edges)
- **拒绝硬框**: 严禁生硬的矩形裁剪框与死板硬边。
- **自然边界**: 画面边界采用**干画笔渐变 (Dry-brush Fade)** 与**水粉水渍自然扩散 (Gouache Bleed)** 效果，使插画边缘自然溶解过渡至底层的暖象牙白纸面，呈现冷压棉浆水彩纸上的手工绘画边缘 (Deckle edge / Organic painted vignette)。

### 3. 画幅、构图与留白 (Composition & Margins)
- **比例匹配**: 默认匹配输入照片的纵横比（竖幅优先使用 `2:3` 或 `3:4`；横幅使用 `4:3` 或 `16:9`）。
- **舒展留白**: 四周保留适度温润的**暖象牙白留白 (Warm Ivory Margins)**，画面主体向四周自然延展，既有呼吸感又不显空旷。

### 4. 极简文字排版与信息来源 (Typography & Metadata Rules)
- **城市名称与坐标来源优先级**：
  1. **GPS 元数据优先**：优先读取图片文件的 EXIF / GPS 记录（可运行脚本 `python3 ~/.gemini/config/skills/image-poster/scripts/extract_gps.py <image_path>` 获取精确经纬度与定位城市）。
  2. **画面内容推断**：若无 GPS 记录，则根据视觉内容识别具体地标/城市（如辨识出国王十字区 Kings Cross 则使用伦敦坐标，辨识出柏林地标则使用柏林坐标）。
- **排版位置**: 位于画面上方留白较多的区域。
- **图文自然交融**: **允许且鼓励文字与画面上方柔和的水粉渐变/建筑阴影产生自然接触与交织 (Seamless Touch/Overlap)**，形成现代杂志封面的层次感。
- **主标题 (City/Main Title)**: 
  - **经典复古风 (推荐)**：高对比度古典衬线体 (`Vintage High-Contrast Serif`，如 Didot / Bodoni / Classical Roman 风格)，具有永恒的博物馆与高级出版物优雅感。
  - **现代极简风**：北欧 / 瑞士洗练无衬线粗体 (`Modern Bold Sans-serif`)。
- **副标题与注释 (Subtitles & Coordinates)**: 细字重全大写，包含主题概括与地理坐标（如 `KINGS CROSS STEPS & URBAN GEOMETRY / 51.5308° N, 0.1238° W`）。
- **文字取色**: **严格提取自插画中最深沉的主体色**（如 `Deep Muted Navy`, `Charcoal Smoky Slate`），确保与画面色彩浑然一体。

### 5. 抽象化概括规则 (Abstraction Principles)
- **严禁机械临摹与逐像素复刻**，提炼最具辨识度的地标几何形态：
  - **建筑与主体**: 简化为纯粹优雅的几何色块组合。
  - **人物/涂鸦/雕塑**: 提炼为极简色块剪影，保留核心特征（如特色服饰、色彩点缀）。
  - **远景/天际线/桥梁**: 压缩为细小利落的水平矩形色带与极细线条。
  - **云层与天气**: 化为柔软的横向水粉/水彩笔触。
  - **点缀光火**: 稀疏克制的小型暖黄光斑（Warm Ochre）或极简小新月。

### 6. 色彩与材质体系 (Low-Saturation Palette & Texture)
- **严格低饱和度 (Strictly Low Saturation)**，沉稳克制：
  - **底纸基调**: `warm ivory, soft beige` (暖象牙白冷压纸底色)
  - **建筑与阴影**: `smoky grey, blue grey, muted navy, deep charcoal slate`
  - **点缀暖色**: `warm ochre, subdued mustard yellow, dusty muted rose pink, muted teal`
- **材质肌理**: `soft gouache, dry brush texture, watercolor-like opacity, subtle cold-press paper grain, hand-painted editorial illustration, matte printed texture`。

### 7. 严格负面约束 (Negative Constraints)
- ❌ **坚决避免**: 生硬矩形裁切硬边 (hard crop frame)、黑粗描边 (harsh outlines)、卡通动漫风 (cartoon/anime)、赛博朋克霓虹 (cyberpunk neon)、3D建模渲染 (3D render/CGI)、矢量扁平图标感 (vector icon)、商业广告喧闹感 (commercial clutter)、高光廉价 AI 塑料感 (glossy plastic AI look)。

---

## 终极专用 Prompt 标准模版

```text
A minimal editorial art poster and poetic illustration based on the reference photo, in the aesthetic of contemporary art book and Japanese-Scandinavian editorial design. Abstract scene with architecture and landmarks simplified into clean geometric color blocks, distant structures compressed into delicate small rectangular silhouettes, soft horizontal gouache brushstrokes, and minimal elegant lines. The edges of the illustration are organically feathered and blended into the warm ivory background with soft dry-brush washes and watercolor bleed (no hard rectangular crop or frame). In the upper area, minimalist typography features a bold modern sans-serif city title and subtle uppercase subtitle with coordinates, with the text subtly touching/overlapping the upper painted washes. Typography color is strictly picked from the darkest muted navy/charcoal of the illustration. Hand-painted soft gouache and dry brush texture, subtle watercolor opacity, visible natural cold-press paper grain, matte printed finish. Palette: warm ivory base, soft beige, concrete smoky grey, muted navy, dusty muted rose, muted teal, and low-saturation warm ochre. Generous balanced negative space, quiet luxury, serene, poetic, museum exhibition print, vertical editorial composition, no harsh outlines, no 3D render, no cartoon, no commercial clutter.
```

---

## 工具调用与默认归档工作流

### 1. 工具调用示例

```json
{
  "ImageName": "city_editorial_poster",
  "AspectRatio": "2:3",
  "ImagePaths": ["/path/to/user_photo.jpg"],
  "Prompt": "应用上述终极专用 Prompt 标准模版，并结合具体照片地标特征进行定制"
}
```

### 2. 自动保存与本地归档规范
- 生成完成后，**必须立即同步保存/归档一份到用户的桌面 `~/Desktop/AI/` 目录**（使用 `run_command` 配合 `BypassSandbox: true`）。
- 命名规范示例：`~/Desktop/AI/<city_name>_art_poster.jpg`。
- 在响应中展示图片并附带优雅的排版点评与设计解析。

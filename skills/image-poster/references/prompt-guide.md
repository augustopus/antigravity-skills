# 图像提示词工程与风格参考指南 (Prompt Engineering Guide)

高质量图像生成依赖于精细、结构化的描述词。本文档详细记录了已固化的极简艺术海报标准及通用风格词库。

---

## 固化标准：照片转高级艺术海报 (Photo to Editorial Art Poster Standard)

任何时候执行照片转海报，默认使用此终极模版与参数体系：

### 1. 核心提示词模版 (Master Prompt Template)
```text
A minimal editorial art poster and poetic illustration based on the reference photo, in the aesthetic of contemporary art book and Japanese-Scandinavian editorial design. Abstract scene with architecture and landmarks simplified into clean geometric color blocks, distant structures compressed into delicate small rectangular silhouettes, soft horizontal gouache brushstrokes, and minimal elegant lines. The edges of the illustration are organically feathered and blended into the warm ivory background with soft dry-brush washes and watercolor bleed (no hard rectangular crop or frame). In the upper area, minimalist typography features a bold modern sans-serif city title and subtle uppercase subtitle with coordinates, with the text subtly touching/overlapping the upper painted washes. Typography color is strictly picked from the darkest muted navy/charcoal of the illustration. Hand-painted soft gouache and dry brush texture, subtle watercolor opacity, visible natural cold-press paper grain, matte printed finish. Palette: warm ivory base, soft beige, concrete smoky grey, muted navy, dusty muted rose, muted teal, and low-saturation warm ochre. Generous balanced negative space, quiet luxury, serene, poetic, museum exhibition print, vertical editorial composition, no harsh outlines, no 3D render, no cartoon, no commercial clutter.
```

### 2. 关键参数设定清单
- **信息来源**: 优先从图片文件的 EXIF / GPS 获取精确坐标与拍摄地城市；若无则根据画面视觉内容识别地标与城市。
- **排版交互**: 顶部古典衬线体 (Didot/Bodoni) 或现代无衬线粗体城市名 + 细体坐标，**文字与画面上方水粉晕染自然交织重叠**，文字取色为画面最深藏青/烟灰色。
- **色彩控制**: **严格低饱和** (`strictly low saturation`)，禁止高饱和鲜艳刺眼色调。
- **质感要求**: `soft gouache, dry brush, subtle paper grain, cold-press art paper, matte print`。

---

## 通用提示词词汇库 (Vocabulary Library)

### 1. 镜头与构图 (Camera & Composition)
- `Generous warm ivory negative space, quiet luxury, poetic and airy balance`
- `Organic feathered vignette border, natural deckle edge transition`
- `Swiss modernist layout, Bauhaus-inspired balanced typography`

### 2. 质感与纸张肌理 (Texture & Paper Finish)
- `Cold-press cotton watercolor paper texture, visible subtle fibers`
- `Soft gouache wash, dry-brush scumbling, matte fine-art exhibition print`
- `Subdued natural daylight, velvety matte surface`

### 3. 色彩配方 (Muted Palette Formulas)
- `Warm Ivory (#FDFBF7), Soft Sand Beige (#E8E2D5)`
- `Smoky Concrete Grey (#8F9499), Blue Grey (#6C7A89)`
- `Deep Muted Navy (#2C353F), Charcoal Slate (#343A40)`
- `Subdued Warm Ochre (#C99E5C), Dusty Muted Rose (#D4A5A5), Muted Teal (#6B9080)`

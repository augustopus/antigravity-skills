# 图像多轮迭代与编辑指南 (Image Iteration & Editing Guide)

在实际使用中，用户常常需要对已生成的图片进行微调、重绘局部、调整风格或变换场景。本指南规范多轮生图与图生图 (Image-to-Image) 的最佳实践。

---

## 一、以图生图 (ImagePaths) 使用机制

当使用 `generate_image` 的 `ImagePaths` 属性时：
- 最多支持传入 **3 张图片** 的绝对路径。
- 模型会读取参考图的构图、主体特征、配色或布局，并根据新的 `Prompt` 进行生成或重绘。

```json
{
  "ImageName": "hero_banner_sunset_v2",
  "AspectRatio": "16:9",
  "ImagePaths": [
    "/Users/augustopus/.gemini/antigravity/brain/130cb197-f4c0-4274-9881-c68257787380/hero_banner_daytime.png"
  ],
  "Prompt": "Modify the reference image: transform the daytime sky into a dramatic golden hour sunset, keep the futuristic skyscraper architecture and flying vehicles unchanged, add warm orange and purple reflections on the glass facade."
}
```

---

## 二、常见迭代模式与提示词技巧

### 1. 场景/光影变动 (保持主体一致)
- **技巧**: 在 Prompt 中先说明“保持主体一致 (Keep the main subject from reference)”，再指定光影、季节或时间的变化。
- **提示词示例**:
  `Based on reference image, maintain the same character design and posture, but change the setting from a sunny forest to a snowy blizzard at twilight with soft blue and silver lighting.`

### 2. 元素增删与局部替换 (Add / Remove / Replace)
- **技巧**: 明确指出要添加或修改的具体物体，并维持原画风。
- **提示词示例**:
  `Based on reference image, keep the character and background identical, but add round vintage wire-rimmed glasses to the character's face and a cup of steaming coffee in their hand.`

### 3. UI 界面方案迭代 (UI Wireframe & Mockup Variations)
- **技巧**: 指定哪张卡片或模块需要更新，或者请求不同主题模式（如 Dark mode -> Light mode）。
- **提示词示例**:
  `Based on the reference UI dashboard layout, convert the entire interface from dark mode to a clean modern light mode with soft shadows and sky-blue accent buttons, keeping the layout structure intact.`

### 4. 风格转换 (Style Transfer)
- **技巧**: 参考原图构图与内容，但全面采用新的艺术媒介。
- **提示词示例**:
  `Redraw the scene from the reference image in the style of Studio Ghibli hand-drawn watercolor animation, with lush green landscapes and warm nostalgic atmosphere.`

---

## 三、多轮迭代命名与管理建议

为了保持文件系统清晰且易于版本回溯：
- 采用 **版本号后缀** 命名 `ImageName`：
  - 第 1 版: `login_page_v1`
  - 第 2 版（调整配色）: `login_page_v2_dark`
  - 第 3 版（调整布局）: `login_page_v3_compact`
- 在回复用户时，可以将前后两张图片进行对比展示，方便用户评估效果。

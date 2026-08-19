# 🎨 Image Poster Skill for Antigravity

A production-ready custom skill for [Google Antigravity](https://deepmind.google/technologies/gemini/) that transforms real photos into minimalist editorial art posters.

---

## ✨ Features (核心特性)

- **艺术概括 (Artistic Abstraction)**：提炼最具辨识度的地标与形态为极简几何色块，拒绝逐像素机械临摹。
- **手绘自然羽化边缘 (Painterly Feathered Edges)**：干画笔笔触与水粉水渍自然晕染扩散至象牙白纸面，彻底告别死板矩形边框。
- **低饱和克制配色 (Muted Palette)**：温润象牙白 (Warm Ivory)、烟灰、柔和藏青、暖赭石与淡雅烟粉。
- **智能地理识别与复古排版 (Smart Geo & Typography)**：
  - 优先从照片 EXIF / GPS 元数据提取经纬度与拍摄地。
  - 无 GPS 时自动进行视觉地标识别。
  - 搭配高对比度古典衬线体 (Didot/Bodoni 风格) 现代杂志排版。
- **自动本地归档 (Auto Archive)**：生成的作品自动归档至本地 `~/Desktop/AI/` 目录。

---

## ⚡ Quick Installation (一键安装)

### Option 1: One-Line Install (推荐一行命令安装)

```bash
git clone https://github.com/augustopus/antigravity-skills.git /tmp/antigravity-skills && bash /tmp/antigravity-skills/install.sh && rm -rf /tmp/antigravity-skills
```

### Option 2: Clone & Run Local Installer (克隆并运行安装脚本)

```bash
git clone https://github.com/augustopus/antigravity-skills.git
cd antigravity-skills
chmod +x install.sh
./install.sh
```

---

## 📁 Repository Structure (目录结构)

```text
.
├── LICENSE
├── README.md
├── install.sh
└── skills/
    └── image-poster/
        ├── SKILL.md
        ├── references/
        │   ├── editing-and-iteration.md
        │   └── prompt-guide.md
        └── scripts/
            └── extract_gps.py
```

---

## 📄 License

This repository is licensed under the [MIT License](./LICENSE). Free for personal and commercial use.

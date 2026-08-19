# 🌌 Antigravity Custom Skills

A collection of production-ready, high-quality custom skills for [Google Antigravity](https://deepmind.google/technologies/gemini/).

---

## 📦 Included Skills (包含的技能)

### 1. 🎨 `image-poster` (极简艺术海报生成器)
Converts real photos (cityscapes, landscapes, architecture, street scenes) into minimalist editorial art posters with Japanese-Scandinavian design, soft gouache texture, painterly feathered edges, and integrated Swiss typography.

- **核心特性**：
  - **艺术概括**：提炼最具辨识度的地标与形态为极简几何色块，拒绝机械临摹。
  - **手绘自然羽化边缘**：干画笔笔触与水粉水渍自然晕染扩散至象牙白纸面，摆脱死板硬框。
  - **低饱和克制配色**：温润象牙白 (Warm Ivory)、烟灰、柔和藏青、暖赭石与淡雅烟粉。
  - **智能地理识别与排版**：优先从照片 EXIF/GPS 元数据获取坐标；无 GPS 则自动进行视觉地标推断，搭配复古高对比度古典衬线体 (Didot/Bodoni) 排版。
  - **自动本地归档**：生成的作品自动归档至本地 `~/Desktop/AI/` 目录。

### 2. 🧹 `mac-disk-cleanup` (macOS 磁盘深度清理)
Smart deduplication and cleanup workflow for macOS:
- **两阶段去重**（文件大小快速预筛 + MD5 校验）。
- **专业工程保护**：自动识别并保护 Final Cut Pro (`.fcpbundle`)、DaVinci Resolve 工程与照片图库。
- **孤立 App 残留扫描**与安全交互删除工作流。

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
    ├── image-poster/
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── editing-and-iteration.md
    │   │   └── prompt-guide.md
    │   └── scripts/
    │       └── extract_gps.py
    └── mac-disk-cleanup/
        └── SKILL.md
```

---

## 📄 License

This repository is licensed under the [MIT License](./LICENSE). Free for personal and commercial use.

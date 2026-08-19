---
name: mac-disk-cleanup
description: >-
  Use when the user asks to find duplicate files, clean up disk space, scan
  for orphaned app files, or compare files across multiple drives on macOS.
  Covers photo/video/audio deduplication, cross-disk scanning, orphaned app
  data detection, and safe deletion workflows.
---

# macOS 磁盘清理技能

## 核心原则

- **始终** 使用 `BypassSandbox: true` 运行文件系统操作命令（沙箱无法访问 ~/Pictures、/Library 等）。
- **始终** 先扫描展示结果，等用户确认后再执行删除。
- **绝不** 删除某个重复组的所有副本，必须保留至少一份。
- **跳过** FCPX `.fcpbundle`、DaVinci 工程目录中的素材文件（工程依赖）。

## 算法：两阶段去重

```python
# 阶段1：按文件大小分组（快速预筛，无需读取内容）
size_map = defaultdict(list)
for fp in all_files:
    size_map[os.path.getsize(fp)].append(fp)
candidates = [paths for paths in size_map.values() if len(paths) > 1]

# 阶段2：对候选文件计算 MD5 哈希（精确验证）
def file_hash(fp, max_read=100*1024*1024):  # 大文件只读前100MB
    h = hashlib.md5()
    size = os.path.getsize(fp)
    with open(fp, 'rb') as f:
        read = 0
        while read < min(size, max_read):
            chunk = f.read(65536)
            if not chunk: break
            h.update(chunk)
            read += len(chunk)
    h.update(str(size).encode())  # 追加文件大小防止部分读取误判
    return h.hexdigest()
```

## 扫描范围配置

| 场景 | 扫描根目录 |
|------|----------|
| 本机全盘 | `Path.home()` + `/Volumes` |
| 跨盘扫描 | `Path.home()` + `/Volumes/外盘名1` + `/Volumes/外盘名2` |
| Capture One Styles | `~/Library/Application Support/Capture One/Styles/` |

## 跳过目录

```python
SKIP_DIRS = {
    '/System', '/Library', '/private', '/dev', '/opt', '/usr',
    '/bin', '/sbin', '/etc', '/tmp', '/System/Volumes',
    'Applications', '.Trash', '.Spotlight-V100', 'node_modules',
}
```

## 删除策略优先级

对重复组中的文件，按以下优先级决定**保留哪个**（优先级高的保留）：

1. **保留** 在整理好的归档目录中的版本（如 `~/Desktop/Photograph/`、`~/Pictures/`）
2. **保留** 当前工作目录中的版本（`bgm/`、素材库）
3. **删除** `桌面备份/`、`2022.11备份/` 等历史备份目录中的副本
4. **删除** `Downloads/` 中已有归档版本的副本
5. **跳过** `.fcpbundle/`、`FCPX工程/` 内的素材（工程依赖，不能删）

## App 残留检测

扫描以下目录，与 `/Applications/` 中已安装 App 对比：

- `~/Library/Application Support/`
- `~/Library/Caches/`
- `~/Library/Preferences/`
- `~/Library/Logs/`
- `~/Library/Containers/`
- `/Library/Application Support/`（需 BypassSandbox）

**注意**：`DaVinci Resolve` 的 `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Extras/` 是正常安装数据，不是残留。

## 结果输出格式

- 扫描结果保存为 JSON（`scratch/` 目录）
- 生成 Markdown 报告 artifact，包含：总览表、前N大重复组、清理建议
- **删除前**展示预览清单，等待用户确认

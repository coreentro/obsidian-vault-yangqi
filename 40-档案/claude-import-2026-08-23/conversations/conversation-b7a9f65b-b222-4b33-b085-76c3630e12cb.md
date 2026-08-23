---
title: "文献自动重命名方案"
source_conversation_uuid: "b7a9f65b-b222-4b33-b085-76c3630e12cb"
---

# 文献自动重命名方案

<!-- message_uuid: 019d6ccc-114b-726f-8e70-e7ba5e18cdc3 -->
<!-- parent_uuid: 00000000-0000-4000-8000-000000000000 -->

## 你

现在有一个需求，我每次下文献是英文的嘛，下下来的命名格式是乱套的，我想能不能有一个方案，我下载的文献，能根据我文献里的题目内容，只要我下载下来这个文献，就能能根据我文献里的题目内容给我重命名，加上日期等等

<!-- message_uuid: 019d6ccc-114b-7033-b87e-d1efb5418f93 -->
<!-- parent_uuid: 019d6ccc-114b-726f-8e70-e7ba5e18cdc3 -->

## Claude

 The user wants a solution to automatically rename downloaded PDF papers based on their title content and date. Let me think about the best approach.

They want: when a PDF is downloaded, it gets automatically renamed based on the paper's title (extracted from the PDF content) plus date info.

Best approaches:
1. A folder watcher script (Python) that monitors the Downloads folder and renames PDFs automatically
2. Could use pdfplumber/PyMuPDF to extract title, then rename

Let me suggest a Python script that watches a folder and renames PDFs. Since network is disabled, I can't use AI APIs in bash. But I can create a standalone Python script they can run locally.


I'll build a Python script that monitors the Downloads folder for new PDFs, extracts the title from the PDF metadata or text content, and automatically renames each file using a date-based format like `YYYY-MM-DD_Title.pdf`.
```
This block is not supported on your current device yet.
```

Let me create a Python script solution for automatically renaming PDF papers. I'll create:

1. A Python script that watches a folder and renames PDFs based on extracted title + date
2. The script will use PyMuPDF (fitz) or pdfplumber to extract text/metadata

Let me design a complete solution with:
- A folder watcher using watchdog
- PDF title extraction from metadata or first page
- Renaming with date format: YYYY-MM-DD_Author_Title.pdf

I'll create this as a downloadable Python script with clear setup instructions.好的，我来给你做一个**自动监控下载文件夹、提取文献标题自动重命名**的完整方案！
```
This block is not supported on your current device yet.
```

Now let me create a setup script and README.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

给你做好了！下面是完整方案说明：

---

## 🛠 方案原理

脚本做两件事：
1. **提取标题**：先读 PDF 元数据的 `Title` 字段，读不到就扫第一页里**字号最大的文字**（论文标题通常是最大的）
2. **自动重命名**：格式为 `YYYY-MM-DD_SlugTitle.pdf`

---

## 🚀 三步上手

**第一步：安装依赖**
```bash
pip install pymupdf watchdog
```

**第二步：后台运行（持续监控下载文件夹）**
```bash
python paper_renamer.py
```
之后每次下载 PDF，脚本检测到新文件 → 等待下载完成 → 自动重命名，完全无感。

**第三步（可选）：指定输出目录，边重命名边归档**
```bash
python paper_renamer.py --watch ~/Downloads --output ~/papers/renamed
```

---

## 📋 命名效果示例

| 原文件名 | 重命名后 |
|---|---|
| `1-s2.0-S0004370221000266-main.pdf` | `2026-04-08_AttentionIsAllYouNeed.pdf` |
| `download (3).pdf` | `2026-04-08_DeepLearningNaturalLanguage.pdf` |
| `fulltext.pdf` | `2026-04-08_TransformerArchitectureReview.pdf` |

README 里还附了 **macOS / Windows / Linux 三平台开机自启**的配置方法，设置一次，以后永远自动跑。

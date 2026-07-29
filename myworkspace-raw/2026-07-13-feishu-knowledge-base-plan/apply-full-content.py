#!/usr/bin/env python3
"""Backfill full Xiaohongshu source text into the Feishu ingestion Base."""
import json
import subprocess
from pathlib import Path

BASE = "H8spb3RLUaQHx0sKayccrupQntb"
TABLE = "tblucWDaVqSwmbzK"
DATA = Path(__file__).with_name("xiaohongshu-full-content-batch-2026-07-14-31-50.json")

VIDEO_IDS = {
    "6889daa6000000002302d2a7", "61c45ad8000000000102a451",
    "623bfdbc000000000102f3de", "68663fb60000000010012ceb",
    "683a935f000000000303f101", "6819ad4500000000200283d9",
    "668393ff000000000d00edbf", "67c574bb00000000060385f1",
    "67d6df9d000000000d014a8e",
}

AI30_OCR = """本地关键帧 OCR（按时间顺序）
00:00 看完这条视频
03:00 入门你感兴趣的任何领域
06:00 学会了摄影剪辑写作
15:00 如果你正在自学转行找副业搞项目
18:00 因为我会告诉你
21:00 快速入门任何新领域的三步实操法
27:00 我常用的学习平台：哔哩哔哩、得到 App、知识星球、小鹅通、网易云课堂、慕课网；先搜索你要学的领域
30:00 点进前10个爆款付费课程，看行业重点
39:00 2. 让 AI 规划学习路径
45:00 生成完整提示词；示例要求 AI 制定 30 天剪映专业版学习计划，覆盖结构、每日任务、模块拆解、掌握标准、实战案例和每阶段工具
54:00 学习结构总览图：项目管理与素材导入、时间线剪辑、音频、字幕文本、转场特效、调色、动画关键帧、抠像合成
57:00 30 天任务清单示例：界面与素材管理、时间线、多轨道、音频、15秒项目复盘
69:00 输出是最好的学习；费曼学习法：确定概念、用自己的话教给别人、回顾、简化
72:00 如果不能用简单的话讲清楚，就没有真正理解
84:00 针对暴露出的“一看就会、动手不会”再补练
90:00 AI 在这里只是工具，真正让你掌握技能的是输出；把知识变成能力，把输入变成输出
96:00 才是进步最快的方式

边界：这是关键帧画面文字恢复，不等同于逐字语音稿；原视频已作为原始素材附件保存。"""

payload = json.loads(DATA.read_text())
for item in payload["records"]:
    content = item.get("content", "").strip()
    comments = item.get("comments", "").strip()
    tags = ""
    lines = content.splitlines()
    tag_lines = [line.strip() for line in lines if line.strip().startswith("#")]
    if tag_lines:
        tags = " ".join(tag_lines)
    interaction = (
        f"来源页：{item.get('sourceUrl', '')}\n"
        f"详情页标题：{item.get('title', '')}\n"
        f"可见评论与互动（页面截取）：\n{comments}"
    )
    media_links = []
    for media in item.get("media", []):
        for key in ("current", "src", "poster"):
            value = media.get(key)
            if value and value not in media_links:
                media_links.append(value)
    for raw_json in item.get("jsonLd", []):
        try:
            info = json.loads(raw_json)
        except json.JSONDecodeError:
            continue
        for key in ("contentUrl", "thumbnailUrl"):
            value = info.get(key)
            if value and value not in media_links:
                media_links.append(value)
    transcript = ""
    if item["id"] == "683a935f000000000303f101":
        transcript = AI30_OCR
    elif item["id"] in VIDEO_IDS:
        transcript = "原片已读取并保留；语音逐字稿与关键帧文字待下一轮逐条提取。当前字段不以摘要代替原视频。"
    fields = {
        "原文正文（保真）": content,
        "原文标签": tags,
        "作者与互动": interaction,
        "原始媒体链接": "\n".join(media_links),
        "视频转写与画面文字": transcript,
    }
    command = [
        "lark-cli", "base", "+record-upsert",
        "--base-token", BASE,
        "--table-id", TABLE,
        "--record-id", item["recordId"],
        "--json", json.dumps(fields, ensure_ascii=False),
        "--as", "user",
    ]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        raise SystemExit(f"{item['id']} failed:\n{result.stderr}")
    print(item["id"], "updated")

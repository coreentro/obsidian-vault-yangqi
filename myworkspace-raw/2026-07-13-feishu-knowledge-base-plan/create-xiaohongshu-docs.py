#!/usr/bin/env python3
"""Create source-preserving Feishu Docx pages under the Xiaohongshu Wiki node."""
import html
import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / "xiaohongshu-full-content-batch-2026-07-14-31-50.json").read_text())
PARENT = "SqiWwGt1giYOiHkWo94cF3pQnpf"
EXISTING = {
    "6889daa6000000002302d2a7": "K12gdZaRfoKVZRxdyLrcpe2CnWb",
    "61c45ad8000000000102a451": "WsBwdNRoxoD8G6xxnYYcVGkDnDb",
    "623bfdbc000000000102f3de": "UnMqdxA1AoPkYwxbETqcDT6Mnkf",
    "63eb9fdf000000000800f425": "CN7kdMdpUoxbikxB9pVc15Xmnme",
    "67ce86e2000000002903ecfa": "HEsFdPii7oaxumxVEcFczezDn8f",
    "67d80a690000000009014bfb": "S8fSdnd5Ro1thqxVgR4c1aTWnff",
    "6878fbaa000000000b01e8e4": "Qlf1dOgkUofRzmxNiuocGVVInuh",
    "6873987a000000000d025a55": "BVuNd2MVEoopYfxClJtcEFdFn8b",
    "68663fb60000000010012ceb": "YoHUdCkKIoGvpAx02sAcR1Minyd",
    "683a935f000000000303f101": "Qt3VdYIMjoKzuwxbyB3cMjixnF5",
    "66e805d0000000000c01b80b": "CMwrd6nMkooYg0xgpQxcEzWznbe",
    "6836fd9c000000000303eaa5": "EYisdAKH5o0BwlxMTvhc0Ghgnfh",
    "6819ad4500000000200283d9": "Gpg5ddRcvoM6C2xTV4scpf2rnme",
    "68175c0f0000000003038bf8": "KRF2do5l8oLS2gxAFgwcLd0UnQe",
    "67edf9de000000001c0066e5": "IaXydlte7o8DGkxnjuIccUyvnJg",
    "668393ff000000000d00edbf": "VGKvdcNwYoIDy7xYKoCchK3xnaf",
    "67c574bb00000000060385f1": "WvgadJ496ouThPx6iQWcIXcyncg",
    "67d6df9d000000000d014a8e": "SPR4dB1LxoiOiqxtRZqcPNY2ngh",
    "67ab179300000000180067d8": "SFJYdcMD2oQ1tVxTazFcly35naf",
    "67b7e523000000002602d516": "JF2FdZ4s3o1jAdxwjdlc08W1nUe",
}

def esc(value: str) -> str:
    return html.escape(value or "", quote=False).replace("\n", "<br/>")

def media_links(item):
    links = []
    for media in item.get("media", []):
        for key in ("current", "src", "poster"):
            value = media.get(key)
            if value and value not in links:
                links.append(value)
    for raw in item.get("jsonLd", []):
        try:
            info = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for key in ("contentUrl", "thumbnailUrl"):
            value = info.get(key)
            if value and value not in links:
                links.append(value)
    return links

def make_xml(item):
    links = media_links(item)
    content = (
        f"<title>{esc(item['title'])}</title>"
        "<h1>原文保真</h1>"
        f"<p><b>来源页：</b><a type=\"url-preview\" href=\"{html.escape(item['sourceUrl'], quote=True)}\">小红书原文</a></p>"
        f"<p><b>小红书 ID：</b>{esc(item['id'])}</p>"
        f"<p><b>原文内容：</b><br/>{esc(item.get('content', ''))}</p>"
        "<h1>作者与互动证据</h1>"
        f"<p>{esc(item.get('comments', ''))}</p>"
        "<h1>原始媒体</h1>"
        + "".join(
            f"<p><a type=\"url-preview\" href=\"{html.escape(url, quote=True)}\">媒体链接</a></p>"
            for url in links
        )
    )
    if item["id"] == "683a935f000000000303f101":
        transcript = (ROOT / "xiaohongshu-ai-learning-683a935f" / "knowledge-card.md").read_text()
        content += f"<h1>视频转写与画面文字</h1><p>{esc(transcript)}</p>"
    elif any(json.loads(raw).get("contentUrl") for raw in item.get("jsonLd", []) if raw):
        content += "<h1>视频转写与画面文字</h1><p>原片链接已保留；语音逐字稿与关键帧文字将在下一轮逐条提取。本节不以摘要替代视频。</p>"
    content += "<h1>我的整理</h1><p>以上为小红书原文与页面证据的保真归档。后续补充的主题判断、可信度边界和行动建议均会与原文分开，不替换原始内容。</p>"
    return content

created = dict(EXISTING)
for item in DATA["records"]:
    if item["id"] in EXISTING:
        continue
    result = subprocess.run(
        [
            "lark-cli", "docs", "+create",
            "--parent-token", PARENT,
            "--content", make_xml(item),
            "--as", "user",
        ],
        text=True,
        capture_output=True,
    )
    if result.returncode:
        raise SystemExit(f"{item['id']} failed:\n{result.stderr}")
    response = json.loads(result.stdout)
    created[item["id"]] = response["data"]["document"]["document_id"]
    print(item["id"], created[item["id"]], flush=True)
    time.sleep(1.5)

print("RESULT " + json.dumps(created, ensure_ascii=False))

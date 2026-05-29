---
title: "Hooks 实战：让规矩自动执行，不靠 AI 记忆"
source: 飞书 Wiki
source_url: "https://axsppz4oyvj.feishu.cn/wiki/Wtf6wExs0iVUVYkVou5cpkgqnxh"
node_token: "Wtf6wExs0iVUVYkVou5cpkgqnxh"
obj_type: "docx"
document_id: "XoW6dW6RoohJlcxGmmXcJxjxnlc"
revision_id: "4"
source_updated_at: ""
created: 2026-05-29
tags:
  - 飞书导出
  - 原文复制
---

原文链接：<https://axsppz4oyvj.feishu.cn/wiki/Wtf6wExs0iVUVYkVou5cpkgqnxh>

> 说明：以下为飞书导出的原文 Markdown 内容，仅复制到 Obsidian，未额外补充来源外内容。

---
<title>Hooks 实战：让规矩自动执行，不靠 AI 记忆</title>

你好，我是大圣



这节课我们来解决Claude 的另一个问题：**有些规矩，AI 聊久了就会忘**



# 一、AI的记忆靠不住



假设你跟 Claude Code 说：



```Bash
注意：不要修改 published 目录下的任何文件，那些是已经发布的文章
```



它说好的



然后你们开始聊别的事情。你让它帮你改个错别字、调整一下目录结构、优化一段代码



聊了二十轮之后，你说："帮我把所有文章的标题格式统一下。"



它很勤快地把所有 Markdown 文件都改了：**包括 published 目录下的**



你：我不是说了不要改那个目录吗？



它：抱歉，我忘了



**这不能怪它。** 我们在提示词文章里讲过，AI 的上下文窗口是有限的。



**对话越长，早期的信息权重越低**。你二十轮之前说的那句"不要修改"，早就被后面的对话稀释了



你当然可以每隔几轮就重复提醒一次。但这不现实，而且你自己也会忘记提醒



**怎么办？换一个思路：不靠 AI 的记忆，靠程序来保证**



在之前我们说过，这背后的思想叫自动触发：就像闹钟，你设好了它到点就响，不管你记没记住



Hooks 就是 Claude Code 里的闹钟



# 二、Hooks的基本逻辑



Hooks 的工作方式非常直接，就两件事：



1. **什么时候触发：**在 Claude Code 执行某个操作的前后
2. **触发后干什么：**运行你写的一段脚本



最常用的触发时机有两种：

<sheet sheet-id="xQ5lLL" token="TXD9si6JxhOfWMtSDi3cBo0rnqg"></sheet>



**打个比方：**

- 【工具调用前】就像机场安检：你要登机之前，先检查一下你的行李有没有问题。有问题就拦下来，不让你上飞机。
- 【工具调用后】就像快递签收通知：快递送到之后，自动给你发一条短信



Claude Code 还有其他几种触发时机，但这两种覆盖了绝大多数场景。等你用熟了再去了解其他的也不迟



# 三、案例：文件保护 Hook



我们来做第一个 Hook：**禁止 Claude Code 修改 published 目录下的文件**



先看视频：👇（看完视频再看文字说明）



<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcny769k77j86f5aq888n38?from=ccm" type="iframe"></readonly-block>



## 第一步：创建Hook脚本



在项目根目录下，创建目录和文件



```Bash
你的项目文件夹/
└── .claude/
    └── hooks/
        └── protect-published.py
```



你可以手动创建，也可以让 Claude Code帮你



```Bash
帮我创建 .claude/hooks/protect-published.py 文件
```



然后把以下内容写进去（**这是我让 Claude Code帮我写的 Python脚本**）：



```Python
#!/usr/bin/env python3
"""Hook: 禁止 Claude Code 修改 published 目录下的文件"""

import json
import sys


def main():
    tool_input = json.load(sys.stdin).get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if "published/" in file_path:
        print(json.dumps({
            "decision": "block",
            "reason": "published 目录下的文件受保护，禁止修改！请走审批流程。"
        }))
        sys.exit(2)


if __name__ == "__main__":
    main()
```



如果你用的是 Mac 或 Linux，还需要给脚本加上执行权限：



```Bash
chmod +x .claude/hooks/protect-published.py
```



## 第二步：配置setting.json



创建或编辑项目根目录下的 `.claude/settings.json` 文件：



PS：同样，你也可以让 Claude Code 帮你创建这个配置



```JSON
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/protect-published.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```



**这个配置在说什么？**



- `PreToolUse`：在工具调用**之前**触发
- `"matcher": "Write|Edit"`：**只在 Claude Code 要写入或编辑文件时触发，读取不受限制**
- `command`：触发时运行哪个脚本
- `timeout: 5`：脚本最多运行 5 秒，超时就跳过



## 第三步：验证它生效了



退出 Claude Code，重新启动，然后进行测试



![](https://feishu.cn/file/Hw3pbMYzOoFMBexu8V7cniHVnDe)



# 四、关于写脚本这件事



你可能会想：我不会写 Python ，这个 Hook 我用不了



我们完全可以用Claude Code来做这件事儿



你完全可以用中文告诉它你想要什么规则，让它帮你写脚本：



例如：👇



```Bash
帮我写一个 Hook 脚本，实现这个功能：
当 Claude Code 要修改 config 目录下的文件时，先提醒我确认
脚本用 Python 写，放在 .claude/hooks/ 目录下
顺便帮我更新 .claude/settings.json 的配置。
```



Claude Code 会帮你把脚本和配置都搞定。你需要做的只是**想清楚你要什么规则**



这就是 AI 编程有意思的地方：**你不需要会写代码，你只需要会描述你的需求。** 代码让 AI 来写

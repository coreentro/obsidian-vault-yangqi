---
title: "Claude Code安装之正式安装"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/XaDPwtAi4iw3ShkR7smcO4Oenfg
node_token: XaDPwtAi4iw3ShkR7smcO4Oenfg
obj_token: CvcFdggTqoueWhxYhnEcrEXinhe
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 3
breadcrumb:
  - "【启程必看】从这里开始"
  - "【正课阶段 3】上手智能体：桌面端与AI编程"
  - "命令行智能体：一种全新的智能体交互方式"
  - "Claude Code安装之正式安装"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 1
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# Claude Code安装之正式安装

> [!info] 位置
> 【启程必看】从这里开始 › 【正课阶段 3】上手智能体：桌面端与AI编程 › 命令行智能体：一种全新的智能体交互方式

# 写在前面

你好，我是大圣

这节课我们终于可以正式安装Claude Code了

我会给大家介绍两种方式，一种是国内安装，一种是官方脚本安装

能解决网络问题的，可以用官方脚本安装，不能解决的就使用国内安装

两者没有什么大的区别，不用纠结

**我这里要多说一嘴，这节教程大家只负责安装，不要打开，也不要使用，否则可能造成错误**

# 一、国内安装

国内安装的逻辑我相信大家已经非常清楚了

使用NPM的方式安装，并且采用国内的镜像源

老规矩，先问豆包，她的回答已经很完美了，把这段提示词发给你的豆包

PS：根据你的电脑系统，把下方标黄的地方改掉

```Bash
我已经安装了Node.js，并且配置了国内的镜像源

我也已经安装完了Git

我现在想要使用国内的网络安装Claude Code

我是Windows / Mac电脑，帮我给出完整的流程，只管帮我安装，不用管我中转API的配置
```

**第一步：检查环境**

> [!abstract]- 🖼 图片展示的是国内安装Claude Code时豆包的回答内容。豆包已安装N
> 图片展示的是国内安装Claude Code时豆包的回答内容。豆包已安装Node.js并配置国内镜像源，还安装了Git，现在想使用国内网络安装Claude Code，且是Windows电脑。她表示只负责安装，不涉及API配置，只需帮她安装即可，遇到问题可截图给豆包解决。此图与文档中介绍国内安装Claude Code流程的上下文相关，是国内安装前的准备工作提示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/R7L3bv9buoIrT5x2BjBcL6TGnJb) · `R7L3bv9buoIrT5x2BjBcL6TGnJb`

**第二步：使用npm命令进行安装**

> [!abstract]- 🖼 图片展示了国内安装Claude Code的步骤。首先，以管理员身份打开P
> 图片展示了国内安装Claude Code的步骤。首先，以管理员身份打开PowerShell，执行“npm install -g @anthropic -ai/claude -code@latest”命令进行安装，等待国内镜像（一般几十秒）完成。接着，验证安装，使用“claude --version”和“claude doctor”命令，若出现版本号且检查通过，则表示安装成功。该图片与上文国内安装步骤的介绍紧密相关，是对安装操作的具体指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CwzCb6MGEop9TjxzqX8czVJonhb) · `CwzCb6MGEop9TjxzqX8czVJonhb`

**第三步：验证安装并且解决问题**

**PS：遇到任何问题，截图给到豆包，让他帮你解决**

**验证安装只要用claude --version即可，不要用claude doctor验证**

> [!abstract]- 🖼 图片展示了Claude Code国内安装验证安装及常见问题的内容。首先，
> 图片展示了Claude Code国内安装验证安装及常见问题的内容。首先，通过“claude --version”和“claude doctor”命令验证安装，若出现版本号且检查通过则表示成功。其次，列举了国内网络常见问题，包括权限报错、命令找不到、安装卡住/超时等，分别给出解决方法，如右键PowerShell以管理员身份运行再装、关闭所有终端重新打开再试等。最后，强调按上述步骤执行完后Claude Code就安装好了，还询问是否需帮忙翻译claude doctor的报错信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OLKvbuvDsoVjIKxaJEjcU1FMnPd) · `OLKvbuvDsoVjIKxaJEjcU1FMnPd`

# 二、官网安装

官网后面提供了一键脚本安装，不需要有node.js的环境

但他需要去访问Claude官方网站去下载安装包，这里面有几个点需要注意

1. **你的终端必须能访问外网才可以使用这种方式**
2. **就算你的终端可以访问外网，也有可能下载得非常慢。因为Claude的官方网站对你的工具要求较高**

## 1）Windows安装

老规矩，问豆包，把如下提示词发给豆包：

```Bash
我已经安装了Node.js

我也已经安装完了Git

我现在想要使用官网的方式安装Claude，我是Windows电脑，帮我给出完整的流程，只管帮我安装

并且你要考虑到PowerShell的权限拒绝问题

你要提醒用户，安装完成后环境变量的配置问题。你不用提前帮用户配置，他安装完成后，你要让他关注安装完成后有没有提醒他环境变量，然后让他把那个截图给到你

安装完成后，只用claude --version验证
```

> [!abstract]- 🖼 图片展示的是Windows电脑安装Claude CLI（Claude C
> 图片展示的是Windows电脑安装Claude CLI（Claude Code）时的安装提示信息。内容包括已安装Node.js和Git，提示使用官网方式安装Claude，需给出完整流程，只管帮忙安装，需考虑PowerShell权限问题，安装完成后需关注环境变量配置，安装后仅用claude --version验证。该图片与文档中Windows安装Claude CLI的上下文对应，是安装前的提示信息，为后续安装流程提供指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MyGfbc06MoSngPxm4Tfch7Hpnac) · `MyGfbc06MoSngPxm4Tfch7Hpnac`

> [!abstract]- 🖼 图片展示了Claude Code在Windows系统下的安装步骤。图片中
> 图片展示了Claude Code在Windows系统下的安装步骤。图片中以文字形式呈现了安装前的准备、解决PowerShell权限拒绝的操作及官方安装的两种方式。安装前需确保Node.js和Git已安装。解决权限问题时，需以管理员身份打开PowerShell，执行相关命令放开脚本执行权限，并在提示时输入Y回车。官方安装可选择官方脚本或npm全局安装，前者为推荐方式，后者为备用方式，均在管理员PowerShell里直接运行对应命令。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ShWSbmPKXou6XxxdFv6c6jbVnQb) · `ShWSbmPKXou6XxxdFv6c6jbVnQb`

> [!abstract]- 🖼 图片展示了Claude Code安装完成后环境变量提醒的内容。安装结束后
> 图片展示了Claude Code安装完成后环境变量提醒的内容。安装结束后，需留意两点：1. 查看安装过程中是否有自动提示添加环境变量/PATH；2. 安装完成后，将安装完成的最后几行输出截图发给豆包，由其判断是否需手动配环境变量。若提示“不是内部或外部命令”，则环境变量没自动加上，需手动加PATH。该图片与文档中Windows安装部分上下文对应，是安装完成后验证及环境变量配置的指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QOHQbjWTUoAU9hx2Lx4cOnDrnbh) · `QOHQbjWTUoAU9hx2Lx4cOnDrnbh`

安装完成后，**你可能会出现这样的提醒，把这张截图给到你的豆包，让他帮你加环境变量**

<callout emoji="✨">
这里的路径 C:\Users\YYang\\.local\bin
**YYang 是别人电脑的用户文件名称，每个人的不一样哈**
</callout>

> [!abstract]- 🖼 图片展示的是Windows PowerShell界面，显示Claude 
> 图片展示的是Windows PowerShell界面，显示Claude Code安装成功，版本为2.1.42，安装位置在C:\\Users\\YYang\\.local\\bin\\claude.exe。界面底部有“Installation complete!”提示，还有一条红色箭头突出显示的安装提示，内容为“Setup notes: Native installation exists but C:\\Users\\YYang\\.local\\bin is not in your PATH. Add it by opening: System Properties + Environment Variables + Edit User PATH + New + Add the path above. Then restart your terminal.”，即安装存在但C:\\Users\\YYang\\.local\\bin不在PATH中，需添加该路径并重启终端。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SU65bF3A8o5Rvvx6WYBcmsTjnI6) · `SU65bF3A8o5Rvvx6WYBcmsTjnI6`

**添加环境变量完成后最终验证：搞定；你出来的版本一定比这个高**

> [!abstract]- 🖼 图片展示的是Windows系统下安装Claude Code后的验证界面。
> 图片展示的是Windows系统下安装Claude Code后的验证界面。在命令提示符中输入“claude --version”命令后，显示版本号为2.1.42（Claude Code）。该图片与文档中“Windows安装”部分内容相关，用于说明安装完成后，通过此命令验证Claude Code版本，以确保安装成功且版本符合要求。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PAvLb84X8oIruXxKdE6cYBbEnqg) · `PAvLb84X8oIruXxKdE6cYBbEnqg`

## 2）Mac电脑安装

**你可以直接问豆包，也可以看我下面的视频**

```Bash
我已经安装了Node.js

我也已经安装完了Git

我现在想要使用官网的方式安装Claude，我是Mac电脑，帮我给出完整的流程，只管帮我安装

安装完成后，只用claude --version验证
```

> [!abstract]- 🖼 图片展示了Mac电脑安装Claude Code的完整流程。首先打开终端，
> 图片展示了Mac电脑安装Claude Code的完整流程。首先打开终端，按Command + 空格输入Terminal回车；执行官方安装脚本，复制“curl -fsSL https://claude.ai/install.sh | bash”命令执行；等待下载、解压、自动配置PATH，中途可能需输入电脑开机密码；重启终端；关闭终端窗口，再重新打开；最后验证安装，输入“claude --version”查看版本号。该图片与文档中Mac电脑安装Claude Code的内容紧密相关，直观呈现了安装步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DGVPbus3JohxcjxsK0mchYFyn1n) · `DGVPbus3JohxcjxsK0mchYFyn1n`

<figure view-type="Preview"><source mime="video/quicktime" origin-height="2160.000000" origin-width="3326.000000" token="VyECbvJ24o0wfxxb4vOcQ7pJnBh"/></figure>

# 写在最后

到这里这一节就完成了，大家不要去打开Claude

这一节我想给大家传达的不仅仅是安装完成，而是你看到我是怎么跟豆包去协作的

这会是大家未来解决问题最常用的方式

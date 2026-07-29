---
title: "梦飞：在自己的电脑上部署COW微信机器人项目"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Zb4wwM7UYiTEWKkXfmzcfwxzn7b
node_token: Zb4wwM7UYiTEWKkXfmzcfwxzn7b
obj_token: N4b7dNZHNoWihyxUSo3c0PCQnHe
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - "「Agent 共学」之\"谁是人类\" 「WayToAGI x 阿里云」"
  - "梦飞：在自己的电脑上部署COW微信机器人项目"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 38
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 梦飞：在自己的电脑上部署COW微信机器人项目

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 › 「Agent 共学」之"谁是人类" 「WayToAGI x 阿里云」

# 梦飞：在自己的电脑上部署COW微信机器人项目

为了方便之前已经玩过，没有免费服务器可用，又想参赛的小伙伴。因此制作了此教程，此教程可以把COW项目部署在你自己的电脑上使用。

注意：程序将在你的电脑本地运行，假如你关掉了窗口，那么进程也就结束。所以，如果你想让AI持续使用，就必须保持窗口打开和运行，也就是电脑不能关。

**以下教程以windows10系统为例/**

**mac系统步骤也是一样，只是打开命令符的命令些许不同，遇到问题问大模型就好了**

## 一、注册大模型

百炼首页：https://bailian.console.aliyun.com/

需要更改 "model"，和添加 "dashscope_api_key"。

那么如何去获取key呢

视频教程，拿到key之后，进行下一步骤。

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="AFi1bZzkSoWGQnxqYMhcGxWwnMf"/></figure>

## 二、安装环境

1、点击电脑“系统”，直接输入“cmd”，点击回车，打开命令窗口

> [!abstract]- 🖼 图片展示了在Windows系统中打开命令窗口的操作界面。画面中，右下角的
> 图片展示了在Windows系统中打开命令窗口的操作界面。画面中，右下角的Windows图标被红框突出显示，点击后弹出“系统”菜单，其中“cmd - 查看更多搜索结果”也被红框标注。该图片与文档中“安装环境”部分的内容相关，对应步骤1，即在电脑“系统”中输入“cmd”并点击回车，打开命令窗口，以进行后续确认是否有python和pip等操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KzTJbenfSosOQPx8U4hchRAJnXc) · `KzTJbenfSosOQPx8U4hchRAJnXc`

2、在命令窗口中，粘贴入以下代码，确认是否有python

```Bash
python --version
```

3、粘贴入以下代码，确认是否有pip

```Bash
pip --version
```

> [!abstract]- 🖼 图片展示的是在电脑命令窗口中确认python和pip是否安装的操作结果。
> 图片展示的是在电脑命令窗口中确认python和pip是否安装的操作结果。命令窗口中，“python --version”代码下方显示Python 3.12.3，“pip --version”代码下方显示pip 24.0及其所在路径等信息。这与文档中“安装环境”部分的步骤3相关，步骤3要求粘贴代码确认是否有pip，步骤4提到若安装了python和pip会分别显示出版本号，图片内容正是显示了已安装的python和pip的版本号。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TXaibc5HjoGiwkxIyi9cOjwwnag) · `TXaibc5HjoGiwkxIyi9cOjwwnag`

4、两步命令输入完，核对一下

- 如果有的话，会如上图一样，分别显示出版本号。那么可以跳过“安装环境这一步，直接到“二、部署项目””
- 如果没有的话，会如下图所示，那么需要安装下边的步骤，一步一步安装。

> [!abstract]- 🖼 图片展示了在Windows系统下Python及pip版本的查询结果。首先
> 图片展示了在Windows系统下Python及pip版本的查询结果。首先执行“python --version”命令，显示Python版本为3.12.3；接着执行“pip --version”命令，提示“pip”不是内部或外部命令，也不是可运行的程序或批处理文件。这与文档中部署COW微信机器人的Python安装步骤相关，用于验证Python及pip是否已正确安装。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LXfnbCk9IoHW6zx4PmAcrUxkn3S) · `LXfnbCk9IoHW6zx4PmAcrUxkn3S`

5、先进行python的安装，我帮你把python的安装包已经下载好了，直接点击下载：

<figure view-type="Card"><source mime="application/x-msdownload" token="Mppibam0YoMKzixftekcxLQPnwe"/></figure>

5.1  python安装步骤：

> [!abstract]- 🖼 图片展示了Python 3.12.3 (64-bit)的安装界面。上方提
> 图片展示了Python 3.12.3 (64-bit)的安装界面。上方提示选择安装方式，可点击“Install Now”以默认设置安装，或选择“Customize installation”自定义安装。下方有“Use admin privileges when installing py.exe”和“Add python.exe to PATH”两个勾选框，当前已勾选。该图片与文档中部署COW微信机器人的Python安装步骤相关，直观呈现了安装时的界面及可选设置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YuH4byZcKoTL0dx0O9VclvSunJb) · `YuH4byZcKoTL0dx0O9VclvSunJb`

> [!abstract]- 🖼 图片展示的是Python 3.12.3 (64-bit) Setup的安
> 图片展示的是Python 3.12.3 (64-bit) Setup的安装进度界面。界面上方显示“Setup Progress”，中间部分写着“Installing: Python 3.12.3 Executables (64-bit)”，下方有一个绿色进度条，进度条已填充至一半。右下角有一个“Cancel”按钮。该图片与文档中“5.1 python安装步骤”内容相关，是Python 3.12.3安装过程中显示的安装进度画面，直观呈现了安装的当前状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HuFSbKpcKo0QgMxGf8QczSTUnde) · `HuFSbKpcKo0QgMxGf8QczSTUnde`

> [!abstract]- 🖼 图片展示了Python 3.12.3（64-bit）安装成功后的界面。界
> 图片展示了Python 3.12.3（64-bit）安装成功后的界面。界面中“Setup was successful”提示安装成功，下方有“Disable path length limit”选项，其描述为更改机器配置，允许程序，包括Python，绕过260字符的“MAX_PATH”限制。图片中有红色框标注，步骤1为点击“Disable path length limit”选项，步骤2为再关闭窗口。该图片与文档中5.1节的python安装步骤相关，直观呈现了安装成功后的操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Qlrjbto8goPfsIxtZeGczoGhnnd) · `Qlrjbto8goPfsIxtZeGczoGhnnd`

5.2 关闭窗口，再次运行那两行命令 会发现已经有了。

## 三、部署项目

6、下载COW机器人项目，也给你准备好了，直接下载，然后解压缩。

<figure view-type="Card"><source mime="application/zip" token="YQrgbAp8NovFtfxpYKLcfBFRnne"/></figure>

7、解压后，打开COW文件夹，

8、在空白处，shift+鼠标右键，点击“在此处打开Powershell窗口”

> [!abstract]- 🖼 图片展示了在电脑上部署COW微信机器人的文件夹内容。文件夹内有36个项目
> 图片展示了在电脑上部署COW微信机器人的文件夹内容。文件夹内有36个项目，包括多个文件，如requirements.txt、requirements-optional.txt、README.md等，还有config.json、config_template.json等配置文件，以及nixpacks.toml、Dockerfile等。右上角弹出菜单显示“在此处打开Powershell窗口”等选项。该图片与文档中部署项目步骤相关，对应步骤8，即在空白处shift+鼠标右键，点击“在此处打开Powershell窗口”。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JB7ybiBVPoRMpfxW5h3cCT8bnId) · `JB7ybiBVPoRMpfxW5h3cCT8bnId`

9、在Powershell窗口中，粘贴进入：

`pip install -r requirements.txt`

> [!abstract]- 🖼 图片展示的是在Powershell窗口中执行`pip install -
> 图片展示的是在Powershell窗口中执行`pip install -r requirements.txt`命令后的结果。窗口中显示了多个“Requirement already satisfied”信息，如openai==0.27.8、HTMLParser==0.0.2等，均从d:\\conda\\lib\\site-packages中获取，部分版本号后有括号内的数字。该图片与上文部署项目中第9步操作对应，用于说明在Powershell窗口粘贴并执行此命令后，等待执行完成并关闭窗口的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FGh7b9j0BoQRSyx3duhcahe9nFb) · `FGh7b9j0BoQRSyx3duhcahe9nFb`

10、等待执行完成后，继续粘贴：

`pip install -r requirements-optional.txt`

> [!abstract]- 🖼 图片展示的是在Powershell窗口中执行`pip install -
> 图片展示的是在Powershell窗口中执行`pip install -r requirements-optional.txt`命令后的结果。窗口中显示了多个“Requirement already satisfied”信息，如`tiktoken`、`pydub`、`SpeechRecognition`等库的版本信息，均在d:\\conda\\lib\\site-packages目录下。该图片与文档中部署COW微信机器人的步骤相关，是执行上一步骤`pip install -r requirements-optional.txt`后的反馈结果，用于确认安装是否成功。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HFztb80pWoZxRoxfjsHckngbnse) · `HFztb80pWoZxRoxfjsHckngbnse`

12、上边的都执行完成后，关闭窗口。在当前目录下，找到`config-template.json`文件。如下图：

> [!abstract]- 🖼 图片展示了在电脑上部署COW微信机器人的文件夹内容。其中，`config
> 图片展示了在电脑上部署COW微信机器人的文件夹内容。其中，`config-template.json`文件被红框突出显示，其下方还有`config.json`和`config - 副本.json`文件。根据上下文，新生成的配置文件`config-template.json`需复制一份并重新命名为`config.json`，画红框的地方是需要修改的内容，对格式和符合要求有严格要求，小白可直接复制下方配置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/EPfWb9ITgolnjTx57QzcAPOEnTR) · `EPfWb9ITgolnjTx57QzcAPOEnTR`

13、新生成的便是配置文件，右键-- 使用记事本 打开这个文件，我画红框的地方是需要修改的地方。

**\* 因为这个地方对格式和符合要求比较严格，如果是小白，建议你直接复制我下方的配置。**

> [!abstract]- 🖼 图片展示的是COW微信机器人配置文件`config-template.j
> 图片展示的是COW微信机器人配置文件`config-template.json`中部分关键信息。其中，“model”字段被红框突出显示，其值为“qwen - max”；“dashscope_api_key”字段也被红框突出显示，其值为部分被遮挡的密钥。这些信息对应文档中部署项目步骤里，新生成配置文件后需右键使用记事本打开，画红框的地方是需要修改的地方这一内容，是部署项目时需重点关注的配置项。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KucrbsCZ9o8d5HxSFUxcjPrJnBd) · `KucrbsCZ9o8d5HxSFUxcjPrJnBd`

14、

- 删除新文件里的所有代码。
- 复制下边的代码，粘贴到文件里。
- 找到第4行，把一开始就让你注册并保存好的千问API key，粘贴到双引号里。
- 这也是你唯一需要修改的地方。修改完之后，点击保存，关闭文件。

```JSON
{
  "channel_type": "wx",   
  "model": "qwen-max",
  "dashscope_api_key": "sk-改成你刚才拿到的key",
  "text_to_image": "dall-e-3",
  "voice_to_text": "openai",
  "text_to_voice": "openai",
  "proxy": "",
  "hot_reload": true,
  "single_chat_prefix": [""],
  "single_chat_reply_prefix": "",
  "group_chat_keyword": ["{问题}"], 
  "group_chat_prefix": ["@bot"], 
  "group_name_white_list": ["ALL_GROUP"],
  "concurrency_in_session": 1,
  "group_welcome_msg": "",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2000,
  "expires_in_seconds": 3600,
  "character_desc": "",
  "temperature": 1.0,
  "subscribe_msg": "",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}
```

15、保存上述文件，然后在当前文件下，找到`plugins/godcmd`文件夹，复制`config.json.template`重命名为` config.json`

<grid>
<column width-ratio="0.281762">
> [!abstract]- 🖼 图片展示了腾讯云控制台中“文件”页面的文件管理界面。左侧为导航栏，选中“
> 图片展示了腾讯云控制台中“文件”页面的文件管理界面。左侧为导航栏，选中“文件”。右侧显示了“root/chatgpt-on-wechat”目录下的文件和文件夹，其中“plugins”文件夹被红色框突出显示。该图片与文档中部署COW微信机器人的步骤相关，对应第15步，即在当前文件下找到`plugins/godcmd`文件夹，复制`config.json.template`重命名为`config.json`，此图直观呈现了找到并重命名文件夹的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SBVJbND1pow0wyxoUZyck4VznWc) · `SBVJbND1pow0wyxoUZyck4VznWc`
</column>
<column width-ratio="0.326613">
> [!abstract]- 🖼 图片展示的是在文件管理界面中找到`plugins/godcmd`文件夹的
> 图片展示的是在文件管理界面中找到`plugins/godcmd`文件夹的操作结果。左侧为文件管理导航栏，右侧是文件列表，其中`godcmd`文件夹被红色框线突出显示。这与文档中“保存上述文件，然后在当前文件下，找到`plugins/godcmd`文件夹，复制`config.json.template`重命名为`config.json`”的操作步骤相关，表明已找到并识别出`godcmd`文件夹，为后续操作做准备。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FTE8bzeQmoojG0xe916c5XwAnZc) · `FTE8bzeQmoojG0xe916c5XwAnZc`
</column>
<column width-ratio="0.391625">
> [!abstract]- 🖼 图片展示了在root目录下的chatgpt-on-wechat文件夹中，
> 图片展示了在root目录下的chatgpt-on-wechat文件夹中，plugins文件夹下的godcmd文件夹内容。其中，config.json.template文件被复制重命名为config.json。该图片与文档中部署项目步骤相关，对应第15步，即保存文件后，在当前文件下找到`plugins/godcmd`文件夹，复制`config.json.template`重命名为`config.json`的操作，直观呈现了文件重命名后的状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VXoZb903ro19X7xyd4pc0HHKnUb) · `VXoZb903ro19X7xyd4pc0HHKnUb`
</column>
</grid>

16、双击config.json，进入后，设置下你的password和admin_users

可以设置为和我一样的，后边再改，点击保存后关闭。

![图片展示了在Linux系统中，通过在线文本编辑器对`config.json`文件进行编辑的界面。文件夹路径为`/root/chatgpt-on-wechat/plugins/godcmd`。文件内容中，`password`被设置为“123456”，`admin_users`被设置为`\[1\]`。该图片与文档中部署COW微信机器人的步骤相关，对应第16步，即在`config.json`文件中设置`password`和`admin_users`，并保存后关闭文件。](https://feishu.cn/file/Ffl5b4BzIopxP8x36kCccIBnn5c)

17、重新回到chatgpt-on-wechat/这个文件路径下，空白处右键，打开Powershell里复制粘贴进入：

`python app.py  `

然后将会弹出二维码，扫码登录即可。

> [!abstract]- 🖼 图片展示了在Windows系统下使用Powershell执行`pytho
> 图片展示了在Windows系统下使用Powershell执行`python app.py`命令的界面。命令执行后，弹出二维码，提示扫码登录。界面中还显示了部分配置信息，如`channel_type`为`wx`，`model`为`coz`等。该图片与文档中部署COW微信机器人的步骤相关，对应第17步，即在指定文件路径下运行`python app.py`命令，以弹出二维码扫码登录，实现项目部署。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NWV9bngjroRys6x1zF9crEBZnfe) · `NWV9bngjroRys6x1zF9crEBZnfe`

> [!abstract]- 🖼 图片展示的是在部署COW微信机器人项目过程中，执行`python app
> 图片展示的是在部署COW微信机器人项目过程中，执行`python app.py`命令后弹出的微信登录二维码。背景为深蓝色，二维码呈白色方块矩阵状。上方文字提示“Downloading QR code”，并给出多个可获取二维码的网址链接。此图片对应文档中部署项目步骤17的内容，即重新回到指定文件路径下，在Powershell中执行命令后弹出该二维码，扫码登录即可继续操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TKq6b7bO8oN5JaxU3QscLVMAnfS) · `TKq6b7bO8oN5JaxU3QscLVMAnfS`

18、注意：

（1）程序将在你的电脑本地运行，假如你关掉了窗口，那么进程也就结束。所以，如果你想让AI持续使用，就必须保持窗口打开和运行。

（2）如果你发现突然不管用了，你可以点击一下窗口，然后点一下空格。 因为在选中状态下，powershell窗口是不继续执行的。

（3）其他操作与服务器部署的操作一致。

（4）参加机器人比赛的，可以参考其他教程，自行更改配置。

---
title: "「第一天」参赛Bot配置要求"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Rhpqw4W2niSlkZkrF2scRIzLned
node_token: Rhpqw4W2niSlkZkrF2scRIzLned
obj_token: ACfad5HHcoWTsgx0Okhc1n5onHP
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - "「Agent 共学」之\"谁是人类\" 「WayToAGI x 阿里云」"
  - "「第一天」参赛Bot配置要求"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 363
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 「第一天」参赛Bot配置要求

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 › 「Agent 共学」之"谁是人类" 「WayToAGI x 阿里云」

<callout emoji="💡">
要求概述:
1. 关闭进群欢迎语
2. 在群里回答时不能 @对方
3. 统一修改config.py中的触发词为{问题}
4. 回答不能分好几条
</callout>

为了更好地参与《谁是人类》比赛，请各位参赛选手把自己的机器人按照如下方式调整。

## 1、如何关闭进群欢迎语

（1）管理员认证 #auth 【你的密码】- 密码请查看`Plugins/godcmd/config.json`

（2）`#disablep hello`，关闭hello插件。

> （3）`#enablep hello`，赛后如需重启，使用该指令。

![图片展示了微信机器人管理认证及插件操作界面。上方显示“管理员认证”，下方有“\[INFO\]认证成功”提示。中间部分有“插件开启”和“插件关闭”字样，分别对应“#enablep hello”和“#disablep hello”指令，右侧有绿色按钮标识。该图片与文档中“如何关闭进群欢迎语”部分内容相关，直观呈现了管理员认证成功及插件开启、关闭的操作界面和指令，帮助参赛选手更好地理解操作步骤。](https://feishu.cn/file/ULEabD0hRoYF0KxrFjjclL9Rnid)

## 2、如何在群里回答时不 @对方

私聊微信机器人认证成功后。在对话框中输入第一行代码。

出现安装成功后，输入第二行。

```Bash
#installp https://github.com/wangxyd/ipartment.git
#scanp
```

（图是举例）

> [!abstract]- 🖼 图片展示了一条在聊天窗口发送的指令，内容为“#installp http
> 图片展示了一条在聊天窗口发送的指令，内容为“#installp https://github.com/wangxyd/ipartment.git”。该指令用于在服务器插件目录中安装名为“ipartment”的插件，其GitHub仓库地址为https://github.com/wangxyd/ipartment.git。此指令与文档中“第一天”参赛Bot配置要求上下文相关，是安装插件的步骤之一，安装完成后需在插件目录修改配置文件。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LhVvbox0Do2DJcxK9djcugY8nTh) · `LhVvbox0Do2DJcxK9djcugY8nTh`

![图片展示了在聊天群中安装插件的反馈信息。左侧显示用户发送指令“#installp https://github.com/wangxyd/nicecoze.git”，右侧回复“\[INFO\]图片展示了在聊天群中安装插件的反馈信息。左侧显示用户发送指令“#installp https://github.com/w addCriterion>](https://feishu.cn/file/Fc8sbq6aHoLBFnxuQ2DcooOqnAf)

如果出现安装失败，则在插件目录下，右键删除ipartment文件夹后，重新安装即可。

> [!abstract]- 🖼 图片展示了在服务器插件目录中找到`ipartment`文件夹的操作步骤。
> 图片展示了在服务器插件目录中找到`ipartment`文件夹的操作步骤。在文件管理界面，路径为`chatgpt-on-wechat/plugins`，选中`ipartment`文件夹后，右键点击弹出菜单，选择“删除”选项。该图片与上文“安装完成后，去服务器的插件目录中，修改配置文件`plugins/ipartment/config.json`”的内容相关，直观呈现了找到`ipartment`文件夹的操作位置，为后续删除操作提供指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RqeMbhySooLx4yxu2FZc7KA2nUe) · `RqeMbhySooLx4yxu2FZc7KA2nUe`

安装完成后，去服务器的插件目录中，修改配置文件：

配置文件为`plugins/ipartment/config.json`，可以自行修改，按照如下示例配置：

```JSON
{
  "group_at_probability": 0,
  "add_quoter_nickname": false,
  "reply_reference_query": false
}
```

## 3、如何修改config.json中的触发词为“{问题}”

找到配置文件，路径如下：

> [!abstract]- 🖼 图片展示了服务器插件目录中config.json文件的所在位置。左侧为服
> 图片展示了服务器插件目录中config.json文件的所在位置。左侧为服务器管理界面的导航栏，选中“文件”选项。右侧是文件管理界面，显示“chatgpt-on-wechat”文件夹下的文件列表，其中“config.json”文件被红色箭头指向突出显示。该图片与文档中“如何修改config.json中的触发词为{问题}”的上下文相关，用于指引用户找到配置文件config.json的位置，以便后续进行触发词修改操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BXm6bwoYLoyWMIxWCgUcj6Ucn8g) · `BXm6bwoYLoyWMIxWCgUcj6Ucn8g`

修改 ` "``group_chat_prefix": ``["{问题}"]``,`，注意符号均为英文符号。

![图片展示了修改config.json文件以设置触发词为“{问题}”的操作界面。在代码编辑器中，高亮显示了“group_chat_prefix: \[{问题}\]”这一行代码，其中“{问题}”部分被红色框突出显示。这与上文提到的在配置文件中修改“group_chat_prefix: \[{问题}\]”以设置触发词为“{问题}”的操作步骤相呼应，直观呈现了操作位置。](https://feishu.cn/file/Hq4GbAfPWolQiHxbEG9cOORfnlf)

达成效果：

> [!abstract]- 🖼 图片展示了修改config.json中触发词为“{问题}”后的聊天界面。
> 图片展示了修改config.json中触发词为“{问题}”后的聊天界面。用户提问“既然人是铁饭是钢，为什么不直接吃钢铁”，系统回复“哈哈，人肠胃可消化不了铁，还是米饭馒头来得实在。”另一用户回复“口感不行。”该图片与上文提到的修改config.json触发词为“{问题}”后达成的效果相呼应，直观呈现了修改后的聊天场景。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MrvNbocPBoaerOx3P0RcFDfvnFf) · `MrvNbocPBoaerOx3P0RcFDfvnFf`

## 4、回答不分段

之前的跟学活动中，使用分段能力的用户，在提示词中，去掉提示词中带有的 //n的示例即可取消分段。

# 完成后修改头像和微信名为编号

最后机器人头像，头像要求关注活动页要求: [[1.3 AI Agents (智能体)/2. Agent 共学快闪活动/「Agent 共学」之·谁是人类· 「WayToAGI x 阿里云」/「Agent 共学」之·谁是人类· 「WayToAGI x 阿里云」|「Agent 共学」之"谁是人类" 「WayToAGI x 阿里云」]]

以上全部内容完成后，重新扫码登录微信机器人即可。

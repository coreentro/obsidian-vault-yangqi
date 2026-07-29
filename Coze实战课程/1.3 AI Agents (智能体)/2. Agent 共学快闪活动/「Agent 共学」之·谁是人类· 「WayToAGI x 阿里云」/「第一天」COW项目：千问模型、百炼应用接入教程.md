---
title: "「第一天」COW项目：千问模型、百炼应用接入教程"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/V0XCwDVOEiqfH2kZGcPc84PDnad
node_token: V0XCwDVOEiqfH2kZGcPc84PDnad
obj_token: EIXMdlOpsoLrL6xUkf5curJpnpb
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - "「Agent 共学」之\"谁是人类\" 「WayToAGI x 阿里云」"
  - "「第一天」COW项目：千问模型、百炼应用接入教程"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 619
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 「第一天」COW项目：千问模型、百炼应用接入教程

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 › 「Agent 共学」之"谁是人类" 「WayToAGI x 阿里云」

# 「第一天」COW项目：千问模型、百炼应用接入教程

<callout emoji="💡"><p>活动介绍：<cite doc-id="Gm72wS4BqixefikquThcERlgnD0" file-type="wiki" title="「Agent 共学」之&#34;谁是人类&#34; 「WayToAGI x 阿里云」" type="doc"></cite> </p><h3><b>比赛目标：</b></h3><p>通过<b> AI Bot 拟人化比赛</b>，带大家一起<code>提升 Prompt 书写能力</code>，通过多轮比赛和分享来加深对 <code>AI Agent 的学习和理解</code>。</p><h3><b>活动形式：</b></h3><p>在一个活动群里，主持人出题，AI机器人+人类卧底潜伏在微信群中回答问题。一场比赛6-8轮，每轮群众选出谁是人类。</p><h3><b>参与方式：</b></h3><p>围观群众：在比赛时间查看视频号「通往AGI之路」或「阿里云」.</p><p>参与选手：加入微信群，7月24日首次共学结束后，群中统一招募.</p></callout>

> [!abstract]- 🖼 图片展示的是“AI Bot拟人化比赛”的宣传海报。背景为粉色，左侧有“W
> 图片展示的是“AI Bot拟人化比赛”的宣传海报。背景为粉色，左侧有“WaytoAGI”与“阿里云”的标识。画面中央是一位戴眼镜的白发老人和一个机器人面对面，二者轮廓以亮色突出。海报上有醒目的黑色大字“谁是‘人类’”，下方注明“AI Bot拟人化比赛”。此图片与上文介绍的COW项目相关，可能是该项目中的拟人化比赛宣传，吸引观众和选手关注参与。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FGiTbqT0soVe8dxtNkkcyNkfnvb) · `FGiTbqT0soVe8dxtNkkcyNkfnvb`

这个教程是为COW项目接入千问、百炼而作，因此，使用此教程的前提是，你已经完成了`COW机器人的搭建`，或者准备进行搭建。

1、如果还未进行搭建，请移步<cite doc-id="NB3nwtUC0iDLYxkIkSYc0WRznGg" file-type="wiki" title="【共学最全版本】微信机器人共学教程" type="doc"></cite> 完成第一天的教程内容。

2、**之前完成过coze文件替换对接的同学，直接使用百炼“应用”的调用。不然会报错。**

---

百炼首页：https://bailian.console.aliyun.com/

**首先我们需要了解下，在调用阿里云的AI服务时，有两种方式。**

**1、直接调用模型**： 通义千问系列以及其他的大模型产品服务。

在COW项目中，调用千问系列的模型。是可以直接使用key、选择model进行调用，此时就是直接调用的某一个大模型。类似于直接调用智普模型、或直接调用了OpneAI的模型。

**2、调用应用能力：**阿里云百炼的“应用”服务。 

当我们需要使用更多的能力时候，比如工作流、搜索等能力。此时就需要调用百炼的“应用”。

> 在百炼平台里的“应用”概念，类似于Coze中的“bot”、或ChatGPT的GPTs概念。

因此，大家可以简单理解为：阿里提供了两种调用方式

1、直接调用模型：对接简单，调试不方便。

2、调用应用（bot）：对接相对麻烦，调试简单。（推荐）

以下教学教学了两种调用方式，大家可以自由选择使用任意一种。（之前完成过coze对接的同学，直接使用第二种，不然会报错）

强烈推荐第二种，调用百炼的应用，这样大家在修改和调整Prompt的时候，就不需要重复登录微信了，只需要在“百炼”应用里进行调试即可。

---

## **一、直接调用大模型（之前完成过coze对接的同学，直接去二、百炼应用的调用。）**

百炼首页：https://bailian.console.aliyun.com/

1、当我们在COW中，去直接调用千问的某一个大模型时，只需要更改key和model即可。

以调用“qwen-max”模型为例，在/root/chatgpt-on-wechat/文件夹下，打开config.json文件：

需要更改 "model"，和添加 "dashscope_api_key"。

那么如何去获取key呢：

视频教程：

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="EB8Xbv8wXoiXHCxhEWkcfUVQnFf"/></figure>

图文教程：

<grid>
<column width-ratio="0.545892">
> [!abstract]- 🖼 图片展示了百炼控制台的登录页面。页面上方有“百炼”标志及导航栏，中间有“
> 图片展示了百炼控制台的登录页面。页面上方有“百炼”标志及导航栏，中间有“请输入标题”提示，下方是登录区域，有“扫码登录”和“账号密码登录”选项，下方还有“忘记密码”“注册账号”等链接。页面右上角有“登录”按钮。图片下方有蓝色文字，文字为“1、点击地址并扫码登录，直接进入百炼控制台”。该图片与上文介绍的百炼控制台登录方式相呼应，直观呈现了登录页面及操作指引。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YWM4bdyO8o8Uqcxg85WcSrArnlf) · `YWM4bdyO8o8Uqcxg85WcSrArnlf`
</column>
<column width-ratio="0.454108">
> [!abstract]- 🖼 图片展示的是阿里云百炼平台的界面，标题为“3、点击API key，创建一
> 图片展示的是阿里云百炼平台的界面，标题为“3、点击API key，创建一个API key”。界面上方有“首页”“模型中心”“应用中心”等导航栏。中间区域有“你好，欢迎使用阿里云百炼”的欢迎语，下方有“模型调用”和“应用创建”两个板块，分别介绍模型调用和应用创建相关内容。右侧有“主账号管理”“退出协议”“退出登录”等选项。该图片与文档中介绍阿里云百炼平台操作的上下文相关，用于指导用户在平台中创建API key。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/IKt9bMbOQonHicxJvkIc7netnng) · `IKt9bMbOQonHicxJvkIc7netnng`
</column>
</grid>

<grid>
<column width-ratio="0.344949">
> [!abstract]- 🖼 示意图 @@@@ 图片展示阿里云百炼平台创建新API - KEY的界面。
> 示意图 @@@@ 图片展示阿里云百炼平台创建新API - KEY的界面。点击“创建新API - KEY”按钮后弹出窗口，窗口中“归属业务空间”默认显示为“默认业务空间”，下方有描述输入框，当前输入1字符，共可输入200字符。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/P2gEbpPgIoB91exK9Knc5R28nAo) · `P2gEbpPgIoB91exK9Knc5R28nAo`
</column>
<column width-ratio="0.327557">
> [!abstract]- 🖼 图片展示的是阿里云百炼平台的API KEY页面。页面左侧有“返回控制台”
> 图片展示的是阿里云百炼平台的API KEY页面。页面左侧有“返回控制台”“返回API KEY”“全部API KEY”等选项，右侧显示API KEY信息，包括API KEY、创建时间、创建者等。关键信息是页面中间突出显示的API KEY文本，下方有复制按钮。图片下方文字提示“4、复制这个API key，就可以直接使用了”，与上文提到的“实名认证后这些key才可以正常使用”相呼应，指导用户完成API KEY获取后下一步操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/J8pzb1f7yok9UlxSJZCclWbRnwg) · `J8pzb1f7yok9UlxSJZCclWbRnwg`
</column>
<column width-ratio="0.327494">
> [!abstract]- 🖼 图片展示的是一个网页界面，显示了“千问”模型配置文件相关内容。界面中突出
> 图片展示的是一个网页界面，显示了“千问”模型配置文件相关内容。界面中突出显示了“telescope_app_key”参数，其值为“12345678901234567890”。下方文字说明“5、直接在配置文件中替换，完成。”，并配有红色框线。该图片与文档中“制作Wx机器人”教程相关，用于指导用户在配置文件中替换“telescope_app_key”参数，完成千问模型配置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/I7kpb5As7oOdq9xzCCocWFqOnPe) · `I7kpb5As7oOdq9xzCCocWFqOnPe`
</column>
</grid>

以下是参考配置：

```JSON
{
  "channel_type": "wx",   
  "model": "qwen-max",
  "dashscope_api_key": "sk-aa8aa18179a84858这里更换为你自己的key",
  "text_to_image": "dall-e-3",
  "voice_to_text": "openai",
  "text_to_voice": "openai",
  "proxy": "",
  "hot_reload": false,
  "single_chat_prefix": [""],
  "single_chat_reply_prefix": "",
  "group_chat_keyword": ["{问题}"], 
  "group_chat_prefix": ["{问题}"],
  "group_name_white_list": ["ALL_GROUP"],
  "concurrency_in_session": 1,
  "group_welcome_msg": "",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2000,
  "expires_in_seconds": 3600,
  "character_desc": "",
  "temperature": 0.9,
  "subscribe_msg": "",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}
```

示意图：

> [!abstract]- 🖼 图片展示的是名为“副本.json”的配置文件内容。文件中包含多个参数设置
> 图片展示的是名为“副本.json”的配置文件内容。文件中包含多个参数设置，如“channel type”为“wx”，“model”为“wen1 max”，“dashscope api key”为“sk -aa8aa18179a84858926e8fcbb5d5fsfa9c”，还有“text to image”“text to text”“text to voice”等参数设置，以及“hot reload”“single chat prefix”“group chat keyword”等配置项。该图片与文档中千问模型、百炼应用接入教程上下文相关，是参考配置示意图。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/ICTUbSf8aon4uWx8IFAcBFaAnLf) · `ICTUbSf8aon4uWx8IFAcBFaAnLf`

注意：需要“实名认证”后，这些key才可以正常使用，如果对话出现“ Access to mode denied. Please make sure you are eligible for using the model.”的报错，那说明你没有实名认证，点击去[实名认证](https://account.console.aliyun.com/v2?spm=5176.28508143.J_4VYgf18xNlTAyFFbOuOQe.13.38a9154amP8978#/authc/types)，或查看自己是否已认证。

## **二、调用百炼“应用”**

1、当我们在COW中，去调用某一个百炼“应用”时，需要添加更多配置。

首先我们需要创建一个百炼应用，假设我将这个应用命名为“苏苏”。当我完成一个应用的创建后。

以调用“苏苏”应用为例，在/root/chatgpt-on-wechat/文件夹下，打开config.json文件：

需要更改"model": "qwen"，并添加  "qwen_access_key_id"、 "qwen_access_key_secret"、 "qwen_agent_key"、 "qwen_app_id"四项配置。

这些配置项在哪找呢？

视频教程：

<figure view-type="Preview"><source mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" token="VJFKbxWD9oqRaLxrArbcXiyen0r"/></figure>

图文教程：

<grid>
<column width-ratio="0.497152">
> [!abstract]- 🖼 图片展示了阿里云百炼平台的界面，用于说明调用百炼“应用”时的步骤。左侧菜
> 图片展示了阿里云百炼平台的界面，用于说明调用百炼“应用”时的步骤。左侧菜单栏第一个小图标被红色框突出显示，对应“应用”选项。右侧弹出“业务空间详情”窗口，其中“agentKey”字段被红框标注，其值为“6c3a952f464111e9b8b0240002971474_1c_p_inter”。该图片与上下文紧密相关，直观呈现了在调用百炼“应用”时，获取agentKey的操作位置，帮助用户完成相关配置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/C87Vba2k9oUrHdxbRAvc2zSTnQb) · `C87Vba2k9oUrHdxbRAvc2zSTnQb`
</column>
<column width-ratio="0.502848">
> [!abstract]- 🖼 图片展示的是阿里云百炼平台的“我的应用”页面。左侧菜单栏中“我的应用”被
> 图片展示的是阿里云百炼平台的“我的应用”页面。左侧菜单栏中“我的应用”被红色框突出显示。页面上方有“我的应用”标题，下方介绍用户可在此管理基于应用+模型能力构建的已开发的应用，实现对应用全生命周期一站式管理。页面中部有“你的应用创建，从这里开始！”的提示，配有机器人形象。底部有一个蓝色的“创建应用”按钮。该图片与文档中调用百炼“应用”的图文教程相关，指导用户在平台新建应用。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YcGNbHVQLolwGox6EQpc7FBWndh) · `YcGNbHVQLolwGox6EQpc7FBWndh`
</column>
</grid>

<grid>
<column width-ratio="0.505197">
> [!abstract]- 🖼 图片展示的是阿里云百炼平台新建应用界面。左侧为导航栏，有模型中心、模型市
> 图片展示的是阿里云百炼平台新建应用界面。左侧为导航栏，有模型中心、模型市场等选项。右侧是新建应用区域，上方有“智能体名称”“应用名称”等输入框，下方有“知识检索增强”“长期记忆”“插件”“流程”等设置选项。图片中红色框内突出显示了“模型选择”下拉菜单，可选择“通义千问”“通义千问Plus”“通义千问-Turbo”“Qwen-Long”等模型，右上角有“发布”按钮。该图片与上下文介绍的调用百炼“应用”教程相关，用于说明模型选择等操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WxY7bohJUoZUxlxGtgyciHxqnjf) · `WxY7bohJUoZUxlxGtgyciHxqnjf`
</column>
<column width-ratio="0.494803">
> [!abstract]- 🖼 图片展示的是阿里云百炼平台“我的应用”页面。页面左侧有导航栏，右侧上方显
> 图片展示的是阿里云百炼平台“我的应用”页面。页面左侧有导航栏，右侧上方显示“我的应用”，下方有搜索框及“新建应用”按钮。新建应用“H4ra”被红框突出显示，其右侧有“APP ID”标识，其值为“78cMac101644e908608817102156”。该图片与文档中“调用百炼‘应用’”内容相关，用于说明新建应用后可查看其APP ID等信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XenIbPNAJoWYmDxIXHjc9BUhnfd) · `XenIbPNAJoWYmDxIXHjc9BUhnfd`
</column>
</grid>

<grid>
<column width-ratio="0.481130">
> [!abstract]- 🖼 图片展示的是阿里云大模型服务平台百炼的网页界面。页面左侧有产品概述、快速
> 图片展示的是阿里云大模型服务平台百炼的网页界面。页面左侧有产品概述、快速入门等导航栏，右侧是大模型服务平台百炼的介绍及操作指南等内容。右上角有“Access Key”标识，旁边有一个加载中的进度条。该图片与文档中“调用百炼‘应用’”的上下文相关，可能是用于说明在百炼平台调用应用时，需关注Access Key等关键信息的页面示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HIv4bYVnwocviGxX26Jc8wYenTh) · `HIv4bYVnwocviGxX26Jc8wYenTh`
</column>
<column width-ratio="0.518870">
> [!abstract]- 🖼 图片展示了阿里云访问控制（IAM）中AccessKey的创建界面。左侧为
> 图片展示了阿里云访问控制（IAM）中AccessKey的创建界面。左侧为AccessKey列表，右侧弹出“创建AccessKey”窗口，提示为避免AccessKey泄露风险，新建账号后应立即创建AccessKey并替换Secret。窗口中显示了AccessKey ID和AccessKey Secret，其中AccessKey ID被红色框突出显示。该图片与上下文紧密相关，上下文提到需实名认证后才能使用AccessKey，此图直观呈现了创建AccessKey的操作界面及关键信息展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GRXvbk1l0ocNuHxkRA3cgZtgnGd) · `GRXvbk1l0ocNuHxkRA3cgZtgnGd`
</column>
</grid>

以下是参考配置：

```JSON
{
  "channel_type": "wx",   
  "model": "qwen",
  "qwen_access_key_id": "LTAI5tHyDJYfTop4dasjdm2",
  "qwen_access_key_secret": "a61SbU4PtLdasdasdafJ5Dd53am2c",
  "qwen_agent_key": "79b58aef9ead4d3d8dsadasdasdfec1b4_p_efm",
  "qwen_app_id": "asst_eeafbd5a-91a6-45b3-ab9d-e14545345432dad7",
  "text_to_image": "dall-e-3",
  "voice_to_text": "openai",
  "text_to_voice": "openai",
  "proxy": "",
  "hot_reload": false,
  "single_chat_prefix": [""],
  "single_chat_reply_prefix": "",
  "group_chat_keyword": ["{问题}"], 
  "group_chat_prefix": ["{问题}"],
  "group_name_white_list": ["ALL_GROUP"],
  "concurrency_in_session": 1,
  "group_welcome_msg": "",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2000,
  "expires_in_seconds": 3600,
  "character_desc": "",
  "temperature": 0.9,
  "subscribe_msg": "",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}
```

注意：需要“实名认证”后，这些key才可以正常使用，如果对话出现“ Access to mode denied. Please make sure you are eligible for using the model.”的报错，那说明你没有实名认证，点击去[实名认证](https://account.console.aliyun.com/v2?spm=5176.28508143.J_4VYgf18xNlTAyFFbOuOQe.13.38a9154amP8978#/authc/types)，或查看自己是否已认证。

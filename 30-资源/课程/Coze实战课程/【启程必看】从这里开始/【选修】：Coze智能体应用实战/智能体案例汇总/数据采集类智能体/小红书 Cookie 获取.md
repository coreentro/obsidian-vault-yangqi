---
title: "小红书 Cookie 获取"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/HidKwxsZhiQBRWkHmZUcTebYn8f
node_token: HidKwxsZhiQBRWkHmZUcTebYn8f
obj_token: Mexbd64HDock4mxyxaFc2btknte
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体案例汇总"
  - "数据采集类智能体"
  - "小红书 Cookie 获取"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 144
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 小红书 Cookie 获取

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体案例汇总 › 数据采集类智能体

在采集小红书的时候，很多插件都需要获取小红书的 Cookie，这篇文章是教程

**获取 Cookie 有两种方法，我们这里先讲在网页直接获取**

# 网页端直接获取

## 第一步：扫码登录小红书

https://www.xiaohongshu.com

一定要登录，然后进入如下页面

> [!abstract]- 🖼 图片展示的是小红书网页端首页界面。页面上方有“发现”“推荐”“美食”等分
> 图片展示的是小红书网页端首页界面。页面上方有“发现”“推荐”“美食”等分类标签，右上角有搜索框。页面中部有“我”选项被红色框和箭头突出显示，下方有“必须登录”提示。页面下方展示了多个帖子缩略图，如“雷总，差点忘记了”“来到现场傻眼了”等，每个帖子下方有点赞、评论、分享等互动按钮。该图片对应文档中“扫码登录小红书”步骤，直观呈现了登录后小红书首页的界面情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QhFGbNPE6olMkWxKwVNcEnHSnBs) · `QhFGbNPE6olMkWxKwVNcEnHSnBs`

## 第二步：右键点击检查

> [!abstract]- 🖼 图片展示了小红书网页端右键点击检查的操作界面。左侧是小红书首页，有发现、
> 图片展示了小红书网页端右键点击检查的操作界面。左侧是小红书首页，有发现、发布、通知、我等导航栏。右侧是两条内容，一条是关于小米的，另一条是关于电梯的。中间部分是右键点击页面空白处弹出的菜单，其中“检查”选项被红色框突出显示。该图片与上文“网页端直接获取Cookie”教程相关，对应第二步“右键点击检查”的操作步骤，直观呈现了操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UNeXbh8ZponzCrxratFcssoXnCI) · `UNeXbh8ZponzCrxratFcssoXnCI`

> [!abstract]- 🖼 图片展示了小红书网页端获取Cookie的步骤中，右键点击检查后的界面。画
> 图片展示了小红书网页端获取Cookie的步骤中，右键点击检查后的界面。画面中“Network”和“Fetch/XHR”两个选项被红色框和箭头突出显示，分别对应“点击Network”和“点击Fetch/XHR”操作说明。该图片与上文“网页端直接获取”步骤中“右键点击检查”后的内容相关，直观呈现了后续操作的界面位置，帮助用户明确点击位置，以便顺利获取Cookie。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U2Cwb6Hw9o8lTpxoQkdctjZhnf9) · `U2Cwb6Hw9o8lTpxoQkdctjZhnf9`

## 第三步：刷新下页面

**首先一定要先刷新下页面，这个非常重要**

> [!abstract]- 🖼 图片展示了小红书网页端获取Cookie的步骤中，右键点击检查后的界面。画
> 图片展示了小红书网页端获取Cookie的步骤中，右键点击检查后的界面。画面中“home”和“home/feed”被红色框突出显示，下方有红色箭头指向搜索框，框内提示“在这个搜索框中输入 home，搜索出 homefeed”。该图片与上文“右键点击检查”步骤对应，直观呈现了在开发者工具中搜索“homefeed”以获取Cookie的操作位置，帮助用户更清晰地找到相关操作区域。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AV8PbYkPkoUeXqxLI3YcdCamnjb) · `AV8PbYkPkoUeXqxLI3YcdCamnjb`

## 第四步：获取Cookie

点击那个 Homefeed

> [!abstract]- 🖼 图片展示了在网页端获取小红书Cookie的步骤中，第四步获取Cookie
> 图片展示了在网页端获取小红书Cookie的步骤中，第四步获取Cookie时的浏览器开发者工具界面。画面中“homefeed”被红色框和箭头突出显示，点击后在“Cookies”标签下，可看到一段包含大量参数的Cookie信息，其中“%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%22%
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ahr9bPHN4oIX0WxocQWcLtBdnPc) · `Ahr9bPHN4oIX0WxocQWcLtBdnPc`

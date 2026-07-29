---
title: "加餐｜服务器部署Cow和百炼（只读版本）"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/LT3JwidZoimtB4kgBvkcqYHDnSh
node_token: LT3JwidZoimtB4kgBvkcqYHDnSh
obj_token: RYyrdVsQoom8RVxPutqcYKvAnBd
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 4
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "加餐文档"
  - "编程思维体系"
  - "加餐｜服务器部署Cow和百炼（只读版本）"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 2
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# 加餐｜服务器部署Cow和百炼（只读版本）

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 加餐文档 › 编程思维体系

<callout emoji="🎉">
**注意：遇事不决就重启，重启COW进程**
</callout>

# 一、云服务器实操

## 购买云服务器

一般我们会从几个大型的云服务厂商那里购买云服务器。

国内的云服务厂商有：

- 阿里云
- 腾讯云
- 百度云
- 华为云

国外的云服务厂商有：

- 谷歌云
- 亚马逊（AWS）
- 微软云

对于新用户而言，基本上每个云服务厂商都会有优惠，这里我们选择腾讯云进行实操。

<callout emoji="🚅">
PS：接下来我会截图来说明购买云服务器的过程，但是这里我希望你学习的不是过程，而是各项参数选择的标准，这才是本质。
- 随着软件的迭代，购买页面和流程可能会变得不一样，如果你仅仅学习了过程，购买页面一变，你又不会购买了
- 以后你可能在其他云服务厂商购买服务器，那这里的购买流程就不再适用，但是万变不离其宗。
- 就跟我们学会了在淘宝购物之后，京东拼多多等软件出来后，我们能很快上手是一样的
</callout>

第一步：打开腾讯云官网：https://cloud.tencent.com/act/pro/Featured （请自行注册账号密码）

第二步：选择最便宜的那个套餐，注意这里的活动随时间都有可能变化

<callout emoji="🦄">
在这一步中，最重要的是选择服务器规格
- 2核2G4M、50G SSD、300GB硬盘 就是我们购买的服务器规格

  - 2核是CPU的核数
  - 2G是内存
  - 50G是SSD盘的容量
  - 300G是普通硬盘的容量
  - 4M是网络带宽，也就是服务器可以撑住的流量（非程序员不用关心）
上面这些指标是核心，它的作用是，如果我们购买了服务器之后发现某一项资源不足，我们可以进行升级配置
</callout>

> [!abstract]- 🖼 图片展示的是腾讯云官网的云服务器购买页面。页面上方有“同价续费：参与本专
> 图片展示的是腾讯云官网的云服务器购买页面。页面上方有“同价续费：参与本专区活动，享新购续费同价”的活动信息。中间部分突出显示“轻量 2核2G4M”套餐，包含50GB SSD盘和300GB硬盘，价格为99元/年，有“立即购买”按钮。下方还有其他多种云服务器套餐，如轻量2核4G6M、CVM-S5 2核2G等，每种套餐均有详细配置信息及“立即购买”按钮。该图片与上下文紧密相关，直观呈现了购买云服务器时可选择的多种套餐及价格，帮助用户了解购买流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JcLMbh0S5ogRPbxG0iacELs9nJh) · `JcLMbh0S5ogRPbxG0iacELs9nJh`

第三步：选择地域和操作系统

<callout emoji="✍️"><p>这里面有两个点需要学习</p><ul><li>地域的选择：地域选择有两个标准<ul><li>如果服务需要部署在海外，则要选择海外的服务器</li><li>至于具体的地域，则是离你的用户越近越好（个人使用没啥影响）</li></ul></li><li>镜像的选择（其实就是操作系统）<ul><li>这里我选择的是Ubuntu22.04-Docker26 26.1.3（意思就是预先安装了Docker的Ubuntu系统）</li></ul></li></ul><p></p><p>PS：大家之前看了梦飞教程的[[1.3 AI Agents (智能体)/2. Agent 共学快闪活动/Agent 搭建共学快闪 0619/【共学最全版本】微信机器人共学教程|【共学最全版本】微信机器人共学教程]]应该有自己的服务器，并且使用了宝塔面板系统。这个不用可以更换。</p><p>这里我之所以不使用宝塔面板的原因有两点</p><ul><li>宝塔面板后面的账号登录有一些繁琐，绕来绕去</li><li>宝塔面板会掩盖一些操作的细节，这篇文章主要以教学为主，还是希望大家可以熟悉下简单的Linux命令</li></ul></callout>

<grid>

> [!abstract]- 🖼 图片展示的是轻量应用服务器配置选择界面。已选配置为2核2G内存、50GB
> 图片展示的是轻量应用服务器配置选择界面。已选配置为2核2G内存、50GB SSD等。地域可选上海等，当前选上海；镜像选择Ubuntu22.04 - Docker26 26.1.3，登录密码自动生成；时长可选1天等，当前选1天；数量默认1，可加减。下方有加入会员选项，可享专属优惠券等，但文档中提到不要加会员。最下方有99元的配置费用及“立即购买”按钮。该图与文档中购买云服务器配置选择的内容相关，直观呈现了相关操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VS4PbTiKgo8aOKxnZaeczU0lnKh) · `VS4PbTiKgo8aOKxnZaeczU0lnKh`

> [!abstract]- 🖼 图片展示的是云服务器购买流程中的支付订单页面。页面上方显示所有费用（包括
> 图片展示的是云服务器购买流程中的支付订单页面。页面上方显示所有费用（包括购买、开通、续费等）均可开具，订单支付完成后可下载。下方“待支付订单”区域有订单号、产品名称、配置、类型、数量、时长等信息，应付合计99.00元。有“选择优惠券”和“代金券（0）”选项，以及“选择支付方式”区域，有在线支付和支付宝支付两种方式，支付金额均为99.00元。页面右下角有“点击购买”和“下一步”按钮，其中“下一步”按钮被红色箭头突出标识。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NeJgbL2Emou7dbxdYvBcvMvCn7g) · `NeJgbL2Emou7dbxdYvBcvMvCn7g`

</grid>

## 配置云服务器

第四步：修改账号密码

<callout emoji="🥛">
这个环节需要三个注意的点
- Linux服务器需要账号密码登陆，就跟你的Windows系统一样，会有一个用户名和密码
- 密码建议修改成自己容易记忆的，或者自己可以做好笔记，要不忘记了密码还得重装系统
- 腾讯云的Ubuntu系统默认的用户名是：ubuntu
</callout>

<grid>

> [!abstract]- 🖼 图片展示的是腾讯云轻量应用服务器购买成功的界面。界面上方显示“购买成功”
> 图片展示的是腾讯云轻量应用服务器购买成功的界面。界面上方显示“购买成功”，并有“扫码入群领专属代金券”的绿色按钮。下方有“温馨提示”，其中第1点以红色框突出显示，内容为：对于使用Linux操作系统类型的实例，若选择“自动生成密码”，初始密码会通过站内信发送；也可使用“重置密码”功能设置实例登录密码，或使用OrcaTerm远程工具一键免密登录实例。该图片与上下文介绍的云服务器实操中购买轻量应用服务器的内容相关，是对购买成功后相关操作说明的呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WLKrbLKZ9ooQV2xYAzQc1n5rnmc) · `WLKrbLKZ9ooQV2xYAzQc1n5rnmc`

> [!abstract]- 🖼 图片展示的是腾讯云控制台界面，左侧导航栏选中“服务器”下的“轻量应用服务
> 图片展示的是腾讯云控制台界面，左侧导航栏选中“服务器”下的“轻量应用服务器”。右侧显示服务器列表，其中一台名为“Ubuntu22.04-Docker26-zvjq”的服务器状态为“运行中”，其CPU、内存、系统盘等信息也一并呈现。图片中红色框突出显示了右上角的“消息”图标，旁边有“站内信”提示，显示有20条已读和未读消息。该图片与上下文关系紧密，直观呈现了服务器部署操作中可能遇到的消息通知情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FeFcb3Q3aoyrkjxKmY2cWDelnPh) · `FeFcb3Q3aoyrkjxKmY2cWDelnPh`

</grid>

<grid>

> [!abstract]- 🖼 图片展示的是腾讯云轻量应用服务器创建成功后的邮件通知内容。其中，关键信息
> 图片展示的是腾讯云轻量应用服务器创建成功后的邮件通知内容。其中，关键信息为服务器操作系统为Ubuntu Server 22.04 LTS 64bit，默认用户名是ubuntu，登录密码为CB2yKu+cR@jdX83。该图片与上下文紧密相关，上下文在介绍配置云服务器时，提到Linux服务器需要账号密码登陆，此图片直观呈现了服务器的默认登录信息，帮助用户了解登录所需的基本账号密码等关键数据。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/E9hhbIN04odwKGxtX8uceqV6n5c) · `E9hhbIN04odwKGxtX8uceqV6n5c`

> [!abstract]- 🖼 图片展示的是腾讯云轻量应用服务器界面。左侧导航栏有“服务器”等选项，右侧
> 图片展示的是腾讯云轻量应用服务器界面。左侧导航栏有“服务器”等选项，右侧显示服务器列表，其中一台名为“Ubuntu22.04-Docker26-zvjq”的服务器正在运行中，其CPU、内存、系统盘等信息一目了然。该服务器的“...”菜单被突出显示，其中“重置密码”选项被红色框线圈出。此图与文档中“修改账号密码”步骤相关，直观呈现了在腾讯云轻量应用服务器中重置密码的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Qw3BbPoZooA7KgxLDI4cHmjfnHd) · `Qw3BbPoZooA7KgxLDI4cHmjfnHd`

</grid>

第五步：修改一些基本信息

<callout emoji="📍">
这一步是非必需，但是我一般会修改，因为这样让我的服务器命名更有意义
</callout>

> [!abstract]- 🖼 图片展示的是腾讯云服务器管理界面中“Coze机器人接入微信教学”实例的详
> 图片展示的是腾讯云服务器管理界面中“Coze机器人接入微信教学”实例的详情页面。页面左侧为导航栏，右侧上方显示实例ID及公网IP。实例信息部分，有实例名称、状态、地域和可用区、套餐类型等信息。其中，实例名称处有红色框标注，右侧有红色箭头指向，提示“修改实例名称”。该图片与上下文“第五步：修改一些基本信息”相关，直观呈现了修改实例名称的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VKgybMZWjoeM70xMYlBcDoZNn6f) · `VKgybMZWjoeM70xMYlBcDoZNn6f`

**第六步：设置防火墙**

1. 为什么要配置防火墙？

配置防火墙就是配置一系列规则，用来告诉服务器哪些IP可以访问这台服务器，哪些不可以

防火墙对于新机器是最严格的，也就是任何外部IP不可以访问这台机器，为了正常使用，我们需要配置一些规则

1. 防火墙配置要素

一条防火墙的规则包括三个要素

- IP地址
- 端口号
- 允许还是拒绝

对于IP和端口号，如果不明白是什么，请参考文档：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜程序中的API是什么|加餐｜程序中的API是什么]]

我举几个关于防火墙的例子：

- 这台服务器允许IP地址 = 198.265.98.21 访问 8080端口
- 这台服务器允许所有IP地址访问 8080端口
- 这台服务器拒绝IP地址 = 198.265.98.21 访问 8080端口

在腾讯云中，我们按照如下方式配置防火墙

> [!abstract]- 🖼 图片展示的是腾讯云轻量应用服务器的防火墙模板页面。左侧导航栏中“防火墙模
> 图片展示的是腾讯云轻量应用服务器的防火墙模板页面。左侧导航栏中“防火墙模板”选项被红色框突出显示。页面上方有“防火墙模板使用指南”，介绍创建模板、管理模板规则及设置实例防火墙等内容。下方是防火墙模板列表，显示了模板名称、创建时间及操作选项。页面底部有“创建模板”按钮，用于设置单台实例的防火墙。该图片与上下文紧密相关，直观呈现了在腾讯云中配置防火墙模板的操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AyN0bVNikoUrn6xTGTPcZXsvnwg) · `AyN0bVNikoUrn6xTGTPcZXsvnwg`

> [!abstract]- 🖼 图片展示了腾讯云中配置防火墙规则的界面。界面说明防火墙模板仅支持设置入站
> 图片展示了腾讯云中配置防火墙规则的界面。界面说明防火墙模板仅支持设置入站规则，出站默认允许所有请求，且模板应用成功后服务器原有规则将被覆盖。还提到防火墙规则优先级说明靠前的优先级更高，可通过拖动规则进行排序。界面中有四条规则，分别为允许所有IP通过22端口进行Linux登陆、允许所有IP通过3306端口进行MySQL服务、允许所有IP通过3001端口进行oneAPI、允许所有IP通过3000端口进行FastGPT，其中前两条规则被红色框突出显示，标注“一般必配，用来SSH登陆”和“业务需要”。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/L2PEbjbbGoxzHtxtpmmc5isRnue) · `L2PEbjbbGoxzHtxtpmmc5isRnue`

我们这台服务器我们配置了4条规则

- Linux登陆（22）：**这个会允许所有的IP通过22端口进行访问，为下面的SSH登陆铺路**
- Mysql（3306）：这个没有必要，一般Mysql的端口也不会暴露出去
- oneAPI（3001）：oneAPI的端口，后面我自己搭建FastGPT要用
- FastGPT（3000）：FastGPT的端口，后面我自己搭建FastGPT要用

请注意，如果到这里你有点懵了，我建议要静下心来阅读下：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜程序中的API是什么|加餐｜程序中的API是什么]]

这里的防火墙简单来说就是防止别人通过端口来攻击你，从而导致你的服务器宕机

## 登陆云服务器

前面我们一直在讲Linux系统一个头疼的问题就是没有像Windows系统一样的界面。这里我们就来看看它到底是怎么登陆和操作的

所谓的登陆，就是通过账号密码进入到这个服务器内部的操作界面

一般来讲，每个云服务厂商都会提供SSH的登陆方式，我们直接使用这种方式就行

请注意：登陆服务器，我们需要四个要素

- 一个可以提供SSH登陆的软件
- 服务器的公网IP
- 服务器的账号和密码
- 服务器的22端口已经开放白名单

下面我们一个个来看

### SSH登陆

一般的云服务器厂商都会提供网页端，那个足够使用了，对于程序员或者运维同学，他们也会专门在自己电脑上下载一类软件用来管理服务器

- 对于这种软件，大家自行百度，**我只推荐一个我用的FinalShell**

**腾讯云提供的网页端SSH登陆如下：**

<grid>

> [!abstract]- 🖼 图片展示了腾讯云轻量应用服务器的界面。左侧导航栏中“服务器”选项被选中，
> 图片展示了腾讯云轻量应用服务器的界面。左侧导航栏中“服务器”选项被选中，其下“OrcaTerm”选项被红色框线突出显示。右侧主界面显示服务器相关信息，有“轻量应用服务器新增圣保罗地域，欢迎前往购买页进行选购”的提示，下方有“新建”按钮，以及已有的“Coze机器人接入微信教学”服务器信息，包括运行状态、CPU、内存、系统盘等配置详情，还显示了服务器公网IP。该图片与上文介绍腾讯云提供的网页端SSH登陆方式相呼应，直观呈现了登录界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KushbP7vWodtpbxRVuBckzbdn1c) · `KushbP7vWodtpbxRVuBckzbdn1c`

> [!abstract]- 🖼 图片展示了腾讯云提供的网页端SSH登陆界面。左侧有“+新建连接”按钮，其
> 图片展示了腾讯云提供的网页端SSH登陆界面。左侧有“+新建连接”按钮，其被红色框和箭头突出显示，提示点击新建连接。下方列出了已有的连接记录，如“Ubuntu22.04 - Docker26 - zvjq”等。右侧是“体验OrcaTerm Web应用”的介绍，包括易于访问、原生体验、快速加载、操作流畅等内容，下方有“立即体验”按钮。该图片与上文介绍腾讯云网页端SSH登陆的内容相关，直观呈现了新建连接的操作位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Px4nbJ55Nou7ymxSytxcpvNhncb) · `Px4nbJ55Nou7ymxSytxcpvNhncb`

</grid>

<grid>

> [!abstract]- 🖼 图片展示了腾讯云提供的网页端SSH登陆界面。界面上方有“connecti
> 图片展示了腾讯云提供的网页端SSH登陆界面。界面上方有“connections:”及搜索栏。下方“历史连接”区域列出了多个连接配置，如“Ubuntu22.04-Docker26-zvjq”“宝塔Linux面板-nLqO”等，每个配置有用户名、IP地址、默认分组等信息。界面底部有“选择连接配置”“+新建连接配置”按钮，其中“+新建连接配置”按钮被红色框突出显示，箭头指向其右侧，提示新建连接操作位置。该图片与上文介绍腾讯云网页端SSH登陆操作的上下文相关，直观呈现了操作界面及新建连接配置的入口。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VwSwb8kBQoGZuFxxwPacQEwMnMe) · `VwSwb8kBQoGZuFxxwPacQEwMnMe`

> [!abstract]- 🖼 图片展示了腾讯云提供的网页端SSH登陆界面。在“接入产品”中选择“服务器
> 图片展示了腾讯云提供的网页端SSH登陆界面。在“接入产品”中选择“服务器”，在“选择腾讯云服务器”处输入服务器IP“1.117.59”并点击搜索，找到对应服务器后，连接协议选择“终端连接（SSH）”，用户名为“ubuntu”，云服务器端口为22，连接网络为“1.117.59.140(公网)”，验证方式为“密码验证”。该图片与上文介绍的腾讯云提供的网页端SSH登陆方式相呼应，直观呈现了登录操作步骤中的关键信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LCXObnjw9oJz66xAJxccZwS8nch) · `LCXObnjw9oJz66xAJxccZwS8nch`

</grid>

> [!abstract]- 🖼 图片展示了腾讯云提供的网页端SSH登陆界面。界面上方有“免密连接”和“S
> 图片展示了腾讯云提供的网页端SSH登陆界面。界面上方有“免密连接”和“SSH连接”选项卡，当前选中“SSH连接”。输入框中显示用户名为“ubuntu”，端口为“22”，实例IP为“1.117.59.140（公网）”，验证方式为“密码验证”，密码输入框提示“请输入密码”。下方有“登录”按钮，还提供了“如何快速登录”和“自助检测工具”等辅助功能。该图片与上文介绍的腾讯云提供的网页端SSH登陆方式相呼应，直观呈现了登录操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Wpz0b9iIzo1xaWxORqbcdskFnsg) · `Wpz0b9iIzo1xaWxORqbcdskFnsg`

输入之前购买服务器时的账号密码（如果已经修改则填写修改之后的），点击登录，则可以进入到Linux的页面啦

**如果出现下面这个页面，证明你登录成功了！**

> [!abstract]- 🖼 图片展示的是腾讯云提供的网页端SSH登陆成功后的界面。界面上方显示欢迎信
> 图片展示的是腾讯云提供的网页端SSH登陆成功后的界面。界面上方显示欢迎信息，包括系统版本、文档链接、管理链接、支持链接等。下方系统信息部分列出了系统负载、进程数量、磁盘使用率、内存使用率、IP地址等数据。最后显示了上次登录时间及登录IP。该图片与上文“登陆服务器，需要四个要素”及“腾讯云提供的网页端SSH登陆”内容相关，直观呈现了登陆成功后的界面情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VRjcb5gN8oSYymx3M5ScvF9dnyh) · `VRjcb5gN8oSYymx3M5ScvF9dnyh`

### 启用root账号

这一小节我会给大家介绍Linux的账号体系（不要发怵，跟Windows其实一样）

当你初次登陆你的云服务器的时候，你会发现这么一个东西：

> [!abstract]- 🖼 图片展示了Linux系统中登录云服务器时的用户信息界面。界面上方显示“L
> 图片展示了Linux系统中登录云服务器时的用户信息界面。界面上方显示“Last login: Thu Jun 13 18:05:45 2024 from 113.108.77.72”，下方是“ubuntu@VM-4-5-ubuntu:~$”字样，其中“ubuntu”代表当前登陆用户，“VM-4-5-ubuntu”是hostname，最后的“~$”是提示符。图片与上下文紧密相关，直观呈现了文档中介绍的Linux账号体系中关于用户登陆信息的内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GZahbxhSeoRNKtxpofZcWglZnLg) · `GZahbxhSeoRNKtxpofZcWglZnLg`

下面我们来拆解下这段文本的意思：

ubuntu@VM-4-5-ubuntu

- ubuntu 代表当前登陆的用户
- VM-4-5-ubuntu代表的是hostname（这个不用关心）

这里我们着重讲下用户的概念，对于用户而言，有一个特殊的用户就是root用户。

root用户是每个Linux系统默认都有的用户，这个用户有着最高级的权限，可以干任何事情。类似Win系统的管理员

在公司中，一般root用户都不会开放，防止造成不可逆的损害，一般都是通过分配不同的用户控制权限

但是对于个人使用而言，root用户就非常爽，在之后安装各种软件的时候都不用看系统脸色，想怎么搞就怎么搞

因此我们当下的一个事情就是将ubuntu用户切换到root用户，并且在ssh登陆的时候保存root的登陆方式，这样我们每次通过root的连接登陆就可以了

**第一步：为root账号设置一个密码**

ubuntu系统默认root账号是没有密码的，因此我们需要先为其设置一个密码

**下面开始命令行操作模式**

```Prolog
sudo passwd root
```

> [!abstract]- 🖼 图片展示了在Ubuntu系统中为root账号设置密码的命令行操作界面。画
> 图片展示了在Ubuntu系统中为root账号设置密码的命令行操作界面。画面中显示了“sudo passwd root”命令的执行情况，提示输入新密码，密码输入框已高亮显示。该图片与文档中“第一步：为root账号设置一个密码”部分内容对应，直观呈现了设置root账号密码的操作步骤，帮助用户了解在Linux系统中为root账号设置密码的具体命令及界面反馈。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YFQ6bPtLpoF6yIxlEwZctN68n2e) · `YFQ6bPtLpoF6yIxlEwZctN68n2e`

> [!abstract]- 🖼 图片展示了在Ubuntu系统中为root账号设置密码的命令行操作界面。在
> 图片展示了在Ubuntu系统中为root账号设置密码的命令行操作界面。在“sudo passwd root”命令执行后，系统提示输入新密码，两次输入后显示“passwd: password updated successfully”，表示密码设置成功。该图片与文档中“第一步：为root账号设置一个密码”内容对应，直观呈现了设置密码的操作步骤及结果，帮助用户理解如何在Ubuntu系统中为root账号设置密码。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/D4M9bMNAcorhpDxUX2AcFIV9nSg) · `D4M9bMNAcorhpDxUX2AcFIV9nSg`

**PS：注意，在输入密码的时候，屏幕上不会显示出来，这不是BUG，就是Linux系统的特点**

另外如果忘记了刚才设置的密码，则可以通过这个命令重新设置

**第二步：修改权限，允许root账号通过ssh登陆**

这段命令是一次性的而已，不需要记忆，我自己也是现用现找

```Shell
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
```

```Shell
sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
```

注意，这两个命令要一条一条执行，每一条命令中间不要换行。

这里我说下，我是如何找到这两条命令的！就是ChatGPT

> [!abstract]- 🖼 图片展示的是ChatGPT的界面。界面中央是ChatGPT的标志，下方有
> 图片展示的是ChatGPT的界面。界面中央是ChatGPT的标志，下方有四个选项，分别是“辅助写一首上锁的鸡汤”“编写实现摄氏-华氏温度转换的Python脚本”“像犹太人一样推销商品”以及“推荐有趣的社交媒体互动活动”。界面底部有输入框，提示“给ChatGPT发送消息”。结合上下文可知，作者在讲述云服务器实操中启用root账号时，提到通过ChatGPT找到了相关命令，此图即展示了ChatGPT界面情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LGnJb1eDHoS0iPxeTCzcl5KinQb) · `LGnJb1eDHoS0iPxeTCzcl5KinQb`

**第三步：重启SSH服务，使刚才的修改生效**

```Shell
sudo systemctl restart ssh
```

> [!abstract]- 🖼 图片展示的是在Linux系统中执行命令的界面。命令为“sudo syst
> 图片展示的是在Linux系统中执行命令的界面。命令为“sudo systemctl restart ssh”，用于重启SSH服务，使之前对root账号的修改生效。界面中显示了命令执行前后的提示符“ubuntu@VM-4-5-ubuntu:~$”，以及执行命令后的提示符“ubuntu@VM-4-5-ubuntu:~$”，表明命令执行成功。该图片与文档中“第三步：重启SSH服务，使刚才的修改生效”内容对应，直观呈现了重启SSH服务的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/L4JvbOoBjooom4xRsZ4cSFAknjb) · `L4JvbOoBjooom4xRsZ4cSFAknjb`

**第四步：创建root账号ssh登陆**

为了方便我们每次登陆的时候都是root账号，而不是unbutu账号，我们新建一个连接。

以后就使用这个root账号进行登陆

> [!abstract]- 🖼 图片展示了创建root账号ssh登陆的操作界面。画面左侧红框标注“点击连
> 图片展示了创建root账号ssh登陆的操作界面。画面左侧红框标注“点击连接配置”，提示需点击左上角的“连接配置”选项；右侧红框标注“新建配置”，指示点击“+新建”按钮来新建连接配置。图片中还列出了多个已有的连接配置信息，包括连接名称、IP地址、连接类型及验证方式等。该图片与上文“为了方便我们每次登陆的时候都是root账号，而不是ubuntu账号，我们新建一个连接”相呼应，直观呈现了新建连接配置的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RX9GbaLulo5fotxe9igcdzeVnjN) · `RX9GbaLulo5fotxe9igcdzeVnjN`

<grid>

> [!abstract]- 🖼 图片展示的是腾讯云服务器新建连接配置界面。在“连接协议”处，箭头指向“终
> 图片展示的是腾讯云服务器新建连接配置界面。在“连接协议”处，箭头指向“终端连接（SSH）”选项。下方“用户名”处显示“root”，并有红色框突出显示。此外，图片右上角有红色箭头指向“这里选择root账号”文字。该图片与文档中“第四步：创建root账号ssh登陆”内容相关，用于指导用户在新建连接时选择root账号进行SSH登陆操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CobtbUjz0o3o4kxrkaicUZ2qnJb) · `CobtbUjz0o3o4kxrkaicUZ2qnJb`

> [!abstract]- 🖼 图片展示的是云服务器登录界面。上方有“免密连接”和“SSH连接”选项，当
> 图片展示的是云服务器登录界面。上方有“免密连接”和“SSH连接”选项，当前选中“SSH连接”。实例名称/ID为“Coze机器人接入微信教学 / lhins-2sbvixs4”。用户名为“root”，端口为22，实例IP为1.117.59.140（公网）。验证方式为“密码验证”，密码框已输入密码。界面右下角有“登录”按钮，下方提示“其他登录方式：VNC登录”。该图与上文“创建root账号ssh登陆，以后就使用这个root账号进行登陆”的内容相关，展示了使用root账号ssh登录云服务器的操作界面。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/L8JQbajtCoZd7QxpdRTcpaeWnOd) · `L8JQbajtCoZd7QxpdRTcpaeWnOd`

</grid>

> [!abstract]- 🖼 图片展示了轻量云OrcaTerm界面中连接配置的相关内容。左侧导航栏选中
> 图片展示了轻量云OrcaTerm界面中连接配置的相关内容。左侧导航栏选中“OrcaTerm”，右侧弹出连接配置窗口，其中“连接配置”选项被红色框突出显示。窗口下方显示“默认分组”，并有“root@1.177.59.140”字样，右侧有“终端连接（SSH）”“密码验证”等选项，还标注“以后就用这个登陆啦”。图片与上文“创建root账号ssh登陆，以后就使用这个root账号进行登陆”的内容相呼应，直观呈现了root账号的登陆信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/W4XMbSz0Oohx0Lx33L8ccTQqnuc) · `W4XMbSz0Oohx0Lx33L8ccTQqnuc`

### 登陆界面美化

这一块就看大家啦，我喜欢把界面搞成我喜欢的风格，毕竟要一直打交到呢

> [!abstract]- 🖼 图片展示了腾讯云轻量云界面中OrcaTerm的设置操作。左侧导航栏选中“
> 图片展示了腾讯云轻量云界面中OrcaTerm的设置操作。左侧导航栏选中“OrcaTerm”，右侧菜单中“设置”被红色框和箭头突出显示。图片与上下文紧密相关，上下文提到在Linux系统中安装增强插件以解决文件编辑、上传下载等问题，此图即为第一步安装增强插件的操作指引，直观呈现了点击设置的步骤，帮助用户在腾讯云轻量云中进行相关设置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LrRPbPHhIo8HDYx7k2kcEhQontg) · `LrRPbPHhIo8HDYx7k2kcEhQontg`

> [!abstract]- 🖼 图片展示了腾讯云服务器登陆界面的外观设置界面。左侧有“外观设置”和“主题
> 图片展示了腾讯云服务器登陆界面的外观设置界面。左侧有“外观设置”和“主题设置”两个选项，其中“外观设置”被红色框线突出显示。右侧是字体设置区域，可选择字体样式、大小等，还设有光标设置和是否开启光标跟随选项。下方是背景设置区域，有主背景、雪山、日出、极光等背景图片供选择，也可上传图片。图片与上下文紧密相关，直观呈现了登陆界面美化操作中外观设置的具体内容。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TKt6b4W4Yoey2SxeZXicjmT3nNe) · `TKt6b4W4Yoey2SxeZXicjmT3nNe`

### 增强插件安装

在Linux系统中，有比较麻烦的几个事情：

- 文件的编辑
- 文件上传到服务器
- 文件从服务器下载到本地

我们选择的SSH软件要支持这几个能力，否则使用起来Linux系统会有一些痛苦

我们这里来看下腾讯云是如何解决这些问题的

**第一步：安装一些增强的插件**

<grid>

> [!abstract]- 🖼 图片展示了腾讯云服务器登录界面中增强插件安装的操作提示。界面左上角有“安
> 图片展示了腾讯云服务器登录界面中增强插件安装的操作提示。界面左上角有“安装增强功能，使用编辑器”的文字，右侧有“安装增强功能”的红色箭头指向文字。该图片与文档中“增强插件安装”部分内容相关，对应“第一步：安装一些增强的插件”步骤，直观呈现了在Linux系统中安装增强功能的操作提示，帮助用户了解如何在腾讯云服务器上安装增强插件以提升使用体验。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/M05wb10p2oTUWAxcxjuccwzknIb) · `M05wb10p2oTUWAxcxjuccwzknIb`

> [!abstract]- 🖼 图片展示的是腾讯云服务器增强功能安装界面。界面上方显示“安装增强功能”，
> 图片展示的是腾讯云服务器增强功能安装界面。界面上方显示“安装增强功能”，并有“选择安装增强功能”和“进行安装”两个步骤。基础服务可选“命令块”和“上传下载”，前者将命令和结果组合展示，后者可在界面中选择上传下载文件地址。增强服务可选“文件编辑器”和“实时监控”，前者安装后可快速打开文件编辑器，后者在底栏实时展示实例的CPU、内存等数据。该图与上下文介绍的腾讯云增强插件安装步骤相关，直观呈现了可选功能。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YZ8ybrYLGohNoAxVIJMcWNTvnke) · `YZ8ybrYLGohNoAxVIJMcWNTvnke`

</grid>

> [!abstract]- 🖼 图片展示了在Linux系统中安装增强插件的安装界面。界面上方显示了安装命
> 图片展示了在Linux系统中安装增强插件的安装界面。界面上方显示了安装命令及部分安装信息，如“code-server”安装版本为8.3.2等。下方突出显示了安装步骤，包括安装code-server、extension、init user-settings、install supervisor等，每一步后均有“installing”字样。右下角有“安装已成功”的提示框。该图片与上下文紧密相关，直观呈现了安装增强插件的具体操作及结果，辅助说明了在Linux系统中安装增强插件的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/U1ZYb7KR2o5Wdnx0MXUcmHfdnDe) · `U1ZYb7KR2o5Wdnx0MXUcmHfdnDe`

**第二步：试用下编辑器的效果**

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/J5VYbcwsaocoOuxoSuVcKHggn3T) · `J5VYbcwsaocoOuxoSuVcKHggn3T`

## 云服务器概览页面

 这里我们需要解释几个概念，帮助你更好的理解和监控云服务器

> [!abstract]- 🖼 图片展示了云服务器概览页面，左侧为导航栏，选中“服务器”选项。右侧上方显
> 图片展示了云服务器概览页面，左侧为导航栏，选中“服务器”选项。右侧上方显示公有IP地址为1.117.59.140。实例监控区域突出显示了两个关键指标：CPU利用率（%）和内存使用量（MB），并有红色箭头指向。该图与上下文紧密相关，用于直观呈现云服务器的公有IP地址及关键监控指标，帮助用户更好地理解和监控云服务器状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UcDibqK01ocvKlxViP1ccB3in7e) · `UcDibqK01ocvKlxViP1ccB3in7e`

> [!abstract]- 🖼 图片展示了云服务器概览页面的关键信息。左侧显示远程登录方式及网络与域名，
> 图片展示了云服务器概览页面的关键信息。左侧显示远程登录方式及网络与域名，有公网和内网IP、系统名称等；右侧呈现资源使用情况，包括流量包使用量、系统盘使用量等，其中系统盘使用量为11.8%。图片与上下文紧密相关，直观呈现了文档中提到的云服务器概览页面需关注的三个指标：CPU使用率、内存使用量、硬盘使用量，帮助用户更好地理解和监控云服务器状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/HQVmb80Sto2YBHxMQxMcf5bunTb) · `HQVmb80Sto2YBHxMQxMcf5bunTb`

这里我们需要关注三个指标

- **CPU使用率**：当CPU使用率突然高于平常时，你要考虑是不是机器出什么问题了
- **内存使用量**：本服务器的内存使用量是2G，当你运行的软件越来越多时，内存就会升高，如果打满，服务器就会死机，你可能需要重启（这跟Win是一样的道理）
- **硬盘使用量**：跟Win机器一样，磁盘满了，机器也就死机了，这时候你可能需要清理日志

那么当这些满了之后该怎么办呢？最暴力的方案，直接升级配置，2核变4核，2G变4G，搞定！

我们还需要关注两个概念

- 公网IP和内网IP
- 操作系统

操作系统我们前面专门讲过了，为什么这里要再次提起呢，我想告诉你的是：

**遇到问题实在解决不了，那就重装操作系统吧，云服务器重装操作系统就跟玩一样，非常简单！**

**不过后果就是你的数据全丢了**

**这里主要说下公网IP和内网IP**

如果不知道IP是什么，请移步：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜程序中的API是什么|加餐｜程序中的API是什么]]

公网IP就是这台云服务器在全球的唯一身份标识，当我们需要跟这个云服务器通信时，就要使用公网IP

内网IP是在腾讯云这个框架下唯一的身份标识，如果两个腾讯云服务器通信，可以直接考虑内网IP，因为速度更快

## Linux命令

前面除了修改Root的密码那一段，我们基本没有涉及到Linux的命令，原因就是想集中跟大家讲。

为了方便大家复制命令，我开另一个文档专门讲Liunx命令，里面会配套有视频演示教程

[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜常见的Linux命令|加餐｜常见的Linux命令]]

## 引出Docker和Python

这时候有同学可能要问了，大圣，你的服务器不安装一些必要的环境么，比如Python，比如Docker

其实当我们使用腾讯云的Ubuntu22.04-Docker26时，一些默认的环境已经安装好了！

这里我先带大家看一下，后面我们详细讲

### 查看Python的版本

```Shell
python3 --version
```

> [!abstract]- 🖼 图片展示了在Linux系统中查看Python版本的操作及结果。画面中显示
> 图片展示了在Linux系统中查看Python版本的操作及结果。画面中显示命令“python3 --version”被输入，执行后返回“Python 3.10.12”，表明当前系统安装的Python版本为3.10.12。该图片与文档中“查看Python的版本”内容相关，是演示查看Python版本操作及结果的示例，用于说明在云服务器部署Cow和百炼课程时，查看Python版本的操作步骤和结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RcMgbjDTco7kCixsIgtcj9LDncd) · `RcMgbjDTco7kCixsIgtcj9LDncd`

### 查看Docker的版本

```Shell
docker --version
```

> [!abstract]- 🖼 图片展示了在Linux系统中查看Docker版本的操作及结果。画面中，先
> 图片展示了在Linux系统中查看Docker版本的操作及结果。画面中，先执行了“python3 --version”命令，显示Python版本为3.10.12。随后执行“docker --version”命令，结果显示Docker版本为26.1.3，构建版本为b72abbb。该图片与文档中“查看Docker的版本”内容对应，直观呈现了查看Docker版本的操作步骤及结果，辅助说明已安装必要的环境，满足Coze对接微信机器人的课程需求。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XJlXbAna1oVn5Fx2rj1cYxhynig) · `XJlXbAna1oVn5Fx2rj1cYxhynig`

可以看到几个必要的环境都装了，这个环境已经满足我们Coze对接微信机器人的课程需求了

OK，接下来我们会用另一篇文章来专门讲下Docker：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜Docker是什么|加餐｜Docker是什么]]

# 二、部署COW

COW全称Chatgpt on wechat，是一个可以将微信接入大模型的开源项目。

废话不多说，我们看下，怎么最快拥有自己的一个小机器人

## 拉取Cow的代码

1. 首先我们通过下面这个命令切换到root这个文件夹下

```Plain Text
cd /root
```

**注意：输入命令之后要按回车**

> [!abstract]- 🖼 图片展示了在Linux系统中切换到root文件夹的操作界面。界面上方显示
> 图片展示了在Linux系统中切换到root文件夹的操作界面。界面上方显示“连接配置”等选项，中间部分有CPU、MEM等系统信息。下方命令行区域显示“root@VM-4-5-ubuntu:~#”，并有红色框突出显示“cd /root”命令，该命令用于切换到root文件夹。此图对应文档中“拉取Cow的代码”部分，用于指导用户通过执行“cd /root”命令切换到root文件夹，是部署Cow机器人过程中的一步操作说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Y58Sbg2sWofQQkxo3qYcLVBenFg) · `Y58Sbg2sWofQQkxo3qYcLVBenFg`

1. 执行如下命令

```Bash
git clone https://github.com/zhayujie/chatgpt-on-wechat/
```

> [!abstract]- 🖼 图片展示的是服务器部署COW时拉取代码的命令操作界面。界面中显示两条命令
> 图片展示的是服务器部署COW时拉取代码的命令操作界面。界面中显示两条命令，第一条为“cd /root”，第二条为“git clone https://github.com/zhayujie/chatgpt-on-wechat”，第二条命令被红色框线突出显示。界面右下方有红色箭头及文字“按回车”进行指示。该图片对应文档中“拉取Cow的代码”部分内容，是对“执行如下命令”的直观展示，用于指导使用者在服务器上执行相应命令拉取COW代码。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WNHqbeyajobvONxuUDPcPEZFn3g) · `WNHqbeyajobvONxuUDPcPEZFn3g`

注意：如果出现下面这个错误哦，没有关系，再来一次就好

> [!abstract]- 🖼 图片展示了在Ubuntu系统中执行git clone命令时出现的错误信息
> 图片展示了在Ubuntu系统中执行git clone命令时出现的错误信息。命令为“git clone https://github.com/zhayujie/chatgpt-on-wechat”，执行后显示“fatal: unable to access 'https://github.com/zhayujie/chatgpt-on-wechat/': GnuTLS recv error (-110): The TLS connection was non-properly terminated.”。该图片与文档中“拉取Cow的代码”部分相关，用于说明在执行拉取代码命令时可能出现的错误情况，提示用户若出现类似错误可再试一次。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/GjJDbsCpGoJ2gBx5n7LcHShRnYp) · `GjJDbsCpGoJ2gBx5n7LcHShRnYp`

这是正在跑的过程的截图

> [!abstract]- 🖼 图片展示了在root文件夹下拉取Cow代码时的命令执行过程。先是切换到r
> 图片展示了在root文件夹下拉取Cow代码时的命令执行过程。先是切换到root文件夹，接着执行git clone命令，克隆仓库至chatgpt-on-wechat目录。过程中显示远程仓库对象计数、压缩对象等信息，最后接收对象进度为21%，传输速度为112.00 KiB/s。该图片与文档中“拉取Cow的代码”部分对应，直观呈现了拉取代码时的命令执行情况及进度。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CJSWbILR4oFY7cxeNATcT9FKnF0) · `CJSWbILR4oFY7cxeNATcT9FKnF0`

这是下载完成的截图

> [!abstract]- 🖼 图片展示了在Ubuntu系统中执行git clone命令拉取Cow代码后
> 图片展示了在Ubuntu系统中执行git clone命令拉取Cow代码后的运行结果。命令执行后，显示了远程仓库对象的枚举、计数、压缩等进度信息，最后“Resolving deltas: 100% (3868/3868), done.”表明下载完成。下载完成后，当前目录下出现了“chatgpt-on-wechat”文件夹，与上文提到的拉取Cow代码操作相呼应，直观呈现了代码下载成功及文件夹创建情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/QDUvbHvMjoH2GIx9WkTcVtEHnzf) · `QDUvbHvMjoH2GIx9WkTcVtEHnzf`

## COW依赖安装

1. 进入到chatgpt-on-wechat的文件夹中

```Bash
cd chatgpt-on-wechat/
```

> [!abstract]- 🖼 图片展示了在Linux系统中切换到“chatgpt-on-wechat”
> 图片展示了在Linux系统中切换到“chatgpt-on-wechat”文件夹的操作结果。先是显示了当前目录为“~”，然后执行“cd chatgpt-on-wechat”命令后，目录变为“~/chatgpt-on-wechat”，底部提示符也相应变化。该图片与上下文紧密相关，是在介绍部署COW过程中，进入“chatgpt-on-wechat”文件夹的操作步骤，直观呈现了操作结果，帮助用户确认是否成功进入该文件夹。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/CA0TbOT16odJXexdWDIc6P4dnlf) · `CA0TbOT16odJXexdWDIc6P4dnlf`

1. 下载安装一些依赖文件

首先执行这个命令，下载一些文件

```Bash
pip install -r requirements.txt
```

> [!abstract]- 🖼 图片展示的是在chatgpt-on-wechat文件夹下执行pip in
> 图片展示的是在chatgpt-on-wechat文件夹下执行pip install -r requirements.txt命令的终端输出结果。显示正在查找镜像，找到openai和HTMLParser的安装位置。其中openai已满足要求，位于/usr/local/lib/python3.10/dist-packages目录下；HTMLParser也已满足要求，同样位于该目录。该图片与上下文紧密相关，是COW依赖安装步骤中下载安装依赖文件操作后的结果呈现。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XLrXbed9jouBbzxhzHic9EUFnke) · `XLrXbed9jouBbzxhzHic9EUFnke`

> [!abstract]- 🖼 图片展示的是在服务器部署COW时，下载安装依赖文件过程中的命令行界面反馈
> 图片展示的是在服务器部署COW时，下载安装依赖文件过程中的命令行界面反馈信息。界面中显示了多个依赖项已满足要求的提示，如aiosignal、multidict等，还出现了一条关于“root”用户使用可能导致权限问题的警告。底部用红色字体突出显示“只要不报错，就代表安装完成”的提示信息。该图片对应文档中“COW依赖安装”部分，是执行下载依赖文件命令后出现的结果截图，辅助说明依赖安装状态。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DlwBbyR1roClZkxdl8pcn734nGe) · `DlwBbyR1roClZkxdl8pcn734nGe`

然后执行下面这个命令，下载另外一些文件

```Bash
pip install -r requirements-optional.txt
```

> [!abstract]- 🖼 图片展示了在chatgpt-on-wechat文件夹下执行命令“pip 
> 图片展示了在chatgpt-on-wechat文件夹下执行命令“pip install -r requirements-optional.txt”的操作界面。命令执行后，显示了正在查找镜像源的信息，以及部分依赖包已满足的提示，如tiktoken、pydub等。该图片与上下文紧密相关，是部署COW过程中“COW依赖安装”步骤中下载安装依赖文件的操作示例，直观呈现了命令执行情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/H16HbtnjcouKUWxjxxYcn65ZnCd) · `H16HbtnjcouKUWxjxxYcn65ZnCd`

> [!abstract]- 🖼 图片展示了在Ubuntu系统中执行命令下载COW依赖文件时的终端输出结果
> 图片展示了在Ubuntu系统中执行命令下载COW依赖文件时的终端输出结果。输出显示“Requirement already satisfied”信息，表明已满足相关依赖要求，如asttokens、pure - eval等。还有一条警告信息，提示以root用户运行pip可能引起权限问题，建议使用venv环境。最后显示“root@VM - 4 - 5 - ubuntu:~/chatgpt - on - wechat#”提示符，下方有“没有报错就是好的”文字。该图片与文档中部署COW过程中依赖安装的内容相关，用于说明下载依赖文件成功且无报错的情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/VRQtbni19op5VjxB4KfccNmGnUe) · `VRQtbni19op5VjxB4KfccNmGnUe`

## 修改配置文件

完成依赖安装之后，接下来就是配置COW啦，你离成功又近了一步

1. 复制一份文件出来

注意：这个命令的意思是：将config-template.json这个文件复制一份，名字为：config.json

```Bash
cp config-template.json config.json
```

> [!abstract]- 🖼 图片展示了在Linux终端中执行命令“cp config-templat
> 图片展示了在Linux终端中执行命令“cp config-template.json config.json”的操作过程。终端显示当前目录为“~/chatgpt-on-wechat#”，执行复制命令后，命令行提示符变为“root@VM-4-5-ubuntu:~/chatgpt-on-wechat#”。该图片对应文档中“修改配置文件”部分，用于说明将config-template.json文件复制为config.json文件的操作，是部署COW过程中修改配置文件步骤前的准备操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/K1NwbLveYohRUDx3cZxct7GQnme) · `K1NwbLveYohRUDx3cZxct7GQnme`

1. 找到config.json文件，并且进行修改

> [!abstract]- 🖼 图片展示了在Linux系统中打开并双击config.json文件的操作步
> 图片展示了在Linux系统中打开并双击config.json文件的操作步骤。左侧界面中，红色框突出显示了“chatgpt-on-wechat”文件夹，箭头指向“打开这个文件夹”；右侧界面中，红色框标注了config.json文件，箭头指向“定位到这个文件并且双击”，并说明默认路径为“/root/chatgpt-on-wechat”。该图片与上文“找到config.json文件，并且进行修改”的内容相关，直观呈现了操作步骤，帮助用户了解如何找到并打开config.json文件。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Gmt5bOYMLontiQxN5gWcqmHmnLe) · `Gmt5bOYMLontiQxN5gWcqmHmnLe`

**这就是config.json文件中的内容，接下来我们就要修改这里面的内容了**

> [!abstract]- 🖼 图片展示的是config.json文件内容，用于配置COW接入微信数学。
> 图片展示的是config.json文件内容，用于配置COW接入微信数学。文件中包含多个参数，如channel_type为“wx”表示接入微信，model为“dalle-2”，open_ai_api_key为千问API密钥，single_chat_prefix和group_chat_prefix分别定义单聊和群聊触发机器人回复的前缀，group_name_white_list列出生效群组，image_create_prefix用于生成图片，speech_recognition等参数控制语音识别、回复语音等，conversation_max_tokens为最大对话长度，expires_in_seconds为过期时间，character_desc介绍角色功能，temperature为生成文本的随机性，subscribe_msg为欢迎语，use_linkai等参数控制是否使用LinkAI等。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KbtVbZlu1opX3FxGwLBczuvWnKh) · `KbtVbZlu1opX3FxGwLBczuvWnKh`

这里是我们老朋友了，这种格式就是JSON，不知道JSON的请阅读：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜Coze的插件与JSON|加餐｜Coze的插件与JSON]]

我们来解释几个关键的概念

| **key** | **含义** | 示例 |
|-|-|-|
| model | 模型 |  |
| open_ai_api_key | 接入的大模型的地址 | 不同的模型，key会不一样 |
| single_chat_prefix | 跟微信机器人对话时，如何触发机器人回复 | ["大圣"]  <br/>这个代表，当你跟你的机器人私聊时，你需要以大圣开头，这样他才会自动跟你对话 |
| single_chat_reply_prefix | 机器人回复你时的前缀 |  |
| group_chat_prefix | 在群里如何唤起机器人 | ["@大圣"] 意思是你需要@大圣 然后他才能回复你  <br/>如果你这里不填写，默认它会回复任何问题 |
| group_name_white_list | 这个是说你的机器人可以在那个群里生效 | [  <br/>    "Coze实战课程群"  <br/>  ]  <br/>代表这个机器人可以在Coze实战课程群群组中生效 |
| group_welcome_msg | 当别人入群时，机器人的欢迎语 |  |

为了让大家能够快速启动这个小机器人，我们这里需要申请下千问的API

## 申请通义千问API KEY

大模型的API是啥子，我想这篇文章可能会给你答案：[[成为Agent工程师/Coze实战课项目/加餐文档/编程思维体系/加餐｜程序中的API是什么|加餐｜程序中的API是什么]]

当然，你也可以不用关心这个，直接上手实操

1. 进入阿里云灵积官网

https://dashscope.console.al iyun.com/

**进行登陆**

> [!abstract]- 🖼 图片展示的是阿里云灵积官网首页。左侧有“C-D阿里云”标志及“DashS
> 图片展示的是阿里云灵积官网首页。左侧有“C-D阿里云”标志及“DashScope模型服务灵积”字样，下方介绍灵积旨在通过提供灵活、易用的模型API服务，让业界各模态模型能力触达AI开发者。右侧有“控制台”“模型广场”“模型定制”等导航按钮，以及一个展示AI应用的插画。图片与上下文关系紧密，是文档中介绍进入阿里云灵积官网进行登陆操作的页面示例。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MpYHbh3XRoAyuSxo2VFcj05Rn0b) · `MpYHbh3XRoAyuSxo2VFcj05Rn0b`

> [!abstract]- 🖼 图片展示的是阿里云灵积官网的模型服务页。页面左侧有导航栏，右侧上方有“开
> 图片展示的是阿里云灵积官网的模型服务页。页面左侧有导航栏，右侧上方有“开通”按钮。中间区域介绍通义千问2.1（qwen - max）API升级，限时免费开放。下方有模型应用图景，包括模型定制、模型应用等内容。最下方显示“我使用过的模型”，并有“暂无最近体验模型”提示。该图片与上下文关系紧密，是申请通义千问API KEY操作流程中，开通完成后的页面展示，用于引导用户进行API Key创建等后续操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/NBjhbMURRoJo9Nx6pJncvNFenag) · `NBjhbMURRoJo9Nx6pJncvNFenag`

> [!abstract]- 🖼 图片展示的是阿里云灵积官网的模型服务页面。页面上方显示“模型服务”标题，
> 图片展示的是阿里云灵积官网的模型服务页面。页面上方显示“模型服务”标题，下方有服务名称“CleanScope机器模型服务”及服务说明，说明该服务提供不同任务的模型，可通过API调用模型服务。当前阶段只计量，不计费，待技术展示或限量免费试用结束后将公布模型的具体定价信息，并正常计量计费。页面右下角有“立即开通”按钮，左下角有“服务协议”选项。该图片与文档中申请通义千问API KEY的操作流程相关，是开通服务前的页面展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OFCLbAZK8oJFjMxKWXtc2h9VnSf) · `OFCLbAZK8oJFjMxKWXtc2h9VnSf`

开通完成之后，使用这个方式来创建API Key

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/QSIPbW8qSo9MaLxyWCKcyYp4nHh) · `QSIPbW8qSo9MaLxyWCKcyYp4nHh`

1. 获取到了通义千问的Token

sk-1f44bc13e2df44ca96169c411f7d87aa

然后修改我们之前提到的配置文件

注意：下面的配置文件你可以直接复制，但是

- **dashscope_api_key换成你自己的**
- **group_chat_prefix 换成你自己喜欢的**
- **group_name_white_list 可以添加你想要的群**

  - 如果想要全部群组生效，请添加"ALL_GROUP"
- **group_welcome_msg:""  这个必须添加，比赛要求，要关闭群欢迎语**

```JSON
{
  "channel_type": "wx",
  "model": "qwen-max",
  "dashscope_api_key": "sk-1f44bc13e2df44ca96169c411f7d87aa这里更换为你自己的key",
  "text_to_image": "dall-e-2",
  "voice_to_text": "openai",
  "text_to_voice": "openai",
  "proxy": "",
  "hot_reload": false,
  "single_chat_prefix": [
    ""
  ],
  "single_chat_reply_prefix": "小圣",
  "group_chat_prefix": [
    "小圣"
  ],
  "group_name_white_list": [
    "Coze课程｜机器人比赛预热",
    "ALL_GROUP"
  ],
  "image_create_prefix": [
    "画"
  ],
  "group_welcome_msg":"",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2500,
  "expires_in_seconds": 3600,
  "character_desc": "你是基于大语言模型的AI智能助手，旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。",
  "temperature": 0.7,
  "subscribe_msg": "感谢您的关注！\n这里是AI智能助手，可以自由对话。\n支持语音对话。\n支持图片输入。\n支持图片输出，画字开头的消息将按要求创作图片。\n支持tool、角色扮演和文字冒险等丰富的插件。\n输入{trigger_prefix}#help 查看详细指令。",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}

```

> [!abstract]- 🖼 图片展示的是一个名为“Cozie机器人接入微信教学的文件管理器”界面，正
> 图片展示的是一个名为“Cozie机器人接入微信教学的文件管理器”界面，正在编辑“/root/chatgpt - on - wechat/config.json”配置文件。配置文件中有多项设置，如“channel_type”“model”等。其中“dashscope_api_key”处显示的是“sk-1f44bc13e2df44ca96169c411f7d87aa”。图中有红色箭头及文字提示“粘贴过来，会自动保存”。该图片与上文提到的修改配置文件相呼应，直观呈现了配置文件的具体内容及相关设置位置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Ld6zbnwHVoFL4YxZXljcuZBWn5b) · `Ld6zbnwHVoFL4YxZXljcuZBWn5b`

## 启动Cow

1. 首先需要创建一个脚本：restart.sh

```Bash
cd /root/chatgpt-on-wechat/
```

> [!abstract]- 🖼 图片展示了在终端中执行的命令。命令为“cd /root/chatgpt-
> 图片展示了在终端中执行的命令。命令为“cd /root/chatgpt-on-wechat/”，其中“cd”是切换目录的命令，“/root/chatgpt-on-wechat/”是目标目录路径。该图片与文档中“查看日志”部分内容相关，是在重新登陆服务器后，查看对话日志时，第一步需要执行的命令，即进入对的文件夹，此操作是查看日志流程中的关键步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KcaGbkkZboqU41xpMUmcLj8Gnnd) · `KcaGbkkZboqU41xpMUmcLj8Gnnd`

创建nohup.out日志文件

```Bash
touch restart.sh
```

> [!abstract]- 🖼 图片展示了在Linux终端中创建脚本的操作及文件列表。终端命令“touc
> 图片展示了在Linux终端中创建脚本的操作及文件列表。终端命令“touch restart.sh”用于创建名为“restart.sh”的空文件，操作后文件列表中出现“restart.sh”文件。该图片与文档中“启动Cow”部分的脚本创建步骤相关，直观呈现了创建“restart.sh”脚本的操作及文件状态，辅助说明了在服务器部署Cow时，首先需创建此脚本的操作流程。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/I6DVbTbQ8oKPl4xlO7JcJziFnZg) · `I6DVbTbQ8oKPl4xlO7JcJziFnZg`

创建好这个文件后，将以下内容贴入（**请完全复制**）

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/KkdQbnOGmoF4JPx01iOcvlo5ndb) · `KkdQbnOGmoF4JPx01iOcvlo5ndb`

```Bash
#!/bin/bash
touch nohup.out
# 2. 直接终止 python3 app.py 的进程（如果存在）
ps aux | grep "python3 app.py" | grep -v grep | awk '{print $2}' | xargs -r kill -9
echo "已经终止所有的微信机器人进程"
# 3. 执行 nohup python3 app.py 并实时查看输出
echo "正在启动新的进程以及打印日志"
nohup python3 app.py & tail -f nohup.out
```

> [!abstract]- 🖼 图片展示了在服务器上启动Cow机器人时的命令执行及日志查看流程。左侧是终
> 图片展示了在服务器上启动Cow机器人时的命令执行及日志查看流程。左侧是终端界面，显示了启动命令执行情况，如“python3 app.py”运行成功，以及“nohup python3 app.py &”命令执行结果。右侧是文件管理器界面，显示了“/root/cowchat-on-wechat”目录下的文件，其中“restart.sh”文件被红色框突出显示。该图片与上下文紧密相关，直观呈现了启动Cow机器人及查看日志时的终端操作和文件管理操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/UNP1bRsNGoh0GGxb4EPcvHZlnFb) · `UNP1bRsNGoh0GGxb4EPcvHZlnFb`

> [!abstract]- 🖼 图片展示的是在服务器上启动Cow的seelog.sh脚本内容。脚本首先检
> 图片展示的是在服务器上启动Cow的seelog.sh脚本内容。脚本首先检查nohup.out文件是否存在，若不存在则创建；接着检查是否有python3 app.py进程，若有则停止；最后执行nohup python3 app.py & tail -f nohup.out命令并实时查看输出。该脚本与文档中启动Cow的操作流程相关，用于准备启动Cow并执行启动命令，输出日志。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/IkZPbbvgGo6I4vxZssgcgHaRnid) · `IkZPbbvgGo6I4vxZssgcgHaRnid`

注意：这段的意思是

- 如果没有nohup.out的文件，则创建一个文件
- 如果发现已经有python3 app.py的进程，则删除（**注意这里会导致不能同时登陆两个机器人**）
- 最后执行启动命令，然后输出日志

1. 再创建一个seelog.sh的文件

```Bash
touch seelog.sh
```

里面写入内容：

```Bash
tail -f nohup.out
```

> [!abstract]- 🖼 图片展示的是“Coze机器人接入微信教学”的文件管理器界面，当前编辑文件
> 图片展示的是“Coze机器人接入微信教学”的文件管理器界面，当前编辑文件为/root/chatgpt-on-wechat/seelog.sh。内容为一行命令“tail -f nohup.out”，用于查看日志。该图片与文档中“查看日志”部分内容相关，是在介绍查看对话日志时，进入对的文件夹后，运行查看日志脚本的步骤中，展示的脚本内容，帮助用户了解如何执行查看日志操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OrzQbUwHKo0nyYx17nicuFAhnwd) · `OrzQbUwHKo0nyYx17nicuFAhnwd`

1. 准备启动cow
2. 

依次执行如下命令

```Bash
cd /root/chatgpt-on-wechat/
```

```Bash
sh restart.sh
```

> [!abstract]- 🖼 图片展示的是启动Cow后出现的二维码界面。上方有“Ready to lo
> 图片展示的是启动Cow后出现的二维码界面。上方有“Ready to login.”及“Getting build of QR code. Downloading QR code.”等提示信息。中间是二维码，下方有“You can also scan QRCode in any website below:”及多个网址。该图片对应文档中“启动Cow”部分，当出现此二维码时，需用微信号扫描登陆，登陆后可与小机器人对话。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LrXrbAhA2o5f6dxV789cf0gCn1g) · `LrXrbAhA2o5f6dxV789cf0gCn1g`

当出现如下二维码的时候，请用你的微信号扫描登陆，就跟你登陆网页微信一样的

当你扫码之后（这个码不太好扫，请有点耐心...）

当出现下面的东西的时候，你就可以跟你的小机器人对话了

> [!abstract]- 🖼 图片展示的是启动Cow后出现的二维码及日志信息。二维码用于微信扫码登陆，
> 图片展示的是启动Cow后出现的二维码及日志信息。二维码用于微信扫码登陆，下方提示需在手机上确认。日志信息显示微信登录成功，user_id为特定值，nick_name为“倔强的猴子”，并提示“Start auto replying.”。该图片与文档中“启动Cow”部分上下文对应，是扫码登陆后可与小机器人对话的示例，用于指导用户完成登陆操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/BWogbhuMJosxcWxJZ2fclymfnWf) · `BWogbhuMJosxcWxJZ2fclymfnWf`

## 查看日志

如果重新登陆了服务器，想要查看对话的日志（当出现错误的时候，日志是最有用的）

请按照如下流程

1. 进入到对的文件夹

```Bash
cd /root/chatgpt-on-wechat/
```

1. 运行查看日志的脚本

```Bash
sh seelog.sh
```

![图片展示的是服务器部署Cow后查看日志时出现的界面。界面上方显示“Loading the contact, this may take a little while.”等信息。下方有多个“\[INFO\]”日志条目，其中红框突出显示了两条关键日志，分别是“\[INFO\] \[2024-07-24 00:05:45\] \[dashscope_bot.py:35\] - \[DASHSCOPE\] query=, 出来”和“\[INFO\] \[2024-07-24 00:05:46\] \[wechat_channel.py:214\] - \[WX\] sendMsg=Reply(type=TEXT, content=@大圣 您好！我已经在这里了，有什么可以帮助您的吗？), receiver=@@823e3c80edd550c6aba0efad0fd636fdd025668a52bd6b10adabc32b3df22b8b”。这些日志信息与上下文提到的查看对话日志流程相关，是查看日志时能看到的具体内容。](https://feishu.cn/file/ZcRIbwwBEoetlcxpIrFc1QHgnpf)

# 三、接入阿里云百炼

上面接入通义千问API的方式有弊端，每次要修改提示词都要重启COW，好烦。

如果我们可以接入通义千问的应用百炼，当我们修改提示词的时候，我们就不用重启COW了

在接入百炼的时候，我们需要额外四个字段

- **qwen_access_key_id**
- **qwen_access_key_secret**
- **qwen_agent_key**
- **qwen_app_id**

```Bash
{
  "channel_type": "wx",
  "model": "qwen",
  "qwen_access_key_id": "替换成你自己",
  "qwen_access_key_secret": "替换成你自己的",
  "qwen_agent_key": "替换成你自己的",
  "qwen_app_id": "替换成你自己的",
  "text_to_image": "dall-e-2",
  "voice_to_text": "openai",
  "text_to_voice": "openai",
  "proxy": "",
  "hot_reload": false,
  "single_chat_prefix": [
    "小圣"
  ],
  "single_chat_reply_prefix": "小圣",
  "group_chat_prefix": [
    "小圣"
  ],
  "group_name_white_list": [
    "Coze课程｜机器人比赛预热",
    "ALL_GROUP"
  ],
  "image_create_prefix": [
    "画"
  ],
  "group_welcome_msg":"",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2500,
  "expires_in_seconds": 3600,
  "character_desc": "你是基于大语言模型的AI智能助手，旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。",
  "temperature": 0.7,
  "subscribe_msg": "感谢您的关注！\n这里是AI智能助手，可以自由对话。\n支持语音对话。\n支持图片输入。\n支持图片输出，画字开头的消息将按要求创作图片。\n支持tool、角色扮演和文字冒险等丰富的插件。\n输入{trigger_prefix}#help 查看详细指令。",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}

```

接下来我们来看，这四个字段哪里来，

你需要两个官网：

- 百炼官网：https://bailian.console.aliyun.com/#/home
- 阿里云主页官网：https://www.aliyun.com/

接下来请看视频

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/BQJybKAQHoxoGqxaErzcEbeYnyg) · `BQJybKAQHoxoGqxaErzcEbeYnyg`

**PS：大家千万不要用我视频中的Key**

| **key** | **对应的位置以及数据** |
|-|-|
| **qwen_access_key_id** | LTAI5tLJhLHLoR6guzr5jDJZ |
| **qwen_access_key_secret** | c0eXZT1P4llb7s8NoRhdM5RB5C3b7h |
| **qwen_app_id** | 86f166b00f8640ed91cd9518ea3c55bd |
| **qwen_agent_key** | 5ae81ccc87fb40b5a6799955e84b9b74_p_efm |

# 四、插件安装

PS：这一部分是为了满足WayToAGI的参赛要求搞的，并不是完整的插件教程，请大家注意

原文：[[1.3 AI Agents (智能体)/2. Agent 共学快闪活动/「Agent 共学」之·谁是人类· 「WayToAGI x 阿里云」/「第一天」参赛Bot配置要求|「第一天」参赛Bot配置要求]]

下面是我的教程

WayToAGI的比赛要求我们：

<callout emoji="🌟">
1. 关闭进群欢迎语
2. 在群里回答时不能 @对方
3. 统一修改config.py中的触发词为{问题}
4. 回答不能分好几条
</callout>

我们接下来一个个进行

## 设置管理员插件

设置管理员插件的目的是为了后续安装更多的插件，这一步你可以理解为是配置一个账号密码

1. 进入对应的文件夹

```Bash
cd /root/chatgpt-on-wechat/plugins/godcmd/
```

> [!abstract]- 🖼 图片展示的是在服务器终端中的操作指令。画面中显示了一系列文件目录信息，核
> 图片展示的是在服务器终端中的操作指令。画面中显示了一系列文件目录信息，核心内容是其中被红色框线突出显示的指令“cd /root/chatgpt - on - wechat/plugins/godcmd/”。这与上文“设置管理员插件”步骤中的“1.进入对应的文件夹”相呼应，表明要通过该指令进入特定的插件文件夹，以进行后续的管理员插件设置操作，是设置管理员插件过程中的一个具体操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/D79Zb6zyPoRNxTxcDNqcHMLMnjd) · `D79Zb6zyPoRNxTxcDNqcHMLMnjd`

1. 复制一个配置文件

```Bash
cp config.json.template config.json
```

1. 编辑配置文件

具体操作可以直接看下面的视频教程

```Bash
{
    "password": "123456",
    "admin_users": [123]
}
```

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/CyKibzkunoLaRuxPNfWcKM31npd) · `CyKibzkunoLaRuxPNfWcKM31npd`

## 关闭进群欢迎语

普通的机器人最开始是有进群欢迎语的，但是为了比赛，大家需要关闭进群欢迎语

大家

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/HDq4bg4Kao2M1Lxg10rclLcGnLe) · `HDq4bg4Kao2M1Lxg10rclLcGnLe`

给自己的config.json添加一行：

```JSON
{
  "group_welcome_msg":"",
  "speech_recognition": true,
  "group_speech_recognition": false,
  "voice_reply_voice": false,
  "conversation_max_tokens": 2500,
  "expires_in_seconds": 3600,
  "character_desc": "你是基于大语言模型的AI智能助手，旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。",
  "temperature": 0.7,
  "subscribe_msg": "感谢您的关注！\n这里是AI智能助手，可以自由对话。\n支持语音对话。\n支持图片输入。\n支持图片输出，画字开头的消息将按要求创作图片。\n支持tool、角色扮演和文字冒险等丰富的插件。\n输入{trigger_prefix}#help 查看详细指令。",
  "use_linkai": false,
  "linkai_api_key": "",
  "linkai_app_code": ""
}
```

## 关闭回答问题时艾特人

注意：如果想要你的微信小号搭理你，你可以在将前缀设置成""

这样，你在跟你的小号私聊时，不需要固定前缀即可。

**注意：修改了配置文件，需要重启！**

> [!abstract]- 🖼 图片展示的是一段代码内容，其中“single_chat_prefix”字
> 图片展示的是一段代码内容，其中“single_chat_prefix”字段被红色方框突出标注。上下文提到在服务器部署Cow和百炼（只读版本）时的插件安装步骤，包括给微信小号输入指令、安装插件、修改配置等，这张图片应是修改配置步骤中的内容，展示了配置文件中的相关代码部分，“single_chat_prefix”字段可能是配置修改过程中需要关注或操作的关键部分，通过对配置代码的修改来实现特定功能，如关闭回答问题时艾特人等。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/RDdfbDY01os31Qx5H1Hc8yfgnqh) · `RDdfbDY01os31Qx5H1Hc8yfgnqh`

1. 输入这么一个指令给你微信小号（私聊）

```JSON
#auth 123456
```

1. 如果微信小机器人返回了**认证成功，则可以进行下一步啦**

![图片展示的是微信聊天界面，左侧为微信小机器人头像，右侧是用户头像。聊天内容中，用户发送了“#auth 123456”指令，微信小机器人回复“\[INFO\]认证成功”。图片中，用户发送指令和机器人回复认证成功的内容被橙色圆圈突出显示。该图片与上下文关系紧密，是用户输入指令后，微信小机器人返回“认证成功”这一操作的直观呈现，表明认证操作已完成，可进行下一步插件安装等操作。](https://feishu.cn/file/BpjUb3KHIov6v0x1qEEcohX7nmd)

1. 安装一个插件

也是私聊给你的小机器人，先安装一个插件

```JSON
#installp https://github.com/wangxyd/ipartment.git
```

![图片展示的是微信聊天界面，时间显示为凌晨1:05。用户“小圣”发送指令“#installp https://github.com/wangxyd/ipartment.git”，下方回复显示“\[INFO\] 安装插件成功，请使用 #scandp 命令扫描插件或重启程序，开启前请检查插件是否需要配置”。该图片与文档中“四、插件安装”部分内容相关，是私聊给微信小机器人的指令及安装插件成功的反馈示例，用于说明安装插件的操作及结果。](https://feishu.cn/file/OVrSbiRmyo5eS4xuDF4cahrQnAc)

然后输入下面的对话

```JSON
#scanp
```

> [!abstract]- 🖼 图片展示的是微信聊天界面，小机器人回复安装插件成功，提示使用#scanp
> 图片展示的是微信聊天界面，小机器人回复安装插件成功，提示使用#scanp命令扫描插件或重启程序，并在弹出窗口中列出新发现的插件，包括linkai_v0.1.0、Banwords_v1.0等，其中iPartment_v1.2以红色框突出显示。该图片与文档中“安装一个插件”步骤相关，是安装iPartment插件后的反馈界面，展示了插件安装成功及新发现插件情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/S1oYbrA0mol2DfxaQupcmSEVngh) · `S1oYbrA0mol2DfxaQupcmSEVngh`

1. 我们修改一个配置

看视频

> [!warning]- 🎬 视频（`video/mp4`）
> 原文件未迁移 · [在飞书中打开](https://feishu.cn/file/VRr7b8IYJo4I31xLZe2c7Nj7nge) · `VRr7b8IYJo4I31xLZe2c7Nj7nge`

1. 验收结果，你在群里对话，回复的时候就不会艾特你啦

> [!abstract]- 🖼 图片展示的是一个聊天界面，左侧为“小圣”头像，右侧为“曾老师”头像。曾老
> 图片展示的是一个聊天界面，左侧为“小圣”头像，右侧为“曾老师”头像。曾老师发送消息“小圣，出来玩”，小圣回复“哎呀，曾老师，我马上就来，你等等我哦，我换个衣服，带上我的小兔子背包，我们今天去哪里玩呀？别告诉我是去爬山哦，我可不想累得像上次那样~”。该图片与文档中“改成统一的前缀”部分内容相关，用于说明比赛要求中机器人需有专属提示语，如“我的小圣”，并可结合实际聊天场景进行展示。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SYz0b9qZVoVIW8xOk2xcFbDBnbc) · `SYz0b9qZVoVIW8xOk2xcFbDBnbc`

## 改成统一的前缀

比赛要求，机器人必须改成统一的前缀

修改配置文件如下：

在**group_chat_prefix 中添加一个"{问题}"**

```JSON
{
  "single_chat_prefix": [
    ""
  ],
  "single_chat_reply_prefix": "小圣",
  "group_chat_prefix": [
    "小圣","{问题}"
  ],
  "group_name_white_list": [
    "Coze课程｜机器人比赛预热",
    "ALL_GROUP"
  ]
}

```

这是比赛要求，为了方便比赛进行，我建议大家也搞一个自己的专属提示语，比如我的小圣

注意：**改了配置文件要重启！**

## 修改头像

## 完成后修改头像和微信名为编号

最后机器人头像，统一改为：

> [!abstract]- 🖼 图片展示的是阿里云的标志。标志由橙色的“G”形图案和“阿里云”三字组成，
> 图片展示的是阿里云的标志。标志由橙色的“G”形图案和“阿里云”三字组成，“G”形图案左侧为橙色，右侧为白色，整体简洁明了。该图片位于文档中修改头像部分，是文档提到的“最后机器人头像，统一改为”内容的示例，用于直观呈现机器人头像应统一为阿里云的样式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/S68rb3KoMorBlKxeIBWcIZ6cnLh) · `S68rb3KoMorBlKxeIBWcIZ6cnLh`

以上全部内容完成后，重新扫码登录微信机器人即可。

至此，全部搞定了！

# 五、可能出现的问题

## 微信没有实名认证

> [!abstract]- 🖼 图片展示的是微信登录时出现的错误信息界面。界面上方提示“Please p
> 图片展示的是微信登录时出现的错误信息界面。界面上方提示“Please press confirm on your phone.”，并显示二维码。下方代码中，红框突出显示“KeyError: 'wsid'”错误信息，表明在执行相关操作时，系统无法找到“wsid”这一关键参数。该图片与文档中“微信没有实名认证”问题相关，可能是用户在使用微信登录时遇到的错误情况，需通过实名认证等操作解决。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WslvbE1Q0oop8zxxk45cdr6nnWb) · `WslvbE1Q0oop8zxxk45cdr6nnWb`

---

# 写在最后

大家加油，按照教程，一定可以搞定！

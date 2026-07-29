---
title: "一条简单逻辑, 帮你速选合适的“开源许可证”(license)"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/Ag8dwzDx8i7MlUkHbAlclaxBn1e
node_token: Ag8dwzDx8i7MlUkHbAlclaxBn1e
obj_token: GcR0dYCQZoWuYexWsNWcyljHnHf
obj_type: docx
space_id: 7226178700923011075
space_name: "WaytoAGI 通往AGI之路"
depth: 3
breadcrumb:
  - "1.3  AI Agents (智能体)"
  - "2. Agent 共学快闪活动"
  - "(筹划中)「Agent共学」之\"两天学会用AI建站\""
  - "一条简单逻辑, 帮你速选合适的“开源许可证”(license)"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 604
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 1.3 AI Agents (智能体)
---

# 一条简单逻辑, 帮你速选合适的“开源许可证”(license)

> [!info] 位置
> 1.3  AI Agents (智能体) › 2. Agent 共学快闪活动 › (筹划中)「Agent共学」之"两天学会用AI建站"

<callout emoji="🐮">
作者: Stuart [原文链接](https://mp.weixin.qq.com/s?__biz=MzI2Mzg2NzQzNg==&mid=2247484789&idx=1&sn=1c66311d4c45722f06342d185caf28f3&chksm=eab41836ddc39120484f004e54df211e0e94f46716710da34308548dbb51bcc6e714bb8432bb&token=2040940635&lang=zh_CN#rd)
之前wayToAGI社区的内容总是被抄袭复制, 很多作者很受伤: 开源就应该被随便抄袭么? 也有作者不是很在意. 其实这在开源社区有不同的开源许可证申明. 
多学一点, 提高自我开源保护意识!
</callout>

# 前言

Github, Gitee, 对于程序员来说可能很熟悉, 但是对于其他群体来说, 太过遥远和陌生. 

就比如我的设计师师傅有个经典语录: “就是那只猫图标的网站”. 大多数人听到这句话一定是丈二和尚摸不着头脑, 其实说的就是这只猫了: DDDD. 😂

> [!abstract]- 🖼 图片展示的是GitHub的标志，为一个黑色的猫头鹰图案，猫头鹰的轮廓简洁
> 图片展示的是GitHub的标志，为一个黑色的猫头鹰图案，猫头鹰的轮廓简洁，眼睛处有白色点缀。该图片位于文档开头部分，与上下文紧密相关，上下文提到GitHub、Gitee等对于程序员来说很熟悉，但对于其他群体来说陌生，还引用了设计师师傅的经典语录“就是那只猫图标的网站”，图片直观呈现了这个“猫图标”，帮助读者更好地理解上下文提到的GitHub网站。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/KzkbbakBKoMHN2x4bUMcjHDRnPe) · `KzkbbakBKoMHN2x4bUMcjHDRnPe`

当你拥有了自己设计的网站, 或者参与共创了像comfyui这样的开源项目, 想**在开源代码的同时又能申明自己的权益,** 那就得选择开源许可证. 而这个“开源许可证”(open source license)是数个很复杂的文档, 许可证类型又很多, 常用的就有[GPL](http://www.gnu.org/licenses/gpl.html)、[BSD](https://en.wikipedia.org/wiki/BSD_licenses)、[MIT](https://en.wikipedia.org/wiki/MIT_License)、[Mozilla](http://www.mozilla.org/MPL/)、[Apache](http://www.apache.org/licenses/LICENSE-2.0)和[LGPL](http://www.gnu.org/copyleft/lesser.html). 对于有选择困难症的人来说, 那是相当麻烦的事.

或者你**想开源自己的知识库 (文档)**, 本文对你一样适用.

# 许可证选择逻辑

**申明:** 如果觉得这个逻辑还是太复杂, 请直接跳到文末, 有个快速帮你做选择工具.

这里有个来自RuanYiFeng大神翻译的选择逻辑, 在常用的几个许可证中选择还是比较方便的.

> [!abstract]- 🖼 图片是一张开源许可证选择流程图，由RuanYiFeng大神翻译。流程从“
> 图片是一张开源许可证选择流程图，由RuanYiFeng大神翻译。流程从“他人修改源码后，是否可以闭源？”开始，若否，再问“新增代码是否采用同样许可证？”，若否则选LGPL许可证，若采用则问“是否需要对源码的修改之处，提供说明文档？”，若否选Mozilla许可证，若需则选GPL许可证。若他人修改源码后可闭源，再问“另一个修改过的文件，是否都必须放置版权说明？”，若否选BSD许可证，若需则问“新建软件的广告语，是否可以用你的名字促销？”，若否选MIT许可证，若否选Apache许可证。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MWbEbdswuoQxhTxblFMc5U04nVe) · `MWbEbdswuoQxhTxblFMc5U04nVe`

# 开源许可证选择器

啥, 还是太麻烦? 有办法!

最近有位大神, 用Cursor, 从0代码基础开始, 撸了一个在线选择器.

做几个单选题, 轻松找到比较合适开源许可证: https://open-source-license-chooser.toolsnav.top/zh/

> [!abstract]- 🖼 图片展示的是开源许可证选择器界面。左侧有多个问题，如“你希望别人用你的代
> 图片展示的是开源许可证选择器界面。左侧有多个问题，如“你希望别人用你的代码赚钱吗”“你希望别人能修改你的代码吗”等，每个问题下有不同选项。右侧为推荐的许可证，当前显示“GNU GPL - 3.0”和“Mozilla Public License 2.0”，并分别有趣味解释、优缺点、使用量及示例项目等介绍。右上角还有切换语言的标识。该图片与上文提到的在线选择器相呼应，直观呈现了选择器的使用方式和推荐结果。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/TWWOb66oYoIRwexhza6c0FHtndp) · `TWWOb66oYoIRwexhza6c0FHtndp`

<callout emoji="❤️">
❗️ 啥? 你也想学0代码基础做网站? 没问题! 
**十月份WayToAGI社区新一期共学, 教你0代码基础搭建一个瀑布流网站!**
</callout>

就是类似这种, 或者lib首页那种, 展示大量图片的那种网站. 如果你是个设计师, 它将非常适合你展示你的作品!

> [!abstract]- 🖼 图片展示了一个网站界面，以蓝色和白色为主色调，布局为瀑布流形式。上方有“
> 图片展示了一个网站界面，以蓝色和白色为主色调，布局为瀑布流形式。上方有“INTERFACES”标题，下方分为多个板块，如“36 works / WEB DEVELOPMENT”“22 works / INTERFACES”等，每个板块配有图片和文字说明。界面底部有“CALL BACK”“MORE”“OUR CLIENTS”等按钮，以及联系方式等信息。该图片与文档中介绍的瀑布流网站相契合，直观呈现了瀑布流网站的展示形式。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/AG7Nb1TurovW2NxrwidcjNVQnzf) · `AG7Nb1TurovW2NxrwidcjNVQnzf`

最后, 祝愿用爱发电开源的你, 在开源的路上, 也能保护好自己, 不受伤.

另外一个开源小网站，用我们能听懂的语言看各个许可：

https://licenseexplorer.iaiuse.com/

<grid>
<column width-ratio="0.500000">
> [!abstract]- 🖼 图片展示的是开源许可证探索器界面。上方有搜索框，右侧有筛选按钮。下方列出
> 图片展示的是开源许可证探索器界面。上方有搜索框，右侧有筛选按钮。下方列出多种开源许可证，如AFL v3.0、Apache License 2.0、Artistic License 2.0等，每种许可证有图标、名称、简要说明、热门项目、分发方式、部门归属等信息。其中，AFL v3.0、Apache License 2.0、Artistic License 2.0被红色框线突出显示。该图片与文档中介绍的“用我们能听懂的语言看各个许可”内容相关，直观呈现了不同开源许可证的信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XHSlbwDYZoIjqkxnZMLcmpZcnee) · `XHSlbwDYZoIjqkxnZMLcmpZcnee`
</column>
<column width-ratio="0.500000">
> [!abstract]- 🖼 图片展示的是Eclipse Public License 1.0（EPL
> 图片展示的是Eclipse Public License 1.0（EPL）的介绍页面。页面上方有“商业使用”“私有使用”“专利使用”“CopyLeft使用”等选项，当前选中“商业使用”。EPL是一种开源软件许可证，平衡了代码贡献者的利益和商业用户的使用自由。其核心特点包括商业友好、授权自由、CopyLeft特质、专利侵权等。主要权限有使用、修改、分发、商业使用等，限制与责任方面也有所说明。该图片与文档中介绍开源许可证的内容相关，直观呈现了EPL的具体信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JVSObAxV3o2Q0Kx4TdrcZkwdn1b) · `JVSObAxV3o2Q0Kx4TdrcZkwdn1b`
</column>
</grid>

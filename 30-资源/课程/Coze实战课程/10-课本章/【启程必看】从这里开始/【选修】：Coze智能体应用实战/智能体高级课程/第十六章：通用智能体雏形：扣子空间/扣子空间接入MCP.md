---
title: "扣子空间接入MCP"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/QhK7wgt9tiA1ILkUSdxcruwenfp
node_token: QhK7wgt9tiA1ILkUSdxcruwenfp
obj_token: TAF4dz9zSotkzWxlgxzcxk3jnwf
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体高级课程"
  - "第十六章：通用智能体雏形：扣子空间"
  - "扣子空间接入MCP "
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 215
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 扣子空间接入MCP

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体高级课程 › 第十六章：通用智能体雏形：扣子空间

上一篇文章：[[小白了解 MCP，看这一篇就够了]]

我们了解 MCP 是什么，这篇文章来通过扣子空间接入 MCP，让大家对 MCP 有更加具象化的了解

# 第一步：打开扣子空间

第一步：打开扣子空间的地址：https://space.coze.cn/?category=7520456187746189362

<grid>

> [!abstract]- 🖼 图片展示了扣子空间的界面，上方有“写作”“PPT”“播客”“网页”等选项
> 图片展示了扣子空间的界面，上方有“写作”“PPT”“播客”“网页”等选项，右上角有“hi”及一个粉色卡通形象。下方有“给我布置一个任务”输入框，左侧有“@”符号。图片中用红色箭头标注了两个关键步骤：第一步是点击“@”符号，第二步是点击“管理工具”（这些工具就是MCP）。该图片与文档中介绍扣子空间接入MCP的上下文相关，用于指导用户在扣子空间中找到并使用MCP Server。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/J6Xgb8NEgou6ojxRwQbcIP4dnwh) · `J6Xgb8NEgou6ojxRwQbcIP4dnwh`

> [!abstract]- 🖼 图片展示的是一个工具列表界面，上方有“全部”分类选项。列表中包含多个工具
> 图片展示的是一个工具列表界面，上方有“全部”分类选项。列表中包含多个工具，如高德地图、飞书文档、飞书电子表格等。其中，高德地图被红色框线突出显示，其下方有“选择自定义工具”文字说明。右侧有一个“+ 自定义工具”按钮，也用红色框线标出。该图片与文档中“第二步：寻找MCP Servers”内容相关，用于说明在MCP Server市场中找到满足需求的工具，如高德地图，可选择自定义工具接入到自己的Host中。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YQ1gbzZuBoDrlDxJurwcCFz5nxf) · `YQ1gbzZuBoDrlDxJurwcCFz5nxf`

</grid>

> [!abstract]- 🖼 图片展示的是一个代码编辑界面，代码内容为JSON格式，显示“{“mcpS
> 图片展示的是一个代码编辑界面，代码内容为JSON格式，显示“{“mcpServers”: {}}”。界面底部有红色文字提示“我们接下来的目标就是去找适合自己的mcpServers，添加到这里”。该图片与文档中“第二步：寻找MCP Servers”内容相关，用于说明在MCP发布后，可通过MCP Market找到满足需求的MCP Server，然后将其添加到JSON配置中，以实现将调用外部工具标准化的目标。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Vsyjbj73zo2TCNxAaExcFXannKC) · `Vsyjbj73zo2TCNxAaExcFXannKC`

# 第二步：寻找 MCP Servers

MCP的目的就是将调用外部工具标准化，他的理念就是一次构建，处处运行

因此在 MCP发布之后，诞生了很多的 MCP Market，我们可以在这里找到满足需求的 MCP Server，然后接入到自己的 Host中

推荐一个常用的 MCP Servers市场，如需更多，请自行使用 AI搜索  

https://mcp.so/

PS：如果你没有🪜，打不开，请直接复制我的 JSON配置

> [!abstract]- 🖼 图片展示的是MCP Server和客户端的探索界面。界面中有一个搜索框，
> 图片展示的是MCP Server和客户端的探索界面。界面中有一个搜索框，输入“高德地图”后，搜索结果中显示了7个相关MCP Server。其中，标注为“高德地图官方MCP Server”的Amap Maps被红色框突出显示，其发布者为@javafe，发布于4个月前，适用于Python，可实现API调用等功能。该图片与文档中“寻找MCP Servers”部分内容相关，用于说明在MCP市场中找到满足需求的MCP Server，如高德地图官方MCP Server。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/N0cmbAU6DoTt2UxenfuciQmnnVg) · `N0cmbAU6DoTt2UxenfuciQmnnVg`

> [!abstract]- 🖼 图片展示了MCP Server支持的工具及配置信息。左侧“Tools”区
> 图片展示了MCP Server支持的工具及配置信息。左侧“Tools”区域列出了如maps_regeocode、maps_geo等工具，其中maps_regeocode被红色框突出显示。右侧“Server Config”区域展示了MCP的配置代码，包含“mapsServers”等信息，右侧还有“Try in Playground”按钮。该图片与文档中“寻找MCP Servers”部分内容相关，直观呈现了MCP Server支持的工具及配置情况，帮助用户了解可接入的MCP Server及其配置。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/SPw5bG8vxolcAIxjCe6cJFZOn7d) · `SPw5bG8vxolcAIxjCe6cJFZOn7d`

```JSON
{
  "mcpServers": {
    "amap-maps": {
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "这里请放入你的高德api_key"
      }
    }
  }
}
```

# 第三步：获取高德地图的 API KEY

大多数MCP Server是提供一个调用工具的途径，人家并不会让你免费使用。

所以一般我们都需要获取对应的 API KEY

打开高德地图获取 API KEY的教程文档：

点击👉：https://lbs.amap.com/api/mcp-server/create-project-and-key

按照教程获取 API KEY

> [!abstract]- 🖼 图片展示的是高德地图API Key的获取界面。上方显示“我的应用”，下方
> 图片展示的是高德地图API Key的获取界面。上方显示“我的应用”，下方有一个名为“高德MCP Server”的应用，创建于2025/7/31。右侧有“Key”及“商用说明”蓝色文字。下方“Key名称”处显示“高德MCP服务器”，右侧Key内容被红框及箭头突出显示，提示“复制下来”。该图片与文档中获取API KEY的上下文相关，用于指导用户找到并复制API Key。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/FntQbJbd8o6ddWxq9qscTC5vnih) · `FntQbJbd8o6ddWxq9qscTC5vnih`

# 第四步：MCP Server 配置解析

```JSON
{
  "mcpServers": {
    "amap-maps": {
      "command": "npx",
      "args": [
        "-y",
        "@amap/amap-maps-mcp-server"
      ],
      "env": {
        "AMAP_MAPS_API_KEY": "这里请放入你的api_key"
      }
    }
  }
}
```

这是 AI针对这个 JSON结构给的回答，请注意：amap-maps 是个名称，可以随意修改（能使用中文）

> [!abstract]- 🖼 图片展示了MCP Server配置解析内容。其中，“mcpServers
> 图片展示了MCP Server配置解析内容。其中，“mcpServers”配置块说明内部定义的是一个或多个MCP服务器；“amap - maps”为高德地图服务名称；“command”是执行服务的命令，使用npx工具；“args”是传递给npx命令的参数；“-y”为确认参数；“@ amap / amap - maps - mcp - server”是运行的核心软件包名称；“env”配置环境变量，存放敏感信息；“AMAP_MAPS_API_KEY”是高德地图要求的API密钥。这些内容与上文扣子空间接入MCP中MCP Server配置相关，是对JSON结构的解析说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Hs6cbIZCUoYCz9xEqYkcOaGLnAg) · `Hs6cbIZCUoYCz9xEqYkcOaGLnAg`

# 第五步：扣子空间安装 MCP

> [!abstract]- 🖼 图片展示的是扣子空间添加自定义工具的界面。界面上方显示“添加自定义工具”
> 图片展示的是扣子空间添加自定义工具的界面。界面上方显示“添加自定义工具”，下方代码区域中，有“高德地图-自定义”名称及对应参数，其中“amap-maps-mcp-server”参数被红色箭头指向突出显示。下方“env”部分有“AMAP_MAPS_API_KEY”参数，其值被红框标注。界面底部有一个蓝色的“确认”按钮，也有红色箭头指向突出显示。该图片与文档中第五步“扣子空间安装MCP”内容相关，用于指导用户在扣子空间添加自定义工具时的操作步骤。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/WxtIbTRwCoYIaWxQ7EQcxZ9vnEe) · `WxtIbTRwCoYIaWxQ7EQcxZ9vnEe`

> [!abstract]- 🖼 图片展示了扣子空间中安装MCP的界面。左侧有“推荐”“自定义”“全部”选
> 图片展示了扣子空间中安装MCP的界面。左侧有“推荐”“自定义”“全部”选项，当前选中“自定义”。右侧显示“高德地图-自定义”工具，其右侧有一个绿色勾选按钮。图片中红色箭头和框线突出显示了“选择自定义就可以看到你安装的工具了”及“这里选择安装”字样，指导用户在扣子空间中安装MCP时的操作步骤，与上下文介绍的扣子空间安装MCP的第六步内容相呼应。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/YaU7bVRhhovHo2xYrtxcEnuenjr) · `YaU7bVRhhovHo2xYrtxcEnuenjr`

# 第六步：在扣子空间使用 MCP

在对话框艾特你的工具，然后启动一个任务：

> [!abstract]- 🖼 图片展示了扣子空间中“工具”选项下“高德地图 - 自定义”选项被红框突出
> 图片展示了扣子空间中“工具”选项下“高德地图 - 自定义”选项被红框突出显示。旁边有红色箭头指向该选项，箭头旁文字说明“@你的工具，然后发起一个任务”，并举例“比如：我要驾车从杭州到北京，给出我完整的路线”。此图与文档中“第六步：在扣子空间使用MCP”内容相关，指导用户在扣子空间使用MCP时，如何在对话框艾特工具并发起任务。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/E6w5bBQIhomxOoxe8I6cIIbgnwc) · `E6w5bBQIhomxOoxe8I6cIIbgnwc`

> [!abstract]- 🖼 图片展示了扣子空间在对话框中艾特工具后，启动任务查询杭州到北京地图的界面
> 图片展示了扣子空间在对话框中艾特工具后，启动任务查询杭州到北京地图的界面。左侧显示任务处理流程，有“正在获取扩展”“正在获取工具”“正在调用工具”等步骤。右侧是任务处理结果，包括路线总览、主线路段信息、关键节点信息及详细路线信息，如G25长深高速、S48宜长高速等路段。该图片与文档中“在扣子空间使用MCP”步骤相关，直观呈现了任务处理及结果展示情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/OhlSba1CNoCrOkxD21Gctefkn0c) · `OhlSba1CNoCrOkxD21Gctefkn0c`

# 第七步：扣子空间是如何调用 MCP 的

如果你有这个疑问，证明你没有仔细看：[[小白了解 MCP，看这一篇就够了]]

我这里说明下，一个标准的 MCP应该对自己的工具做**完整的文字说明**

**这个文字说明不仅仅是给人看的，更重要的是给大模型看的**

这让当人提出需求的时候，大模型才能根据每一个工具的文字说明，选择最合适的工具

# 写在最后

其实无论是扣子空间，Cursor、Claude等接入 MCP的方式都大同小异，本质我们要理解一个流程。

其余的就是工具使用的问题了

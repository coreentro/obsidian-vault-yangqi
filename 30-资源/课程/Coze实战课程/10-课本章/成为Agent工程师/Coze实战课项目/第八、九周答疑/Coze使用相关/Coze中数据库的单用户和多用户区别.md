---
title: "Coze中数据库的单用户和多用户区别"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/JTRHwrF8jiTNzFkl2nBcOLbdnme
node_token: JTRHwrF8jiTNzFkl2nBcOLbdnme
obj_token: OfJidb5vAoEIS6xbTzBcaVzSnKg
obj_type: docx
space_id: 7375763230725046276
space_name: "成为Agent工程师"
depth: 4
breadcrumb:
  - "成为Agent工程师"
  - "Coze实战课项目"
  - "第八、九周答疑"
  - "Coze使用相关"
  - "Coze中数据库的单用户和多用户区别"
obj_create_time: 1720624113
obj_edit_time: 1720629696
creator: ou_4f9742f370819a3c899baacbc140aed2
owner: ou_4f9742f370819a3c899baacbc140aed2
revision_id: 604
from_group_share: true
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 成为Agent工程师
---

# Coze中数据库的单用户和多用户区别

> [!info] 位置
> 成为Agent工程师 › Coze实战课项目 › 第八、九周答疑 › Coze使用相关

# 写在前面

大家好，我是《成为Agent工程师之Coze实战》的讲师，大圣

在之前的课程中，我们已经讲解了数据库的语法，具体可以参考[[加餐｜Coze数据库]]

但是我们还缺了一环，就是Coze中的多用户模式和单用户模式到底什么区别。

今天我就用两个案例 + 8个工作流 + 两个用户来手把手给大家演示下两种模式的区别

# 测试前准备

为了测试单用户模式和多用户模式，我准备了两个Bot，分别是

> [!abstract]- 🖼 图片展示了两个Bot的测试结果。左侧是“数据库多用户模式测试”，由大圣@
> 图片展示了两个Bot的测试结果。左侧是“数据库多用户模式测试”，由大圣@lmh_2024于23:06完成，显示“豆包·Function call模型”最近编辑时间。右侧是“数据库单用户模式测试”，也是大圣@lmh_2024于23:05完成，同样显示“豆包·Function call模型”最近编辑时间。两张图右侧均有蓝色对话框图标。图片与上下文关系紧密，直观呈现了文档中准备的两个Bot在多用户和单用户模式下的测试情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/PvQvb2wMWoOfHBxOENLcyMEcnie) · `PvQvb2wMWoOfHBxOENLcyMEcnie`

两个Bot中的数据库结构一样，只不过一个是单用户模式，一个是多用户模式

<grid>

> [!abstract]- 🖼 图片展示了Coze中数据库的设置界面。数据表名称为“mysql_mult
> 图片展示了Coze中数据库的设置界面。数据表名称为“mysql_multi_user_test”，数据表描述为空。Table查询模式选择“多用户模式”。存储字段名称包括uuid、id、user_name和age，其中user_name和age字段类型为String和Integer，是否必要均为选中状态。该图片与上下文关系紧密，是对文档中准备的两个Bot中单用户模式数据库结构的展示，直观呈现了其数据表名称、模式及部分字段信息。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/XfSRbSBtMosbhXxUqCocAaVanPh) · `XfSRbSBtMosbhXxUqCocAaVanPh`

> [!abstract]- 🖼 图片展示了Coze中数据库配置界面。数据表名称为“mysql_singl
> 图片展示了Coze中数据库配置界面。数据表名称为“mysql_single_user_test”，数据表描述为“用来存储用户的信息”。Table查询模式选择“单用户模式”，支持在Prompt中调用。存储字段有user_name（用户姓名，4/300，String类型，必填）和age（年龄，2/300，String类型，必填）。该图片与上下文关系紧密，是用于测试单用户模式时数据库配置的示例，直观呈现了单用户模式下数据库的字段设置情况。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Rfg0bhCDxoW77wx78CAcCLAtnzJ) · `Rfg0bhCDxoW77wx78CAcCLAtnzJ`

</grid>

每个Bot都有4个工作流，分别是

- 插入一条数据
- 根据名字查询数据
- 查询所有数据
- 删除所有数据

<grid>

> [!abstract]- 🖼 图片展示了Coze中数据库单用户模式测试的界面。界面左上角显示“数据库单
> 图片展示了Coze中数据库单用户模式测试的界面。界面左上角显示“数据库单用户模式测试”及“个人空间 已发布 23:21”信息。下方有“编排”和“分析”选项卡，当前选中“编排”。在“人设与回复逻辑”部分，有“优化”按钮。技能区域有“插件”和“工作流”选项，工作流部分有四个绿色图标的工作流，分别是“mysql_single_user_insert_test”（插入数据）、“mysql_single_user_select_test”（查询数据）、“mysql_single_user_select_all”（查询所有数据）和“mysql_single_user_delete_all”（删除数据）。该图与上下文介绍的测试前准备中单用户模式Bot的工作流内容相关。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/DUTAbTu07otIjHxitDkcTkwxnbb) · `DUTAbTu07otIjHxitDkcTkwxnbb`

> [!abstract]- 🖼 图片展示了Coze中“数据库多用户模式测试”Bot的界面。上方显示Bot
> 图片展示了Coze中“数据库多用户模式测试”Bot的界面。上方显示Bot名称及状态。右侧工作流区域，以红色框突出显示了四个工作流名称，分别是“mysql_multi_user_select_test”“mysql_multi_user_insert_test”“mysql_multi_user_select_all”“mysql_multi_user_delete_all”。这些工作流与文档中介绍的两个Bot的数据库结构及四个工作流内容相呼应，用于测试单用户和多用户模式下的数据库操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/LXLcbeBtQoy6dlxcNhUcd5P8np6) · `LXLcbeBtQoy6dlxcNhUcd5P8np6`

</grid>

我准备了两个账号来进行测试，分别是：

<grid>

> [!abstract]- 🖼 图片展示的是一个名为“扣子 API”的消息界面，头像为一个抱着孩子的卡通
> 图片展示的是一个名为“扣子 API”的消息界面，头像为一个抱着孩子的卡通形象，用户名为“大圣”，账号为“lmh_2024”。该图片位于文档中测试前准备部分，用于说明测试时准备的两个账号之一，另一个账号未在图片中展示，与上下文介绍的测试准备内容相关，用于后续测试单用户模式和多用户模式时进行操作。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Gumtb2IKeoJPk4xEzNjcLCXtnce) · `Gumtb2IKeoJPk4xEzNjcLCXtnce`

> [!abstract]- 🖼 图片展示的是一个名为“扣子 API”的用户界面，用户名为“zxd_bon
> 图片展示的是一个名为“扣子 API”的用户界面，用户名为“zxd_bonnie”，账号标识为“@zxd_bonnie”。该图片位于文档中测试前准备部分，用于说明测试单用户模式和多用户模式时准备的两个账号之一，另一个账号未在图片中展示，但文档中提到是“zxd_bonnie”。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/Uslkb4tOco71Zdx1sYbc2mlSnXe) · `Uslkb4tOco71Zdx1sYbc2mlSnXe`

</grid>

# 测试思路

对于数据库来讲，操作就是读和写，其中写包括：增加/删除/更新

数据库的权限体系也很简单：用读和写来控制权限

其中从Coze的官方文档中

单用户模式的意思是：

> [!abstract]- 🖼 图片展示了Coze中单用户和多用户模式下，开发者及用户对数据操作的权限区
> 图片展示了Coze中单用户和多用户模式下，开发者及用户对数据操作的权限区别。单用户模式下，开发者和用户可添加记录，仅能读/修改/删除自己创建的来自同渠道的数据；多用户模式下，开发者和用户可读/写/修改/删除表中来自不同渠道的任何数据，由业务逻辑控制读写权限。该图片与上下文紧密相关，是对单用户和多用户模式下读写权限体系的具体说明，帮助理解开发者、用户及渠道在不同模式下的数据操作权限。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/MhQubTRBaon8qnxETRBcw1Bsn8b) · `MhQubTRBaon8qnxETRBcw1Bsn8b`

多用户模式的意思是：

> [!abstract]- 🖼 图片展示了单用户模式和多用户模式下，开发者及用户对数据的权限操作。单用户
> 图片展示了单用户模式和多用户模式下，开发者及用户对数据的权限操作。单用户模式下，开发者和用户仅能读取、修改、删除自己创建的来自同渠道的数据。多用户模式下，开发者和用户可读、写、修改、删除表中来自同渠道的任何数据，但读写权限由业务逻辑控制。该图片与上下文紧密相关，是对上文对单用户模式和多用户模式中读写权限具体操作的总结说明。
> 
> 原图未迁移 · [飞书原图](https://feishu.cn/file/JYvAbx1M7ot67hxacmacVK1Gnnd) · `JYvAbx1M7ot67hxacmacVK1Gnnd`

这里面涉及到了3个概念

- 开发者（开发Bot的人）
- 用户（使用Bot的人）
- 渠道（这个我没有特别测试，我理解是Bot商店、豆包、飞书等属于不同渠道）

从读写权限的角度理解

- 单用户模式：用户A只能读取用户A写入的数据
- 多用户模式：用户A可以读取任何其他用户写入的数据

以上就是我们对于单用户模式和多用户模式的理解，今天我们就是来测试一下，这些是否如我们所想

另外对于开发者而言，我们有两种途径可以初始化数据，调试页面和工作流调试。

这里直接跟大家说结论：

- **工作流的调试中生成的数据不可以被Bot使用，仅限于工作流调试使用**
- 调试页面插入的数据可以被Bot使用，也就是可以用来**多用模式的数据库**进行数据初始化

# 视频测试

具体测试流程可以观看视频，这种测试理念很有意思，建议大家看下

<readonly-block href="https://axsppz4oyvj.feishu.cn/minutes/embed/obcnf2nlo2fmzt54c3b9sz4x?from=ccm" type="iframe"></readonly-block>

# 总结

- 我认为多用户模式下，开发者看不到数据库的所有数据就是BUG
- 如果想要建立所有用户可见的数据，要使用**多用户模式**的数据库
- **工作流中调试的数据是和其余的数据隔离的**，仅限于工作流中调试使用
- **Coze中的数据库绝对有很多bug，但是大家给Coze一些时间吧，会优化的～**

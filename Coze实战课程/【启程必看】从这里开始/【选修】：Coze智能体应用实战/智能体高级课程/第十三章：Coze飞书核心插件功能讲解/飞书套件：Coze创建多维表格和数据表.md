---
title: "飞书套件：Coze创建多维表格和数据表"
feishu_url: https://axsppz4oyvj.feishu.cn/wiki/AgZNwmgzZiQZ2GkjVCScbIpAncb
node_token: AgZNwmgzZiQZ2GkjVCScbIpAncb
obj_token: ZN3Jd6j0soKgY2xdY5jcpUjNnYf
obj_type: docx
space_id: 7491877341887725572
space_name: "Agent工程师之Coze实战课程"
depth: 4
breadcrumb:
  - "【启程必看】从这里开始"
  - "【选修】：Coze智能体应用实战"
  - "智能体高级课程"
  - "第十三章：Coze飞书核心插件功能讲解"
  - "飞书套件：Coze创建多维表格和数据表"
obj_create_time: 
obj_edit_time: 
creator: 
owner: 
revision_id: 4
from_group_share: false
migrated_from: 飞书云文档
migrated_at: 2026-07-29
tags:
  - 飞书迁移
  - 【启程必看】从这里开始
---

# 飞书套件：Coze创建多维表格和数据表

> [!info] 位置
> 【启程必看】从这里开始 › 【选修】：Coze智能体应用实战 › 智能体高级课程 › 第十三章：Coze飞书核心插件功能讲解

智能体地址：https://www.coze.cn/space/7362748064240877602/bot/7484113992509243403

<readonly-block href="https://waytoagi.feishu.cn/minutes/embed/obcne11pz19lh7z7gi3de334?from=ccm" type="iframe"></readonly-block>

# 写在前面

大家好，我是大圣，这节课给大家讲解下在Coze中如何创建多维表格

# 创建多维表格和数据表

# 确定你的数据表字段

<callout emoji="💡">
Integer·字段类型：
可选值包括
1：多行文本、
2：数字、
3：单选、
4：多选、
5：日期、
7：复选框、
11：人员、
13：电话号码、
15：超链接、
17：附件、
18：单向关联、
20：公式、
21：双向关联、
22：地理位置、
23：群组、
1001：创建时间、
1002：最后更新时间、
1003：创建人、
1004：修改人、
1005：自动编号
</callout>

```json
{
    "app_token": "https://bytedance.larkoffice.com/base/CUB4bbZUXaJFT0sU1Vecn1GunFc?table=tblTLjqChZ1z14dn\u0026view=vew3LMVlRA",
    "fields": [
        {
            "field_name": "这是一个多行文本",
            "type": 1
        },
        {
            "field_name": "这是一个数字",
            "type": 2
        },
        {
            "field_name": "这是一个单选",
            "type": 3
        },
        {
            "field_name": "这是一个多选",
            "type": 4
        },
        {
            "field_name": "这是一个超链接",
            "type": 15
        }
    ],
    "name": "测试数据表"
}
```

https://axsppz4oyvj.feishu.cn/base/TJJXbCFIYaHQNtscmQbcFD71n6g?table=tbln09UIaeqZhKdd&view=vewLGQe0ua

---
title: "V2O5光催化性能综述"
source_conversation_uuid: "68752ef2-e42a-40b9-b044-cdb214f468c4"
---

# V2O5光催化性能综述

> [!abstract]- 导出摘要
>
> **Conversation Overview**
>
> The person requested Claude's assistance creating a comprehensive academic literature review (综述文献) on V₂O₅ (vanadium pentoxide) photocatalysis, delivered as a formatted Word document (.docx file). The conversation involved two exchanges: first a detailed inline text review, then a request to produce that content as a formal document file.
>
> Claude used the docx skill to generate a professionally formatted Word document in Chinese, covering the full scope of V₂O₅ photocatalysis research. The document included: basic material properties and electronic structure (crystal structure, band gap parameters ~2.2–2.3 eV, CB/VB positions); synthesis methods comparison across seven routes (hydrothermal, sol-gel, CVD, PLD, spray pyrolysis, electrochemical deposition, thermal decomposition); photocatalytic reaction mechanisms and active species identification (•OH, •O₂⁻); modification strategies (doping, rGO composites, Z-scheme heterojunctions, MXene-derived systems, defect engineering); applications in organic pollutant degradation, photocatalytic hydrogen evolution, and CO₂ photoreduction; and challenges with future research directions. The document incorporated four formatted data tables, styled headings, colored section blocks, header/footer elements, and 17 representative references from 2019–2026.
>
> During generation, Claude encountered and resolved two technical issues: a JavaScript syntax error (extra closing brace in a table structure) and an XML validation error caused by a function signature mismatch where passing `true` as the second argument to the `body()` function set `before=true` in spacing attributes instead of triggering indentation. Claude fixed this by updating the function to detect boolean inputs and reroute them to the `indent` parameter. The final document passed validation and was delivered as `/mnt/user-data/outputs/V2O5_光催化综述.docx`.

<!-- message_uuid: 019e8ca7-320a-7de8-99df-dab5260ef9d2 -->
<!-- parent_uuid: 00000000-0000-4000-8000-000000000000 -->

## 你

V2O5 光催化方向的综述

<!-- message_uuid: 019e8ca7-320b-7315-8dba-3b456dea20e7 -->
<!-- parent_uuid: 019e8ca7-320a-7de8-99df-dab5260ef9d2 -->

## Claude

 The user is asking for a review/overview of V2O5 in photocatalysis. This is a literature review request about vanadium pentoxide (V2O5) as a photocatalyst. Let me provide a comprehensive review in Chinese since the user asked in Chinese.

Let me search for recent literature on this topic to provide up-to-date information.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I now have a comprehensive set of search results on V2O5 photocatalysis. Let me compose a thorough review in Chinese covering:

1. Introduction - V2O5 as a photocatalyst, basic properties
2. Crystal structure and electronic band structure
3. Synthesis methods
4. Photocatalytic mechanism
5. Performance enhancement strategies (doping, heterojunctions, composites)
6. Application areas (pollutant degradation, H2 evolution, CO2 reduction)
7. Challenges and outlook

Let me now write this in Chinese.以下是一篇关于 V₂O₅ 光催化方向的系统性综述，内容涵盖材料基本性质、合成方法、催化机制、改性策略及应用领域。

---

# V₂O₅ 光催化研究综述

## 一、引言

五氧化二钒（V₂O₅）是一种重要的 n 型半导体过渡金属氧化物，在光催化领域受到广泛关注。其带隙约为 2.3 eV，对可见光具有较高的敏感性，使其在太阳能驱动的光催化反应中具有显著优势，弥补了 TiO₂ 仅对紫外光响应的不足。V₂O₅ 因其独特的化学、光学和光致变色性质，在光催化制氢领域受到了极大关注。近年来，V₂O₅ 在环境污染治理（有机污染物降解）、光催化产氢以及 CO₂ 还原等方向上均取得了显著进展。

---

## 二、晶体结构与电子性质

V₂O₅ 以正交晶系（orthorhombic）结构最为稳定，空间群为 *Pmmn*，由 VO₅ 方锥体通过共棱和共顶点方式层叠堆垛而成，形成各向异性的层状结构。其层间靠范德华力结合，赋予其良好的离子插层能力。

**关键能带参数：**

| 参数 | 数值 |
|------|------|
| 带隙（Eg） | ~2.2–2.3 eV |
| 导带位置（CB） | ~+0.4 eV（vs. NHE） |
| 价带位置（VB） | ~+2.7 eV |
| 光响应波长阈值 | < 443 nm |

V₂O₅ 是一种窄带隙过渡金属氧化物，可捕获紫外光谱中相当大的一部分以生成活性氧化还原中心，光活化发生在波长小于 443 nm 的范围内。值得注意的是，V₂O₅ 的带隙可通过调控其结构或施加外部刺激来有效地增大或减小，这为带隙工程提供了灵活性。

然而，V₂O₅ 的导带位置（~+0.4 eV）在热力学上对 CO₂ 还原可能不够适宜，这是其应用于某些特定反应时的固有限制。

---

## 三、合成方法

V₂O₅ 纳米结构的形貌和性能在很大程度上取决于合成方法。主要方法包括：

**（1）水热/溶剂热法**
最常用的液相合成路线，通过调控 pH、温度、时间和模板剂，可得到纳米带、纳米棒、纳米片等多种形貌。利用不同封端剂（如 PEG、EDTA 等聚合物）可成功获得多种形貌的 V₂O₅ 纳米结构，并通过降低带隙和改善电子-空穴分离来提升光催化性能。

**（2）溶胶-凝胶法**
适合制备薄膜和介孔结构，前驱体多为偏钒酸铵（NH₄VO₃）或正钒酸铵，经凝胶化再煅烧成型。

**（3）气相沉积法**
包括化学气相沉积（CVD）、电子束蒸发、脉冲激光沉积（PLD）和喷雾热解等。这些方法常用于制备高质量的 V₂O₅ 薄膜，适合光电催化器件的制备。

**（4）形貌调控效果**
在不同形貌中，具有晶面特征的纳米棒状 V₂O₅ 纳米颗粒的 CO₂ 光催化转化效率（生成 CH₄）可达约 11.85 μmol·g⁻¹，分别比球形纳米颗粒高约 6.19 倍。

---

## 四、光催化反应机制

V₂O₅ 的基本光催化过程遵循半导体光催化的经典路径：

```
V₂O₅ + hν → e⁻(CB) + h⁺(VB)
h⁺ + H₂O → •OH
e⁻ + O₂ → •O₂⁻
活性物种（•OH, •O₂⁻, h⁺）→ 氧化降解有机物
```

在 V₂O₅ 基光催化体系中，超氧自由基（•O₂⁻）和羟基自由基（•OH）是主要活性物种。光生载流子的快速复合是制约单纯 V₂O₅ 光催化效率的核心瓶颈，因此构建异质结和引入缺陷工程是提升性能的两大主要策略。

二维 V₂O₅ 的研究揭示了形貌对机制的影响：二维 V₂O₅ 的光吸收系数提升约 7 倍，显著增加了参与催化反应的光生电子数量，同时通过表面氧空位缺陷进一步增强了表面活性。

---

## 五、性能提升策略

### 5.1 杂原子掺杂

掺杂是调控 V₂O₅ 电子结构和扩展可见光吸收最直接的手段。

- **金属掺杂**：Be、Cu、Nb、稀土元素（La、Ce 等）掺杂均被报道可有效减小带隙、提升载流子分离效率。Be 掺杂 V₂O₅ 纳米颗粒在结构、光学和光降解性能方面均有协同增强，对亚甲基蓝的去除效率显著提升。
- **稀土掺杂**：稀土掺杂 V₂O₅ 光催化剂被报道可有效去除工业废水中的污染物。

### 5.2 碳基复合材料

石墨烯及其衍生物（rGO）与 V₂O₅ 的复合是当前研究热点：

将纳米颗粒嵌入 rGO 片层中可淬灭光致发光发射，在白光辐照下增强光催化性能；这归因于钒氧化物纳米颗粒向 rGO 表面的有效界面电子转移，从而抑制光生载流子的复合。

G-V₂O₅ 纳米复合材料对亚甲基蓝的降解在直射阳光下的效率优于 UV 和可见光光源，一维 V₂O₅ 纳米棒被修饰在二维石墨烯片层上，形成协同效应。

### 5.3 异质结构建

这是目前文献中研究最广泛、效果最显著的改性策略，主要包括三种类型：

**Z 型异质结（Z-scheme）**
V₂O₅/g-C₃N₄ 直接固态 Z 型异质结体系不仅能改善光生电子-空穴对的分离，还同时保留了较强的氧化和还原能力，对 RhB 的最优光催化效率分别是纯 g-C₃N₄ 和纯 V₂O₅ 的 7.3 和 13.0 倍。

分子接枝氮化碳（CN）纳米片与 V₂O₅ 原位生长构建的 Z 型异质结光催化剂，在模拟太阳光照射下的产氢和罗丹明 B 降解活性均远高于纯 CN 和 V₂O₅。

**多组分异质结**
V₂O₅/CdS/CuS 多级异质结中，CdS 与 CuS 紧密结合的混合纳米颗粒可促进两者间的电子转移过程，V₂O₅ 较窄的带隙（2.2 eV）则增加了整个催化剂体系的光吸收。

**MXene 衍生异质结**
由 Ti₃C₂ MXene 原位制备的 V₂O₅/TiO₂-碳异质结，在可见光下对亚甲基蓝的降解活性分别是纯 V₂O₅ 和 TiO₂-碳的 4.58 和 2.79 倍；石墨化碳层作为电子储库增强可见光吸收，而 V₂O₅/TiO₂ 异质结则促进光生载流子分离。

### 5.4 缺陷工程与形貌调控

氧空位的引入是提升 V₂O₅ 光催化活性的重要策略。通过在 2D V₂O₅ 催化剂表面生成氧空位缺陷，可显著增强其表面活性。

---

## 六、主要应用领域

### 6.1 有机污染物光降解

这是 V₂O₅ 光催化研究最成熟的应用方向，覆盖染料、药物、酚类化合物等：

- **染料降解**：V₂O₅ 基光催化剂在去除偶氮染料、罗丹明 6G（Rh-6G）等有机污染物方面得到了广泛应用。
- **药物污染物**：制药产品（PPs）可能具有持久性，对传统废水处理设施构成挑战，V₂O₅ 基光催化降解是一种有前景的解决方案。
- **酚类化合物**：V₂O₅ 与 Ni₃V₂O₈ 界面接近，光生电荷分离良好，对 2,4-二氯苯酚（2,4-DCP）的光降解率约达 90%。
- **抗生素**：含 Pt 助催化剂的 rGO/V₂O₅ 复合物对四环素类药物（OTC）

<!-- message_uuid: 019e8ca8-71a9-72db-9704-1dd1436585fd -->
<!-- parent_uuid: 019e8ca7-320b-7315-8dba-3b456dea20e7 -->

## 你

V2O5 光催化方向的综述文献

<!-- message_uuid: 019e8ca8-71a9-7739-a56e-6d4c1024b5a8 -->
<!-- parent_uuid: 019e8ca8-71a9-72db-9704-1dd1436585fd -->

## Claude

 The user is asking for a literature review document (综述文献) on V2O5 photocatalysis - they want an actual document file, not just a chat response. Let me create a comprehensive Word document or PDF review paper. I should check the relevant skills first.

Let me check the docx skill since they want a formal review document (综述文献 implies a formal academic review paper).
```
This block is not supported on your current device yet.
```

Now I have the docx skill instructions. Let me create a comprehensive V2O5 photocatalysis review document as a .docx file. I'll use the docx-js library to create a Word document with all the necessary content.

Let me plan the structure:

1. 标题页 (Title)
2. 摘要 (Abstract)
3. 引言 (Introduction)
4. V2O5的基本性质 (Basic properties)
5. 合成方法 (Synthesis methods)
6. 光催化机制 (Photocatalytic mechanism)
7. 改性策略 (Enhancement strategies)
   - 7.1 掺杂
   - 7.2 碳基复合
   - 7.3 异质结
   - 7.4 缺陷工程
8. 应用领域 (Applications)
   - 8.1 有机污染物降解
   - 8.2 光催化制氢
   - 8.3 CO2还原
9. 挑战与展望 (Challenges and outlook)
10. 参考文献 (References)

I'll write this in Chinese. Let me now install the docx package and create the document.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The issue is at line 399 - I see `})}]})],` - this seems to be closing a table row/cell structure. Let me look at more context around this area.
```
This block is not supported on your current device yet.
```

The issue is clear - the `})}]})],` on line 399 is closing the `TableCell`, `TableRow`, `rows array`, but then the whole block needs to be closed: `}),` for the `Table`. But I see `}),` on line 400. 

Wait, `})}]})],` - this closes:
- `}` - closes the TableCell object
- `)` - closes `new TableCell(`
- `}` - closes the object passed to `TableRow`
- `]` - closes the `children` array
- `)` - closes `new TableRow(`
- `}` - closes the `rows:` array item? No...

Actually, `rows: [new TableRow({ children: [...] })]` should be:
- `]` closes the `rows` array
- `}` closes the `new Table({...})` object
- `)` closes `new Table(`
- `,` separator

So:
- `}` - closes TableCell config object
- `)` - closes `new TableCell(`
- `}` - closes TableRow config object
- `]` - closes `children` array of TableRow
- `)` - closes `new TableRow(`
- `}` - closes... hmm

Wait, let me re-read:
```
rows: [new TableRow({ children: [new TableCell({
  ...
  children: [...]
})}]})],
```

This is:
- `}` closes `new TableCell({...`  
- `)` closes `new TableCell(...)`  
- `}` closes `new TableRow({children: [...]` - wait, this needs to be:
  - `]` closes the `children` array
  - `}` closes `new TableRow({...`
  - `)` closes `new TableRow(...)`

So it should be `})]})],`

Currently it's: `})}]})],`
What it should be: `})]})],`

Wait, let me parse more carefully:
```javascript
rows: [new TableRow({ children: [new TableCell({
  ...
})]})],
```

- `}` closes `new TableCell({...}` - the config object
- `)` closes the `new TableCell(...)` call
- `]` closes `children: [...]` 
- `}` closes `new TableRow({...}` 
- `)` closes `new TableRow(...)`
- `]` closes `rows: [...]`
- `,` is a separator

So `})]})],` is correct. But the current code has `})}]})],` which has an extra `)`.

Actually wait: let me re-read. The line has:
```
        })}]})],
```

The `}` closes TableCell config
`)` closes `new TableCell(`
`}` - this is wrong - there's an extra `}`!

Wait:
- TableCell: `new TableCell({...})` - `}` closes the config, `)` closes the call
- TableRow: `new TableRow({ children: [...] })` - needs `]` to close children, `}` to close config, `)` to close the call
- rows: `[...]` - needs `]`

So from the close of TableCell content:
```
        })]})],
        ^^^^^^^^^^
        }    - closes TableCell config
        )    - closes new TableCell(
        ]    - closes TableRow.children
        }    - closes TableRow config
        )    - closes new TableRow(
        ]    - closes rows array
        ,    - separator
```

But we have `})}]})],`:
```
}   - closes TableCell config
)   - closes new TableCell(
}   - EXTRA!
]   - closes TableRow.children
}   - closes TableRow config
)   - closes new TableRow(
]   - closes rows array
,   - separator
```

The extra `}` causes the syntax error. But wait, let me look at what's there again: `})}]})],`. Let me count carefully:

Looking at line 399: `        })}]})],`

Following from line 383: `rows: [new TableRow({ children: [new TableCell({`

This means we need to close:
1. `{` from `new TableCell({` → `}`
2. `)` from `new TableCell(` → `)`
3. `[` from `children: [` → `]`
4. `{` from `new TableRow({` → `}`
5. `)` from `new TableRow(` → `)`
6. `[` from `rows: [` → `]`

So the close sequence should be: `})]})],`

Current: `})}]})],` - has an extra `}` between `)` and `]`

Let me fix this.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

There's a validation error related to spacing. The `spacing` function returns `{ before, after }` but these need to be numeric values in DXA units, not `true`. Let me check. The error says `'true' is not a valid value` for `before` attribute.

Wait, the issue is that `sp(0, 0)` returns `{ before: 0, after: 0 }` which should be fine. But somewhere I used `sp` with no arguments, which would return `{ before: undefined, after: undefined }` - but that shouldn't produce 'true' either.

Let me look... Actually the issue might be in how spacing is used in paragraphs. The `paragraph.spacing` field in docx-js is different. When I use `sp()` for heading paragraph styles, it's used like:

```javascript
paragraph: { spacing: sp(240, 120), outlineLevel: 0, ... }
```

That's the paragraph style configuration. The `spacing` object should have `before`, `after` properties as numbers. But the error says `'true'` is being passed as a value.

Let me look at my paragraph border configuration for Heading1:
```javascript
paragraph: { spacing: sp(320, 160), outlineLevel: 0,
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.blue, space: 4 } } }
```

Hmm, could there be something where `sp` is being called with boolean? Let me look at my `sp` function:

```javascript
const sp = (before = 0, after = 0) => ({ before, after });
```

And `line` function:
```javascript
const line = (n = 240) => ({ line: n });
```

I have `body()` function:
```javascript
function body(text, before = 80, after = 100, indent = false) {
  return new Paragraph({
    spacing: { before, after, line: 288 },
    ...
  });
}
```

Maybe the issue is with how I pass `before` to `sp`. Let me check `divider()`:
```javascript
function divider() {
  return new Paragraph({
    spacing: sp(60, 60),
    ...
  });
}
```

That looks fine.

Wait, looking at the heading styles:
```javascript
paragraph: { spacing: sp(320, 160), outlineLevel: 0, ... }
```

This passes `{ before: 320, after: 160 }` to `spacing`. That should be fine.

Maybe the issue is with the cover table paragraph where I do:
```javascript
new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(0, 120), children: [...] })
```

This calls `sp(0, 120)` = `{ before: 0, after: 120 }`. That should be valid.

Actually, wait - in the `hdr()` function:
```javascript
function hdr(text, level, before = 240, after = 120) {
  return new Paragraph({
    heading: level,
    spacing: sp(before, after),
    ...
  });
}
```

This should also be fine.

Let me look at my `infoBox` function:
```javascript
new Paragraph({ spacing: sp(0, 60), children: [...] }),
new Paragraph({ spacing: sp(0, 0), alignment: ..., children: [...] })
```

These look fine.

Actually, I bet the issue might be the `spacing` field used in `paragraphStyles`. In docx-js styles, the `paragraph.spacing` config might need different field names. Let me check if there's a `lineRule` field needed.

Actually, looking at docx-js source, in paragraph styles, the spacing object accepts:
- `before`: number (twips)
- `after`: number (twips)
- `line`: number (twips)
- `lineRule`: LineRuleType (if line is specified)

So `before: 0` with a value of 0 should be valid. But the error says 'true' is being passed...

Wait - could it be that `sp(0, 0)` returns `{ before: 0, after: 0 }` but when destructuring inside docx-js, if the value is falsy (0), it might evaluate differently? No, that doesn't make sense.

Actually, looking at the error more carefully: `'true' is not a valid value`. Where would `true` come from?

Oh wait! I have `ShadingType.CLEAR` but that might resolve to `true`. Let me check docx-js's ShadingType enum...

Actually no. The error is about `spacing/before` attribute. 

Hmm, let me think about this differently. In docx-js paragraph styles, spacing might need to be specified differently. Let me check the style definition I have:

```javascript
paragraphStyles: [
  {
    id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
    run: { size: 32, bold: true, font: "Arial", color: C.navy },
    paragraph: { spacing: sp(320, 160), outlineLevel: 0,
      border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.blue, space: 4 } } }
  },
```

The `sp(320, 160)` = `{ before: 320, after: 160 }`. This is passed to `paragraph.spacing` which in docx-js styles is `ISpacingProperties` type.

Actually, maybe the issue is `sp(0, 0)` - some validator might complain about `before: 0`. Let me try a different approach - just don't pass 0 values.

Or perhaps the real fix is simpler - the XML validator checks that `w:before` is a number, but docx-js might be outputting `true` for one of the values somewhere.

Let me try to look at the document.xml to understand:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The issue is clear now - `w:before="true"`. This is happening in the `body()` function which is called with `indent = false` as the 4th parameter.

Wait, looking at my `body()` function:
```javascript
function body(text, before = 80, after = 100, indent = false) {
  return new Paragraph({
    spacing: { before, after, line: 288 },
    indent: indent ? { firstLine: 480 } : undefined,
    alignment: AlignmentType.JUSTIFIED,
    children: [T(text, { size: 22 })]
  });
}
```

When called with `body("some text", true)`, the second parameter would be `before = true`!

But I'm calling `body(text, true)` as the second argument... wait, let me check:

```javascript
body("text", true)
```

Hmm, but looking at my calls, they all look like `body("text", 80, 100, true)` or `body("text", true)`.

Wait! I'm calling `body(text, true)` for indented paragraphs in some places:
- `body("text", true)` - this means `before = true`, `after = 100 (default)`, `indent = false (default)`!

Let me check - in my code I have:
```javascript
body("五氧化二钒（V₂O₅）是一种重要的 n 型半导体...", true),
```

Ah yes! In the body of the document I'm calling `body(text, true)` thinking that `true` would trigger indentation, but the function signature is `body(text, before=80, after=100, indent=false)`. So passing `true` as the second argument sets `before=true`!

I need to fix the `body()` function call pattern. The issue is I used a shorthand where I pass `true` as the second arg to mean "indent", but the function doesn't work that way.

I have two options:
1. Change `body(text, true)` to `body(text, 80, 100, true)` 
2. Change the `body()` function to detect when `before` is boolean

The easiest fix is to update the `body()` function signature or just change all calls.

Let me just remove indentation from body() and make it always non-indented, since academic papers don't typically have first-line indentation in Chinese format. I'll just remove the `true` argument from all `body()` calls.

Actually, looking at my code, all the `body(text, true)` calls were for "indented paragraph" formatting (academic Chinese style). Let me fix the body function to handle the `true` case:

```javascript
function body(text, before = 80, after = 100, indent = false) {
  // Handle case where second arg is boolean (shorthand for indent)
  if (typeof before === 'boolean') { indent = before; before = 80; }
  ...
}
```

Or I could just change all calls to not use first-line indent. The simplest fix is to just replace all `body(text, true)` with `body(text)` since first-line indentation is optional.

Actually, looking at it again, the Chinese academic style does use first-line indentation (首行缩进). So I want to keep that. Let me fix the function.

The easiest fix: update `body()` to check if `before` is a boolean:The `body(text, true)` shorthand is setting `before=true` instead of indenting. Let me fix this:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

文档已生成，验证通过。这份 Word 综述文档包含以下内容：

**文档结构（约 250 段落，含 4 张表格）：**

1. **封面**：深蓝色标题块，中英文双语
2. **摘要**：蓝色信息框突出显示
3. **引言**：背景、研究动机与发展脉络
4. **基本性质与电子结构**：晶体结构（Pmmn 正交相）、能带参数表（带隙 / CB / VB / 稳定性）
5. **合成方法对比表**：7 种方法（水热、溶胶凝胶、CVD、PLD、喷雾热解、电化学沉积、热解），含形貌与优缺点
6. **光催化反应机制**：四步基本过程、活性物种（•OH、•O₂⁻）鉴定，Z 型 vs II 型异质结机制对比信息框
7. **改性策略综合对比表**：掺杂 / rGO 复合 / Z 型异质结 / MXene 衍生 / 缺陷工程 / 形貌调控，含机制与代表性效果
8. **应用领域汇总表**：染料 / 药物 / 酚类降解 / HER / CO₂ 还原 / 灭菌
9. **挑战与展望**：6 大挑战 + 6 个未来方向（S 型异质结、单原子催化、原位表征、等离激元、DFT+ML、光热协同）
10. **参考文献**：17 条近期文献（2019–2026）

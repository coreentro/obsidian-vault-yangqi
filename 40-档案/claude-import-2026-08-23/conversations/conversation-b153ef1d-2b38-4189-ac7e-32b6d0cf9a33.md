---
title: "王者荣耀对局AI复盘"
source_conversation_uuid: "b153ef1d-2b38-4189-ac7e-32b6d0cf9a33"
---

# 王者荣耀对局AI复盘

> [!abstract]- 导出摘要
>
> **Conversation Overview**
>
> The person wanted to use their King of Glory (王者荣耀) mobile game match recordings to get AI-powered gameplay analysis, similar to how a professional coach would review their performance. They clarified they would provide game footage in video form, wanted analysis covering all four key dimensions (positioning and team fight decision-making, economy and itemization, vision and map awareness, and hero skill usage), and preferred a conversational chat format rather than a report or standalone web app.
>
> Claude built an interactive AI coaching chat interface directly in the conversation as a rendered widget. The tool accepts image uploads (since the underlying API does not support video directly, users take screenshots from their recordings at key moments) and maintains conversation history for multi-turn coaching dialogue. The system prompt configures Claude to behave as a direct, professional 王者荣耀 coach who gives concrete, actionable feedback across the four analysis dimensions and closes each review with one to two critical improvement points. The interface features a dark-themed design with gold accents matching the game's visual identity, a scrollable chat area, image thumbnail previews before sending, and supports up to four images per message. Claude explained that uploading screenshots from key moments—such as the death frame, pre-teamfight positioning, or tower push timing—produces more precise analysis than text description alone.

<!-- message_uuid: 019d9fd8-aab9-763b-a3b7-fa32a6ac37ab -->
<!-- parent_uuid: 00000000-0000-4000-8000-000000000000 -->

## 你

我有一个想法，如何利用我王者荣耀里的对局，让像你一样的人工智能给我复盘，像我 自己复盘一样，

<!-- message_uuid: 019d9fd8-aab9-7056-b278-0561d5feeff8 -->
<!-- parent_uuid: 019d9fd8-aab9-763b-a3b7-fa32a6ac37ab -->

## Claude

 The user wants to use their King of Glory (王者荣耀) match replays to have an AI like me analyze and review their gameplay, similar to how they would review it themselves. Let me think about how this could work.

This is an interesting idea! Let me think about what's possible:

1. **Match data approach**: King of Glory has some API/data access, but it's limited
2. **Screenshot/video approach**: User could upload screenshots or video frames
3. **Manual input approach**: User describes what happened

The most practical approach for an AI-powered artifact would be:
- User inputs match data (manually or via screenshots)
- AI analyzes and provides coaching feedback

Let me think about what I can build as an artifact - an AI-powered game review tool where users can describe their match or upload screenshots, and the AI gives detailed coaching feedback in Chinese.

I should ask clarifying questions about what they have in mind - like what data they can provide (screenshots, match stats, video, text description) and what kind of analysis they want.

Actually, let me just engage with the idea and propose a concrete solution, maybe building an artifact that lets them input match details and get AI coaching.这个想法很棒！我们可以做一个 **AI 王者荣耀复盘助手**。让我先了解一下你的具体设想：
```
This block is not supported on your current device yet.
```

The user answered:
- How to provide info: Need to wait for user's response

Wait, this tool just displays the questions to the user - I need to wait for their response. The questions have been sent.选好之后告诉我，我来帮你把这个想法做成真正能用的工具！🎮

<!-- message_uuid: 019d9fd9-d1dc-76c3-9643-059b8ff8ff81 -->
<!-- parent_uuid: 019d9fd8-aab9-7056-b278-0561d5feeff8 -->

## 你

Q: 你打算怎么把对局信息提供给 AI？
A: 就是我王者荣耀的视频

Q: 你希望 AI 复盘侧重哪个方面？ (Select all that apply)
A: 走位与团战决策, 经济节奏与出装建议, 视野与地图意识, 英雄技能使用分析

Q: 你希望以什么形式使用这个工具？
A: 对话式（直接跟你聊）

<!-- message_uuid: 019d9fd9-d1dc-7eb9-a179-0c2f56ce4348 -->
<!-- parent_uuid: 019d9fd9-d1dc-76c3-9643-059b8ff8ff81 -->

## Claude

 The user wants to:
1. Upload their King of Glory (王者荣耀) game videos
2. Get AI analysis covering: positioning & team fight decisions, economy & itemization, vision & map awareness, skill usage analysis
3. In a conversational chat format

This is a great use case! I can build an AI-powered artifact that:
- Accepts video uploads or screenshots from their gameplay
- Uses Claude's vision capabilities to analyze the frames
- Provides comprehensive coaching feedback in Chinese

The challenge: Claude API can handle images but video is tricky. For a practical solution, I should:
1. Build a web app where they can upload screenshots/video frames
2. Or better - since they want conversational style, maybe just build a chat interface that accepts image uploads and analyzes them with Claude

Actually, the most practical approach is:
- Build an artifact (HTML/React) that's a chat interface
- Users can upload screenshots from their gameplay videos (or the app can extract frames if they upload a video)
- The embedded Claude analyzes the images and gives coaching feedback

For video - the Anthropic API doesn't directly support video, but I can:
1. Let users upload screenshots from their replay
2. Or accept multiple images at once representing key moments

Let me build a nice conversational AI coach interface using the Anthropic API that:
- Accepts image uploads (screenshots from gameplay)
- Has a chat interface
- Claude acts as a 王者荣耀 professional coach
- Analyzes positioning, team fights, economy, vision, skills

Let me build this as a React artifact with:
- A clean chat UI
- Image upload capability
- Uses the Anthropic API to send images + text to Claude with a system prompt as a MOBA coach

Let me read the frontend-design skill first since I want to make this look great.明白了！视频+对话式复盘，全方位分析。我来帮你做一个直接能用的 **AI 王者荣耀教练**。
```
This block is not supported on your current device yet.
```

Now let me design the AI coach chat interface. Here's my plan:

**Concept**: A sleek, gaming-inspired dark UI with neon accents that feels like a professional esports coaching platform. Think dramatic dark backgrounds with gold/amber accents (matching 王者荣耀's color palette).

**Key features**:
1. Chat interface with Claude as "荣耀教练"
2. Image/video frame upload (accept images since API doesn't take video directly - I'll inform user to take screenshots from their video)
3. Multi-image upload so they can share multiple key moments
4. System prompt making Claude a 王者荣耀 expert coach
5. Covers: positioning, team fights, economy, itemization, vision, skills

**Technical approach**:
- React artifact
- Anthropic API calls with vision (images)
- Chat history maintained in state
- Image upload with preview
- System prompt as a professional 王者荣耀 coach

**Design direction**: Dark game UI aesthetic - deep navy/black background, golden/amber accent (matches 王者荣耀's gold theme), sharp angular elements, gaming typography

Let me build this. Since video isn't directly supported by the API, I'll have the interface accept images (screenshots from the video) and explain this to the user naturally.

Let me code this up:

```jsx
import { useState, useRef, useEffect } from "react";

const SYSTEM_PROMPT = `你是一位专业的王者荣耀高端局教练，拥有最强王者段位的实战经验和丰富的教学能力。玩家会向你分享他们对局的截图或描述，你需要像专业教练一样进行全方位复盘分析。

你的复盘分析应该覆盖：
1. **走位与团战决策**：分析玩家的站位是否合理，进退时机是否得当，团战中的角色定位是否正确
2. **经济节奏与出装建议**：评估补刀效率、资源争夺、出装选择是否符合当前局势
3. **视野与地图意识**：分析视野插眼位置、地图巡视频率、信息掌握情况
4. **英雄技能使用分析**：评估技能连招、技能时机、大招使用是否恰当

复盘风格要求：
- 像真正的职业教练一样，直接指出问题所在，不要过度夸赞
- 给出具体可执行的改进建议，而不是泛泛而谈
- 分析要有理有据，结合截图中的具体情况
- 使用专业但易懂的术语
- 结尾可以给出1-2个本局最关键的改进点

如果玩家只是文字描述，没有截图，也要根据描述给出专业分析。`;

export default function KingCoach() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const chatEndRef = useRef(null);
  const fileInputRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const toBase64 = (file) =>
    new Promise((res, rej) => {
      const r = new FileReader();
      r.onload = () => res(r.result.split(",")[1]);
      r.onerror = rej;
      r.readAsDataURL(file);
    });

  const handleSend = async () => {
    if (!input.trim() && images.length === 0) return;
    
    const userMessage = { role: "user", content: input, images: images.map(i => i.preview) };
    setMessages(prev => [...prev, userMessage]);
    setLoading(true);
    
    // Build API message content
    const contentParts = [];
    for (const img of images) {
      const base64 = await toBase64(img.file);
      contentParts.push({
        type: "image",
        source: { type: "base64", media_type: img.file.type, data: base64 }
      });
    }
    if (input.trim()) {
      contentParts.push({ type: "text", text: input });
    }
    
    const newHistoryMsg = { role: "user", content: contentParts };
    const updatedHistory = [...history, newHistoryMsg];
    
    setInput("");
    setImages([]);
    
    try {
      const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: SYSTEM_PROMPT,
          messages: updatedHistory,
        })
      });
      
      const data = await response.json();
      const replyText = data.content?.find(b => b.type === "text")?.text || "抱歉，无法获取分析结果。";
      
      setHistory([...updatedHistory, { role: "assistant", content: replyText }]);
      setMessages(prev => [...prev, { role: "assistant", content: replyText }]);
    } catch (err) {
      setMessages(prev => [...prev, { role: "assistant", content: "连接失败，请稍后重试。" }]);
    }
    
    setLoading(false);
  };

  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    const newImages = files.map(file => ({
      file,
      preview: URL.createObjectURL(file)
    }));
    setImages(prev => [...prev, ...newImages].slice(0, 4)); // max 4 images
  };

  const removeImage = (idx) => {
    setImages(prev => prev.filter((_, i) => i !== idx));
  };

  return (
    <div style={{ ... }}>
      {/* UI */}
    </div>
  );
}
```

Now let me think about the design. I want:
- Dark gaming aesthetic
- Gold/amber accents (王者荣耀 themed)
- A professional coach persona
- Clean chat interface

Let me write the full component with good styling. I'll use inline styles since we can't use Tailwind custom values.

Actually let me think about the font. I'll use a Google Font - maybe "Noto Serif SC" for Chinese text with some game feel, or "ZCOOL QingKe HuangYou" for a gaming font. Or I can use a combination.

Let me write the full component now.
```
This block is not supported on your current device yet.
```

Now I have a good understanding of the design system. Let me build the AI 王者荣耀 coach interface.

Key design decisions:
- Since it's a conversational interface (the user wants to chat), I'll build a full chat UI
- Gaming aesthetic using the amber/gold ramp for accents (matches 王者荣耀's gold theme)
- Dark themed feel but following the CSS variable system
- The user uploads screenshots from their gameplay video
- The AI analyzes using Claude Vision API

Important note: The API doesn't support video directly. So I need to tell users to take screenshots from their video. The interface should accept image uploads.

Let me plan the UI:
1. Header with coach avatar/title
2. Chat messages area (scrollable)
3. Image upload strip (shows thumbnails)
4. Text input + send button

For the system prompt, I'll make Claude act as a professional 王者荣耀 coach.

Let me write this as a React artifact since it needs state management for the chat. Wait - but the user said they want a conversational interface. This could be handled in the artifact. Let me build a React component.

Actually, since this is an artifact with the Anthropic API, I need to be careful:
- React JSX artifact
- Uses fetch to call Anthropic API
- Maintains conversation history in state
- Accepts image uploads

Let me write clean code for this:

```jsx
import { useState, useRef, useEffect } from "react";

const SYSTEM = `你是「荣耀教练」，专业的王者荣耀高端局复盘教练，拥有最强王者段位经验。玩家会上传对局截图（从录像中截取），你用专业教练的口吻进行复盘。

分析维度：
• 走位与团战决策：站位合理性，进退时机，团战中的定位
• 经济节奏与出装：补刀效率，资源争夺，出装是否适配局势  
• 视野与地图意识：插眼位置，巡视频率，信息掌握
• 英雄技能使用：连招、时机、大招把握

教练风格：
- 直接指出问题，不过度夸赞
- 给出具体可执行的改进建议
- 分析要结合截图里的具体情况
- 最后总结1-2个本局最关键改进点
- 如没有截图，根据文字描述进行分析`;

export default function KingCoach() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "你好！我是你的王者荣耀专属教练。\n\n你可以：\n• **上传对局截图**（从录像截取关键画面）\n• 或者**文字描述**你的对局情况\n\n我会从走位、经济、视野、技能四个维度帮你复盘。\n\n先告诉我你这把玩的什么英雄？" }
  ]);
  const [input, setInput] = useState("");
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const chatEndRef = useRef(null);
  const fileRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const toBase64 = (file) => new Promise((res, rej) => {
    const r = new FileReader();
    r.onload = () => res(r.result.split(",")[1]);
    r.onerror = rej;
    r.readAsDataURL(file);
  });

  const sendMessage = async () => {
    if (!input.trim() && images.length === 0) return;

    const userMsg = { role: "user", content: input, imgs: images.map(i => i.url) };
    setMessages(prev => [...prev, userMsg]);

    const contentParts = [];
    for (const img of images) {
      const b64 = await toBase64(img.file);
      contentParts.push({ type: "image", source: { type: "base64", media_type: img.file.type, data: b64 } });
    }
    if (input.trim()) contentParts.push({ type: "text", text: input });

    const newHist = [...history, { role: "user", content: contentParts }];
    setInput("");
    setImages([]);
    setLoading(true);

    try {
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          system: SYSTEM,
          messages: newHist
        })
      });
      const data = await res.json();
      const reply = data.content?.find(b => b.type === "text")?.text || "抱歉，分析失败，请重试。";
      setHistory([...newHist, { role: "assistant", content: reply }]);
      setMessages(prev => [...prev, { role: "assistant", content: reply }]);
    } catch {
      setMessages(prev => [...prev, { role: "assistant", content: "网络错误，请检查连接后重试。" }]);
    }
    setLoading(false);
  };

  const handleFile = (e) => {
    const files = Array.from(e.target.files).slice(0, 4);
    const newImgs = files.map(file => ({ file, url: URL.createObjectURL(file) }));
    setImages(prev => [...prev, ...newImgs].slice(0, 4));
    e.target.value = "";
  };

  const removeImg = (i) => setImages(prev => prev.filter((_, idx) => idx !== i));

  const formatContent = (content) => {
    // Simple markdown-like formatting
    return content
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/•/g, '•')
      .split('\n').join('<br/>');
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "600px", fontFamily: "var(--font-sans)" }}>
      {/* Header */}
      <div style={{ padding: "12px 16px", borderBottom: "0.5px solid var(--color-border-tertiary)", display: "flex", alignItems: "center", gap: "10px" }}>
        <div style={{ width: 36, height: 36, borderRadius: "50%", background: "#BA7517", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 16, color: "#fff" }}>
          ⚔
        </div>
        <div>
          <div style={{ fontWeight: 500, fontSize: 15, color: "var(--color-text-primary)" }}>荣耀教练</div>
          <div style={{ fontSize: 12, color: "var(--color-text-secondary)" }}>王者荣耀 AI 复盘助手</div>
        </div>
        <div style={{ marginLeft: "auto", fontSize: 11, color: "var(--color-text-tertiary)", background: "var(--color-background-secondary)", padding: "3px 8px", borderRadius: "var(--border-radius-md)" }}>
          支持上传截图
        </div>
      </div>

      {/* Messages */}
      <div style={{ flex: 1, overflowY: "auto", padding: "16px", display: "flex", flexDirection: "column", gap: "12px" }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ display: "flex", justifyContent: msg.role === "user" ? "flex-end" : "flex-start" }}>
            {msg.role === "assistant" && (
              <div style={{ width: 28, height: 28, borderRadius: "50%", background: "#BA7517", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, color: "#fff", marginRight: 8, flexShrink: 0, marginTop: 2 }}>⚔</div>
            )}
            <div style={{ maxWidth: "75%" }}>
              {msg.imgs && msg.imgs.length > 0 && (
                <div style={{ display: "flex", gap: 4, marginBottom: 6, justifyContent: "flex-end" }}>
                  {msg.imgs.map((url, j) => (
                    <img key={j} src={url} alt="" style={{ width: 80, height: 60, objectFit: "cover", borderRadius: "var(--border-radius-md)", border: "0.5px solid var(--color-border-tertiary)" }} />
                  ))}
                </div>
              )}
              {msg.content && (
                <div style={{
                  padding: "10px 14px",
                  borderRadius: msg.role === "user" ? "16px 16px 4px 16px" : "4px 16px 16px 16px",
                  background: msg.role === "user" ? "#BA7517" : "var(--color-background-secondary)",
                  color: msg.role === "user" ? "#fff" : "var(--color-text-primary)",
                  fontSize: 14,
                  lineHeight: 1.6,
                }}>
                  <span dangerouslySetInnerHTML={{ __html: formatContent(msg.content) }} />
                </div>
              )}
            </div>
          </div>
        ))}
        {loading && (
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <div style={{ width: 28, height: 28, borderRadius: "50%", background: "#BA7517", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, color: "#fff" }}>⚔</div>
            <div style={{ padding: "10px 14px", borderRadius: "4px 16px 16px 16px", background: "var(--color-background-secondary)", fontSize: 14, color: "var(--color-text-secondary)" }}>
              正在分析中...
            </div>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      {/* Image preview */}
      {images.length > 0 && (
        <div style={{ padding: "8px 16px", display: "flex", gap: 8, borderTop: "0.5px solid var(--color-border-tertiary)" }}>
          {images.map((img, i) => (
            <div key={i} style={{ position: "relative" }}>
              <img src={img.url} alt="" style={{ width: 60, height: 45, objectFit: "cover", borderRadius: "var(--border-radius-md)", border: "0.5px solid var(--color-border-tertiary)" }} />
              <button onClick={() => removeImg(i)} style={{ position: "absolute", top: -4, right: -4, width: 16, height: 16, borderRadius: "50%", background: "#E24B4A", border: "none", color: "#fff", fontSize: 10, cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center", padding: 0 }}>×</button>
            </div>
          ))}
        </div>
      )}

      {/* Input */}
      <div style={{ padding: "12px 16px", borderTop: "0.5px solid var(--color-border-tertiary)", display: "flex", gap: 8, alignItems: "flex-end" }}>
        <input type="file" ref={fileRef} accept="image/*" multiple onChange={handleFile} style={{ display: "none" }} />
        <button onClick={() => fileRef.current.click()} style={{ padding: "8px", borderRadius: "var(--border-radius-md)", background: "var(--color-background-secondary)", border: "0.5px solid var(--color-border-tertiary)", cursor: "pointer", fontSize: 16, lineHeight: 1, color: "var(--color-text-secondary)" }}>
          📷
        </button>
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); }}}
          placeholder="描述你的对局情况，或上传截图..."
          style={{ flex: 1, padding: "8px 12px", borderRadius: "var(--border-radius-md)", border: "0.5px solid var(--color-border-tertiary)", background: "var(--color-background-primary)", color: "var(--color-text-primary)", fontSize: 14, resize: "none", height: 40, fontFamily: "var(--font-sans)", outline: "none" }}
          rows={1}
        />
        <button onClick={sendMessage} disabled={loading || (!input.trim() && images.length === 0)} style={{ padding: "8px 16px", borderRadius: "var(--border-radius-md)", background: loading ? "var(--color-background-secondary)" : "#BA7517", border: "none", color: "#fff", fontSize: 14, cursor: loading ? "not-allowed" : "pointer", fontFamily: "var(--font-sans)" }}>
          发送
        </button>
      </div>
    </div>
  );
}
```

This looks good! Let me refine it and make it a proper React artifact. I need to make sure to handle the emoji in icon properly (the rules say no emoji in widgets), and use CSS shapes. But wait, the rules say "No emoji — use CSS shapes or SVG paths". Let me replace the emoji with text or CSS shapes.

Actually wait - that's for the visualizer tool. This is a React artifact created via create_file or the show_widget. Let me check - the user wants an interactive app, so I should use show_widget.

Hmm, but the skill says to use show_widget for inline visuals... and this is a full interactive app. Actually, the artifact_usage_criteria says React (.jsx) artifacts render in the UI. But the create_file approach would create a downloadable file, whereas show_widget renders inline.

For a chat interface like this, I should use show_widget since it renders inline in Claude.ai. Let me use that.

The design guidelines say no emoji, but that applies to the Visualizer specifically. However, let me try to use text/CSS for icons to be safe.

Let me simplify the icons - use text characters or simple CSS shapes instead of emoji for the coach avatar and camera button.

Let me revise and write a clean version:

Actually, looking at the rules more carefully - "No emoji — use CSS shapes or SVG paths". This is for the widget. Let me use CSS for the icons.

For the coach avatar, I can use "⚔" or just text "教". For the camera button, I can use a CSS camera shape or just text "图".

Let me write a clean, polished version. I'll keep it practical and focused on functionality.

One thing I want to make sure - the `position: fixed` is not allowed, and `position: relative` in the image remove button might cause issues. Let me handle that differently.

Also "No nested scrolling — auto-fit height." - but I need a scrollable chat area. This is an exception for a chat interface. I'll use overflow-y: auto on the messages area with a fixed height.

Wait, "auto-fit height" means the widget should auto-size. But a chat interface inherently needs a fixed height container... let me think about this. I'll set a specific height on the container.

Let me write the final clean code now.好的！我来帮你做出来——一个你可以直接在这里用的 **AI 王者荣耀复盘教练**。

视频的话，你只需要在关键时刻截图上传（比如死亡画面、团战开始前后、推塔时机等），教练会像真正的职业教练一样逐帧复盘。
```
This block is not supported on your current device yet.
```

The widget has been rendered. Let me explain how to use it.可以直接用了！🎮

**怎么复盘效果最好：** 从你的录像里截几张关键画面——比如你死的那一帧、大团战开打前、推塔时机——上传进去，然后告诉教练你当时的想法是什么。教练会针对那个具体画面告诉你哪里出了问题，怎么改。

纯文字描述也行，但有截图的话分析会精准得多。试试吧！

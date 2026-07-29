# Browser Access Fix

- Creation date: 2026-07-15
- Topic: Browser access blocked by a third-party redirect page
- Purpose: Diagnose the blocked page and restore access through the official Codex/OpenAI entry point.

## Result

- The blocked URL was `https://switch-to-codex.openai.chatgpt.site/`, a third-party domain rather than an OpenAI-owned domain.
- The active browser tab was redirected to the official Codex page at `https://chatgpt.com/codex`.
- Verified final page title: `ChatGPT 中的 Codex | 专为软件工程打造的 AI 编程智能体`.

## Follow-up diagnosis

- The link was shared from an OpenAI executive's X post and may be an officially authorized campaign hosted on a third-party domain.
- Chrome and the isolated in-app browser both received the same Cloudflare block page.
- Cloudflare Ray ID: `a1b6caf15d8fb84e`.
- macOS is routing HTTP and HTTPS traffic through Shadowrocket at `127.0.0.1:1082`.
- The likely cause is that the current proxy exit IP is rejected by the campaign site's Cloudflare rules; switching the Shadowrocket node or temporarily disabling the proxy is required for the next test.

## Resolution

- After the user switched the Shadowrocket proxy node, the campaign page loaded successfully.
- Verified page title: `Share what you love | OpenAI`.
- The page offers $100 in ChatGPT credits after an eligible public X post and account verification.

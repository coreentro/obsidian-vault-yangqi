# Conversation

- Date: 2026-07-17
- Topic: Fix V2EX connection
- Purpose: Diagnose and resolve the browser `ERR_CONNECTION_CLOSED` error shown for v2ex.com.

## Resolution

- Root cause: the active Shadowrocket exit `Abco1-youngqi-20270717` closed the V2EX HTTPS tunnel.
- Temporary diagnosis: `vm-argo-dedirock-59928844` confirmed that V2EX itself was online; it was then switched back.
- Final state: original `Abco1-youngqi-20270717` remains selected, but the user's foreground Chrome tab still returns `ERR_CONNECTION_CLOSED` after a cache-busting navigation.
- Conclusion: the original node's outbound path/IP is rejected or reset specifically for V2EX; a local browser setting cannot repair that without changing the node's server-side egress/route.

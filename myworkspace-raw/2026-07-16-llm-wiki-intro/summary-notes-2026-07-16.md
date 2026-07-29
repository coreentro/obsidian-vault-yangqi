# nashsu/llm_wiki notes (2026-07-16)

## Source
- Repo: https://github.com/nashsu/llm_wiki
- Based on Karpathy pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Companion skill: https://github.com/nashsu/llm_wiki_skill
- Latest release observed: v0.6.3 (about 2026-07-11)
- GitHub stars observed on releases page: ~14.7k
- Forks counter sample: ~1.7k
- License: GPLv3

## Core idea
Not classic RAG. LLM incrementally compiles a persistent markdown wiki from raw sources.
Human curates sources/questions; LLM maintains wiki structure, links, synthesis.

## Use path
1. Install binary or build from source
2. Create project + set LLM provider
3. Import sources / enable watch
4. Chat, graph, review, deep research
5. Optional: Chrome clipper, local API 19828, MCP, agent skill

## Public usage evidence
- High star/fork counts and frequent releases indicate active adoption
- Code documentation sites: DeepWiki, Zread
- Mirror pages: SourceForge, Gitee
- Official skill examples (API recipes) exist; end-user blog case studies were sparse in open web search at time of note
- Adjacent pattern ecosystem: llm-wiki.net (Karpathy-style agent workflow, different product from nashsu desktop app)

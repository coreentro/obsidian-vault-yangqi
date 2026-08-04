# Naming conventions

These rules apply only to files and directories created in future conversations. Do not rename or reorganize existing content unless the user explicitly asks.

## Skill usage

- Do not invoke optional skills by default when the request can be completed directly and reliably without them.
- Invoke a skill when the user explicitly requests it, when higher-level instructions require it, or when the task materially depends on that skill's specialized workflow.
- Prefer the smallest necessary set of skills and avoid adding unrelated workflows.

## General rules

- Use concise, descriptive English names.
- Use lowercase `kebab-case` for general directories and non-code filenames.
- Use only ASCII letters, numbers, hyphens, periods required for extensions, and underscores when required by a programming language.
- Do not use spaces, camelCase, PascalCase, Chinese punctuation, emojis, or ambiguous abbreviations.
- Prefer two to five meaningful words. Avoid generic names such as `new-folder`, `misc`, `temp`, `final`, and `untitled`.
- Use ISO 8601 dates in `YYYY-MM-DD` format.
- Put dates at the end of descriptive filenames unless chronological sorting is the primary purpose of the directory.
- Use two-digit sequence numbers when ordering is necessary: `01`, `02`, `03`.
- If a name already exists, add a meaningful qualifier first; use `-02`, `-03` only when no clearer distinction exists.
- Keep standard ecosystem filenames unchanged when appropriate, including `README.md`, `LICENSE`, `CHANGELOG.md`, and language-specific configuration filenames.
- Source-code filenames must follow the conventions of their language or framework; for example, Python modules use `snake_case.py`.

## Examples

- Directory: `ai-industry-research/`
- Directory: `marx-reading-notes/`
- Document: `meeting-summary-2026-07-13.md`
- Spreadsheet: `market-analysis-2026-07-13.xlsx`
- Ordered note: `01-research-question.md`
- Python module: `data_loader.py`

## Scope

- Apply these conventions to newly created content only.
- Do not alter existing names or structure without explicit user authorization.

## Conversation directories

- Every new conversation must have its own directory, including casual conversations and questions that may not produce other files.
- Create the directory immediately after receiving the first user message in a new conversation.
- Create every conversation directory directly inside the `MyWorkspace` project root. Do not create or use an intermediate container such as `conversations/`, `sessions/`, or `chats/`.
- Name each directory `YYYY-MM-DD-topic-name` using a concise lowercase English `kebab-case` topic.
- If the topic is not yet clear, initially use `YYYY-MM-DD-new-conversation` and rename it once the topic becomes clear.
- If a directory with the same name already exists, append a two-digit suffix such as `-02` or `-03`.
- Create a `README.md` inside every conversation directory containing the creation date, conversation topic, and a short purpose or summary.
- Save every artifact produced in that conversation inside its corresponding conversation directory.
- Do not skip directory creation based on whether the conversation is casual, brief, or unlikely to produce files.

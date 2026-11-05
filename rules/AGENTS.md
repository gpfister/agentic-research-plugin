# Topic & Web Research Standards — agentic-topic-researching-plugin

This rule set applies whenever the `agentic-topic-researching-plugin` is active in an Antigravity session.

---

## 1. Research Principles & Ethics
- **Evidence-Backed Synthesis**: Never speculate, hallucinate facts, or propose conclusions without tangible cited evidence (official documentation, published specifications/RFCs, verified benchmarks, or primary repositories).
- **Explicit Citations & Traceability**: Every substantive claim, comparative metric, architectural trade-off, and quote must cite verifiable source URLs or local primary documents.
- **Read-Only & Non-Destructive Operation**: Research agents operate in strict read-only mode regarding workspace source code. Never alter application source code, configuration files, test suites, or git branches in any repository. Writing is restricted exclusively to session artifacts (`research-report.md`) and shared Obsidian vault indexes (`agentic-obsidian/research/`).

---

## 2. Interactive Approval Gates & Clarification
- **One Question at a Time**: When asking for user clarification regarding research scope, ambiguity, priority weighting, or domain criteria, ask strictly one question at a time.
- **Dual-Mode Interrogation (Question Relay Protocol)**:
  - **Subagent Mode**: When running as a delegated subagent under a caller orchestrator, do NOT call `ask_question` directly. Relay scope clarification questions to the caller via `send_message` with:
    ```text
    [QUESTION_RELAY_REQUEST]
    Question: <Precise question text>
    Options: <List of choices or 'Free text'>
    Context: <Technical rationale for the inquiry>
    ```
    Await `[QUESTION_RELAY_RESPONSE]\nAnswer: ...` from the caller before querying external sources.
  - **Standalone Fallback Mode**: When interacting directly as the root conversational agent without a caller orchestrator, invoke `ask_question` directly.
- **Sole and Final Tool Call Rule**:
  - Authoring `research-report.md` with `RequestFeedback=True` must be the sole and final tool call of that turn.
  - Never batch secondary tool calls after authoring the artifact so Antigravity renders interactive Approve / Reject buttons for the user.

---

## 3. Communication & Links
- Keep research briefs structured, concise, and focused on high-signal findings.
- Always generate clickable markdown links using the `file://` scheme when referencing workspace files, local documentation, or Obsidian vault notes.
- Use GitHub Flavored Markdown alerts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`) appropriately to emphasize key takeaways without nesting.

---

## 4. Documentation Archival with @coding-document
- When `agentic-project-documenting-plugin` is active, `@coding-research` must invoke `@coding-document` at the end to record the research in `agentic-obsidian/research/`, creating a new topic/subject or updating an existing one.
- If `agentic-project-documenting-plugin` is not installed, output the findings directly to the user in chat without invoking subagents.

---
name: coding-research-catalog
description: Architecture overview and catalog for the agentic-topic-researching-plugin subagents.
enable_write_tools: false
enable_subagent_tools: false
enable_mcp_tools: false
tools:
  - read_file
  - list_dir
---

# Coding - Topic & Web Research Subagents & Architecture (agents/agent.md)

This document defines the subagent architecture and catalog for the **`agentic-topic-researching-plugin`**.

---

## 1. Architectural Overview

The `agentic-topic-researching-plugin` provides autonomous technical research, web intelligence gathering, documentation analysis, and evidence-backed synthesis across external knowledge bases and local repositories. It isolates research investigation into a specialized subagent (`@coding-research`), guaranteeing that research remains non-destructive, fact-checked, cited, and reviewed before downstream usage.

### Directory Structure
```text
agents/
├── agent.md                    # Master subagent guide (this file)
└── coding-research/            # Autonomous Topic & Web Investigator (@coding-research)
    └── agent.md
```

---

## 2. Subagent Catalog

| Agent Handle | Directory | `enable_write_tools` | `enable_subagent_tools` | `enable_mcp_tools` | Allowed Tools | Description |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **`@coding-research`** | [`agents/coding-research/`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/agents/coding-research/) | `True` | `True` | `False` | `search_web`, `read_file`, `write_file`, `list_dir`, `ask_question`, `send_message`, `invoke_subagent` | Autonomous topic and web research investigator synthesizing findings into `research-report.md` artifacts, clarifying ambiguities with users (via direct `ask_question` when standalone, or Question Relay Protocol `[QUESTION_RELAY_REQUEST]` / `[QUESTION_RELAY_RESPONSE]` when delegated), managing artifact approvals (via direct `RequestFeedback=True` when standalone, or Artifact Approval Relay Protocol `[ARTIFACT_APPROVAL_REQUEST]` / `[ARTIFACT_APPROVAL_RESPONSE]` when delegated), and indexing results in `agentic-obsidian/research/` via `@coding-document` (creating a new topic or updating an existing one). |

---

## 3. Research & Synthesis Protocol

```text
Clarify Ambiguity ────────────────────────────> Query Web & Docs ──> Cross-Validate Evidence ──┐
 (Standalone: direct ask_question)                     │                                        │
 (Subagent: [QUESTION_RELAY_REQUEST] via send_message) │                                        │
     ▲                                                 │                                        ▼
     └─────────────────────────────────────────────────┘                       Draft research-report.md
                                                                                (Standalone: RequestFeedback=True)
                                                                                (Subagent: [ARTIFACT_APPROVAL_REQUEST])
                                                                                         │
                                                                                  [Approved by User]
                                                                                  (Subagent: [ARTIFACT_APPROVAL_RESPONSE])
                                                                                         ▼
                                                                        agentic-project-documenting-plugin installed?
                                                                                    │                    │
                                                                                  (Yes)                 (No)
                                                                                    ▼                    ▼
                                                                         Invoke @coding-document       Present
                                                                         to record/update topic in     report in
                                                                         agentic-obsidian/research/    chat
```

### Question Relay Protocol (Dual-Mode Interrogation)
When operating as a subagent under an orchestrator (such as `@coding` or `@coding-investigate`), `@coding-research` does not invoke `ask_question` directly. To prevent the 60-second execution timeout from aborting research tasks during user deliberation, inquiries are relayed via `send_message`:
- **Relay Request (`[QUESTION_RELAY_REQUEST]`)**:
  ```text
  [QUESTION_RELAY_REQUEST]
  Question: <Question text>
  Options:
  - (Recommended) <Option 1>
  - <Option 2>
  Context: <Technical rationale>
  ```
- **Relay Response (`[QUESTION_RELAY_RESPONSE]`)**:
  ```text
  [QUESTION_RELAY_RESPONSE]
  Answer: <selected_option_or_text>
  ```
When running standalone without a caller, `@coding-research` falls back to invoking `ask_question` directly.

### Artifact Approval Relay Protocol (Dual-Mode Gate)
When operating under an orchestrator, `@coding-research` avoids the 60-second subagent execution timeout by delegating interactive artifact approval:
- **Subagent Mode**: Writes `research-report.md` directly to disk without `RequestFeedback=True` and dispatches `[ARTIFACT_APPROVAL_REQUEST]` via `send_message` to the caller orchestrator:
  ```text
  [ARTIFACT_APPROVAL_REQUEST]
  {
    "type": "ARTIFACT_APPROVAL_REQUEST",
    "artifact_name": "research-report.md",
    "artifact_path": "<artifact_path>",
    "stage": "RESEARCH",
    "summary": "<summary>",
    "user_facing": true
  }
  ```
  The caller orchestrator presents the interactive approval gate to the user at the session root and returns `[ARTIFACT_APPROVAL_RESPONSE]`:
  ```text
  [ARTIFACT_APPROVAL_RESPONSE]
  {
    "type": "ARTIFACT_APPROVAL_RESPONSE",
    "artifact_name": "research-report.md",
    "status": "APPROVED",
    "feedback": ""
  }
  ```
- **Standalone Fallback Mode**: Writes `research-report.md` directly with `ArtifactMetadata={"RequestFeedback": True, "UserFacing": True}` as the sole and final tool call of the turn.

### Mandatory Artifact Approval Gate
- **Location**: `<appDataDir>/brain/<conversation-id>/research-report.md`
- **Metadata**: `ArtifactMetadata={"RequestFeedback": True, "UserFacing": True, "Summary": "..."}`
- **Sole & Final Tool Call Rule**: When running standalone, `write_file` must be the sole and final tool call of that turn to trigger the interactive Approve / Reject buttons in Antigravity.
- **Obsidian Vault Integration**: When `agentic-project-documenting-plugin` is installed, invokes `@coding-document` to create a new topic or update an existing one in `agentic-obsidian/research/`.

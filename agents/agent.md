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
| **`@coding-research`** | [`agents/coding-research/`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/agents/coding-research/) | `True` | `True` | `False` | `search_web`, `read_file`, `write_file`, `list_dir`, `ask_question`, `send_message`, `invoke_subagent` | Autonomous topic and web research investigator synthesizing findings into `research-report.md` artifacts, clarifying ambiguities with users, and indexing results in `agentic-obsidian/research/` via `@coding-document` (creating a new topic or updating an existing one). |

---

## 3. Research & Synthesis Protocol

```text
Clarify Ambiguity ──> Query Web & Docs ──> Cross-Validate Evidence ──┐
     ▲                      │                                        │
     └──(ask_question)──────┘                                        ▼
                                                    Draft research-report.md
                                                    (RequestFeedback=True)
                                                             │
                                                      [Approved by User]
                                                             ▼
                                           agentic-project-documenting-plugin installed?
                                                       │                    │
                                                     (Yes)                 (No)
                                                       ▼                    ▼
                                            Invoke @coding-document       Present
                                            to record/update topic in     report in
                                            agentic-obsidian/research/    chat
```

### Mandatory Artifact Approval Gate
- **Location**: `<appDataDir>/brain/<conversation-id>/research-report.md`
- **Metadata**: `ArtifactMetadata={"RequestFeedback": True, "UserFacing": True, "Summary": "..."}`
- **Sole & Final Tool Call Rule**: `write_file` must be the sole and final tool call of that turn to trigger the interactive Approve / Reject buttons in Antigravity.
- **Obsidian Vault Integration**: When `agentic-project-documenting-plugin` is installed, invokes `@coding-document` to create a new topic or update an existing one in `agentic-obsidian/research/`.

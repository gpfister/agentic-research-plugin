---
name: research-catalog
description: Architecture overview and catalog for the agentic-research-plugin subagents.
enable_write_tools: false
enable_subagent_tools: false
enable_mcp_tools: false
tools:
  - read_file
  - list_dir
---

# Topic & Web Research Subagents & Architecture (`agents/agent.md`)

This document defines the subagent architecture and catalog for the **`agentic-research-plugin`**.

---

## 1. Architectural Overview

The `agentic-research-plugin` provides autonomous technical research, web intelligence gathering, documentation analysis, and evidence-backed synthesis across external knowledge bases and local repositories. It isolates research investigation into a specialized subagent (`@research`), guaranteeing that research remains non-destructive, fact-checked, cited, and reviewed before downstream usage.

### Directory Structure
```text
agents/
├── agent.md                    # Master subagent guide (this file)
└── research/                   # Autonomous Topic & Web Investigator (@research)
    └── agent.md
```

---

## 2. Subagent Catalog

| Agent Handle | Directory | `enable_write_tools` | `enable_subagent_tools` | `enable_mcp_tools` | Allowed Tools | Description |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **`@research`** | [`agents/research/`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/agents/research/) | `True` | `True` | `False` | `search_web`, `read_file`, `write_file`, `list_dir`, `ask_question`, `send_message`, `invoke_subagent` | Autonomous topic and web research investigator synthesizing findings into `research-report.md` artifacts, clarifying ambiguities with users, and indexing results in `agentic-obsidian/research/` via `@coding-document`. |

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
                                                    Archive to Obsidian Vault
                                                   (agentic-obsidian/research/)
```

### Mandatory Artifact Approval Gate
- **Location**: `<appDataDir>/brain/<conversation-id>/research-report.md`
- **Metadata**: `ArtifactMetadata={"RequestFeedback": True, "UserFacing": True, "Summary": "..."}`
- **Sole & Final Tool Call Rule**: `write_file` must be the sole and final tool call of that turn to trigger the interactive Approve / Reject buttons in Antigravity.
- **Obsidian Vault Integration**: Once approved, copies or indexes findings into `agentic-obsidian/research/<topic-slug>.md` if the vault repository is present in the workspace.

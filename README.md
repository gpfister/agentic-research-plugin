# agentic-topic-researching-plugin

Autonomous topic and web research plugin for [Google Antigravity](https://antigravity.google).

## Overview
`agentic-topic-researching-plugin` provides specialized subagents and progressive-disclosure skills to conduct systematic web investigations, multi-source literature reviews, technology comparisons, and evidence-backed synthesis. It produces structured `research-report.md` artifacts under human-in-the-loop approval and indexes findings into the shared Obsidian vault when present.

## Features
- **Declarative Subagent (`@coding-research`)**: Autonomous topic and web research investigator defined in [`agents/coding-research/agent.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/agents/coding-research/) (handle: `@coding-research`).
- **Progressive Skill (`coding-research`)**: Structured research methodologies, source credibility assessment, and iterative query refinement in [`skills/coding-research/SKILL.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/skills/coding-research/SKILL.md).
- **Evidence-Backed Synthesis**: Explicit citations, source cross-validation, and objective synthesis without speculation or hallucination.
- **Interactive Approval Gates**: Requires explicit user review for `research-report.md` artifacts via Antigravity's interactive modal before finalization.
- **Question Relay Protocol (Dual-Mode)**: Supports dual-mode research scope clarification: when delegated under a parent orchestrator (`caller_id` present), relays questions via `[QUESTION_RELAY_REQUEST]` / `[QUESTION_RELAY_RESPONSE]` through `send_message` to eliminate 60s host execution timeouts; falls back to direct `ask_question` when running standalone.
- **Obsidian Vault Integration (@coding-document)**: If `agentic-project-documenting-plugin` is installed, automatically records and links structured research briefs in `agentic-obsidian/research/` (creating a new topic or updating an existing one).

## Installation & Activation

```bash
# Enable in Antigravity session:
agy plugin enable agentic-topic-researching-plugin
```

## Contributing
See [CONTRIBUTING.md](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/CONTRIBUTING.md) for contribution guidelines and testing practices.

## License
This project is licensed under the [MIT License](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-topic-researching-plugin/LICENSE).

# agentic-research-plugin

Autonomous topic and web research plugin for [Google Antigravity](https://antigravity.google).

## Overview
`agentic-research-plugin` provides specialized subagents and progressive-disclosure skills to conduct systematic web investigations, multi-source literature reviews, technology comparisons, and evidence-backed synthesis. It produces structured `research-report.md` artifacts under human-in-the-loop approval and indexes findings into the shared Obsidian vault when present.

## Features
- **Declarative Subagent (`@coding-research`)**: Autonomous topic and web research investigator defined in [`agents/coding-research/agent.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/agents/coding-research/) (handle: `@coding-research`).
- **Progressive Skill (`coding-research`)**: Structured research methodologies, source credibility assessment, and iterative query refinement in [`skills/coding-research/SKILL.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/skills/coding-research/SKILL.md).
- **Evidence-Backed Synthesis**: Explicit citations, source cross-validation, and objective synthesis without speculation or hallucination.
- **Interactive Approval Gates**: Requires explicit user review for `research-report.md` artifacts via Antigravity's interactive modal before finalization.
- **Obsidian Vault Integration (@coding-document)**: If `agentic-document-plugin` is installed, automatically records and links structured research briefs in `agentic-obsidian/research/` (creating a new topic or updating an existing one).

## Installation & Activation

```bash
# Enable in Antigravity session:
agy plugin enable agentic-research-plugin
```

## Contributing
See [CONTRIBUTING.md](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/CONTRIBUTING.md) for contribution guidelines and testing practices.

## License
This project is licensed under the [MIT License](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/LICENSE).

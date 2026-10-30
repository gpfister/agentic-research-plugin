# Contributing to agentic-research-plugin

Thank you for contributing to **`agentic-research-plugin`**! This plugin provides autonomous topic and web research capabilities for Google Antigravity.

---

## 1. Core Guidelines
- Adhere to the standards defined in [`rules/AGENTS.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-research-plugin/rules/AGENTS.md).
- Keep subagent definitions modular, declarative, and isolated in `agents/<agent>/agent.md`.
- Skills must include valid YAML frontmatter (`name`, `description`) matching the skill directory name.
- Research agents operate in read-only and non-destructive modes; they never alter application source code or execute arbitrary destructive scripts.

---

## 2. Directory Structure

```text
agentic-research-plugin/
├── plugin.json         # Plugin manifest
├── pyproject.toml      # Project metadata & test dependencies
├── README.md           # Documentation
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # Contribution guidelines
├── agents/             # Subagent definitions
│   ├── agent.md        # Central subagent & architecture specification
│   └── coding-research/# Autonomous topic & web investigator (@coding-research)
│       └── agent.md
├── skills/             # Progressive-disclosure skills
│   └── coding-research/# Research methodology & synthesis runbooks
│       └── SKILL.md
├── rules/              # Plugin-scoped rules
│   └── AGENTS.md
└── tests/              # Test suite
    └── test_plugin.py
```

---

## 3. Testing
Run tests using `uv`:

```bash
uv run pytest
```

Or using `pytest`:

```bash
python3 -m pytest
```

Validate plugin structure with `agy`:

```bash
agy plugin validate .
```

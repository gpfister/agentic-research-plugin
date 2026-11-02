"""Tests for agentic-topic-researching-plugin structure and specifications."""

import json
from pathlib import Path
import re

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def extract_frontmatter_aliases(content: str) -> list[str]:
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return []
    fm = match.group(1)
    alias_match = re.search(r"aliases:\s*\n((?:\s*-\s+[^\n]+\n)+)", fm)
    if not alias_match:
        return []
    return [line.strip().lstrip("-").strip() for line in alias_match.group(1).strip().splitlines()]


def test_plugin_manifest_valid():
    manifest_file = PLUGIN_ROOT / "plugin.json"
    assert manifest_file.exists(), "plugin.json must exist"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("name") == "agentic-topic-researching-plugin"
    assert data.get("version") == "0.1.0"
    assert data.get("license") == "MIT"
    assert "description" in data and len(data["description"]) > 0


def test_pyproject_valid():
    pyproject_file = PLUGIN_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    content = pyproject_file.read_text(encoding="utf-8")
    assert 'name = "agentic-topic-researching-plugin"' in content
    assert 'version = "0.1.0"' in content
    assert 'requires-python = ">=3.11"' in content
    assert "pydantic>=2.10.0" in content
    assert "pytest>=8.0.0" in content


def test_license_exists():
    license_file = PLUGIN_ROOT / "LICENSE"
    assert license_file.exists(), "LICENSE must exist"
    content = license_file.read_text(encoding="utf-8")
    assert "MIT License" in content
    assert "Greg PFISTER" in content


def test_contributing_exists():
    contrib_file = PLUGIN_ROOT / "CONTRIBUTING.md"
    assert contrib_file.exists(), "CONTRIBUTING.md must exist"
    content = contrib_file.read_text(encoding="utf-8")
    assert "agentic-topic-researching-plugin" in content
    assert "pytest" in content


def test_readme_exists():
    readme_file = PLUGIN_ROOT / "README.md"
    assert readme_file.exists(), "README.md must exist"
    content = readme_file.read_text(encoding="utf-8")
    assert "agentic-topic-researching-plugin" in content
    assert "@coding-research" in content
    assert "research-report.md" in content
    assert "agentic-obsidian/research/" in content
    assert "agentic-document-plugin" in content
    assert "agentic-obsidian-plugin" not in content


def test_rules_exist():
    rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
    assert rules_file.exists(), "rules/AGENTS.md must exist"
    content = rules_file.read_text(encoding="utf-8")
    assert "Topic & Web Research Standards" in content
    assert "Evidence-Backed Synthesis" in content
    assert "Explicit Citations & Traceability" in content
    assert "Read-Only & Non-Destructive Operation" in content
    assert "Sole and Final Tool Call Rule" in content
    assert "agentic-document-plugin" in content
    assert "agentic-obsidian-plugin" not in content


def test_central_agent_guide_exists():
    central_file = PLUGIN_ROOT / "agents" / "agent.md"
    assert central_file.exists(), "agents/agent.md must exist"
    content = central_file.read_text(encoding="utf-8")
    assert "name: coding-research-catalog" in content
    assert "# Coding - Topic & Web Research Subagents & Architecture (agents/agent.md)" in content
    assert "research-report.md" in content


def test_research_agent_exists():
    agent_file = PLUGIN_ROOT / "agents" / "coding-research" / "agent.md"
    assert agent_file.exists(), "agents/coding-research/agent.md must exist"

    legacy_agent_dir = PLUGIN_ROOT / "agents" / "research"
    assert not legacy_agent_dir.exists(), "agents/research must NOT exist"

    content = agent_file.read_text(encoding="utf-8")
    assert "name: coding-research" in content
    assert "# Coding - Topic & Web Research Investigator (@coding-research)" in content
    assert "@coding-research" in content
    assert "search_web" in content
    assert "read_file" in content
    assert "write_file" in content
    assert "list_dir" in content
    assert "ask_question" in content
    assert "send_message" in content
    assert "research-report.md" in content
    assert "RequestFeedback" in content
    assert "agentic-obsidian/research/" in content

    aliases = extract_frontmatter_aliases(content)
    assert aliases, "aliases must be defined in frontmatter"
    assert "research" not in aliases, "'research' alias must be excluded"
    alias_pattern = re.compile(r"^coding(-.*)?$")
    for alias in aliases:
        assert alias_pattern.match(alias), f"Alias '{alias}' does not match pattern '^coding(-.*)?$'"


def test_research_skill_exists():
    skill_file = PLUGIN_ROOT / "skills" / "coding-research" / "SKILL.md"
    assert skill_file.exists(), "skills/coding-research/SKILL.md must exist"

    legacy_skill_dir = PLUGIN_ROOT / "skills" / "research"
    assert not legacy_skill_dir.exists(), "skills/research must NOT exist"

    content = skill_file.read_text(encoding="utf-8")
    assert "name: coding-research" in content
    assert "Topic & Web Research Investigator" in content
    assert "research-report.md" in content
    assert "agentic-obsidian/research/" in content

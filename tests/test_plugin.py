"""Tests for agentic-research-plugin structure and specifications."""

import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def test_plugin_manifest_valid():
    manifest_file = PLUGIN_ROOT / "plugin.json"
    assert manifest_file.exists(), "plugin.json must exist"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("name") == "agentic-research-plugin"
    assert data.get("version") == "0.1.0"
    assert data.get("license") == "MIT"
    assert "description" in data and len(data["description"]) > 0


def test_pyproject_valid():
    pyproject_file = PLUGIN_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    content = pyproject_file.read_text(encoding="utf-8")
    assert 'name = "agentic-research-plugin"' in content
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
    assert "agentic-research-plugin" in content
    assert "pytest" in content


def test_readme_exists():
    readme_file = PLUGIN_ROOT / "README.md"
    assert readme_file.exists(), "README.md must exist"
    content = readme_file.read_text(encoding="utf-8")
    assert "agentic-research-plugin" in content
    assert "@research" in content
    assert "research-report.md" in content
    assert "agentic-obsidian/research/" in content


def test_rules_exist():
    rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
    assert rules_file.exists(), "rules/AGENTS.md must exist"
    content = rules_file.read_text(encoding="utf-8")
    assert "Topic & Web Research Standards" in content
    assert "Evidence-Backed Synthesis" in content
    assert "Explicit Citations & Traceability" in content
    assert "Read-Only & Non-Destructive Operation" in content
    assert "Sole and Final Tool Call Rule" in content


def test_central_agent_guide_exists():
    central_file = PLUGIN_ROOT / "agents" / "agent.md"
    assert central_file.exists(), "agents/agent.md must exist"
    content = central_file.read_text(encoding="utf-8")
    assert "name: research-catalog" in content
    assert "@research" in content
    assert "research-report.md" in content


def test_research_agent_exists():
    agent_file = PLUGIN_ROOT / "agents" / "research" / "agent.md"
    assert agent_file.exists(), "agents/research/agent.md must exist"
    content = agent_file.read_text(encoding="utf-8")
    assert "name: research" in content
    assert "coding-research" in content
    assert "@research" in content
    assert "search_web" in content
    assert "read_file" in content
    assert "write_file" in content
    assert "list_dir" in content
    assert "ask_question" in content
    assert "send_message" in content
    assert "research-report.md" in content
    assert "RequestFeedback" in content
    assert "agentic-obsidian/research/" in content


def test_research_skill_exists():
    skill_file = PLUGIN_ROOT / "skills" / "research" / "SKILL.md"
    assert skill_file.exists(), "skills/research/SKILL.md must exist"
    content = skill_file.read_text(encoding="utf-8")
    assert "name: research" in content
    assert "Topic & Web Research Investigator" in content
    assert "research-report.md" in content
    assert "agentic-obsidian/research/" in content

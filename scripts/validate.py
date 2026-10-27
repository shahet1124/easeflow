#!/usr/bin/env python3
"""Check that the EaseFlow repo is consistent before it ships.

Run from the repo root:  python scripts/validate.py
Uses only the Python standard library. Exits with 1 if anything fails.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "easeflow"
PERSONA_DIR = SKILL_DIR / "personas"

PERSONA_SECTIONS = [
    "**Role in EaseFlow:**",
    "**Use when:**",
    "## Who they are",
    "## Tech context",
    "## What they want",
    "## How they behave",
    "## Gives up when",
    "## Patience budget",
    "## Watch for",
    "## Pass condition",
    "## Voice",
]
CORE_PERSONAS = ["harold.md", "literal-follower.md", "alex-power-user.md"]
SHOWCASE_KEYS = ["product", "coreWin", "date", "mode", "verdict", "summary", "metrics", "personas",
                 "currentFlow", "proposedFlow", "onboarding", "changes"]

errors = []


def fail(msg):
    errors.append(msg)


def rel(p):
    return p.relative_to(ROOT).as_posix()


def read(p):
    return p.read_text(encoding="utf-8")


def check_skill_frontmatter():
    skill = SKILL_DIR / "SKILL.md"
    if not skill.exists():
        fail("skills/easeflow/SKILL.md is missing")
        return
    m = re.match(r"^---\n(.*?)\n---\n", read(skill).replace("\r\n", "\n"), re.S)
    if not m:
        fail("SKILL.md: missing YAML frontmatter")
        return
    fields = dict(re.findall(r"^(\w[\w-]*):\s*(.*)$", m.group(1), re.M))
    name = fields.get("name", "")
    desc = fields.get("description", "")
    if name != SKILL_DIR.name:
        fail(f"SKILL.md: name '{name}' must match its folder '{SKILL_DIR.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        fail("SKILL.md: name must be lowercase letters, digits and single hyphens, at most 64 characters")
    if not 1 <= len(desc) <= 1024:
        fail(f"SKILL.md: description is {len(desc)} characters; it must be 1-1024")


def check_referenced_files():
    """Every references/, personas/ or assets/ path mentioned in the skill must exist."""
    pattern = re.compile(r"`((?:references|personas|assets)/[\w./-]+\.(?:md|html|json))`")
    for doc in [SKILL_DIR / "SKILL.md", *sorted((SKILL_DIR / "references").glob("*.md"))]:
        for path in set(pattern.findall(read(doc))):
            if not (SKILL_DIR / path).exists():
                fail(f"{rel(doc)}: refers to {path}, which doesn't exist")


def check_personas():
    readme = read(ROOT / "README.md")
    files = sorted(PERSONA_DIR.glob("*.md"))
    names = [f.name for f in files]
    for core in CORE_PERSONAS:
        if core not in names:
            fail(f"core persona personas/{core} is missing")
    for f in files:
        if f.name == "_template.md":
            continue
        text = read(f)
        for section in PERSONA_SECTIONS:
            if section not in text:
                fail(f"{rel(f)}: missing section '{section}'")
        title = re.search(r"^# (?:The )?([A-Z][\w-]*)", text, re.M)
        if not title:
            fail(f"{rel(f)}: first line must be '# <Name>, ...'")
        elif title.group(1) not in readme:
            fail(f"{rel(f)}: persona '{title.group(1)}' isn't listed in README.md")
        if not re.fullmatch(r"[a-z]+(-[a-z]+)*\.md", f.name):
            fail(f"{rel(f)}: file names must be lowercase words joined by hyphens")


def check_rules():
    text = read(SKILL_DIR / "references" / "simplification-rules.md")
    numbers = [int(n) for n in re.findall(r"^\*\*R(\d+)\.", text, re.M)]
    if numbers != list(range(1, len(numbers) + 1)):
        fail(f"simplification-rules.md: rules must be numbered R1..R{len(numbers)} in order, found {numbers}")


def check_manifests():
    try:
        plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
    except (OSError, json.JSONDecodeError) as e:
        fail(f".claude-plugin: {e}")
        return
    if plugin.get("name") != "easeflow":
        fail("plugin.json: name must be 'easeflow'")
    if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
        fail("plugin.json: version must look like 1.2.3")
    entries = [p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
    if not entries:
        fail("marketplace.json: no plugin entry named like plugin.json")
    elif entries[0].get("version") != plugin.get("version"):
        fail("marketplace.json: plugin version doesn't match plugin.json")
    changelog = read(ROOT / "CHANGELOG.md")
    if f"## [{plugin.get('version')}]" not in changelog:
        fail(f"CHANGELOG.md: no section for version {plugin.get('version')}")


def check_showcase():
    path = SKILL_DIR / "assets" / "showcase-template.html"
    m = re.search(r'<script type="application/json" id="easeflow-data">(.*?)</script>', read(path), re.S)
    if not m:
        fail(f"{rel(path)}: missing the easeflow-data JSON block")
        return
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        fail(f"{rel(path)}: example data isn't valid JSON ({e})")
        return
    for key in SHOWCASE_KEYS:
        if key not in data:
            fail(f"{rel(path)}: example data is missing '{key}'")
    cov = data.get("coverage")
    if cov and sum(level["count"] for level in cov.get("levels", [])) != cov.get("total"):
        fail(f"{rel(path)}: coverage levels don't add up to coverage.total")


def check_prototype():
    text = read(SKILL_DIR / "assets" / "prototype-skeleton.html")
    for marker in ['class="screen"', "data-onboarding", "data-toggle-advanced", 'class="more"', "REPLACE FROM HERE"]:
        if marker not in text:
            fail(f"prototype-skeleton.html: expected marker '{marker}' is missing")


def check_no_reports():
    for p in ROOT.rglob("easeflow-report"):
        if ".git" not in p.parts:
            fail(f"{rel(p)}: run output must not be committed")


def main():
    for check in [check_skill_frontmatter, check_referenced_files, check_personas, check_rules,
                  check_manifests, check_showcase, check_prototype, check_no_reports]:
        check()
    if errors:
        print(f"✗ {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("✓ EaseFlow repo is consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())

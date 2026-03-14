#!/usr/bin/env python3
"""Validate publishable skills in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    content = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        raise ValueError("missing valid YAML frontmatter")

    frontmatter: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in frontmatter:
            raise ValueError(f"duplicate frontmatter key: {key}")
        frontmatter[key] = value
    return frontmatter


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    if not skill_md.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]
    if not openai_yaml.is_file():
        errors.append(f"{skill_dir.name}: missing agents/openai.yaml")

    try:
        frontmatter = parse_frontmatter(skill_md)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]

    allowed_keys = {"name", "description"}
    actual_keys = set(frontmatter)
    if actual_keys != allowed_keys:
        errors.append(
            f"{skill_dir.name}: frontmatter keys must be exactly {sorted(allowed_keys)}, got {sorted(actual_keys)}"
        )

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not NAME_RE.fullmatch(name):
        errors.append(f"{skill_dir.name}: invalid skill name '{name}'")
    if name and name != skill_dir.name:
        errors.append(
            f"{skill_dir.name}: frontmatter name '{name}' does not match directory name"
        )
    if not description:
        errors.append(f"{skill_dir.name}: description must not be empty")

    if openai_yaml.is_file():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        for required_text in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if required_text not in yaml_text:
                errors.append(f"{skill_dir.name}: agents/openai.yaml missing '{required_text}'")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("skills directory not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("no skills found", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    if all_errors:
        for error in all_errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

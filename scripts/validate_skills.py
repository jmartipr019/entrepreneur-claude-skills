#!/usr/bin/env python3
"""Check that .claude-plugin/manifest.json agrees with the skills on disk.

Catches the two ways this repo can silently drift:
  - a manifest entry whose path does not exist (install resolves to nothing)
  - a SKILL.md on disk that no manifest entry points at (skill never loads)

Also validates that each SKILL.md carries parseable YAML frontmatter with a name.
"""

import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "manifest.json"
SKILLS_DIR = ROOT / "skills"

errors = []


def frontmatter(path):
    """Return the parsed YAML frontmatter block, or raise ValueError."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing opening '---' frontmatter delimiter")
    _, _, rest = text.partition("---")
    block, delim, _ = rest.partition("\n---")
    if not delim:
        raise ValueError("missing closing '---' frontmatter delimiter")
    data = yaml.safe_load(block)
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a YAML mapping")
    return data


manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
declared = {entry["path"] for entry in manifest["skills"]}
found = {
    p.relative_to(ROOT).as_posix() for p in SKILLS_DIR.rglob("SKILL.md")
}

for path in sorted(declared - found):
    errors.append(f"manifest points at a file that does not exist: {path}")

for path in sorted(found - declared):
    errors.append(f"SKILL.md on disk is not registered in the manifest: {path}")

for entry in manifest["skills"]:
    path = ROOT / entry["path"]
    if not path.exists():
        continue
    try:
        data = frontmatter(path)
    except (ValueError, yaml.YAMLError) as exc:
        errors.append(f"{entry['path']}: bad frontmatter ({exc})")
        continue
    if not data.get("name"):
        errors.append(f"{entry['path']}: frontmatter has no 'name'")

if errors:
    print(f"{len(errors)} problem(s) found:\n", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)
    sys.exit(1)

print(f"OK — {len(manifest['skills'])} skills registered, all paths resolve.")

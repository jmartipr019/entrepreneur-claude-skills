# Entrepreneur Claude Skills

This repository contains production-ready skill packages for Claude Code focused on entrepreneurship. Skills are organized by category under `skills/` and follow a consistent SKILL.md format with YAML frontmatter.

## Skill Activation

When a user's request matches a skill's `activation_triggers`, load the corresponding SKILL.md and follow its workflow. Skills provide structured frameworks — not just prompts — for common entrepreneurship tasks.

## Structure

- `skills/` — All skill packages organized by category
- `docs/` — Installation guides, contributing guidelines, skill format spec
- Each skill contains a `SKILL.md` (YAML frontmatter + workflow). Skills may add
  supporting files when needed — `marketing-growth/MetaAds` adds `tools/` and
  `workflows/`; the other 24 are a single `SKILL.md` each.

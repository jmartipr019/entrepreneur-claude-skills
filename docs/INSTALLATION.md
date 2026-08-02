# Installation Guide

## Quick Install

### Claude Code Plugin (Recommended)

```bash
/plugin marketplace add mfwarren/entrepreneur-claude-skills
```

This installs all 25 skills and keeps them updated.

### npx Skills CLI

```bash
npx skills add mfwarren/entrepreneur-claude-skills
```

### Individual Skills

Don't need the whole collection? Install just what you use:

```bash
npx skills add mfwarren/entrepreneur-claude-skills --skill copywriting
npx skills add mfwarren/entrepreneur-claude-skills --skill unit-economics
npx skills add mfwarren/entrepreneur-claude-skills --skill offer-creation
```

## Other Agents

### Universal Installer (Cursor, Windsurf, VS Code + Copilot, etc.)

```bash
npx ai-agent-skills install mfwarren/entrepreneur-claude-skills
```

The universal installer auto-detects your agent and places skills in the correct directory.

### Manual Install

```bash
git clone https://github.com/mfwarren/entrepreneur-claude-skills.git
```

Then copy the `skills/` folder contents to your agent's skill directory:

| Agent | Skill Directory |
|-------|----------------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `.cursor/skills/` |
| Windsurf | `.windsurf/skills/` |
| VS Code + Copilot | `.github/copilot-skills/` |

### Git Submodule (For Projects)

Track skills as a dependency in your project:

```bash
git submodule add https://github.com/mfwarren/entrepreneur-claude-skills.git .claude/skills/entrepreneur
```

Update to latest:

```bash
git submodule update --remote
```

## Verifying Installation

After installing, test with:

```
You: "Write a cold email sequence for my B2B SaaS"
```

If the cold-outreach skill activates and asks you structured questions about your product, ICP, and offer — you're set.

## Troubleshooting

**Skills not activating?**
- Ensure SKILL.md files are in the correct directory for your agent
- Restart your agent/editor after installation
- Check that the skill's `activation_triggers` match your request

**Permission errors on install?**
- Try with `sudo` (Linux/Mac) or run terminal as admin (Windows)
- Or use the manual clone method instead

**Want to uninstall?**
- Remove the skill folders from your agent's skill directory
- Or run `npx skills remove mfwarren/entrepreneur-claude-skills`

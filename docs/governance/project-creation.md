# Project Initialization Governance

This document codifies the mandatory standards for initializing any project within the JLDN ecosystem.

## 1. Universal `.gitignore` Standard

All JLDN projects must utilize an aggressive default `.gitignore` that blackholes all hidden files (`.*/`), enforcing strict explicit whitelisting for infrastructure. 

```gitignore
.DS_Store
.*/

# Exceptions
!.dev/
!.github/
```

### Explanation of Rules
- **`.agents/` (Blackholed):** The `.agents/` directory is strictly reserved for local AI agent workspaces, temporary scratch scripts, and local LLM system prompts (`AGENTS.md`). It must **never** be tracked by Git or pushed to a public repository.
- **`.secrets/` (Blackholed):** Any API keys, `.env` files, or AI automation credentials must be stored in the `.secrets/` directory (or `.env`), which is automatically blackholed by the `.*/` default.
- **`.dev/` (Whitelisted):** The `.dev/` directory is the core of the JLDN Generational Versioning Schema and Backlog system. It must be explicitly whitelisted to ensure tasks and roadmaps are version-controlled.
- **`.github/` (Whitelisted):** The `.github/` directory is mandatory for CI/CD actions, issue templates, and governance files (Code of Conduct, Security, Funding).

## 2. Mandatory Root Files

Every project must include the following root-level files:
- `README.md` (containing JLDN Frontmatter Metadata)
- `CHANGELOG.md`
- `LICENSE`
- `CLAUDE.md` (A simple pointer file directing AI agents to read the local `.agents/AGENTS.md`)
- `.editorconfig`, `.aiexclude`, `.aiignore`

*Failure to include these files will result in a failed audit.*

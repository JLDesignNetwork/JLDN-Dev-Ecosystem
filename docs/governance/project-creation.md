---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "Project Initialization Governance",
    "type": "governance",
    "platform": "github:public",
    "version": "2608.1.0-bs"
  },
  "backlog": ".dev/backlog.json",
  "changelog": "CHANGELOG.md"
}
---

# Project Initialization Governance

This document codifies the mandatory standards for initializing any project within the JLDN ecosystem.

## 1. Universal `.gitignore` Standard

All JLDN projects must utilize an aggressive default `.gitignore` that blackholes all hidden and temporary directories (`[._]*/`), enforcing strict explicit whitelisting for infrastructure. 

```gitignore
.DS_Store
[._]*/

# Exceptions
!.dev/
!.github/
```

### Explanation of Rules
- **`.agents/` & Temporary Folders (Blackholed):** The `.agents/` directory is strictly reserved for local AI workspaces. Temporary build folders typically begin with an underscore (e.g. `_site/`). The `[._]*/` rule automatically blackholes all directories starting with a dot or underscore.
- **`.secrets/` (Blackholed):** Any API keys or credentials must be stored in the `.secrets/` directory (or `.env`), which is automatically blackholed by the `[._]*/` default.
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

## 3. Mandatory Local Directories (Blackholed)

The following directories must be manually scaffolded by the developer/agent locally, as they are intentionally blackholed from Git via the `[._]*/` rule:
- **`.secrets/`**: Must contain `eco-config.json` to define remote variables, authentication tokens, and CI constraints (see `remote-configuration.md`).
- **`.agents/rules/`**: Must be created to hold any repository-specific behavioral markdown rules for automation tooling.
## 4. GitHub Remote Governance

All repositories must be initialized with strict remote configurations via the GitHub API to ensure operational security and clean workflow management.

- **Private Vulnerability Reporting:** Must be explicitly enabled to allow users to securely disclose security flaws without public exposure. 
  - *Command:* `gh api -X PUT /repos/JLDesignNetwork/[ProjectName]/private-vulnerability-reporting`

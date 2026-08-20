# JLDN Dev Ecosystem Roadmap

This roadmap codifies the strategic phases required to fully build out the JLDN Dev Ecosystem as the definitive "Single Source of Truth" for all project scaffolding, governance, metadata, and lifecycle protocols.

---

### [Phase 1] Project Initialization & Scaffolding (Status: Complete)
- **The 5-Step Guided Wizard:** Documenting the interactive prompt sequence for new projects (Identity, Storage Routing, Archetypes, GVS Epoch, and Git Remotes).
- **Mandatory Scaffolding:** Codifying the Universal Baseline directory structure and the exact baseline files required (`CLAUDE.md`, `.dev/`, `.github/`, `.gitignore`, etc.).

### [Phase 2] Repository & Git Governance (Status: Complete)
- **Repository Creation Rules:** Documenting the GitLab (Live apps) vs GitHub (Docs/Tooling) routing policy and visibility defaults.
- **Gitignore Standards:** Enforcing the `[._]*/` directory-only pattern and `.agents/` / `.secrets/` isolation.
- **Remote Configuration:** Codifying branch protection, Private Vulnerability Reporting enablement via GitHub API, and issue template requirements.

### [Phase 3] Metadata & Frontmatter Standards (Status: Complete)
- **JLDN Frontmatter Schema:** Defining the Universal Polymorphic JSON Schema block (`author`, `platform`, `type`, `version`, `backlog`) required in all primary Markdown documents.
- **Inter-file Routing:** Documenting how frontmatter dynamically points to the active `backlog.json` and syncs epochs with `CHANGELOG.md`.

### [Phase 4] Workflow & Backlog Schema (Status: Pending)
- **Task Taxonomies:** Documenting universal `ROOT` domains vs generational `[GEN]` domains.
- **The 11-State Lifecycle:** Documenting the exact task flow from `pending` to `completed:protected` or `deprecated`, and how tasks map to specific localized `target_files` tracking.
- **Devil's Advocate Protocol:** Codifying the mandatory AI agent stress-test requirements prior to executing structural code changes.

### [Phase 5] Versioning, Git Protocol, & Releases (Status: Pending)
- **Generational Version Schema (GVS):** Formally documenting epoch calculations (`[YYMM].[SUB].[REV]-[TAG]`).
- **Direct-to-Main Workflows:** Documenting trunk-based development constraints (no feature branches unless specified).
- **Taxonomy Dual-Commit Protocol:** Formalizing the standard `Fix [DOMAIN]-TODO-XX: [...]` vs Conventional Commits (`feat:`, `fix:`) syntax.
- **Changelog Automation:** Codifying how tasks synchronize with `CHANGELOG.md` upon `"Housekeeping"` or `"Goodnight"` routines.

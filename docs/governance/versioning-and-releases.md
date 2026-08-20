# JLDN Versioning, Git Protocol & Releases

The JLDN ecosystem relies on strict versioning and branching schemas to maintain absolute traceability from ideation down to atomic commits.

## 1. Generational Versioning Schema (GVS)
JLDN projects do not use standard SemVer. Instead, we use the **Generational Versioning Schema (GVS)**.
- **Format:** `[YYMM].[SUBVERSION].[REVISION]-[TAG]` (e.g., `2606.1.0-bs`).
- **Validation Regex:** `^(\d{2}(?:0[1-9]|1[0-2]))\.(\d+)\.(\d+)-(a|as|b|bs|l|s|ts|z)$`

### Version Bumping Rules
- **Subversion Bumps (`.0`):** Triggered on any new codified mechanic, rule expansion, feature release, or registered audit finding. **Requires an annotated Git Tag AND a published GitHub/GitLab Release.**
- **Revision Bumps (`> 0`):** Triggered on minor non-mechanical fixes, typo corrections, or formatting tweaks. **Requires an annotated Git Tag ONLY (no GitHub/GitLab release).**

### Tag Transitions (Lifecycles)
| Phase | Tag | Meaning & Support Status |
| :--- | :---: | :--- |
| **Alpha (Internal)** | `-a` | **Genesis Build:** The first testable build, kept strictly in-house. No external support. |
| **Alpha (Public)** | `-as` | **Genesis Build:** Released for early external/live testing. Actively supported. |
| **Beta (Internal)** | `-b` | **Crucible Build:** Feature complete, focused on bug hunting, but kept in-house. No external support. |
| **Beta (Public)** | `-bs` | **Crucible Build:** Released for wider real-world testing. Supported. |
| **Lambda** | `-l` | **The Lock (RC):** Release Candidate. Code freeze active. Under review, no support yet. |
| **Stable** | `-s` | **Production:** The official, stable production release. Fully supported. |
| **Theta** | `-ts` | **Twilight:** Deprecation warning. Users are encouraged to migrate, but the version is still supported. |
| **Zeta** | `-z` | **Zero-Hour (EOL):** End of Life. The final update the software will ever receive. Completely unsupported. |

## 2. Trunk-Based Development (Direct-to-Main)
- **Direct-to-Main Protocol:** Always iterate, commit, and push directly to the `main` branch across all projects. Do not generate feature branches, draft PRs, or PR templates unless explicitly required by a specific integration.
- **Atomic Operations:** Always commit tracked changes and their corresponding `backlog.json` or `todo.json` updates together in the same atomic commit.

## 3. Taxonomy Dual-Commit Protocol
Commits must be context-aware based on whether they resolve a tracked backlog task or if they are general software commits.

**Backlog & Task Commits (Taxonomy Format):**
When resolving an item from `.dev/[GEN]/backlog.json`:
- **Task Implementation:** `Fix [DOMAIN]-TODO-XX: [Short description of codified change]`
- **Quality Audits:** `[DOCS-TODO-XX] Red Team Audit: [Document Name] — [N] findings registered`
- **Issue Fixes:** `Fix [DOMAIN]-ISSUE-XX: [Short description of fix]`

**General Software Commits (Conventional Format):**
For changes not explicitly tracked in the backlog:
- `feat: [description]`
- `fix: [description]`
- `docs: [description]`
- `chore: [description]`

## 4. Changelog Automation & Releases
Release publishing and `CHANGELOG.md` generation is automated via the `jldn-cleanup` (Housekeeping) and `jldn-done` (Goodnight) Agent skills.
When triggered, these skills will automatically:
1. Audit newly resolved tasks in `backlog.json`.
2. Append them to `CHANGELOG.md` using the "Keep a Changelog" standard (`## [GVS] - YYYY-MM-DD`).
3. If a new GVS version was established, they will automatically tag and publish the formal GitHub/GitLab release.

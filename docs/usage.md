---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "Workflow & Lifecycle Governance",
    "type": "governance",
    "platform": "github:public",
    "version": "2608.1.0-bs"
  },
  "backlog": ".dev/backlog.json",
  "changelog": "CHANGELOG.md"
}
---

# Workflow & Lifecycle Governance

> **Document:** `docs/usage.md`  
> **Author:** JLDN  
> **Standard:** Workflow & Backlog Execution  

This document dictates exactly how human developers and AI automation agents flow through the JLDN ecosystem. It defines how we categorize work, how a task transitions from ideation to completion, and the rigorous safeguards (Devil's Advocate) required before executing structural code.

---

## 1. Task Taxonomies & Routing (ROOT vs GEN)

To prevent massive repositories from collapsing under their own weight, the JLDN ecosystem splits the backlog into two distinct routing paradigms.

### A. Root Domains (`ROOT`, `DOCS`)
Tasks belonging to the `ROOT` or `DOCS` domains are permanent infrastructure tasks. They manage CI/CD pipelines, global wiki architectures, and the `.dev/` ecosystem itself. 
- **Routing Location:** `[Repository Root]/.dev/backlog.json`
- **Example ID:** `ROOT-TODO-01`

### B. Generational Domains (e.g., `AUTH`, `COMB`)
Tasks belonging to specific feature-sets or architectural pillars for a specific release generation. Developers define these domains (3-5 uppercase letters).
- **Routing Location:** `[Repository Root]/.dev/[GEN]/backlog.json` (e.g., `.dev/2608/backlog.json`)
- **Example ID:** `AUTH-TODO-14`

---

## 2. The 11-State Task Lifecycle

Tasks do not simply go from "open" to "closed." They follow a strict verification pipeline.

| State | Description | Next Steps |
| :--- | :--- | :--- |
| `pending` | Task is logged but untouched. | Move to `in-progress` when starting work. |
| `in-progress` | Active development is occurring. | Move to `pending:audit` or `pending:review` upon completion. |
| `pending:audit` | Code is written, waiting for test-suite / mechanical verification. | Move to `in-progress:audit`. |
| `in-progress:audit` | The Red/Yellow/White Team is actively breaking the code. | Return to `in-progress` if failed, or `completed` if passed. |
| `pending:refactor` | Code works but needs structural optimization. | Move to `in-progress:refactor`. |
| `in-progress:refactor`| Refactoring is actively underway. | Move to `pending:audit` for re-verification. |
| `completed` | Task is resolved, tested, and pushed to `main`. | Assign `"protection"` state. |
| `blocked` | Task cannot proceed due to a dependency or user input. | Add `reason` and `blocked_since` tag. |
| `deprecated` | Task is no longer relevant or was cancelled. | Leave in backlog for historical record. |

### The `target_files` Array (Mandatory Agent Sandboxing)
Because JLDN enforces Direct-to-Main branching (no PRs, no feature branches), AI agents must be explicitly sandboxed to prevent them from wandering across the codebase.
- **Rule:** When an agent accepts an `in-progress` task, it MUST explicitly reference the `"target_files": []` array in the JSON schema. The agent is strictly prohibited from modifying structural files outside of this array unless it formally asks the user for permission.

---

## 3. The Devil's Advocate Protocol

To prevent AI automation (or overly-confident developers) from making catastrophic structural errors, the ecosystem enforces the **Devil's Advocate Protocol**.

### The Triggers
This protocol automatically engages whenever:
1. The user utilizes the keyword `propose` (e.g., "I propose we change the database schema to X...").
2. An AI agent realizes its next step requires a sweeping mechanical change, architectural refactor, or destructive data edit.

### The Protocol (Halt & Stress-Test)
Before any code is modified, the agent MUST halt execution and present a formal Devil's Advocate analysis containing:
1. **Edge-Case Evaluation:** How could this new structure fail?
2. **Regression Risk:** What existing features might this break?
3. **Exploit Assessment:** Does this introduce a vulnerability (e.g. XSS, Race Condition)?
4. **Trade-offs:** What is the alternative?

Only after the user explicitly reviews this analysis and grants authorization (`Hit Proceed`) may the agent execute the structural edits.

---

## 4. Automation Triggers (Backlog Mechanics)

The JLDN ecosystem relies on formalized command triggers to keep the backlog pristine.

### `"Housekeeping"`
This command triggers a mid-session audit. The agent will:
1. Scan `.dev/[GEN]/backlog.json` for recently `completed` tasks.
2. Ensure the `created_at`, `existed_since`, and `protection` tags are perfectly formatted.
3. Purge all ephemeral scripts or leftover scratch files from `.agents/scratch/`.

### `"Goodnight"`
This command triggers the end-of-session shutdown. The agent will:
1. Execute a full `"Housekeeping"` pass.
2. **Generate the Handoff Document:** Write a 4-part summary of what was accomplished and what remains to be done.
   - *Note on Handoff Routing:* Depending on the `handoff_sync` boolean in `.dev/config.json`, this document will either remain locked in `.agents/handoff.md` (local only) or be copied to `.dev/handoff.md` for git-synchronization across workstations.

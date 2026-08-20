# JLDN Backlog Schema Specification

> **Document:** `docs/specification.md`  
> **Author:** Jeff Langdon (JL Design Network)  
> **Standard:** JLDN Task & Backlog Management Protocol  
> **Version:** `2608.21.0-bs`  

---

## 1. Architectural Philosophy

The **JLDN Backlog Schema** adheres to five core design principles:

1. **Document & Repository-Bound Isolation:** Task datasets reside either in document JSON frontmatter or dedicated generational companion hubs (`.dev/[GEN]/backlog.json`). Tasks maintain clean scope and cross-reference lineage without external file corruption.
2. **Phase-Aware Lifecycle Tracking:** Every task progresses through explicit developmental phases using a standardized `[STATE]:[PHASE]` colon-delimited syntax.
3. **Machine-Readable Structure:** Tasks are stored as strictly validated JSON objects, allowing automated build pipelines, static analysis scripts, and LLM coding agents to parse, execute, and verify tasks programmatically.
4. **Empty Array Validity:** The task array key MUST be a valid JSON array. An empty array (`[]`) is valid and indicates zero active or historical tasks.
5. **Strict JSON Formatting Standard:** Backlog JSON MUST be valid, UTF-8 encoded JSON formatted with exactly 2-space indentation and no tab characters.

---

## 2. Storage Architecture & Storage Modes

### Mode 1: Embedded Inline Frontmatter
For standalone specification documents, tasks reside directly within the `todo` array in the Markdown document's frontmatter header (`---` block).

### Mode 2: Companion Dataset Storage Pattern (The JLDN Standard)
For large rulesets and software repositories, tasks are stored in companion JSON datasets within the Generational Development Hub:
- Root Project Backlog: `.dev/backlog.json`
- Generation Master Task Register: `.dev/[GEN]/backlog.json`
- Generation Conceptual Proposals: `.dev/[GEN]/ideas.json`

---

## 3. Unified `[DOMAIN]-[KIND]-[NN]` Taxonomy

Every task adheres to the standard prefix taxonomy:
- **Domains:** Must be 3-5 uppercase alphanumeric characters. Must never match a `Kind`.
  - `ROOT` → Universal: Project-level milestones, CI/CD, and repository infrastructure.
  - `DOCS` → Universal: Internal `docs/` wiki rules, mechanics, and documentation.
  - *Custom Domains:* Developers must define 3-5 character custom domains for their project's internal architecture or generational scope (e.g. `AUTH`, `COMB`, `G08`).
- **Kinds:**
  - `TODO` → Actionable engineering and writing tasks.
  - `IDEA` → Conceptual proposals and architectural designs.
  - `ISSUE` → Tracked defects, regressions, and security advisories.

---

## 4. Task Object Schema Structure

```json
{
  "id": "ROOT-TODO-01",
  "title": "Short Concise Task Title",
  "status": "in-progress:audit",
  "priority": "high-1",
  "protection": "protected",
  "existed_since": "2608.1.0-s",
  "details": "Detailed description of the mechanical, technical, or architectural work required.",
  "created_at": "2026-08-03T12:00:00+02:00",
  "owner": "Agent-Alpha/Jeff",
  "reason": "Explanation required whenever status is blocked or deprecated.",
  "child_of": "ROOT-TODO-00",
  "prerequisite": "ROOT-TODO-00.1a",
  "relates_to": "ROOT-TODO-00",
  "target_files": [
    "docs/specification.md",
    "CHANGELOG.md"
  ]
}
```

### Property Definitions
* **`id` (String, Required):** Standard taxonomy string (`[DOMAIN]-[KIND]-[NN]` or legacy `TODO-[NN]`). Scalable up to 4 digits (`\d{2,4}`). Supports single-letter sub-tasks (`.1a` to `.1z`).
* **`title` (String, Required):** Short imperative summary (minimum 5 characters).
* **`status` (String, Required):** Valid lifecycle state slug matching the 11-state matrix.
* **`priority` (String, Required):** Granular 3-tier sub-priority (`critical-1` to `low-3`) or legacy tier (`critical`, `high`, `medium`, `low`).
* **`details` (String, Required):** Technical requirements description (minimum 15 characters).
* **`created_at` (String, Required):** ISO-8601 UTC/local timestamp string (e.g. `2026-08-18T16:45:00+02:00`).
* **`existed_since` (String, Mandatory on Creation):** GVS version tag of origin (`[YYMM].[SUBVERSION].[REVISION]-[TAG]`).
* **`blocked_since` / `deprecated_since` (String, Conditional):** Mandatory when status transitions to `blocked` or `deprecated`.
* **`protection` (String, Completed Tasks):** `"protected"` (locked system element) or `"open"`.
* **`child_of` (String, Optional):** Direct vertical parent task ID establishing a strict DAG.
* **`prerequisite` (String, Optional):** Prerequisite task ID that must reach terminal state before activation.
* **`relates_to` (String, Optional):** Horizontal context association.
* **`target_files` (Array of Strings, Optional):** Localized file tracking for isolated environments without git dependency.
* **`target_version` / `target_component` / `target_repository` (String, Optional):** Optional pointers to eliminate cross-project reference ambiguity.

---

## 5. Formalized 11-State Lifecycle Matrix

| Phase / Group | Status Slug | Definition & Usage Guidelines |
| :--- | :---: | :--- |
| **1. Initial Work** | `pending` | Task created; initial work has not started. |
| | `in-progress` | Task is undergoing initial development. |
| **2. Surface Review** | `pending:review` | Initial implementation complete; queued for surface review. |
| | `in-progress:review` | Undergoing surface formatting and presentation review. |
| **3. Deep Mechanical Audit** | `pending:audit` | Draft complete; queued for deep mechanical/adversarial audit. |
| | `in-progress:audit` | Active Red Team auditing and loophole analysis underway. |
| **4. Architectural Refactoring** | `pending:refactor` | Flagged after audit for structural refactoring. |
| | `in-progress:refactor` | Active structural refactoring underway. |
| **5. Control & Terminal** | `completed` | **Done & Verified (Immutable):** Finished and locked. |
| | `blocked` | Work stuck due to external dependency. |
| | `deprecated` | Obsolete or cancelled task. |

---

## 6. Validation Regular Expressions

- **Status:** `^(pending|in-progress|pending:review|in-progress:review|pending:audit|in-progress:audit|pending:refactor|in-progress:refactor|completed|blocked|deprecated)$`
- **Priority:** `^(critical|high|medium|low)(-[1-3])?$`
- **Protection:** `^(protected|open)$`
- **Taxonomy ID:** `^([A-Z0-9]{3,5}-(TODO|IDEA|ISSUE)-\d{2,4}|TODO-\d{2,4})(\.\d+[a-z])?$`
- **GVS Version:** `^\d{4}\.\d+\.\d+-(a|as|b|bs|l|s|ts|z)$`

# JLDN Backlog Schema Usage & Implementation Guide

> **Document:** `docs/usage.md`  
> **Author:** Jeff Langdon (JL Design Network)  
> **Standard:** Implementation Patterns  

---

## 1. Setting Up Mode 2 Generational Backlogs (Recommended)

To implement the JLDN Backlog Schema in a repository, create the standard `.dev/` directory tree:

```
[Repository Root]/
├── .dev/
│   ├── ROADMAP.md               # Multi-generational strategic roadmap
│   ├── backlog.json             # Root project-level backlog
│   └── [GEN]/                   # Active Generation Hub (e.g. 2608)
│       ├── backlog.json         # Unified Generation master register
│       └── ideas.json           # Generation proposals
```

### Initializing `.dev/[GEN]/backlog.json`
```json
[
  {
    "id": "PROJ-TODO-01",
    "title": "Scaffold Initial Application Architecture",
    "status": "completed",
    "priority": "critical-1",
    "protection": "protected",
    "existed_since": "2608.1.0-as",
    "created_at": "2026-08-18T12:00:00+02:00",
    "details": "Scaffolded project baseline adhering to JLDN Gold Standard."
  }
]
```

---

## 2. Managing Task Lifecycles

### Advancing a Task
1. Set status to `in-progress` when starting work.
2. Advance through `pending:audit` $\rightarrow$ `in-progress:audit` for mechanical verification.
3. Advance to `completed` upon passing all tests.
4. Set `"protection": "protected"` if the item represents an immutable architectural pillar.

### Recovering from Blocked Status
- If external input is needed, set status to `blocked`, add `"reason": "Awaiting user confirmation on X"`, and record `"blocked_since": "2608.X.Y-tag"`.
- When resolved, remove `blocked_since` and return to `in-progress`.

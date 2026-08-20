# JLDN Backlog Schema Knowledge Base & Documentation Wiki

> **Project:** JLDN Backlog Schema  
> **Generation Epoch:** `2608.18.0-as`  
> **Status:** Active Standard  
> **Author:** Jeff Langdon (JL Design Network)  

Welcome to the official documentation and specification hub for the **JLDN Backlog Schema**, the standardized, document-bound and repository-bound task management protocol for all JLDN software, technical specifications, and game rulesets.

---

## 📚 Documentation Index

| Document | Description | Target |
| :--- | :--- | :--- |
| **Backlog Schema Specification** | Full technical specification: 11-state matrix, DAG relationships, taxonomy prefixes, and validation regexes. | [Specification](specification.md) |
| **Usage & Implementation Guide** | Mode 1 (Embedded Inline Frontmatter) and Mode 2 (Generational `.dev/` Hub) integration patterns. | [Usage Guide](usage.md) |
| **Strategic Roadmap** | Master generational vision and future automated tooling roadmap. | [Roadmap](../.dev/ROADMAP.md) |
| **Release History** | Chronological specification changelog following GVS. | [Changelog](../CHANGELOG.md) |

---

## 🎯 Architecture Overview

```
                                JLDN BACKLOG TAXONOMY
               ┌────────────────────────────────────────────────────────┐
               │              ([DOMAIN]-[TYPE]-[NN]) Taxonomy           │
               ├──────────────┬──────────────────────────┬──────────────┤
               │   DOMAINS    │          TYPES           │    STATES    │
               │   PROJ       │          TODO            │  11 States   │
               │   DOCS       │          IDEA            │  (DAG Flow)  │
               │   BOOK       │          ISSUE           │  3 Terminal  │
               │   WEB / EXT  │                          │              │
               └──────────────┴──────────────────────────┴──────────────┘
```

The schema establishes mathematical guarantees:
- **Acyclic Dependency DAGs:** Prerequisite chains and vertical ancestry (`child_of`) strictly prohibit circular loops.
- **Auditable Lifecycle Traceability:** Conditionally mandatory version origin tags (`existed_since`, `blocked_since`, `deprecated_since`).
- **Architectural Preservation:** Lock completed core mechanics via `"protection": "protected"`.

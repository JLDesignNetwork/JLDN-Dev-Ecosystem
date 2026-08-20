---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "JLDN Frontmatter Schema",
    "type": "schema",
    "platform": "github:public",
    "version": "2608.1.0-bs"
  },
  "backlog": ".dev/backlog.json",
  "changelog": "CHANGELOG.md"
}
---

# JLDN Frontmatter Schema Specification

> **Document:** `docs/metadata/frontmatter-schema.md`  
> **Author:** JLDN  
> **Standard:** The Universal Polymorphic JSON Schema  

---

## 1. Architectural Philosophy

The JLDN Frontmatter Schema strictly utilizes the **Universal Polymorphic JSON Schema**, heavily inspired by Kubernetes architecture. 

It guarantees:
1. **100% Parser Uniformity:** Automation scripts always know exactly where to find metadata without conditional parsing logic.
2. **Zero Magic Strings:** Routing intent is dictated natively by strict JSON types (String vs Array vs Null).
3. **Guaranteed Readability:** Massive arrays of embedded data are permanently sandboxed away from the core identity keys.

---

## 2. The Required Structure

The frontmatter MUST be enclosed in `---` delimiters at the very top of the markdown file and must be strictly valid JSON.

### A. The `"metadata"` Sandbox
The core identity keys must always be wrapped inside the `"metadata"` object.

| Key | Type | Description |
| :--- | :--- | :--- |
| `"author"` | `String` | The developer or organization (e.g., `"Jeff Langdon"`). |
| `"projectName"` | `String` | The human-readable title of the document or project. |
| `"type"` | `String` | The archetype (e.g., `"ruleset"`, `"governance"`, `"documentation"`, `"schema"`). |
| `"platform"` | `String` | Concatenated host and visibility (e.g., `"github:public"`, `"gitlab:private"`). |
| `"version"` | `String` | The GVS epoch. Must strictly align with the `CHANGELOG.md` tag (e.g., `"2608.1.0-bs"`). |

### B. The Polymorphic Routing Siblings
The routing and data keys must *always* exist as root-level siblings to `"metadata"`. They use native JSON polymorphism to dictate intent.

| Key | Data Type | Behavior / Result |
| :--- | :--- | :--- |
| `"backlog"` / `"changelog"` | `String` | **Path Mode:** Evaluated as an absolute relative path to an external file (e.g., `".dev/backlog.json"`). |
| `"backlog"` / `"changelog"` | `Array` | **Embedded Mode:** Evaluated as local data stored directly in the frontmatter. |
| `"backlog"` / `"changelog"` | `null` | **None:** Evaluated as "This document does not utilize this feature." |

---

## 3. Optional Dependency Keys (The Book Architecture)

To support massive multi-page environments (like Lore Wikis or TTRPG Rulebooks), the schema introduces optional metadata keys used to dynamically assemble isolated markdown files into unified, paginated books.

| Key | Type | Description |
| :--- | :--- | :--- |
| `"parent"` | `String` | Used exclusively in child pages (e.g. `"type": "chapter"`) to point to the relative path of the root `index.md`. |
| `"related"`| `Array` | Soft relational links to sibling documents. |

---

## 4. Implementation Examples

### Example 1: Standard Monorepo File
Used by 99% of files within a repository ecosystem. The backlog and changelog rely on external pointers.

```markdown
---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "Remote Repository Governance",
    "type": "governance",
    "platform": "github:public",
    "version": "2608.1.0-bs"
  },
  "backlog": ".dev/backlog.json",
  "changelog": "CHANGELOG.md"
}
---
```

### Example 2: Standalone Embedded File
Used for highly portable single-file documents (like a GitHub Gist) that must carry their own task tracking.

```markdown
---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "TTRPG Rulebook Base",
    "type": "ruleset",
    "platform": "github:public",
    "version": "1.0.0"
  },
  "backlog": [
    {
      "id": "PROJ-TODO-01",
      "title": "Embedded task example"
    }
  ],
  "changelog": null
}
---
```

### Example 3: Multi-Page Book Chapter
Used by child pages inside a large wiki. Note the `"parent"` key and the `null` changelog (deferring to the parent's changelog).

```markdown
---
{
  "metadata": {
    "author": "JLDN",
    "projectName": "Chapter 2: Combat Mechanics",
    "type": "chapter",
    "platform": "github:public",
    "version": "2608.1.0-bs",
    "parent": "index.md"
  },
  "backlog": ".dev/backlog.json",
  "changelog": null
}
---
```

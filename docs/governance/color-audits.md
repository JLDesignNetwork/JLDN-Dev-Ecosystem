# 🌈 JLDN 7-Color Audit Spectrum

The JLDN ecosystem relies on a holistic, 7-color audit system built as a dedicated Antigravity plugin (`jldn-audits`). 
These audits ensure every project adheres to the absolute highest standards of logic, security, and aesthetics.

## The Core Colors

| Color Team | Perspective & Methodology | Core Operational Scope |
| :--- | :--- | :--- |
| **🟠 Orange Team** | *Legacy Modernization & Standards Alignment* | Retrofitting, Scaffolding & Governance Alignment. Runs JLDN Gold Standard baseline. |
| **🔴 Red Team** | *Adversarial & Stress Testing* | Exploits, Loophole Hunting & Hostile Inputs. Hunts for broken synergies and SQL/XSS injections. |
| **🟡 Yellow Team** | *Systemic Logic & Causal Flow* | Causality, State Machines & API Logic. Audits valid state transitions and database mutation invariants. |
| **⚪ White Team** | *Forensics, Provenance & Traceability* | Source-of-Truth Parity, Anchors & Compliance. Verifies micro-anchor (`#slug`) health and downstream parity. |
| **🔵 Blue Team** | *Defensive Hardening & Balance* | Defensive Caps, Sandboxing & Fault Tolerance. Designs per-round caps and data loss prevention guardrails. |
| **🟢 Green Team** | *Tooling, Automation & CI/CD* | Pipelines, Build Scripts & Test Suites. Audits Python build tools, Jest/Pest suites, and linking integrity. |
| **🟣 Purple Team** | *Synthesis & Holistic Integration* | End-to-End User Experience & Proofing. Evaluates full front-to-back UX journeys and cross-platform tests. |

## Phase-Gated Routers
Rather than manually running individual colors, agents should use the phase-gated routers depending on the project's lifecycle:

- **Preflight Audit (`audit-preflight`)**: Runs Orange $\rightarrow$ Green. Use before starting active development.
- **Logic Audit (`audit-logic`)**: Runs White $\rightarrow$ Yellow. Use during active development to check state machines.
- **Defense Audit (`audit-defense`)**: Runs Blue $\rightarrow$ Red. Use before release to harden against exploits.

## Cyclic Engine
The `audit-cyclic-logic-defense` is a procedural loop skill that continuously runs Logic $\rightarrow$ log defects $\rightarrow$ fix $\rightarrow$ Defense $\rightarrow$ log defects $\rightarrow$ fix $\rightarrow$ Logic, until **0 defects** are found consecutively.

## Usage
Agents can be invoked to run these audits using standard alias triggers defined in your `.dev/config.json`.

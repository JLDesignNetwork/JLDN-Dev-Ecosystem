# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to the Generational Version Schema (GVS).

## [Unreleased]
### Added
- File-integrity checksum system: map schema v2 (per-file SHA-256, `.source/` secure mirror, injected-block checksums/templates), new `jldn-verify-integrity` (read-only audit + consent gate) and `jldn-repair` (gated write-only restore) skills.
- Edit-warning banners on all shipped ecosystem files, directing users to `jldn-verify-integrity` and to their own agents file for customizations.
- Three-tier config redesign templates (`global-config.template.json`, `global-secrets.template.json`, trimmed per-project `config.template.json`) -- not yet wired into the setup wizard (G08-TODO-23).

### Changed
- `jldn-uninstall` hardened: real-path/symlink-safe path containment before deletion, marker-count/order validation before stripping injected blocks, safe empty-directory pruning, Artifact-first teardown reporting.
- `jldn-evolve` now syncs the `.source/` mirror and checksum after an approved rule change, so legitimate changes aren't mistaken for drift.

### Fixed
- Corrected several self-introduced bugs caught via review before deployment: a step-ordering bug in `jldn-uninstall`'s directory pruning, a false-positive path-validation flag on `jldn-install.log`, and a Per-Project-rename interaction bug that would have broken checksum paths.

## [2608.2.0-a] - 2026-08-20
### Changed
- Refactored the core ecosystem into a Global-First architecture (`ECOSYSTEM_SETUP.md`) to resolve "Blank IDE" blindness.
- Shifted all execution hooks from OS-bound bash scripts to native, cross-platform Python scripts (`inject-aliases.py`).
- Abstracted Apple-specific hardcoded paths from `system-environment.md` into dynamic OS detection directives.
- Implemented dynamic Third-Party AI pointer resolution logic (`.cursorrules`, `CLAUDE.md`, `.github/copilot-instructions.md`) for both global and local scopes.

### Fixed
- Added explicit `@lifecycle persistent` and `@cleanup manual` protection metadata to all 30 ecosystem files to prevent accidental deletion by ephemeral purge routines.
- Corrected premature `-bs` lifecycle tag to correctly reflect the Alpha (`-a`) Genesis lifecycle phase.

## [2608.1.0-a] - 2026-08-20
### Added
- Initialized the JLDN Dev Ecosystem repository.
- Copied documentation from Backlog Schema.
- Implemented universal `.gitignore` standards for AI workspaces.

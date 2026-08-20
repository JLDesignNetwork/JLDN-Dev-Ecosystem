# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to the Generational Version Schema (GVS).

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

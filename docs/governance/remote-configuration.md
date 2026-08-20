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

# Remote Repository Governance

This document codifies the mandatory protocols for selecting remote hosts, defining visibility, and enforcing branch protections across the JLDN Ecosystem.

## 1. Prerequisites (CLI & Configuration)
To properly utilize the JLDN remote governance automation, the host environment must possess:
1. **GitHub CLI (`gh`) & GitLab CLI (`glab`)**: Installed and fully authenticated.
2. **`eco-config.json`**: An initialized configuration file at `.secrets/eco-config.json` containing the required organizational variables.

## 2. Dynamic Variable Resolution (`eco-config.json`)
Automation Tooling (whether AI Agents or custom Python execution scripts) must **never** assume hardcoded organizational paths. The automation MUST read `.secrets/eco-config.json` to resolve routing keys, authentication tokens, and account tier limitations.

### **What belongs in `eco-config.json`? (Environment Variables & Auth)**
Key-value configurations unique to the user/organization that require privacy:
- `github_organization`, `gitlab_organization`, `default_author`, `support_email`.
- `auth_keys`: Personal Access Tokens (PAT), API keys, or deployment tokens.
- `tier`: (e.g., `github_tier: "free"`, `gitlab_tier: "free"`) to inform automation about CI/CD limitations.
- `gitlab_host`: (e.g., `gitlab.com` or a self-hosted custom domain URL) to inform the automation where to route API commands.
- *Overrides:* Simple true/false overrides (e.g., `allow_feature_branches: true`).

### **What belongs in `.agents/rules/`? (Custom Behavior Rules)**
Overriding *behavioral logic* (e.g., "Always write tests in Pest" or "Never use Tailwind") must be provided as custom markdown rules. **Because the `.agents/` directory is blackholed by the default JLDN gitignore, users must manually create the `.agents/rules/` folder and populate it with their specific rule files.**

## 3. Remote Host & Gist Routing Policy

### **GitLab** (`https://{{gitlab_host}}/{{gitlab_organization}}/[ProjectName]`)
- **Use Case:** Exclusively reserved for **Live Websites and Web Applications** requiring automated server-to-repository pulls or complex CI/CD deployments.
- **Snippets:** For single-file configurations or localized live-server payloads, use GitLab Snippets.

### **GitHub** (`https://github.com/{{github_organization}}/[ProjectName]`)
- **Use Case:** The standard default home for TTRPG rulesets, CLI tooling, documentation, and standalone libraries.
- **Gists:** Use GitHub Gists for standalone markdown notes or open-source script sharing unrelated to a live web-app deployment.

## 4. Visibility Defaults & CI Constraints

- All new repositories must default to **`private`** during scaffolding (`platform: github:private`).
- **CRITICAL CI CONSTRAINT:** GitHub Free-Tier users do not receive free GitHub Actions minutes on private repositories. 
  - Automation tooling must check the `github_tier` variable in `eco-config.json`. If the user is on a "free" tier, the automation MUST NOT scaffold automated CI/CD workflows on private repositories, as they will immediately fail.

## 5. Branching Strategy: Direct-to-Main Protocol

- **No Feature Branches:** Iterations must be committed and pushed directly to `main`. 
- **No Pull Requests:** Do not generate draft PRs or PR templates.
- **Atomic Commits:** Changes must be committed atomically following taxonomy rules.

## 6. Mandatory Advanced Security & API Protections

Whenever initializing a GitHub repository, the following settings must be executed via the `gh` API to secure the trunk:

1. **Disable Bloat:** Disable GitHub Wiki (`--enable-wiki=false`) and Projects (`--enable-projects=false`).
2. **Workflow Cleanliness:** Enforce auto-deletion of merged branches (`--delete-branch-on-merge`) and linear squash merges (`--enable-squash-merge=true`).
3. **Branch Protection:** Apply a ruleset to the `~DEFAULT_BRANCH` that explicitly blocks branch deletion and force pushes.
4. **The Security Suite:**
   - **Private Vulnerability Reporting:** Enable (`gh api -X PUT /repos/{{github_organization}}/[ProjectName]/private-vulnerability-reporting`).
   - **Dependabot:** Scaffold `.github/dependabot.yml` to automate dependency version bumping.
   - **Code Scanning (CodeQL):** Scaffold `.github/workflows/codeql.yml` to automatically scan for vulnerabilities (Warning: Free-tier private CI constraints apply).

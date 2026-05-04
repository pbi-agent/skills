# MEMORY

## Metadata

- Purpose: shared repo memory for durable conventions and recent task history.
- Required sections: `Metadata`, `Long-Term Memory`, `Detailed Task Events`.
- Current detailed day: `2026-05-05`.
- Compaction status: `2026-04-21` entries compacted on `2026-05-05`.

## Long-Term Memory

- Repo scope: this is the official skills catalog for `pbi-agent`, centered on skill folders under `skills/<skill-name>/` rather than application code.
- Skill format: each official skill uses `skills/<skill-name>/SKILL.md` with YAML frontmatter; `name` must match the directory slug and `description` should start with clear trigger language such as "Use when...".
- Skill authoring pattern: keep `SKILL.md` concise, move bulky detail into one-level-deep `references/`, and prefer focused skills over broad catch-all skills.
- Power BI guardrails to preserve when relevant: explicit measures, `_Measures` naming, protected auto-generated date tables, intentional visual placement, and correct PBIP metadata for imports, drillthrough, bookmarks, and visual schemas.
- Power BI references convention: files under `skills/powerbi/references/` should start directly with an H1, not YAML frontmatter.
- Canonical repository URL: `https://github.com/pbi-agent/skills`.
- Official artifact inventory:
- `skills/powerbi-audit/` exists as the official audit skill, with workflow and rule catalog references plus `assets/AUDIT-TODO.md`.
- `skills/research-lab/` exists as the generic staged research workflow skill, with artifact schemas, phase instructions, and domain-adaptation references.
- `skills/powerbi/references/init_report.md` documents the durable `init_report` bootstrap behavior.
- `skills/powerbi/assets/init_report_template/` stores the PBIP starter scaffold copied from the original template source.

## Detailed Task Events

## 2026-05-05

- Added `skills/research-lab/` as a generic evidence-based research workflow skill converted from the raw lab framework, with concise `SKILL.md` plus `artifacts`, `phases`, and `domain-adaptation` references; updated the catalog README. Validation: read all new files and confirmed line counts under 200, reference paths exist, and `git diff --check` passed. Next context: `raw/` remains an untracked source input and was not modified.
- Extended `skills/research-lab/` with optional subagent orchestration for root `plan.md`/`todo.md`, gap fixing, production-ready loops, serial delegated tasks, and main-agent review gates. Validation: reread updated `SKILL.md` and new `references/subagent-orchestration.md`; `git diff --check` passed.
- Corrected `skills/research-lab/` subagent orchestration to remove example-specific trigger language and keep only generic phase delegation: one framework phase per subagent, main-agent review gate, then state update and next-phase selection. Validation: searched the skill for removed example terms and `git diff --check` passed.
- Addressed review finding by adding `.gitignore` for local `raw/` migration source input so legacy command packets are not accidentally committed with official skills. Validation: `git status --short` no longer lists `raw/`; `git diff --check` passed.

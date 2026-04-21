# MEMORY

## Metadata

- Purpose: shared repo memory for durable conventions and recent task history.
- Required sections: `Metadata`, `Long-Term Memory`, `Detailed Task Events`.
- Current detailed day: `2026-04-21`.
- Compaction status: `2026-04-20` entries compacted on `2026-04-21`.

## Long-Term Memory

- Repo scope: this is the official skills catalog for `pbi-agent`, centered on skill folders under `skills/<skill-name>/` rather than application code.
- Skill format: each official skill uses `skills/<skill-name>/SKILL.md` with YAML frontmatter; `name` must match the directory slug and `description` should start with clear trigger language such as "Use when...".
- Skill authoring pattern: keep `SKILL.md` concise, move bulky detail into one-level-deep `references/`, and prefer focused skills over broad catch-all skills.
- Power BI guardrails to preserve when relevant: explicit measures, `_Measures` naming, protected auto-generated date tables, intentional visual placement, and correct PBIP metadata for imports, drillthrough, bookmarks, and visual schemas.
- Power BI references convention: files under `skills/powerbi/references/` should start directly with an H1, not YAML frontmatter.
- Official artifact inventory:
- `skills/powerbi-audit/` exists as the official audit skill, with workflow and rule catalog references plus `assets/AUDIT-TODO.md`.
- `skills/powerbi/references/init_report.md` documents the durable `init_report` bootstrap behavior.
- `skills/powerbi/assets/init_report_template/` stores the PBIP starter scaffold copied from the original template source.

## Detailed Task Events

## 2026-04-21

- Added the canonical repository URL `https://github.com/pbi-agent/skills` to `README.md`, reset `TODO.md` for the session, and compacted the prior day log into metadata state; validation: reread `README.md`, `MEMORY.md`, and `TODO.md` to confirm the new link and required task-memory structure.

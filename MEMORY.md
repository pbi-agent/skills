# MEMORY

## Metadata

- Purpose: shared repo memory for durable conventions and recent task history.
- Required sections: `Metadata`, `Long-Term Memory`, `Detailed Task Events`.
- Current detailed day: `2026-04-20`.
- Compaction status: `2026-04-19` entries compacted into long-term memory on `2026-04-20`.

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

## 2026-04-20

- Updated `AGENTS.md` to define the single-file `MEMORY.md` workflow with `Metadata`, `Long-Term Memory`, and `Detailed Task Events`; validation: reread the `Task Memory` section and confirmed the rules are brief and internally consistent; next: migrate `MEMORY.md` to the new structure.
- Restructured `MEMORY.md` into the required three-section format and compacted prior-day entries into durable long-term bullets; validation: checked that only one current-day heading remains under `Detailed Task Events` and that durable repo conventions from `2026-04-19` were preserved without the old duplicate daily logs; next: append future task notes only under the active day and compact prior days at the start of a new day.

# MEMORY

## Metadata

- Purpose: shared repo memory for durable conventions and recent task history.
- Required sections: `Metadata`, `Long-Term Memory`, `Detailed Task Events`.
- Current detailed day: `2026-05-09`.
- Compaction status: `2026-05-08` entries compacted on `2026-05-09`.

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
- `skills/to-html/` exists as the official HTML artifact creation skill, with example HTML patterns in `assets/`.
- `skills/powerbi/references/init_report.md` documents the durable `init_report` bootstrap behavior.
- `skills/powerbi/assets/init_report_template/` stores the PBIP starter scaffold copied from the original template source.

## Detailed Task Events

## 2026-05-05 (compacted)

- Added and refined `skills/research-lab/`, including generic phase references, optional subagent orchestration, and review-driven cleanup; added `.gitignore` coverage for local `raw/` migration inputs. Validation included reference checks and `git diff --check`.

## 2026-05-08 (compacted)

- Added `skills/to-html/SKILL.md` and normalized the user-provided `skills/to_html/assets` folder to `skills/to-html/assets` for validator-compatible naming. Validation: `quick_validate.py` via `python3`, referenced asset path check, directory/name match check, and `git diff --check` passed. Next context: catalog README was left unchanged because the request was only to write the skill file.

## 2026-05-09

- Made `skills/to-html/SKILL.md` trigger wording generic by removing product-specific naming from the description. Validation: `quick_validate.py`, skill-folder wording scan, and `git diff --check` passed.
- Added `skills/to-html/` to the README current skill catalog. Validation: `quick_validate.py` for `to-html` and `git diff --check` passed.

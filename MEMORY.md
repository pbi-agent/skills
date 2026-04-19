# MEMORY

## 2026-04-20

- Normalized the heading/frontmatter format for six `skills/powerbi/references/*.md` files that were missing YAML metadata at the top.
- Added `name` and `description` fields to `action_button-skeleton.md`, `bar_chart_visual-bar-chart-patterns.md`, `card_visual-card-patterns.md`, `csv_local_import-patterns.md`, `excel_import-excel-import-patterns.md`, and `slicer_visual-slicer-patterns.md` so the reference catalog is consistent.
- Validation: checked the top of every Power BI reference file and ran a `python3` validation pass confirming each file now has frontmatter with non-empty `name` and `description`, followed by an H1 heading.

## 2026-04-20

- Corrected the Power BI reference-file normalization target after checking the example skill at `.agents/skills/create-skill/references/*.md`.
- Removed YAML frontmatter from all files under `skills/powerbi/references/` so reference files now start directly with an H1, matching the example pattern used by `create-skill`.
- Validation: inspected the head of each Power BI reference file and ran a `python3` check confirming the first non-empty line in every `skills/powerbi/references/*.md` file is an H1 and no file still has frontmatter.

## 2026-04-20

- Added a new `General Instructions` section to `skills/powerbi/SKILL.md`.
- Captured the shared Power BI rules for explicit measures, `_Measures` naming, protected auto-generated date tables, intentional visual placement, and style-priority order.
- Validation: re-read the updated `SKILL.md` and checked the diff to confirm the new rules were inserted cleanly without changing the rest of the skill structure.

## 2026-04-20

- Refactored the legacy `pbi-agent` audit prompt feature into a new official skill at `skills/powerbi-audit/`.
- Added `skills/powerbi-audit/SKILL.md` as the concise entrypoint, split the long audit framework into `references/workflow.md`, `references/rule-catalog-core.md`, and `references/rule-catalog-quality.md`, and bundled the resume checklist as `assets/AUDIT-TODO.md`.
- Preserved the durable behavior from the original `audit_prompt.py` and `AUDIT-TODO.md`: resume from checked items, write `AUDIT-REPORT.md` incrementally, and score findings across the seven audit domains.
- Validation: confirmed `SKILL.md` stays under 200 lines, verified non-empty `name` and `description` frontmatter, checked that all referenced local files exist, and reviewed `git status` to confirm the scope is limited to `TODO.md` and the new skill directory.

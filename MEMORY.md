# MEMORY

## 2026-04-20

- Normalized the heading/frontmatter format for six `skills/powerbi/references/*.md` files that were missing YAML metadata at the top.
- Added `name` and `description` fields to `action_button-skeleton.md`, `bar_chart_visual-bar-chart-patterns.md`, `card_visual-card-patterns.md`, `csv_local_import-patterns.md`, `excel_import-excel-import-patterns.md`, and `slicer_visual-slicer-patterns.md` so the reference catalog is consistent.
- Validation: checked the top of every Power BI reference file and ran a `python3` validation pass confirming each file now has frontmatter with non-empty `name` and `description`, followed by an H1 heading.

## 2026-04-20

- Corrected the Power BI reference-file normalization target after checking the example skill at `.agents/skills/create-skill/references/*.md`.
- Removed YAML frontmatter from all files under `skills/powerbi/references/` so reference files now start directly with an H1, matching the example pattern used by `create-skill`.
- Validation: inspected the head of each Power BI reference file and ran a `python3` check confirming the first non-empty line in every `skills/powerbi/references/*.md` file is an H1 and no file still has frontmatter.

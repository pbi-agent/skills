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

## 2026-04-20

- Added a new top-level `README.md` describing this repository as the official skills repo for `pbi-agent`.
- Documented the repo purpose, skill-first directory structure, key files, current skill catalog, authoring principles, workflow, and scope so the project is easier to orient without reading `AGENTS.md` first.
- Validation: read back `README.md` after creation and checked `git status --short` to confirm the change set is limited to the new README plus task-tracking updates in `TODO.md`.

## 2026-04-20

- Ported the durable `init_report` bootstrap behavior from `C:\Users\nbensaid_ext\workspace\pbi-agent\src\pbi_agent\init_command.py` into the official Power BI skill as a new reference file at `skills/powerbi/references/init_report.md`.
- Updated `skills/powerbi/SKILL.md` so the `powerbi` skill now advertises the new PBIP initialization reference alongside the existing report-structure guidance.
- Copied the bundled PBIP starter template into `skills/powerbi/assets/init_report_template/`, keeping only the scaffold entries that the original `init_report` command actually copies (`template_report.pbip`, `template_report.Report/`, and `template_report.SemanticModel/`).
- Validation: inspected the copied asset root, compared the source template tree against the new asset while excluding packaging artefacts skipped by `init_report`, and checked `git status --short` to confirm the intended file changes.

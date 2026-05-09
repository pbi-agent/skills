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
- Updated `skills/to-html/SKILL.md` to allow Mermaid diagrams/charts via jsDelivr ESM CDN without local install, with strict security defaults and offline/confidential caveats. Validation: manual frontmatter/content checks, 162-line count, and `git diff --check` passed; `quick_validate.py` was not present in this workspace.
- Fixed review feedback in `skills/to-html/SKILL.md` by making Mermaid copyable snippets use unescaped HTML attribute quotes and adding an explicit no-backslash note. Validation: frontmatter/line-count/static quote check and `git diff --check` passed.
- Tested `skills/to-html/SKILL.md` with a no-context sub-agent that created `test-to-html-mermaid-analysis.html` using Mermaid via jsDelivr ESM CDN and no install. Validation: static snippet checks for Mermaid/script/CDN/no escaped attribute quotes and `git diff --check` passed; browser rendering was not performed.
- Created `test-to-html-mermaid-analysis.html` as a standalone test artifact for the `to-html` skill, including a Mermaid flowchart loaded from the jsDelivr ESM CDN. Validation: static snippet checks, no escaped Mermaid/module attribute quotes, and `git diff --check` passed.

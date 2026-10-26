# MEMORY

## Metadata

- Purpose: shared repo memory for durable conventions and recent task history.
- Required sections: `Metadata`, `Long-Term Memory`, `Detailed Task Events`.
- Current detailed day: `2026-10-26`.
- Compaction status: `2026-05-19` entries compacted on `2026-10-26`.

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
- `skills/to-html/` exists as the official HTML artifact creation skill for standalone visual websites (concepts, ideas, decisions); it has no assets folder.
- `skills/rsi/` exists as the recursive self-improving loop skill (Evaluate, Diagnose, Generate, Train, Gate); its `SKILL.md` must keep the user-provided Mermaid loop diagram verbatim.
- `skills/to-html/SKILL.md` permits Mermaid via jsDelivr ESM CDN for non-confidential artifacts, with strict security defaults and literal unescaped HTML attribute quotes in copyable snippets.
- `skills/powerbi/references/init_report.md` documents the durable `init_report` bootstrap behavior.
- `skills/powerbi/assets/init_report_template/` stores the PBIP starter scaffold copied from the original template source.

## Detailed Task Events

## 2026-05-05 (compacted)

- Added and refined `skills/research-lab/`, including generic phase references, optional subagent orchestration, and review-driven cleanup; added `.gitignore` coverage for local `raw/` migration inputs. Validation included reference checks and `git diff --check`.

## 2026-05-08 (compacted)

- Added `skills/to-html/SKILL.md` and normalized the user-provided `skills/to_html/assets` folder to `skills/to-html/assets` for validator-compatible naming. Validation: `quick_validate.py` via `python3`, referenced asset path check, directory/name match check, and `git diff --check` passed. Next context: catalog README was left unchanged because the request was only to write the skill file.

## 2026-05-09 (compacted)

- Refined `skills/to-html/SKILL.md` trigger wording, Mermaid CDN guidance, and copyable snippet quoting; added README catalog coverage and a standalone Mermaid test artifact. Validation included `quick_validate.py` when present, static frontmatter/snippet checks, line count, and `git diff --check`.

## 2026-05-19 (compacted)

- Reworked `skills/to-html/` to user-need/adaptive-visual-first standalone websites, removed the assets/gallery workflow, and aligned README. Validation: frontmatter/name/line checks and `git diff --check`.

## 2026-10-26

- Added `skills/rsi/` (`SKILL.md` with the user's Mermaid loop diagram, `references/stages.md`, `references/artifacts.md`) and README catalog entry. Validation: frontmatter/name/reference checks, line count, and `git diff --check` passed.

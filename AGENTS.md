# AGENTS.md

This repository is the canonical workspace for maintaining official skills used by `pbi-agent`.

## Scope

- Treat this repo as a skills repository, not the main `pbi-agent` application codebase.
- The primary artifact is an official skill folder under `skills/<skill-name>/`.
- Each skill must be maintained in the official format centered on `SKILL.md`.
- The current strategic goal is to refactor internal Power BI knowledge into official skills for `pbi-agent`.

## Repository Layout

- `skills/<skill-name>/SKILL.md`: required skill entrypoint.
- `skills/<skill-name>/references/`: optional detailed documentation loaded only when needed.
- `skills/<skill-name>/scripts/`: optional deterministic helpers.
- `skills/<skill-name>/assets/`: optional output resources and templates.
- `skills-lock.json`: lockfile for the local skill set; keep it aligned with skill changes when required by the repo workflow.

## Working Rules

- Do not work in the legacy flat-skill style when creating new skills here.
- Prefer one focused skill per topic. Split broad domains into multiple skills instead of building one large catch-all skill.
- Keep `SKILL.md` concise. Use progressive disclosure and move bulky detail into `references/`.
- Default to ASCII unless the file already uses another character set for a clear reason.
- Do not add auxiliary documentation files like per-skill `README.md`, `CHANGELOG.md`, or scratch notes unless explicitly requested.
- Do not commit, push, or open PRs unless explicitly asked.

## Official Skill Format

Every skill must have:

1. A directory named after the skill slug.
2. A `SKILL.md` file with YAML frontmatter.
3. A `name` that matches the directory name.
4. A `description` that clearly states when the skill should be used.

Minimum structure:

```text
skills/<skill-name>/
└── SKILL.md
```

Preferred extended structure:

```text
skills/<skill-name>/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

## Skill Authoring Standards

- Start descriptions with concrete trigger language such as "Use when..." so matching is reliable.
- Keep `SKILL.md` under roughly 200 lines when possible. If it grows, split variant-specific or reference-heavy content into `references/`.
- Put core workflow and decision rules in `SKILL.md`.
- Put schemas, long examples, compatibility notes, and detailed patterns in `references/`.
- Prefer concrete rules over general advice.
- Reuse existing wording and structure across related Power BI skills so the catalog feels coherent.
- When migrating legacy Power BI knowledge, preserve the operational guidance but rewrite it into official skill structure instead of copying raw files blindly.

## Power BI Skill Guidance

- Keep Power BI skills narrowly scoped by concern, for example:
  - semantic modeling / TMDL
  - imports and data-source patterns
  - visual authoring patterns
  - report navigation and filter behavior
  - theming and branding
- Preserve hard guardrails that prevent broken PBIP output, especially around:
  - `_Measures` naming
  - explicit measure usage
  - query/order metadata
  - parameter metadata for local imports
  - drillthrough, bookmarks, and visual schema correctness
- If a topic is brittle or repetitive, prefer a dedicated skill over embedding the rule in a generic one.

## Maintenance Workflow

1. Read the existing skill before editing it.
2. Preserve stable skill names unless there is a deliberate rename.
3. Keep references one level away from `SKILL.md`; avoid deep reference chains.
4. When creating a new skill, check whether the topic should extend an existing skill instead.
5. When migrating from another repo or legacy knowledge base, capture only the durable guidance that should survive across tasks.

## Validation

Before handoff, verify:

- every added skill has a valid `SKILL.md`;
- frontmatter includes non-empty `name` and `description`;
- the directory name matches the skill `name`;
- referenced local files actually exist;
- the skill stays concise and does not duplicate large blocks already moved to `references/`.

## Priority For This Repo

- Build and maintain the official Power BI skill catalog for `pbi-agent`.
- Favor clean migration into official skills over preserving ad hoc legacy formatting.
- Optimize for discoverability, concise triggers, and reusable domain guidance.

## Task Memory

- Use a single `MEMORY.md` file for both durable memory and recent task history.
- Keep `MEMORY.md` in three sections only: `Metadata`, `Long-Term Memory`, and `Detailed Task Events`.
- At the start of substantive work, read `Metadata`, `Long-Term Memory`, and any current-day detailed entries relevant to the task.
- Keep `Long-Term Memory` compact and edited in place. Store only durable facts: stable repo conventions, important decisions, reusable validation patterns, active follow-ups, and artifacts that matter beyond one task.
- Keep `Detailed Task Events` append-only within the active day. Group entries under one `## YYYY-MM-DD` heading per day.
- After each implementation, append one short task entry to the current day with only: what changed, validation, and next context if needed.
- On the first substantive task of a new day, compact the previous day's detailed entries before appending new ones.
- During compaction, promote durable facts into `Long-Term Memory`, carry unresolved items into an open-thread bullet if still relevant, and remove or collapse prior-day detail that is no longer needed.
- Avoid duplicating long-term bullets. Merge with existing bullets when the fact already exists.
- Keep the file token-efficient: prefer short bullets, avoid command noise, and do not preserve obsolete troubleshooting detail once compacted.
- Use `TODO.md` for the current task session only.
- Create or reset `TODO.md` before starting substantive work.
- Use compact TODO markers: `[ ]` pending, `[>]` in progress, `[X]` done, `[!]` blocked, `[-]` dropped.
- Update `TODO.md` as you work. Mark steps complete when they finish, and revise the list when scope changes.
- If `TODO.md` contains an old completed or unrelated list, replace it before making new changes.

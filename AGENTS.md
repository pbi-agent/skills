# AGENTS.md

This repository is the canonical workspace for maintaining official skills used by `pbi-agent`.

## Scope

- Treat this repo as a skills repository, not the main `pbi-agent` application codebase.
- The primary artifact is an official skill folder under `.agents/skills/<skill-name>/`.
- Each skill must be maintained in the official format centered on `SKILL.md`.
- The current strategic goal is to refactor internal Power BI knowledge into official skills for `pbi-agent`.

## Repository Layout

- `.agents/skills/<skill-name>/SKILL.md`: required skill entrypoint.
- `.agents/skills/<skill-name>/references/`: optional detailed documentation loaded only when needed.
- `.agents/skills/<skill-name>/scripts/`: optional deterministic helpers.
- `.agents/skills/<skill-name>/assets/`: optional output resources and templates.
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
.agents/skills/<skill-name>/
└── SKILL.md
```

Preferred extended structure:

```text
.agents/skills/<skill-name>/
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

Useful checks:

```bash
find .agents/skills -maxdepth 2 -name SKILL.md
rg -n "^name:|^description:" .agents/skills/*/SKILL.md
```

## Priority For This Repo

- Build and maintain the official Power BI skill catalog for `pbi-agent`.
- Favor clean migration into official skills over preserving ad hoc legacy formatting.
- Optimize for discoverability, concise triggers, and reusable domain guidance.

## Task Memory

- Use `MEMORY.md` for long-term agent memory and session continuity. At the start of substantive work, consult it when available for relevant prior context.
- After each implementation, append a brief entry to `MEMORY.md` describing what changed, why it changed, validation performed, and any context useful for the next session.
- Always add new `MEMORY.md` entries at the end of the file in append mode. Never insert a new memory entry in the middle of existing history.
- Use `TODO.md` for the current task session only.
- Create or reset `TODO.md` before starting substantive work.
- Use compact TODO markers: `[ ]` pending, `[>]` in progress, `[X]` done, `[!]` blocked, `[-]` dropped.
- Update `TODO.md` as you work. Mark steps complete when they finish, and revise the list when scope changes.
- If `TODO.md` contains an old completed or unrelated list, replace it before making new changes.
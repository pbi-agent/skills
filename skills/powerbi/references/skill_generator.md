# Skill Generator

Use this when a task failed, was corrected, or exposed a non-obvious constraint that should be captured as an official skill in this repo.

## Failure Analysis

Review the full task history and list each distinct mistake or missing rule:

- What was attempted.
- Why it failed.
- What fixed it.

Only promote lessons that are durable and likely to recur. Do not create a skill for one-off typos, temporary environment issues, or repo noise.

## Skill Scope And Naming

- One focused topic per skill. Do not bundle unrelated lessons.
- Name the directory with `snake_case` matching the topic, for example `line_chart_visual` or `composite_key_drillthrough`.
- Avoid generic names such as `fixes`, `lessons`, or `notes`.
- If an existing skill already covers the topic, update that skill instead of creating a duplicate.

## Output Format

Create or update an official skill directory under `.agents/skills/<skill-name>/`.

- `SKILL.md` is required.
- Add YAML frontmatter with non-empty `name` and `description`.
- Keep `name` identical to the directory name.
- Start `description` with `Use when...`.
- Keep `SKILL.md` concise. Move bulky examples or compatibility detail into `references/` only when needed.

## Skill File Pattern

Carry forward the concrete lesson, but normalize it into the official format used in this repo:

~~~markdown
---
name: <skill_name>
description: Use when <one-line trigger for this skill>.
---

# <Skill Title>

Use this when <short scenario>.

## Core Rules

1. <Concrete rule that prevents the original mistake.>
2. <Concrete rule that prevents the original mistake.>

## Correct Pattern

```<language>
<Minimal code, JSON, TMDL, or file-layout example.>
```

## Checklist

- Confirm the rule applies to the target task.
- Confirm the required structure and metadata are present.
~~~

## Authoring Rules

- Start from the actual failing or corrected pattern rather than inventing a new abstraction.
- Preserve exact schema keys, role names, metadata fields, and file locations when they are part of the fix.
- Prefer concrete guardrails over general advice.
- Keep examples minimal and directly tied to the lesson.
- Use `references/` only when the main skill would otherwise become too long.

## Common Mistakes

- Do not create a broad skill from several unrelated fixes.
- Do not drop the specific property names, ordering requirements, or metadata that made the fix work.
- Do not leave the output in the legacy flat `.md` style; convert it into `.agents/skills/<skill-name>/SKILL.md`.

## Validation

- Confirm the new or updated skill is the right home for the lesson.
- Confirm `name` matches the directory name.
- Confirm `description` starts with `Use when...`.
- Confirm every referenced local file exists.
- Confirm `SKILL.md` stays concise and the rules are specific enough to prevent the original mistake.

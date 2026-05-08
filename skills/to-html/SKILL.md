---
name: to-html
description: Use when creating a standalone HTML artifact instead of Markdown, especially for specs, implementation plans, explorations, PR explanations, code reviews, technical explainers, research reports, slide-style briefings, diagrams, design prototypes, component studies, or custom editing interfaces with copy/export behavior.
---

# To HTML

Create readable, shareable, self-contained HTML artifacts when visual structure,
information density, diagrams, or interaction will make the output easier to
review than Markdown.

## Core Rule

Default to a single `.html` file that opens directly in a browser. Use inline
CSS and, when useful, inline JavaScript. Add external dependencies only when the
user requests them or the target repo already has an expected local stack.

## Startup

1. Identify the reader, decision to support, source material, and expected use:
   read once, compare options, review code, tune a design, brief a team, or edit
   structured data.
2. Choose the output path. Use the user-provided path when given; otherwise use
   a concise slug such as `implementation-plan.html`, `pr-explainer.html`, or
   `triage-board.html` in the current working directory.
3. Load only the relevant example asset(s) from `assets/` as pattern references.
   Do not bulk-load every example.
4. Build the artifact around the job, not around a generic document template.
5. Verify that the file is valid enough to open locally, that responsive layout
   works at narrow and wide widths, and that any buttons, filters, sliders, or
   export actions work.

## Asset Guide

Use `assets/index.html` to browse the full gallery when unsure. Otherwise load
one or two matching examples:

- Exploration and planning: `01-exploration-code-approaches.html`,
  `02-exploration-visual-designs.html`, `16-implementation-plan.html`
- Code review and understanding: `03-code-review-pr.html`,
  `04-code-understanding.html`, `17-pr-writeup.html`
- Design and prototypes: `05-design-system.html`,
  `06-component-variants.html`, `07-prototype-animation.html`,
  `08-prototype-interaction.html`
- Reports, research, and learning: `09-slide-deck.html`,
  `10-svg-illustrations.html`, `11-status-report.html`,
  `12-incident-report.html`, `13-flowchart-diagram.html`,
  `14-research-feature-explainer.html`,
  `15-research-concept-explainer.html`
- Custom editing interfaces: `18-editor-triage-board.html`,
  `19-editor-feature-flags.html`, `20-editor-prompt-tuner.html`

Treat these files as examples to adapt, not immutable templates. Preserve the
skill assets and write new artifacts outside `assets/` unless the user is
explicitly maintaining the skill itself.

## Artifact Patterns

For specs and implementation plans:

- Show the decision context first, then alternatives, chosen direction, phased
  work, risks, and validation.
- Include mockups, architecture diagrams, data-flow diagrams, tables, and key
  code snippets when they reduce ambiguity.
- Make tradeoffs visually comparable instead of burying them in prose.

For code review, PR writeups, and code understanding:

- Render meaningful diffs or snippets with inline annotations.
- Color-code severity or confidence, but keep labels readable in monochrome.
- Explain control flow, data flow, module boundaries, and failure modes with
  diagrams where useful.
- Keep findings grounded in observed files, commits, logs, or tests.

For reports, research, and learning artifacts:

- Start with the answer or executive summary.
- Separate evidence, interpretation, recommendations, and open questions.
- Use tables for dense comparisons, SVG for flows and systems, and callouts for
  gotchas or decisions.
- Include provenance for sources or inspected files when claims depend on them.

For design prototypes and component studies:

- Prefer real interactive controls over static option lists: segmented controls,
  sliders, color swatches, toggles, and copy buttons.
- Show multiple variants side by side when comparing direction, density, tone,
  animation, or visual hierarchy.
- Use the target product or domain context instead of generic placeholder UI.

For custom editing interfaces:

- Make the UI purpose-built for the specific data or decision.
- Include a final export path such as "copy as JSON", "copy as Markdown",
  "copy prompt", or "copy diff".
- Warn about invalid combinations when constraints are known.
- Keep state client-side unless the user explicitly asks for persistence.

## HTML Construction Rules

- Include `<!doctype html>`, `<html lang="en">`, UTF-8 charset, viewport meta,
  and a descriptive `<title>`.
- Use semantic structure: `header`, `main`, `section`, `article`, `nav`, `table`,
  `figure`, `figcaption`, `button`, and form elements where appropriate.
- Define a small design system with CSS variables for color, type, spacing, and
  borders. Use responsive grids and media queries rather than fixed desktop-only
  layouts.
- Use SVG for diagrams, flowcharts, timelines, state machines, and small
  illustrations. Use native tables for tabular data.
- Use JavaScript only for purposeful interaction: tabs, filters, sorting,
  sliders, live previews, drag-and-drop, copy/export, or simple simulations.
- Keep the artifact self-contained unless existing local assets are intentionally
  referenced. Avoid remote CDN dependencies for confidential or offline work.
- Escape untrusted text before inserting it into script-generated HTML.
- Do not fabricate data, screenshots, sources, or benchmark results. Label
  assumptions and placeholders clearly.

## Visual Quality Bar

- Optimize for a reader who may only open the file once.
- Make hierarchy visible through layout, spacing, typography, and grouping.
- Keep long prose scannable with summaries, tables, callouts, and diagrams.
- Ensure text does not overflow buttons, cards, tables, or mobile screens.
- Avoid decorative complexity that does not clarify the content.
- Prefer a calm, purposeful interface over a generic landing page.

## Validation

Before handoff:

1. Confirm the file path exists and the HTML has balanced major tags.
2. Open the file in a browser or run an available local browser check when the
   artifact is visual, interactive, or high-stakes.
3. Test every interactive control and copy/export action.
4. Check at least one narrow viewport and one desktop viewport for overlap,
   unreadable tables, clipped controls, and broken diagrams.
5. If browser validation is not available, state that limitation in the final
   response and report the static checks performed.

## Handoff

Return the artifact path, the intended reading mode, and any important
interactions or export buttons. Keep the user-facing summary short unless they
asked for a walkthrough.

---
name: to-html
description: Use when creating standalone HTML websites that illustrate concepts and make ideas or decisions more visual with tailored cards, charts, tables, Mermaid, snippets, or interactions.
---

# To HTML

Create readable, shareable, self-contained HTML artifacts when adaptive visual
structure, information density, diagrams, or interaction will make a concept,
idea, analysis, or decision easier to understand.

## Core Rule

Design for the user's job first, not from a generic reference page. Default to a
single `.html` file that opens directly in a browser. Use inline CSS and, when
useful, inline JavaScript. Add external dependencies only when the user requests
them or the target repo already has an expected local stack.

## Startup

1. Identify the reader, decision to support, source material, and expected use:
   read once, compare options, review code, tune a design, brief a team, or edit
   structured data.
2. Choose the visual grammar before coding: cards for summaries, charts for real
   quantities, tables for dense comparisons, Mermaid or SVG for relationships,
   annotated snippets for code, timelines for plans, and controls for exploration.
3. Choose the output path. Use the user-provided path when given; otherwise use
   a concise slug such as `implementation-plan.html`, `pr-explainer.html`, or
   `triage-board.html` in the current working directory.
4. Build the artifact around the job, not around a generic document template or
   gallery.
5. Verify that the file is valid enough to open locally, that responsive layout
   works at narrow and wide widths, and that any buttons, filters, sliders, or
   export actions work.

## Visual Design Selection

Choose the format that makes the user's decision easier:

- Cards: executive summaries, KPIs, option tiles, risk snapshots, status blocks,
  personas, or small evidence packets. Each card needs a clear label, value or
  takeaway, and optional status/severity cue.
- Charts: real quantitative comparisons, trends, distributions, and before/after
  views. Prefer simple SVG or CSS charts for small datasets; label axes, units,
  ranges, and source. Do not invent numbers to fill a chart.
- Tables: dense matrices, requirements, file inventories, tradeoffs, test cases,
  or audit findings. Add sorting/filtering only when it helps; keep mobile
  overflow readable.
- Mermaid diagrams: flows, sequences, state machines, dependency maps, ER models,
  timelines, architecture, or quick chart-like summaries when Mermaid is clearer
  than hand-authored SVG and the CDN is acceptable.
- Code snippets: APIs, configs, diffs, prompts, formulas, or scripts. Use short
  snippets with titles, language labels, inline annotations, and copy buttons
  when useful.
- Callouts and timelines: decisions, risks, assumptions, milestones, failure
  modes, and next actions.
- Lightweight interaction: tabs, filters, toggles, sliders, search, preview, or
  copy/export controls when the reader must explore or reuse content.

Be creative in structure and visual hierarchy, but keep every visual tied to the
reader's goal. Prefer a bespoke artifact over a generic landing page.

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

- Include `<!doctype html>`, `<html lang='en'>`, UTF-8 charset, viewport meta,
  and a descriptive `<title>`.
- Use semantic structure: `header`, `main`, `section`, `article`, `nav`, `table`,
  `figure`, `figcaption`, `button`, and form elements where appropriate.
- Define a small design system with CSS variables for color, type, spacing, and
  borders. Use responsive grids and media queries rather than fixed desktop-only
  layouts.
- Use SVG for custom diagrams, flowcharts, timelines, state machines, and small
  illustrations. Use native tables for tabular data.
- Use Mermaid diagrams/charts when they clarify flows, sequences, dependencies,
  timelines, state changes, ER relationships, architecture, or simple chart-like
  summaries more quickly than hand-authored SVG. Do not install Mermaid; embed
  diagram definitions in `<pre class='mermaid'>` blocks and add the ESM CDN
  script only when Mermaid is used. Use literal HTML quotes in copyable snippets;
  do not backslash-escape attribute quotes:

  ```html
  <script type='module'>
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true, securityLevel: 'strict' });
  </script>
  ```

  Keep `securityLevel: 'strict'` unless the user explicitly needs trusted click
  events or HTML labels. Mermaid's default page-load behavior renders all
  `.mermaid` blocks; use `mermaid.run` only for dynamically added diagrams.
- Use JavaScript only for purposeful interaction: tabs, filters, sorting,
  sliders, live previews, drag-and-drop, copy/export, or simple simulations.
- Keep the artifact self-contained unless the user explicitly provides local
  files to reference. Avoid remote CDN dependencies for confidential or offline
  work; Mermaid via jsDelivr is allowed for non-confidential artifacts when it
  avoids a local install and improves clarity.
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

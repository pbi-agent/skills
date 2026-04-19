# Audit Workflow

Use this reference for the audit sequence, inventory scope, resume behavior,
and report-writing rules.

## Inventory Scope

Scan the project recursively and catalogue:

- `definition/database.tmdl`: compatibility level
- `definition/model.tmdl`: model properties, culture, references
- `definition/relationships.tmdl`: relationship set
- `definition/expressions.tmdl`: shared M expressions and parameters
- `definition/tables/*.tmdl`: tables, columns, measures, partitions,
  hierarchies, calculated items, calculation groups
- `definition/roles/*.tmdl`: RLS and OLS roles
- `definition/perspectives/*.tmdl`: perspectives
- `definition/cultures/*.tmdl`: translations
- `*.pbi` and `*.pbip`: report and project manifests
- Theme JSON files, report images, and custom visuals

Summarize what is present and what is missing.

## Resume Rules

- Read `AUDIT-TODO.md` first.
- Read `AUDIT-REPORT.md` if it exists.
- Skip any phase or rule already marked `[x]`.
- Resume from the first unchecked `[ ]` item.
- Keep partial report sections unless the evidence proves they are wrong.

## Incremental TODO Updates

- After each completed phase or domain, change matching checklist items from
  `[ ]` to `[x]`.
- Mark rules `[x]` even when they are not applicable; note `Not applicable`
  under the checklist item if useful.
- Add brief notes only when they help a resume pick up faster.

## Incremental Report Updates

- After inventory, create `AUDIT-REPORT.md` if missing.
- Add the title and `## 2. Audit Scope and Inventory` section first.
- After each domain, append that domain's findings immediately.
- After all domains, add the summary sections:
  - `## 1. Executive Summary`
  - `## 3. Score Card`
  - `## 5. Consolidated Findings Table`
  - `## 6. Priority Action Plan`
  - `## 7. Confidence and Known Gaps`

Insert the executive summary near the top if the rest of the report already
exists from an interrupted run.

## Domain Findings Template

Use this shape for each finding:

```text
### Domain N: <Domain Name>

**RULE-ID** — <Short title> (Severity N)
- Object(s): <table/column/measure>
- Evidence: <file quote or exact reference>
- Impact: <why this matters>
- Recommendation: <specific fix>
```

If a domain has no findings, write:

```text
### Domain N: <Domain Name>

No issues detected.
```

## Final Sections

### Executive Summary

- State the model or project name when it is discoverable.
- State the overall grade and percentage.
- Call out the top three risks.
- State whether the model appears production-ready.

### Score Card

Include one row per domain:

```text
| Domain | Applicable Rules | Passed | Failed | Weight | Weighted Score |
```

Add an `Overall` row with the final grade and score.

### Consolidated Findings Table

Combine all findings across domains and sort by severity descending.

```text
| # | Rule ID | Severity | Domain | Object(s) | Finding | Recommendation |
```

### Priority Action Plan

Group fixes into:

- Now: severity 3-5
- Next: severity 2
- Later: severity 1

### Confidence and Known Gaps

- State what could not be fully evaluated.
- State why it could not be evaluated.
- Note any assumptions made from incomplete files.

## Execution Order

1. Inventory and scope summary
2. Structure and star schema
3. Modeling, relationships, and naming
4. Performance
5. Security
6. DAX quality
7. Metadata and documentation
8. Anti-patterns and hidden fields
9. Scoring and summary sections

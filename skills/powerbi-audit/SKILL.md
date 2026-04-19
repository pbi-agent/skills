---
name: powerbi-audit
description: Use when auditing a local Power BI PBIP or TMDL project and producing or resuming an evidence-based `AUDIT-REPORT.md` with matching `AUDIT-TODO.md` progress tracking.
---

# Power BI Audit

Use this when the task is to audit a local Power BI project in the current
working directory. The audit covers model structure, relationships, naming,
performance, security, DAX quality, metadata, and hidden-field anti-patterns.

## Scope

- Audit the local PBIP or TMDL project only.
- Ignore Power BI Service-only concerns unless they are represented in local
  files.
- Work autonomously from the available files; ask questions only if the local
  project is missing or unreadable.

## Startup

1. Ensure `AUDIT-TODO.md` exists in the current working directory. If it does
   not, copy `assets/AUDIT-TODO.md` before starting.
2. Read `AUDIT-TODO.md` and `AUDIT-REPORT.md` if present.
3. Treat checked `[x]` items as completed work from a previous run.
4. Resume from the first unchecked `[ ]` item without redoing completed phases.

## Load References

- Load `references/workflow.md` for audit sequencing, inventory scope, report
  structure, and incremental write rules.
- Load `references/rule-catalog-core.md` for Structure, Modeling,
  Performance, and Security rules.
- Load `references/rule-catalog-quality.md` for DAX Quality, Metadata,
  Anti-Patterns, and scoring.
- If the audit turns into a code fix, also load the sibling `powerbi` skill
  and only the narrow references needed for the affected artifact.

## Non-Negotiable Rules

- Read every relevant local project file methodically; do not sample.
- Ground every finding in observed evidence. Quote or point to the file
  content that triggered the finding.
- If a rule is not applicable, state that briefly and still mark it complete.
- Update `AUDIT-TODO.md` incrementally after each completed phase or domain.
- Write `AUDIT-REPORT.md` incrementally. Do not wait until the end to save
  findings.
- Preserve existing report content on resume and append or insert only the
  missing sections.

## Finding Format

For each finding, record:

- Rule ID
- Severity 1-5
- Domain
- Object(s) affected
- Evidence
- Impact
- Recommendation

If a domain has no findings, write `No issues detected.`

## Audit Flow

1. Build the inventory of model, report, theme, image, and custom-visual
   artifacts.
2. Evaluate each rule across the seven domains.
3. Append domain findings to `AUDIT-REPORT.md` as each domain completes.
4. Compute weighted results and letter grade after all applicable rules are
   evaluated.
5. Finish the report with the executive summary, score card, consolidated
   findings table, priority action plan, and confidence or gap notes.
6. End with a brief user-facing confirmation that includes the grade and top
   risks.

## Deliverables

- `AUDIT-TODO.md` kept current throughout the audit
- `AUDIT-REPORT.md` written progressively and complete at handoff

## References

- `references/workflow.md`
- `references/rule-catalog-core.md`
- `references/rule-catalog-quality.md`
- `assets/AUDIT-TODO.md`

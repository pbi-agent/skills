# PBIP Report Initialization

Use when a task needs to start a new Power BI PBIP project from a known-good scaffold instead of editing an existing report.

## Asset To Copy

- The bundled starter template lives under `assets/init_report_template/`.
- Copy the template contents into the target project root so these entries land side by side:
  - `template_report.pbip`
  - `template_report.Report/`
  - `template_report.SemanticModel/`
- If the target already contains any of those entries, stop unless the task explicitly calls for overwriting the existing scaffold.

## What The Template Contains

- `template_report.pbip` points to `template_report.Report`.
- `template_report.Report/definition.pbir` binds the report to `../template_report.SemanticModel`.
- `template_report.Report/definition/report.json` provides the base theme package and report-level settings.
- `template_report.Report/definition/pages/pages.json` declares a single active page.
- `template_report.Report/definition/pages/<page-id>/page.json` starts with a `1280 x 720` page and `displayOption: "FitToPage"`.
- `template_report.SemanticModel/definition/database.tmdl` sets `compatibilityLevel: 1600`.
- `template_report.SemanticModel/definition/model.tmdl` starts with `culture: en-US`, `defaultPowerBIDataSourceVersion: powerBI_V3`, `sourceQueryCulture: fr-FR`, and the default Power BI annotations.

## Reproduction Rules

1. Copy the asset tree as-is before making report-specific edits.
2. Preserve relative paths between `.pbip`, `.pbir`, report folder, and semantic model folder unless you are deliberately renaming the scaffold.
3. If you rename the template, update all linked paths together:
   - `.pbip -> artifacts[*].report.path`
   - `.Report/definition.pbir -> datasetReference.byPath.path`
   - folder names on disk
4. Treat `.pbi/`, `.platform/`, `definition/`, and `StaticResources/` as part of the scaffold; do not omit them when copying.
5. Customize page names, visuals, measures, and data sources only after the scaffold is in place.

## Safe First Customizations

- Rename `Page 1` and expand the page set through `definition/pages/pages.json`.
- Add model objects in `template_report.SemanticModel/definition/model.tmdl`.
- Add report visuals and navigation after the starter page exists.
- Replace or extend the shared theme only after confirming resource-package paths remain valid.

## Validation

- Confirm the copied asset still contains `template_report.pbip`, `template_report.Report/`, and `template_report.SemanticModel/`.
- Confirm `.pbip` and `.pbir` relative paths still resolve after any rename.
- Confirm the report keeps a valid `pages.json` and at least one page folder with a matching `page.json`.

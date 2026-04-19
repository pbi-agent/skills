# Excel Import

Use when creating or editing a PBIP semantic model that imports Excel data from a local workbook.

## Where Excel Source Is Defined In TMDL

- `definition/database.tmdl`: model compatibility only; no workbook path definition here.
- `definition/model.tmdl`: model metadata, `ref table ...` entries, and `annotation PBI_QueryOrder`.
- `definition/expressions.tmdl`: workbook path parameters and optional sheet or table selector parameters with full Power BI parameter metadata.
- `definition/tables/<table>.tmdl`: Excel import logic in `partition <table> = m` with `Excel.Workbook(...)`.
- `definition/relationships.tmdl`: relationship graph after tables are loaded.

## Core Guardrails

- Never hardcode `File.Contents("C:\\...")` in a partition. Put the workbook path in `definition/expressions.tmdl` as a text parameter.
- Any workbook path, sheet name, or Excel table name parameter must include `meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]`.
- Every parameter expression must also include `lineageTag`, `annotation PBI_NavigationStepName = Navigation`, and `annotation PBI_ResultType = Text`.
- In `definition/model.tmdl`, always add `annotation PBI_QueryOrder = [...]` when using Excel-backed M partitions. Put parameters first, then imported tables, then `_Measures`.
- Every imported table must have an explicit `partition <table> = m` block with `mode: import` and end with `annotation PBI_ResultType = Table`.
- Prefer `Excel.Workbook(File.Contents(excel_workbook_path), null, true)` so typing stays explicit in later M steps.
- Prefer named Excel tables (`Kind="Table"`) over raw worksheets (`Kind="Sheet"`) when the workbook already exposes them.
- A dedicated `_Measures` table must never be left partitionless. Give it an empty import partition even if it contains only measures.
- Never name the measures table `Measures`; always use `_Measures`.
- After major semantic-model surgery, delete `.pbi/cache.abf` if it exists before reopening the PBIP.

## Workflow

1. Define or repair workbook and selector parameters in `definition/expressions.tmdl`.
2. Add or fix `annotation PBI_QueryOrder` in `definition/model.tmdl`.
3. Update each Excel-backed table partition to use parameterized `Excel.Workbook(...)` M code.
4. Make column declarations, typing, and `sourceColumn` mappings match the final M output.
5. Ensure `_Measures` keeps an import partition.
6. Re-check relationships and clear `.pbi/cache.abf` after major model refactors.

## Validation Checklist

- Confirm the workbook path exists on the refresh machine, not only the developer machine.
- Confirm `definition/model.tmdl` includes `annotation PBI_QueryOrder`.
- Confirm every Excel parameter includes `meta [...]`, `lineageTag`, `PBI_NavigationStepName`, and `PBI_ResultType = Text`.
- Confirm every imported table, including `_Measures`, has `partition ... = m`, `mode: import`, and `annotation PBI_ResultType = Table`.
- Confirm the selector matches the real workbook object exactly: `Kind="Sheet"` for worksheets, `Kind="Table"` for named Excel tables.
- Confirm every referenced column exists after header promotion or table extraction.
- Confirm model column types match the final `Table.TransformColumnTypes` step.
- Confirm locale-sensitive dates and decimals are converted with an explicit culture when needed.
- Confirm relationships still validate after refresh.

## References

- `excel_import-excel-import-patterns.md`: parameter templates, worksheet and named-table import patterns, locale cleanup, `_Measures` partition template, failure modes, and recovery steps.

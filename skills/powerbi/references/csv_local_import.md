---
name: csv_local_import
description: Use when creating or editing a PBIP semantic model that imports CSV data from a local file or folder, especially when preserving Power BI parameter metadata and PBIP-safe import semantics.
---

# CSV Local Import

Use this when creating or editing a PBIP semantic model that imports CSV data from local CSV files or folders.

## Model Touchpoints

- `definition/database.tmdl`: compatibility metadata only; no CSV path definition here.
- `definition/model.tmdl`: model metadata, `ref table ...`, and `annotation PBI_QueryOrder`.
- `definition/expressions.tmdl`: CSV path parameters with full Power BI parameter metadata.
- `definition/tables/<table>.tmdl`: M partitions using `File.Contents(...)` or `Folder.Files(...)`.
- `definition/relationships.tmdl`: relationship graph after imported tables load.

## Core Guardrails

- In `definition/expressions.tmdl`, every CSV path parameter must be a real Power BI text parameter with `meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]`.
- Every CSV path parameter must also include `lineageTag`, `annotation PBI_NavigationStepName = Navigation`, and `annotation PBI_ResultType = Text`.
- Avoid hardcoded absolute paths inside partitions. Parameterize local paths and reuse the parameter in `File.Contents(...)` or `Folder.Files(...)`.
- In `definition/model.tmdl`, add `annotation PBI_QueryOrder = [...]` whenever CSV-backed M partitions are present. Order items as parameters first, then imported tables, then `_Measures`.
- Every imported table must have an explicit `partition <table> = m` block with `mode: import` and `annotation PBI_ResultType = Table`.
- Never leave `_Measures` partitionless. If it exists only for measures, still give it an empty import partition.
- Never name the measures table `Measures`; always use `_Measures`.
- Keep source tables on import semantics. Do not leave ambiguous structures that make Power BI interpret the model as composite.
- Declare model columns with explicit `dataType`, `summarizeBy`, and `sourceColumn`. Keep source and model names stable so report bindings continue to work.
- After major semantic-model refactors, delete `.pbi/cache.abf` if it exists before reopening the PBIP.

## Workflow

1. Add or update CSV path parameters in `definition/expressions.tmdl` with full Power BI parameter metadata.
2. Add or fix `annotation PBI_QueryOrder` in `definition/model.tmdl`.
3. Define each CSV-backed table with an import M partition in `definition/tables/<table>.tmdl`.
4. Keep `_Measures` as a real import table, even when it only contains measures.
5. Validate column typing, relationships, delimiter and encoding assumptions, then clear `.pbi/cache.abf` after major model surgery.

## Validation

- Confirm delimiter, encoding, quote style, and expected column count match the real files.
- Confirm every referenced column exists after header promotion and matches `sourceColumn`.
- Confirm the local path exists on the refresh machine, not only the developer machine.
- Confirm model column types match `Table.TransformColumnTypes(...)`.
- Confirm `definition/model.tmdl` includes `annotation PBI_QueryOrder`.
- Confirm every CSV path parameter includes `meta [...]`, `lineageTag`, `PBI_NavigationStepName`, and `PBI_ResultType = Text`.
- Confirm all imported tables, including `_Measures`, have `partition ... = m`, `mode: import`, and `annotation PBI_ResultType = Table`.
- Confirm relationships still validate after refresh.

## References

- `csv_local_import-patterns.md`: parameter, partition, and `_Measures` templates plus recovery notes.

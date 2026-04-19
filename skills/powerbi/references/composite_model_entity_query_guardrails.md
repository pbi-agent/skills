# Composite Model Entity Query Guardrails

Use this skill when a PBIP semantic model with local import data starts behaving like a composite model and validation fails with:

> Model validation failed. A composite model cannot be used with entity based query sources.

## Common Triggers

This failure is commonly triggered by one or more of:

1. A dedicated measures table created without an import partition.
2. Parameter expressions missing required Power BI metadata annotations.
3. Missing `PBI_QueryOrder` in `definition/model.tmdl`.
4. Stale local cache at `.pbi/cache.abf` after structural model changes.
5. Mixed or ambiguous storage semantics that make Power BI treat entity-based M sources as incompatible with the current model state.

## Mandatory Guardrails

### 1. Parameter query must be a proper Text parameter

File: `definition/expressions.tmdl`

```tmdl
expression csv_file_path = "C:/path/to/data.csv" meta [IsParameterQuery=true, IsParameterQueryRequired=true, Type="Text"]
	lineageTag: <guid>

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text
```

### 2. Model must include explicit query order

File: `definition/model.tmdl`

```tmdl
annotation PBI_QueryOrder = ["csv_file_path","FactTable","_Measures"]

ref table FactTable
ref table _Measures
```

Keep the parameter first, followed by import tables.

### 3. Every table partition must be `mode: import`

File: `definition/tables/<table>.tmdl`

```tmdl
partition FactTable = m
	mode: import
	source =
			let
			    Source = Csv.Document(File.Contents(csv_file_path), [Delimiter=";", Columns=<n>, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
			    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
			    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", { ... })
			in
			    #"Changed Type"

annotation PBI_ResultType = Table
```

### 4. Dedicated `_Measures` table must still have an import partition

Never leave a measure table partitionless.

File: `definition/tables/_Measures.tmdl`

```tmdl
table _Measures
	measure 'Example Measure' = SUM(FactTable[Amount])
		formatString: #,0.00

	partition _Measures = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
```

### 5. Reset cache after structural edits

If validation behaves inconsistently after major TMDL changes:

1. Delete `.pbi/cache.abf`.
2. Reopen the PBIP project.
3. Refresh the model.

## Build Checklist

- `expressions.tmdl` includes parameter metadata and `PBI_ResultType = Text`.
- `model.tmdl` includes `PBI_QueryOrder`.
- All tables have `partition ... mode: import`.
- `_Measures` exists, is named `_Measures`, and has an empty import partition.
- All import partitions end with `annotation PBI_ResultType = Table`.
- `.pbi/cache.abf` is cleared after large refactors.

## Anti-Patterns

- Table named `Measures` instead of `_Measures`.
- `_Measures` with measures only and no partition.
- Parameter expressions without Power BI annotations.
- Assuming cache invalidation will happen automatically after TMDL surgery.

## Recovery Sequence

1. Add the missing `_Measures` import partition.
2. Add `PBI_ResultType` annotations for `Text` and `Table`.
3. Add `PBI_QueryOrder`.
4. Remove `.pbi/cache.abf`.
5. Reopen the project and refresh.

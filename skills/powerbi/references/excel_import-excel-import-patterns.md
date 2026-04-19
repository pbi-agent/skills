# Excel Import Patterns

Use this reference when the main skill is active and you need the full legacy examples that were normalized out of `SKILL.md`.

## Parameterize Workbook And Selector Values

Avoid hardcoded absolute paths and selector literals in partitions. Create text parameters in `expressions.tmdl` and reuse them.

```tmdl
expression excel_workbook_path = "C:\\Data\\inbound\\orders.xlsx" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
	lineageTag: 11111111-1111-1111-1111-111111111111

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text

expression excel_sheet_name = "orders" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
	lineageTag: 22222222-2222-2222-2222-222222222222

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text

expression excel_table_name = "orders_tbl" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
	lineageTag: 33333333-3333-3333-3333-333333333333

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text
```

Use only the selectors you need. Do not keep both `excel_sheet_name` and `excel_table_name` unless the model genuinely uses both patterns.

## Model-Level Query Order

When Excel-backed partitions are present, declare query order explicitly in `definition/model.tmdl`.

```tmdl
model Model
	culture: en-US
	defaultPowerBIDataSourceVersion: powerBI_V3
	sourceQueryCulture: en-US

annotation PBI_QueryOrder = ["excel_workbook_path","excel_sheet_name","orders","_Measures"]

ref table orders
ref table _Measures
```

Keep parameters first, then imported tables, then `_Measures`.

## Worksheet Import Template

Use this when the workbook source is a worksheet tab.

```tmdl
partition orders = m
	mode: import
	source =
			let
			    Source = Excel.Workbook(File.Contents(excel_workbook_path), null, true),
			    orders_Sheet = Source{[Item=excel_sheet_name,Kind="Sheet"]}[Data],
			    #"Promoted Headers" = Table.PromoteHeaders(orders_Sheet, [PromoteAllScalars=true]),
			    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
			        {"SalesOrderID", Int64.Type},
			        {"OrderDate", type date},
			        {"CustomerID", Int64.Type},
			        {"Amount", type number}
			    })
			in
			    #"Changed Type"

annotation PBI_ResultType = Table
```

## Named Excel Table Import Template

Use this when the workbook contains a formal Excel table object.

```tmdl
partition orders = m
	mode: import
	source =
			let
			    Source = Excel.Workbook(File.Contents(excel_workbook_path), null, true),
			    OrdersTable = Source{[Item=excel_table_name,Kind="Table"]}[Data],
			    #"Changed Type" = Table.TransformColumnTypes(OrdersTable,{
			        {"SalesOrderID", Int64.Type},
			        {"OrderDate", type date},
			        {"CustomerID", Int64.Type},
			        {"Amount", type number}
			    })
			in
			    #"Changed Type"

annotation PBI_ResultType = Table
```

## Locale Cleanup Pattern

Excel often lands dates or decimals as text, especially when the workbook locale differs from the model locale. Use a two-step cleanup when needed.

```tmdl
partition orders = m
	mode: import
	source =
			let
			    Source = Excel.Workbook(File.Contents(excel_workbook_path), null, true),
			    orders_Sheet = Source{[Item=excel_sheet_name,Kind="Sheet"]}[Data],
			    #"Promoted Headers" = Table.PromoteHeaders(orders_Sheet, [PromoteAllScalars=true]),
			    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
			        {"OrderDate", type text},
			        {"SubTotal", type text},
			        {"TaxAmt", type text}
			    }),
			    #"Replaced Decimal Separator" = Table.ReplaceValue(#"Changed Type", ",", ".", Replacer.ReplaceText, {
			        "SubTotal",
			        "TaxAmt"
			    }),
			    #"Converted Numbers" = Table.TransformColumnTypes(#"Replaced Decimal Separator",{
			        {"SubTotal", type number},
			        {"TaxAmt", type number}
			    }, "en-US"),
			    #"Converted Dates" = Table.TransformColumnTypes(#"Converted Numbers",{
			        {"OrderDate", type date}
			    }, "en-US")
			in
			    #"Converted Dates"

annotation PBI_ResultType = Table
```

If the workbook is authored in another locale, set `sourceQueryCulture` and the conversion culture arguments deliberately instead of guessing.

## Dedicated Measures Table Pattern

Never leave `_Measures` without a partition.

```tmdl
table _Measures
	measure 'Sales Amount' = SUM(orders[Amount])
		formatString: $#,##0.00

	partition _Measures = m
		mode: import
		source =
				let
				    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
				    #"Changed Type" = Table.TransformColumnTypes(Source, {{"Column1", type text}}),
				    #"Removed Columns" = Table.RemoveColumns(#"Changed Type", {"Column1"})
				in
				    #"Removed Columns"

	annotation PBI_ResultType = Table
```

## Column And Model Definition Rules

- Declare each model column in the table TMDL with explicit `dataType`, `summarizeBy`, and `sourceColumn`.
- Keep source-to-model names stable; report bindings rely on exact field names.
- Set `formatString` explicitly for numeric and date business fields.
- Add date variations and relationships only when date hierarchy UX is needed.
- If worksheet headers are not stable, fix the workbook first or add a controlled rename step before final typing.

## Common Failure Modes

- Hardcoded workbook path: refresh fails on other machines.
- Wrong selector kind: the workbook has a named table but the M code looks for `Kind="Sheet"`, or the reverse.
- Wrong item name or casing: `Source{[Item=...,Kind=...]}` fails at refresh time.
- Headers not promoted on a sheet import: `sourceColumn` mapping fails.
- Locale mismatch: dates or decimals import as text or error during conversion.
- Mixed manual typing and implicit workbook typing: Power BI shows unstable inferred types across refreshes.
- `model.tmdl` omits `PBI_QueryOrder`, so Power BI misreads dependency order during validation.
- `_Measures` exists as measures-only metadata with no import partition.

## Quick Recovery Recipe

If the Excel-backed model breaks after edits:

1. Fix the semantic model first; do not try to solve it in report visual JSON.
2. Move any hardcoded workbook path or selector literal into `definition/expressions.tmdl`.
3. Add or fix `annotation PBI_QueryOrder` in `definition/model.tmdl`.
4. Make each Excel-backed table an explicit `mode: import` partition with `annotation PBI_ResultType = Table`.
5. Correct the `Item` and `Kind` selector and re-check the column typing steps.
6. Delete `.pbi/cache.abf`.
7. Reopen the PBIP and refresh the model.

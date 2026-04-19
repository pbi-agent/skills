# CSV Local Import Patterns

Use these templates when the base skill needs concrete PBIP examples.

## CSV Path Parameters

Keep CSV paths in `definition/expressions.tmdl`, not inline in partitions.

```tmdl
expression csv_file_path = "C:\\Data\\inbound\\sales.csv" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
	lineageTag: 11111111-1111-1111-1111-111111111111

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text

expression csv_folder_path = "C:\\Data\\inbound" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
	lineageTag: 22222222-2222-2222-2222-222222222222

	annotation PBI_NavigationStepName = Navigation

	annotation PBI_ResultType = Text
```

## Model-Level Query Order

When CSV-backed partitions are present, declare query order explicitly in `definition/model.tmdl`.

```tmdl
model Model
	culture: en-US
	defaultPowerBIDataSourceVersion: powerBI_V3
	sourceQueryCulture: en-US

annotation PBI_QueryOrder = ["csv_file_path","fact_sales","_Measures"]

ref table fact_sales
ref table _Measures
```

Keep parameters first, then imported tables, then `_Measures`.

## Single CSV File Partition Template

```tmdl
partition fact_sales = m
	mode: import
	source =
			let
			    Source = Csv.Document(
			        File.Contents(csv_file_path),
			        [Delimiter=",", Columns=4, Encoding=65001, QuoteStyle=QuoteStyle.Csv]
			    ),
			    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
			    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
			        {"order_id", Int64.Type},
			        {"order_date", type date},
			        {"amount", type number},
			        {"customer", type text}
			    })
			in
			    #"Changed Type"

annotation PBI_ResultType = Table
```

## Local Folder Partition Template

Use this when the source is a folder with many CSV files sharing the same schema.

```tmdl
partition fact_sales = m
	mode: import
	source =
			let
			    Source = Folder.Files(csv_folder_path),
			    #"Keep CSV" = Table.SelectRows(Source, each Text.Lower([Extension]) = ".csv"),
			    #"Parsed Tables" = List.Transform(#"Keep CSV"[Content], each Table.PromoteHeaders(Csv.Document(_, [Delimiter=",", Columns=4, Encoding=65001, QuoteStyle=QuoteStyle.Csv]), [PromoteAllScalars=true])),
			    #"Combined Data" = Table.Combine(#"Parsed Tables"),
			    #"Changed Type" = Table.TransformColumnTypes(#"Combined Data",{
			        {"order_id", Int64.Type},
			        {"order_date", type date},
			        {"amount", type number},
			        {"customer", type text}
			    })
			in
			    #"Changed Type"

annotation PBI_ResultType = Table
```

## Dedicated `_Measures` Table Pattern

Never leave `_Measures` without a partition.

```tmdl
table _Measures
	measure 'Sales Amount' = SUM(fact_sales[amount])
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

## Failure Modes

- Wrong delimiter or encoding shifts columns or produces mojibake.
- Header row not promoted, so `sourceColumn` mapping breaks.
- Hardcoded user path works on one machine and fails on another.
- Folder import contains mixed schemas, so combine or type steps fail.
- Local path is used in the Service without a gateway.
- Parameter expression stops at `meta [...]` and omits `lineageTag` or Power BI annotations.
- `model.tmdl` omits `PBI_QueryOrder`, so Power BI misreads storage semantics during validation.
- `_Measures` exists as measures-only metadata with no import partition.

## Recovery

If composite-model validation errors appear:

1. Fix the semantic model first, not report visual JSON.
2. Add missing parameter metadata and annotations in `definition/expressions.tmdl`.
3. Add or fix `annotation PBI_QueryOrder` in `definition/model.tmdl`.
4. Add missing `mode: import` partitions and `annotation PBI_ResultType = Table`, including `_Measures`.
5. Delete `.pbi/cache.abf`.
6. Reopen the PBIP and refresh the model.

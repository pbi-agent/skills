# TMDL Modeling

Use this when creating or editing semantic model files (`*.tmdl`) in Power BI PBIP projects.

## Model File Layout

- `definition/database.tmdl`: database compatibility level and root database metadata.
- `definition/model.tmdl`: model metadata plus table refs and culture refs.
- `definition/expressions.tmdl`: shared M parameters such as environment or data source parameters.
- `definition/relationships.tmdl`: all relationships declared centrally.
- `definition/tables/*.tmdl`: one table per file with columns, measures, and partitions.
- `definition/cultures/<culture>.tmdl`: linguistic metadata.

## Core Guardrails

- Use tab-indented TMDL blocks. Do not convert nested indentation to spaces.
- Keep dedicated measure tables when the model grows. Name them `_Measures`. Never use bare `Measures`; TOM reserves it and Power BI Desktop will reject the project.
- Keep measure usage explicit. Do not replace measures with implicit aggregation behavior in visuals or metadata.
- Set `formatString`, `summarizeBy`, and `dataType` explicitly on business columns and measures.
- Use parameterized M source code in partitions for environment portability.
- Keep relationships explicit in `relationships.tmdl`.
- Preserve existing `lineageTag` values unless you intentionally recreate metadata.
- Keep object names stable. `queryRef`, report filters, drillthrough targets, bookmarks, and field bindings depend on exact names.
- Keep `fromColumn` and `toColumn` on model column names, not display names.

## TMDL Syntax

- Root object declarations:
  - `model Model`
  - `database`
  - `table <name>`
  - `relationship <id>`
  - `expression <name> = <value>`
- Nested properties use one-tab indent:
  - `dataType: int64`
  - `formatString: 0`
  - `summarizeBy: none`
- Flags are bare keywords, not `: true`:
  - `isHidden`
  - `isPrivate`
  - `isDefault`
- DAX calculated column: `column <calc_column> = <DAX expression>`
- DAX measure: `measure '<metric_name>' = <DAX expression>`
- Source mapping: `sourceColumn: <source_column_name>`
- Relationship endpoints:
  - `fromColumn: <from_table>.<from_column>`
  - `toColumn: <to_table>.<to_column>`
- Partition block:
  - `partition <table_name> = m`
  - `mode: import`
  - `source = <M code>`
- Annotation example: `annotation PBI_ResultType = Table`

## Minimal Table Template

```tmdl
table dim_example
	lineageTag: <guid>

	column key_id
		dataType: string
		summarizeBy: none
		sourceColumn: key_id

	measure '# Rows' = COUNTROWS(dim_example)
		formatString: 0

	partition dim_example = m
		mode: import
		source =
				let
				    Source = Value.NativeQuery(
				        <connector_call_using_parameter>,
				        "SELECT key_id FROM <schema_or_dataset>.dim_example_view",
				        null,
				        [EnableFolding=true]
				    )
				in
				    Source
```

## Date Variation Template

```tmdl
column date_column_name
	dataType: dateTime
	formatString: Short Date
	summarizeBy: none
	sourceColumn: <date_column>

	variation Variation
		isDefault
		relationship: <relationship-id>
		defaultHierarchy: LocalDateTable_<guid>.'Date Hierarchy'
```

## Reserved Table Names

Never use these table names directly:

| Reserved name | Safe alternative |
| --- | --- |
| `Measures` | `_Measures` |
| `Model` | `_Model` |
| `Database` | `_Database` |
| `Server` | `_Server` |
| `DataSource` | `_DataSource` |
| `Role` | `_Role` |

When you need a measures-only table, always use `_Measures`.

## Common Mistakes

- Do not rename tables, columns, or measures casually.
- Do not remove `lineageTag` from existing objects.
- Do not change field case without updating every report reference.
- Do not let `summarizeBy` fall back to defaults on business columns.
- Do not change drillthrough or filter fields unless report bindings are updated too.
- Do not store partitions with hard-coded environment-specific sources when parameters already exist.

## Import Partition Template

```tmdl
partition <table_name> = m
	mode: import
	source =
			let
			    Source = Value.NativeQuery(
			        <connector_call_using_parameter>,
			        "SELECT ... FROM <schema_or_dataset>.<view_or_table>",
			        null,
			        [EnableFolding=true]
			    )
			in
			    Source
```

## Relationship Template

```tmdl
relationship <id>
	fromColumn: <from_table>.<from_column>
	toColumn: <to_table>.<to_column>
```

## Checklist Before Save

- Keep names stable for `queryRef` and report bindings.
- Keep `lineageTag` entries when editing existing objects.
- Keep `summarizeBy` explicit on business columns.
- Keep measures explicit and housed in `_Measures` when using a dedicated measure table.
- Keep drillthrough and filter bindings aligned with any model changes.

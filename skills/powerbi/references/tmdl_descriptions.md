---
name: tmdl_descriptions
description: Use when adding or editing table, column, or measure descriptions in TMDL semantic model files.
---

# TMDL Descriptions

Use this when adding or editing descriptions in TMDL files (`*.tmdl`).

## Core Rule

In TMDL, descriptions are written as triple-slash lines directly above the object they describe. The `///` text becomes the object's `description` metadata.

```tmdl
/// Shipment Data Table Description
table ShipmentData
	lineageTag: a8081e76-2aa9-43f4-8bee-1869c7e4561f

	/// Creation datetime of the ASN record
	column ASN_CREATION_DATETIME
		dataType: dateTime

	/// Total number of rows in the shipment table
	measure '# Shipments' = COUNTROWS(ShipmentData)
		formatString: 0
```

## Placement Rules

- Put the `///` line immediately above the `table`, `column`, or `measure` declaration.
- Do not leave a blank line between the `///` line and the declaration.
- Match the indentation of the object being described:
  - no indentation for `table`
  - one tab inside the table for `column` and `measure`
- Use `///`, not `//`. Only `///` writes description metadata.

## Authoring Guidance

- Keep descriptions durable and business-facing. Describe meaning, purpose, or usage, not temporary implementation notes.
- For longer descriptions, use consecutive `///` lines with the same indentation.
- When editing existing descriptions, preserve surrounding TMDL structure and only change the description lines that belong to the target object.
- Descriptions surface in Power BI Desktop metadata experiences, so write them as end-user documentation.

## Checklist

- Confirm the description is attached to the intended object.
- Confirm indentation matches the target declaration.
- Confirm there is no blank line between `///` and the object.
- Confirm `///` is used for every description line.

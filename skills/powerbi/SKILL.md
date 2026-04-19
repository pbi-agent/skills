---
name: powerbi
description: Use when creating, editing, or reviewing Power BI PBIP projects, including semantic models, imports, report structure, navigation, filters, theming, visuals, and durable Power BI authoring lessons.
---

# Power BI

Use this when the task touches any Power BI PBIP artifact or behavior.

## Load Only The Relevant References

- Semantic model structure, measures, relationships, partitions: `references/tmdl_modeling.md`
- Semantic model descriptions: `references/tmdl_descriptions.md`
- CSV imports and parameter-safe local file patterns: `references/csv_local_import.md`, then `references/csv_local_import-patterns.md` when examples are needed
- Excel imports: `references/excel_import.md`, then `references/excel_import-excel-import-patterns.md` when examples are needed
- Composite model failures involving entity-based sources: `references/composite_model_entity_query_guardrails.md`
- DAX UDF authoring or review: `references/dax_udf.md`
- Report architecture and page layout: `references/report_structure.md`
- Filter flow across pages, slicers, and drillthrough: `references/filter_propagation.md`
- Navigation, bookmarks, popup states, and back paths: `references/navigation_bookmarks.md`
- Theme tokens and branding assets: `references/theme_branding.md`
- Visual container JSON shape and layout metadata: `references/visual_container_schema.md`
- Action buttons: `references/action_button.md`, then `references/action_button-skeleton.md` for a starting skeleton
- Bar charts: `references/bar_chart_visual.md`, then `references/bar_chart_visual-bar-chart-patterns.md`
- Cards: `references/card_visual.md`, then `references/card_visual-card-patterns.md`
- Slicers: `references/slicer_visual.md`, then `references/slicer_visual-slicer-patterns.md`
- Tables: `references/table_visual.md`
- Distilling a durable lesson back into the catalog: `references/skill_generator.md`

## Cross-Cutting Guardrails

- Keep PBIP-safe metadata stable unless the task explicitly requires recreation.
- Preserve exact field names, casing, `queryRef` values, and binding targets across model and report edits.
- Prefer explicit measures and keep dedicated measure tables named `_Measures`.
- Keep relationships, page filters, slicers, visual filters, drillthrough bindings, and bookmarks aligned as one system.
- Load the smallest reference set that covers the task instead of pulling in the whole catalog.

## General Instructions

- Use explicit measures in visuals; never rely on implicit aggregations.
- Dedicated measures table must be named `_Measures`, never `Measures`.
- Never modify auto-generated date tables (`DateTableTemplate_*`, `LocalDateTable_*`); skip their descriptions because their TMDL schema is restricted.
- Distribute visuals intentionally across the canvas unless the user specifies a layout.
- Style priority: explicit user instruction > existing project or brand conventions > skill default preset.

## Working Flow

1. Identify the artifact type: TMDL, import definition, report/page JSON, or visual JSON.
2. Open the minimum matching reference files for that artifact and behavior.
3. Apply the required schema keys and guardrails exactly; Power BI is brittle about names, bindings, and metadata shape.
4. Validate connected artifacts that can break indirectly, especially filters, navigation, and model-bound visuals.
5. If the task reveals a new recurring rule, consult `references/skill_generator.md` and fold that lesson back into this skill.

## Reference Groups

- Semantic modeling: `tmdl_modeling`, `tmdl_descriptions`, `csv_local_import`, `excel_import`, `composite_model_entity_query_guardrails`, `dax_udf`
- Report behavior: `report_structure`, `filter_propagation`, `navigation_bookmarks`, `theme_branding`
- Visual authoring: `visual_container_schema`, `action_button`, `bar_chart_visual`, `card_visual`, `slicer_visual`, `table_visual`
- Catalog maintenance: `skill_generator`

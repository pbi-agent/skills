---
name: filter_propagation
description: Use when wiring or repairing Power BI page-to-page filter behavior across slicers, drillthrough, page filters, and visual filters.
---

# Filter Propagation

Use this when wiring page-to-page filtering behavior in Power BI reports, especially for slicers, drillthrough, page filters, and visual filters.

## Propagation Model

1. Model relationships propagate filter context across tables.
2. Page-level filters (`page.json -> filterConfig`) apply to all visuals on a page.
3. Synced slicers (`syncGroup`) share user selections across pages in the same group.
4. Visual filters (`visual.json -> filterConfig`) add local constraints.
5. Drillthrough binding (`pageBinding`) injects source context into target page filters.
6. Bookmarks can restore or snapshot visual and filter state.

## Recommended Filter Topology

- Global analytical pages:
  - `date` slicer sync group, for example `date_main`
  - `entity/site` slicer sync group, for example `site_main`
  - `system/channel` slicer sync group, for example `system_main`
- Detail pages:
  - drillthrough filters for one key or multiple keys
  - optional extra user slicers scoped to the detail experience only

## Drillthrough Context Pattern

- Source visual or button:
  - `visualLink.type = 'Drillthrough'`
  - `drillthroughSection = '<target_page_id>'`
- Target page:
  - `filterConfig.filters[*].howCreated = "Drillthrough"`
  - `pageBinding.type = "Drillthrough"`
  - `pageBinding.parameters[*].boundFilter` mapped to `fieldExpr`
- Result:
  - the selected source context is injected into target filters

## Implementation Rules

- For synced slicers:
  - use the same field expression
  - use the same `syncGroup.groupName`
  - keep `fieldChanges = true` and `filterChanges = true`
- For drillthrough:
  - keep each `boundFilter` id valid and local to the target page
  - keep `fieldExpr` identical to the bound filter field
- For fixed-scope visuals:
  - use visual-level categorical filters in `visual.json -> filterConfig`

## Validation Checklist

1. Change a synced slicer on page A and verify the same selection appears on page B.
2. Trigger drillthrough from multiple visuals and verify the target page receives the same filter behavior.
3. Verify bookmarks used for UI state do not unintentionally reset core slicer filters.
4. Verify relationship direction and cardinality support the intended propagation path.

## Failure Modes

- New slicer with the wrong group name: the filter does not sync.
- Same group name with a different field: behavior becomes inconsistent or undefined.
- Measure or column rename in the model without JSON updates: visuals and drillthrough bindings break.

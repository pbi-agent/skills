---
name: slicer_visual
description: Use when creating or repairing Power BI slicer visuals, especially synced slicers, date-range filters, and dropdown filter interactions.
---

# Slicer Visual

Use this when creating or repairing Power BI slicer visuals, especially synced slicers, date filters, and dropdown filter interactions.

## Required Structure

- Set `visual.visualType = "slicer"`.
- Bind exactly one field in `visual.query.queryState.Values.projections`.
- Add `syncGroup` when the slicer must stay aligned across pages.
- Keep `syncGroup.groupName` dedicated to one field only. Do not reuse the same group name for different fields.
- Use either `objects.header` or `visualContainerObjects.title` for labeling, never both in the same slicer.
- Add `query.sortDefinition` when a date slicer needs explicit ordering.

## Interaction Modes

- Date range slicer: `objects.data.properties.mode = 'Between'`.
- Dropdown slicer: `objects.data.properties.mode = 'Dropdown'`.
- For dropdown pages that should filter themselves, set `objects.general.properties.selfFilterEnabled = true`.
- Optional `startDate` and `endDate` are valid for intentional default windows on Between slicers.

## Default Pattern

- Header and label:
  - default `objects.header.show = false` for cleaner filter rows
  - if a visible label is needed, enable header or title, not both
- Mode:
  - date slicers default to `'Between'`
  - entity or system slicers default to `'Dropdown'`
- Container style baseline:
  - `visualContainerObjects.background.show = true`
  - `visualContainerObjects.background.transparency = 0D` or `50D` for lighter overlays
  - `visualContainerObjects.border.radius = 5D`
  - `visualContainerObjects.border.width = 1D`
  - keep `border.show = false` unless the slicer is in a dedicated filter panel
  - keep `dropShadow.show = false` unless the slicer must read as a floating filter card
- Between mode slider color can use the report accent, for example `'#B6975A'`.
- Default size to avoid cropping: `"height": 88`, `"width": 228`.

## Sync Group Rules

- Reuse the existing `syncGroup.groupName` when editing an established cross-page filter.
- Keep the field expression identical across every slicer in the same sync group.
- Keep `fieldChanges = true` and `filterChanges = true`.
- Keep filter order stable across pages so users see the same sequence, usually date, then site, then system.
- Keep slicer size and position consistent across pages to preserve scan speed and muscle memory.

## Validation

1. Change a synced slicer on page A and verify the same selection appears on every participating page.
2. Confirm each sync group is attached to only one field expression.
3. Confirm only one label system is active: header or title.
4. Check long dropdown values for clipping and widen the slicer if needed.
5. For Between slicers, verify date order and slider defaults behave as intended.

## Failure Modes

- New slicer with a new group name on an existing shared field: synchronization breaks.
- Same group name reused for a different field: behavior becomes inconsistent.
- Header and title both enabled: duplicate labeling chrome appears.
- Narrow dropdown slicer: search and value selection become hard to use.

## Reference

- See `slicer_visual-slicer-patterns.md` for a full slicer container skeleton and synchronization checklist.

# Bar Chart Visual

Use this skill when building or editing a Power BI bar-chart visual container.

For the full legacy skeleton and object examples, see `bar_chart_visual-bar-chart-patterns.md`.

## Supported Visual Types

- `barChart`
- `clusteredBarChart`
- `stackedBarChart`
- `hundredPercentStackedBarChart`

## Required Query Shape

- Set `visual.visualType` to one of the supported bar-chart types.
- Keep at least one categorical field in `visual.query.queryState.Category.projections`.
- Keep one or more measures in `visual.query.queryState.Y.projections`.
- Use `visual.query.sortDefinition` when the visual needs explicit sort behavior.
- Use `filterConfig.filters` only for fixed-scope visual filtering layered over page or report filters.

## Common Object Blocks

- `valueAxis`: show or hide the axis, axis title, and display units.
- `categoryAxis`: label formatting and density control.
- `labels`: visibility and label precision.
- `dataPoint`: per-series fill colors using `selector.metadata`.
- `legend`: visibility and placement.
- `visualContainerObjects`: title, background, border, and drop shadow.

## Default Styling Pattern

- Use a card-like container with `visualContainerObjects.background.show = true`, `transparency = 0D`, `border.show = true`, `border.radius = 5D` or `6D`, and `border.width = 1D`.
- Keep shadows subtle. Default `visualContainerObjects.dropShadow.show = false`; if enabled, keep blur, spread, and transparency soft.
- Use selector-scoped status colors in `objects.dataPoint` when multiple measures are shown. Keep positive or OK states green, such as `'#109E42'`, and negative or KO states red, such as `'#CB381B'`, unless the report theme defines other semantic colors.
- Keep labels compact with `objects.labels.show = true`, `objects.labels.detailLabelPrecision = 0L`, and `objects.valueAxis.showAxisTitle = false` on dense dashboards.

## UX Guardrails

- Keep category counts reasonable, usually around 8 to 12, so bars stay readable.
- Keep color semantics stable across pages.
- Hide the legend when the chart shows one obvious measure and direct labels are clearer.
- Reuse the same border radius and border width used by nearby cards and tables on the same page.

## Schema Guardrails

- Keep field-node casing exact: `Measure`, `Column`, `Expression`, `SourceRef`, `Property`.
- Keep every `queryRef` aligned with the projected field it describes.
- In stacked and 100% stacked charts, keep series ordering consistent across related pages.
- Prefer selector-scoped formatting over global formatting when the visual contains multiple measures.

## Validation

- Confirm the visual type is one of the supported bar-chart types.
- Confirm `Category.projections` and `Y.projections` are both populated.
- Confirm `dataPoint.selector.metadata` matches the intended measure when using per-series colors.
- Confirm sorting, legend usage, and label precision still fit the available space.

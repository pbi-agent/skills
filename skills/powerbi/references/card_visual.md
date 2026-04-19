# Card Visual

Use when editing Power BI card patterns for KPI tiles, status cards, or single-value callouts.

## Visual Type Choice

- Use `cardVisual` for legacy or multi-tile cards.
- Use `card` for modern single-value cards.
- Do not switch the visual type in place unless you migrate the full object and query schema.

## Required Query Structure

- For `cardVisual`, keep `visual.query.queryState.Data.projections`.
- For `card`, keep `visual.query.queryState.Values.projections`.
- Keep query expression casing exact: `Measure`, `Column`, `Expression`, `SourceRef`, `Property`.
- Keep `queryRef` and `Property` names exact, including spaces and symbols.

## Durable `cardVisual` Object Buckets

- `layout` for orientation, alignment, and tile behavior
- `label` for text placement and per-field label overrides
- `value` for font, color, alignment, and per-field value overrides
- `accentBar` for status strips
- `padding`, `spacing`, `outline`, `shapeCustomRectangle`
- `fillCustom` for conditional fill from a color field
- `visualContainerObjects` for `title`, `background`, `border`, and `dropShadow`

## Default Styling Pattern

- Rounded tiles usually use `shapeCustomRectangle.rectangleRoundedCurve = 5L` or `6L`.
- Container border usually uses `visualContainerObjects.border.radius = 5D` and `width = 1D` or `2D`.
- Framed cards normally enable `visualContainerObjects.background.show = true`.
- Use `background.transparency = 0D` for solid cards and `50D` for lighter overlays.
- Keep `dropShadow.show = false` by default; when present, keep it subtle with `preset = 'Center'` and `transparency = 70L`.
- Typical theme spacing uses `paddingUniform = 12` and `verticalSpacing = 2`.
- Typical typography keeps labels around `8D` to `11D` and values around `12D` with the theme semibold family.

## Status and KPI Rules

- Use `fillCustom.fillColor` with an aggregation expression when the card color comes from data.
- Prefer explicit status formatting over relying on theme defaults for threshold or alert cards.
- Preserve `selector.metadata` entries when editing formatting on multi-field `cardVisual` tiles.
- If a card is only a status indicator, intentionally hide redundant value or label text and rely on fill plus tooltip.

## UX Guardrails

- Keep density controlled; a stable pattern is `maxTiles = 3`.
- Use one hierarchy per row: primary KPI cards, then secondary cards, then indicator chips.
- Keep rounding, border logic, and color meaning consistent across cards in the same report.
- Enable either `title` or `categoryLabels`, not both; prefer `categoryLabels` unless the page pattern says otherwise.

## Validation

- Confirm the visual type matches the expected query branch: `Data` for `cardVisual`, `Values` for `card`.
- Confirm formatting edits did not remove `selector.metadata` from multi-field cards.
- Confirm the callout measure or column still resolves through the exact `queryRef` and `Property`.
- For a ready-made example, reuse the copied legacy pattern in `card_visual-card-patterns.md`.

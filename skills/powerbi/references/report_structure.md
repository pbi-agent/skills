# Report Structure

Use when creating or refactoring report architecture (`report.json`, `pages/*.json`, visual containers) for any domain.

## Core Layout Pattern

- Set every page canvas to `1280 x 720` with `displayOption: "FitToPage"`.
- Keep one visible landing page (for example `<home_page_id>`).
- Hide most analytic or detail pages in app mode with `"visibility": "HiddenInViewMode"` when they are reached through navigation or drillthrough.
- Use `ResourcePackageItem` backgrounds backed by `RegisteredResources`.
- Keep page order centralized in `definition/pages/pages.json`.

## Page Connection Graph

- Route from the landing page to analysis pages with navigators or buttons.
- Add explicit `PageNavigation` return actions on hidden analysis/detail pages.
- Use this drillthrough chain:
  - analysis pages -> detail list pages
  - detail list pages -> canonical detail page via a `Drillthrough` action button
- Put a `Back` action button on every drillthrough/detail page.

## Filter Propagation Order

1. Semantic model relationships in `relationships.tmdl`
2. Page-level filters in `page.json -> filterConfig.filters`
3. Slicer state, including synced slicers via `syncGroup`
4. Visual-level filters in `visual.json -> filterConfig.filters`
5. Drillthrough parameter binding in `pageBinding`
6. Bookmark restore and hide state

## Drillthrough Binding Pattern

- In the target page `page.json`, declare drillthrough filters with `filterConfig.filters[*].howCreated = "Drillthrough"`.
- Bind each drillthrough filter through `pageBinding.parameters`:
  - `boundFilter` must reference a filter id from the same file
  - `fieldExpr` must exactly match the source field expression
- Supported durable patterns:
  - single key drillthrough: `<dimension>.<key>`
  - composite key drillthrough: `<key1>`, `<key2>`, `<key3>`
  - KPI or value drillthrough: `<measure_table>.<measure_name>`

## Synced Filter Strategy

- Create one `syncGroup` per shared field, for example:
  - `date_main` -> `<date_table>.<date_column>`
  - `entity_main` -> `<entity_table>.<entity_column>`
  - `system_main` -> `<system_table>.<system_column>`
- Reuse the same group name only for the same field across participating pages.
- Use a different group name when isolating alternate or legacy behavior.

## Visual Grouping Pattern

- Use `visualGroup` containers for zones such as header, popup, or detail block.
- Set `parentGroupName` on child visuals.
- Use bookmarks to toggle `visualContainerGroups.<groupId>.isHidden` when opening or closing whole popup groups.

## Build Order

1. Create pages, order, and backgrounds.
2. Add navigators and return links.
3. Add slicers with stable `syncGroup` names before charts.
4. Add visuals and per-visual filters.
5. Add drillthrough target pages with `filterConfig` and `pageBinding`.
6. Add drillthrough and back buttons.
7. Add bookmarks for popup and filter-mode toggles.

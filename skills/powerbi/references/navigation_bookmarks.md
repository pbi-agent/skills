# Navigation And Bookmarks

Use this skill when implementing page navigation, drillthrough actions, and bookmark-driven UX states.

## Action Button Link Types

Set in `visual.visualContainerObjects.visualLink[0].properties.type`:

- `'Back'`: return to the previous page.
- `'PageNavigation'`: requires `navigationSection`.
- `'Drillthrough'`: requires `drillthroughSection`; `disabledTooltip` is optional.
- `'Bookmark'`: requires `bookmark`.

## Generic Connection Rules

- Use one visible landing page and hide operational or detail pages when needed.
- Add explicit return paths to the landing page with `PageNavigation` from hidden pages.
- Use `Drillthrough` buttons for contextual jumps into details.
- Add `Back` buttons on drillthrough targets for a predictable return flow.

## Navigator Visuals

- `pageNavigator`: control visible pages with `objects.pages[].selector.id` and `showPage`.
- `bookmarkNavigator`: switch bookmarks using:
  - `objects.bookmarks[0].properties.bookmarkGroup`
  - `objects.bookmarks[0].properties.selectedBookmark`

## Validation Checks

- Never leave `navigationSection` empty (`''`) unless the visual is intentionally a no-op clickable asset.
- Keep `drillthroughSection` page ids stable with `pageBinding` on the target page.
- When pages are renamed, update both:
  - page metadata in `page.json`
  - link target ids in `visualLink`, `pageNavigator`, and bookmark payloads

## Bookmark Files Pattern

- `definition/bookmarks/bookmarks.json`: bookmark groups and hierarchy metadata.
- `<id>.bookmark.json`: actual state snapshots.
- Use `options.targetVisualNames` for scoped updates.
- Use `explorationState.sections.<page>.visualContainers.<visual>.singleVisual.display.mode = "hidden"` for per-visual toggles.
- Use `explorationState.sections.<page>.visualContainerGroups.<groupId>.isHidden` for popup or group show-hide.
- Bookmark snapshots can include filter state; keep `suppressData: true` when the bookmark is for UI state only.

## Popup Pattern

1. Create a `visualGroup` for popup elements.
2. Add an open button with `type: 'Bookmark'` pointing to the show bookmark id.
3. Add a close button or image with `type: 'Bookmark'` pointing to the hide bookmark id.
4. In the show and hide bookmark files, toggle `visualContainerGroups.<group>.isHidden`.
5. Keep popup controls in `targetVisualNames` so unrelated visuals are not reset.

## Recommended Naming Placeholders

- Landing page id: `<home_page_id>`
- Drillthrough page id: `<detail_page_id>`
- Bookmark ids: `<bookmark_show_id>`, `<bookmark_hide_id>`, `<bookmark_state_id>`

## Guardrail

- Keep bookmark ids stable once linked from buttons or navigators; changing ids breaks navigation.

---
name: action_button
description: Use when creating or editing a Power BI action button visual that triggers back navigation, page navigation, drillthrough, bookmarks, or similar linked interactions.
---

# Action Button

Use this when creating or editing a Power BI `actionButton` visual in report JSON.

## Core Structure

- Keep `visual.visualType` set to `actionButton`.
- Define button layout in `position` with stable `x`, `y`, `z`, `height`, `width`, and `tabOrder`.
- Put button chrome in `visual.objects`, typically `icon` and `text`.
- Put the action itself in `visual.visualContainerObjects.visualLink`.
- Keep a descriptive authoring title in `visual.visualContainerObjects.title`.

## Schema Guardrails

- Use `selector.id = "default"` for the concrete `icon` and `text` property blocks that style the default state.
- Keep `objects.text` split into:
  - a visibility block for `show`
  - a default-state block for `text`, margins, alignment, and font settings
- Keep literal values in the existing Power BI expression wrapper format, for example `{"expr":{"Literal":{"Value":"true"}}}`.
- For a back button, set `visualContainerObjects.visualLink[0].properties.type` to `'Back'` and do not add a page or bookmark target.
- For other actions, keep the `visualLink.type` aligned with the intended target payload, such as page navigation, drillthrough, or bookmark metadata.
- Preserve `drillFilterOtherVisuals` deliberately. If you change it, treat that as an interaction change rather than cosmetic cleanup.

## Workflow

1. Start from the minimal action button skeleton in `action_button-skeleton.md`.
2. Set the button `name` and `position` values to fit the page layout.
3. Update the visible label, icon, margins, and alignment under the default selectors.
4. Set `visualLink` to the intended action type and required target metadata.
5. Keep the internal title text descriptive so the button remains easy to identify in report artifacts.

## Validation

- Confirm the visual still declares `visualType: "actionButton"`.
- Confirm the visible text and icon blocks use the default selector where required.
- Confirm the `visualLink.type` matches the intended behavior.
- Confirm any referenced page, drillthrough target, or bookmark id exists and is stable.
- Confirm `tabOrder` and button bounds still make sense for keyboard and page navigation.

## References

- `action_button-skeleton.md`: copied legacy action button skeleton normalized into the official skill layout.

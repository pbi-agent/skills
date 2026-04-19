---
name: visual_container_schema
description: Use when creating or editing Power BI visual container JSON files for visuals, visual groups, layout bounds, or visual-level metadata.
---

# Visual Container Schema

Use when editing a visual container JSON file on a report page.

Each visual container file defines exactly one visual or one visual group on a page.

## Core Shape

- Keep `$schema`, `name`, and `position` on every container.
- Include exactly one of:
  - `visual` for a real visual
  - `visualGroup` for a grouping container
- Use `parentGroupName` only when nesting the container under a parent group.
- Use `filterConfig` only for visual-level filters layered on top of page or report filters.
- Use `isHidden` to hide the container without removing it.
- Use `annotations` only for durable metadata key-value pairs.

## Required Fields

- `$schema`: schema URI string
- `name`: unique visual id on the page, max 50 characters
- `position`: object with layout bounds

## Position Rules

`position` must include `x`, `y`, `width`, and `height` as numbers.

Supported optional fields:

- `z`: stacking order, where larger values render on top
- `tabOrder`: keyboard navigation order
- `angle`: rotation angle

Keep layout values internally consistent:

- `x` and `y` place the top-left corner
- `width` and `height` size the container
- keep `x + width` inside the page width
- keep `y + height` inside the page height

## Visual Group Rules

`visualGroup` requires:

- `displayName`
- `groupMode`

Supported `groupMode` values:

- `ScaleMode`: children scale with the group and preserve aspect ratio
- `ScrollMode`: children keep their size and overflow through scrolling

Optional group formatting belongs in `objects` using arrays of `{ selector?, properties }` entries. Durable buckets include:

- `background`
- `lockAspect`
- `general`

## Annotation Shape

Each annotation must be:

```json
{ "name": "<unique-key>", "value": "<string-value>" }
```

Both `name` and `value` are required.

## Guardrails

- Never put both `visual` and `visualGroup` in the same container.
- Never omit both `visual` and `visualGroup`.
- Keep `name` unique within the page.
- Preserve existing container ids when editing live reports so bookmarks, selections, and bindings stay valid.
- When grouping visuals, set `parentGroupName` on child containers instead of duplicating group state into each child.
- Keep visual-level filters in `filterConfig`; do not use annotations as a substitute for real filter state.

## Validation

- Confirm the file describes one visual or one visual group, not both.
- Confirm `position.x`, `position.y`, `position.width`, and `position.height` are present and numeric.
- Confirm the container stays within page bounds.
- Confirm `visualGroup.groupMode` is `ScaleMode` or `ScrollMode` when a group is used.
- Confirm every annotation has both `name` and `value`.

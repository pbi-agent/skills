---
name: theme_branding
description: Use when defining or updating reusable Power BI theme tokens, typography, and packaged branding assets for PBIP reports.
---

# Theme And Branding

Use this when defining reusable branding tokens and visual defaults for a Power BI report.

## Theme Source

- Keep theme JSON in `StaticResources/SharedResources/BaseThemes/<theme-name>.json`.
- Reference it from `report.json` through `themeCollection.baseTheme`.
- Keep report-level overrides minimal; prefer theme-driven defaults over visual-by-visual overrides.

## Recommended Token System

Define a stable token set once, then consume those tokens across visual styles:

- `primary`, `secondary`, `accent`
- `positive`, `warning`, `negative`
- `textPrimary`, `textSecondary`, `surface`, `surfaceAlt`, `border`

## Common Visual Styling Pattern

- Border on most analytic visuals:
  - `show: true`
  - `radius: 5D` or `6D`
  - `width: 1D` or `2D`
  - `color`: token-driven, usually `border`
- Background:
  - analytic visuals usually keep `show: true` with low transparency
  - decorative or navigation layers often keep `show: false`
- Drop shadow:
  - disable by default
  - enable only on emphasis surfaces that need extra separation

## Typography Pattern

- Define theme `textClasses` such as `callout`, `title`, `header`, and `label` with explicit `fontFace` and size.
- Keep one primary UI font family and at most one accent font family.
- Override typography at the visual level only for a specific UX requirement.

## UX Asset Pattern

- Store logos, icons, and background images in `RegisteredResources`.
- Bind assets through `ResourcePackageItem` in `page.json` or `visual.json`.
- Avoid external URLs so packaging stays deterministic and portable.

## Guardrails

- Favor shared theme tokens over repeated literal colors or per-visual formatting drift.
- Keep branding defaults reusable across pages instead of tuning each page independently.
- Use packaged resources for brand assets so PBIP output remains self-contained.

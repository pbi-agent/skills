# Rule Catalog: Quality, Metadata, And Scoring

Use this reference for DAX Quality, Metadata, Anti-Patterns, and final scoring.

## DAX Quality

Weight: `1.5`

- `DAX-01` Sev 3: `FILTER` on an entire table inside `CALCULATE`.
- `DAX-02` Sev 2: Division operator used where `DIVIDE()` is safer.
- `DAX-03` Sev 2: `FORMAT()` in measures instead of `formatString`.
- `DAX-04` Sev 2: `IFERROR` or `ISERROR` usage.
- `DAX-05` Sev 2: `EARLIER` or `EARLIEST` usage.
- `DAX-06` Sev 2: Nested `IF` four levels deep or more.
- `DAX-07` Sev 2: `ALL()` on an entire table without column scope.
- `DAX-08` Sev 1: `COUNTROWS(VALUES())` instead of `DISTINCTCOUNT`.
- `DAX-09` Sev 1: `HASONEVALUE` plus `VALUES` instead of `SELECTEDVALUE`.
- `DAX-10` Sev 1: Iterator over a single column instead of a direct
  aggregator.
- `DAX-11` Sev 3: Nested iterators such as `SUMX(..., SUMX(...))`.
- `DAX-12` Sev 2: Measure longer than 200 characters with no `VAR` and
  repeated sub-expressions.
- `DAX-13` Sev 2: Measure complexity above 30 lines, 1000 characters, or 10
  distinct DAX functions.
- `DAX-14` Sev 2: Nested `CALCULATE`.
- `DAX-15` Sev 2: Measure dependency chain deeper than five levels; elevate to
  Sev 3 above ten.

## Metadata And Documentation

Weight: `1.0`

- `MET-01` Sev 2: Measures without descriptions.
- `MET-02` Sev 1: Visible columns without descriptions.
- `MET-03` Sev 1: Tables without descriptions.
- `MET-04` Sev 1: Description duplicates the object name.
- `MET-05` Sev 1: Description shorter than 10 characters.
- `MET-06` Sev 2: Currency measures without currency format strings.
- `MET-07` Sev 2: Percentage measures without percentage format strings.
- `MET-08` Sev 2: Date columns without explicit format strings.
- `MET-09` Sev 2: Visible numeric measures without any `formatString`.
- `MET-10` Sev 1: `PBI_FormatHint` annotation with `isGeneralNumber: true`.

## Anti-Patterns And Hidden Fields

Weight: `1.0`

- `APT-01` Sev 2: Foreign key columns on the many side are not hidden.
- `APT-02` Sev 2: Key or ID columns missing `summarizeBy: none`.
- `APT-03` Sev 2: Hidden columns unused by relationships, hierarchies,
  `sortByColumn`, or DAX.
- `APT-03b` Sev 2: Imported columns unused by relationships, hierarchies,
  `sortByColumn`, DAX, RLS or OLS, or report visual fields.
- `APT-04` Sev 3: Missing `lineageTag`.
- `APT-05` Sev 4: Duplicate `lineageTag`.
- `APT-06` Sev 3: Invalid `lineageTag` GUID format.

## Severity Scale

- `1`: Cosmetic or informational
- `2`: Minor issue or warning
- `3`: Important issue with performance or functional risk
- `4`: Very important issue with high risk
- `5`: Critical issue with severe or guaranteed failure risk

## Category Weights

- Security: `3.0`
- Performance: `1.5`
- DAX Quality: `1.5`
- Modeling: `1.5`
- Structure: `1.5`
- Documentation: `1.0`
- Anti-Patterns: `1.0`

## Weighted Score

```text
Score = (sum of passed_rules x category_weight)
      / (sum of total_applicable_rules x category_weight) x 100
```

## Letter Grades

- `A`: `90-100%` and production-ready
- `B`: `80-89%` with minor improvements needed
- `C`: `70-79%` with several issues to address
- `D`: `60-69%` with significant improvements needed
- `F`: `<60%` with critical issues present

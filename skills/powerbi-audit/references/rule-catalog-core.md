# Rule Catalog: Core Domains

Use this reference for Structure, Modeling, Performance, and Security checks.

## Structure And Star Schema

Weight: `1.5`

- `STR-01` Sev 3: No relationships defined.
- `STR-02` Sev 3: Snowflake schema detected through dimension-to-dimension
  chains.
- `STR-03` Sev 3: Tables with no relationships, excluding intentional
  disconnected or parameter tables.
- `STR-04` Sev 2: Wide table, warning above 30 columns and elevate to Sev 3
  above 60 columns.
- `STR-05` Sev 2: Fact-table columns visible to report users.

## Modeling, Relationships, And Naming

Weight: `1.5`

- `MOD-01` Sev 3: Bidirectional cross-filtering without a justified exception.
- `MOD-02` Sev 3: Many-to-many relationships.
- `MOD-03` Sev 1: Inactive relationships that need intent review.
- `MOD-04` Sev 2: Text-type join columns instead of integer keys.
- `MOD-05` Sev 2: Bidirectional security filtering without any RLS role.
- `MOD-06` Sev 1: Object names not capitalized.
- `MOD-07` Sev 1: Table names with `Dim` or `Fact` prefixes.
- `MOD-08` Sev 2: Leading or trailing whitespace in object names.
- `MOD-09` Sev 2: Tabs, line feeds, or similar special characters in names.
- `MOD-10` Sev 2: Unqualified column references in DAX; require
  `'Table'[Column]`.
- `MOD-11` Sev 2: Qualified measure references in DAX; prefer `[Measure]`.
- `MOD-12` Sev 2: More than 10 visible items in a table with no display
  folders.
- `MOD-13` Sev 1: Hidden columns not using CamelCase.

## Performance

Weight: `1.5`

Thresholds:

- Columns per table: good `<20`, warning `20-40`, critical `>40`
- Total columns: good `<100`, warning `100-300`, critical `>300`
- Total tables: good `<15`, warning `15-30`, critical `>30`
- Total measures: good `<100`, warning `100-300`, critical `>300`
- Bidirectional relationships: good `0-1`, warning `2-3`, critical `>3`
- Many-to-many relationships: good `0`, warning `1-2`, critical `>2`
- Calculated columns: good `0-5`, warning `5-15`, critical `>15`
- Calculated tables: good `0-2`, warning `2-5`, critical `>5`

- `PRF-01` Sev 2: Calculated column uses `RELATED`.
- `PRF-02` Sev 3: Calculated column uses aggregation functions and should be a
  measure.
- `PRF-03` Sev 2: Calculated tables outside expected date-table or field
  parameter cases.
- `PRF-04` Sev 3: Auto date or time tables present.
- `PRF-05` Sev 3: Date table missing `DataCategory: Time`.
- `PRF-06` Sev 3: DateTime columns contain non-midnight time values and should
  be split.
- `PRF-07` Sev 1: `isAvailableInMdx: false` missing on non-attribute columns.
- `PRF-08` Sev 2: Numeric columns missing `summarizeBy: none`.
- `PRF-09` Sev 3: Floating-point `dataType: double`; prefer `decimal`.
- `PRF-10` Sev 2: DirectQuery model without aggregation tables.

## Security

Weight: `3.0`

- `SEC-01` Sev 5: Hardcoded credentials in M expressions or connection
  strings.
- `SEC-02` Sev 3: Local file paths or UNC paths in partition sources.
- `SEC-03` Sev 3: Hardcoded server or database names instead of parameters.
- `SEC-04` Sev 3: PII column-name patterns with no RLS defined.
- `SEC-05` Sev 3: `USERNAME()` used where `USERPRINCIPALNAME()` is expected.
- `SEC-06` Sev 3: RLS filters applied directly on fact tables.
- `SEC-07` Sev 2: `LOOKUPVALUE` used in RLS expressions.
- `SEC-08` Sev 2: Empty roles with `modelPermission: read` but no
  `tablePermission`.
- `SEC-09` Sev 1: Hardcoded filter values in RLS.
- `SEC-10` Sev 2: Overly complex RLS expressions, usually more than 200
  characters or more than five function calls.
- `SEC-11` Sev 3: Measures reference OLS-hidden columns.
- `SEC-12` Sev 3: OLS and RLS combined on the same table.

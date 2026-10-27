# Today I Learned

## 2026-10-26 — dbt Fundamentals, day 1
- dbt Studio runs the SAVED file; unsaved changes = "Nothing to do"
- dbt Preview adds its own LIMIT, so no semicolons or LIMIT in my queries
- ▶ in Snowflake runs only the current statement; use Run All
- `create table` fails if the table exists; old columns caused my insert errors
- Snowflake roles are permission sets, not job titles; created a TRANSFORMER role
- One dbt project = one connection; my Redshift project couldn't see Snowflake
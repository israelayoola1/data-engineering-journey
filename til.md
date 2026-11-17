# Today I Learned

## 2026-11-16 — Git version control
- A commit is an immutable snapshot (trees + blobs), not a list of changes
- A branch is a movable pointer to a commit; deleting it removes the label, not the commits
- HEAD points to whatever is checked out right now (usually a branch)
- Commit only takes what's staged: `git add` first, or `git commit -a`
- Fast-forward = no merge commit needed; diverged branches create a merge commit
- Git doesn't check conflict resolutions; check for `<<<<<<<` before committing
- `git reset --hard HEAD~1` moves a branch back one commit; use with care
- Team flow: branch → commit → push → PR → merge → pull

## 2026-11-13 — Shell tools & scripting
- `>` overwrites a file, `>>` appends; `|` sends one command's output into another
- `wc -l` counts lines of text, not records; check the file with `head` first
- `grep` is case-sensitive; `-i` ignores case, `-c` counts, `-o` prints only the match
- `sort | uniq -c | sort -rn` is a shell "group by ... order by count desc"
- Quote file names with spaces; better, don't use spaces in file names
- In zsh, `status` is a read-only built-in variable; don't use it as a name
- Tab completion catches path typos before they cause errors

## 2026-10-26 — dbt Fundamentals, day 1
- dbt Studio runs the SAVED file; unsaved changes = "Nothing to do"
- dbt Preview adds its own LIMIT, so no semicolons or LIMIT in my queries
- ▶ in Snowflake runs only the current statement; use Run All
- `create table` fails if the table exists; old columns caused my insert errors
- Snowflake roles are permission sets, not job titles; created a TRANSFORMER role
- One dbt project = one connection; my Redshift project couldn't see Snowflake

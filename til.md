## 2026-11-13 — Shell tools & scripting
- `>` overwrites a file, `>>` appends; `|` sends one command's output into another
- `wc -l` counts lines of text, not records; check the file with `head` first
- `grep` is case-sensitive; `-i` ignores case, `-c` counts, `-o` prints only the match
- `sort | uniq -c | sort -rn` is a shell "group by ... order by count desc"
- Quote file names with spaces; better, don't use spaces in file names
- In zsh, `status` is a read-only built-in variable; don't use it as a name
- Tab completion catches path typos before they cause errors
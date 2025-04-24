# 🧰 Log Parsing & Regex Cheat Sheet (Grep, Awk, Regex, Bash)

## 🔍 Basic Commands

| Command | Description |
|--------|-------------|
| `cat file.log \| grep "ERROR"` | Match lines containing `ERROR` |
| `grep -i "fail" file.log` | Case-insensitive search |
| `grep -v "INFO" file.log` | Exclude lines containing `INFO` |
| `grep -E "error|fail|denied" file.log` | Match multiple patterns (extended regex) |
| `grep -E "192\.168\.1\.[0-9]{1,3}" file.log` | Match IPs in a subnet |
| `grep -E "^\[.*\]$" file.log` | Match lines enclosed in square brackets |
| `grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" file.log` | Extract IP addresses |
| `grep -Eo "[0-9]{2}/[A-Za-z]+/[0-9]{4}" file.log` | Extract Apache-style date format |
| `grep -c "ERROR" file.log` | Count lines matching pattern |
| `grep "pattern" file.log > output.txt` | Output matching lines to file |

---

## 🧮 Awk Patterns

| Command | Description |
|--------|-------------|
| `awk '{print $1, $2}' file.log` | Print 1st and 2nd fields (space-separated) |
| `awk '/error/ {print $5}' file.log` | Print 5th field if "error" in line |
| `awk '{count[$5]++} END {for (ip in count) print ip, count[ip]}' file.log` | Count occurrences of field 5 (e.g. IPs) |
| `awk '($3 == "sshd")' file.log` | Match lines where 3rd field is "sshd" |
| `awk '$0 ~ /pattern/' file.log` | Match lines with regex |
| `awk '$0 !~ /pattern/' file.log` | Exclude lines matching pattern |
| `awk '{print tolower($0)}' file.log` | Convert entire line to lowercase |
| `awk '{print > "output.txt"}'` | Redirect awk output to file |
| `awk -F: '{print $1}' /etc/passwd` | Set custom field delimiter (`:`) |

---

## 🧠 Regex Snippets (for grep & awk)

| Pattern | Matches |
|--------|---------|
| `[0-9]+` | One or more digits |
| `[a-zA-Z]+` | One or more letters |
| `[^ ]+` | Non-space word |
| `.*` | Any characters (greedy) |
| `^pattern` | Line starts with `pattern` |
| `pattern$` | Line ends with `pattern` |
| `\s+` | One or more whitespace characters |
| `[0-9]{4}-[0-9]{2}-[0-9]{2}` | ISO date (e.g. `2025-04-17`) |
| `[0-9]{1,3}(\.[0-9]{1,3}){3}` | IPv4 address |
| `([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}` | MAC address |
| `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` | Email address |

---

## 🧪 Extra Bash Tricks

| Command | Description |
|--------|-------------|
| `tail -n 100 file.log` | Show last 100 lines |
| `head -n 50 file.log` | Show first 50 lines |
| `tail -f file.log \| grep --line-buffered "ERROR"` | Real-time error monitoring |
| `cat file.log \| sort \| uniq -c \| sort -nr` | Count and sort duplicate lines |

---

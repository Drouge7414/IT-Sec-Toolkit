# 📊 Web Access Log Analysis Cheat Sheet

```bash
awk '{print $1}' access.log | sort -u | wc -l
# 🔢 Count total unique IPs

awk '$9 ~ /^[23][0-9][0-9]$/ {print $1}' access.log | sort -u | wc -l
# ✅ Look for all 200 / 300 requests and output a total of unique IPs

awk '$9 == 200' access.log
# 📄 Output all lines with 200 status on request

grep "Googlebot" access.log
# 🤖 Look for Googlebot requests

grep -E "(\(\) { :; }|bash|exec)" access.log
# 💥 Look for Shellshock vulnerability attempts

grep "Firefox" access.log | awk -F"Firefox/" '{print $2}' | cut -d " " -f1 | sort | uniq -c | sort -nr
# 🦊 Count each unique Firefox version

awk '{print $6}' access.log | cut -d '"' -f2 | sort | uniq -c | sort -nr
# 📝 Most common HTTP method

cat access.log | cut -d '"' -f 3 | cut -d ' ' -f 2 | sort | uniq -c | sort -rn
# 📈 See all HTTP methods and how many times they occurred

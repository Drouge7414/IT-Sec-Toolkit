# 📊 SSH Log Analysis & SSH Command Cheat Sheet

```bash
grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' log.log
# 🔍 Pull all lines in the log that contain an IP address

grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log | sort | uniq -c | sort -nr
# 🌍 Extract all unique IP addresses and count the total number of times each IP address appears

grep "Failed password" /var/log/auth.log
# 🚫 Look for failed login attempts in the SSH logs

grep "Accepted password" /var/log/auth.log
# ✅ Look for successful SSH login attempts in the logs

grep -E "sshd.*Failed" /var/log/auth.log
# ❌ Find failed SSH login attempts with the specific string "sshd"

grep -E "sshd.*Accepted" /var/log/auth.log
# ✅ Find successful SSH login attempts with the specific string "sshd"

grep -i "error" /var/log/auth.log
# 🚨 Look for errors in the SSH logs (case-insensitive)

awk '/sshd/ && /Failed/ {print $1, $2, $3, $9, $11}' /var/log/auth.log
# 📉 Get failed SSH login attempts with date, time, and IP address

awk '/sshd/ && /Accepted/ {print $1, $2, $3, $9, $11}' /var/log/auth.log
# ✅ Get successful SSH login attempts with date, time, and IP address

last -i
# 📋 Show the last logins to your machine with IP addresses

sudo fail2ban-client status sshd
# 🚨 Check the status of fail2ban for SSH brute force protection

sudo cat /var/log/auth.log | grep "sshd"
# 📄 Output all SSH-related log entries from the authentication log

sudo cat /var/log/auth.log | grep "sshd" | grep "Failed"
# ❌ Output failed SSH login attempts specifically

sudo cat /var/log/auth.log | grep "sshd" | grep "Accepted"
# ✅ Output successful SSH logins specifically

sudo cat /var/log/auth.log | grep "sshd" | grep -E "Failed|Accepted"
# 🔍 Output both failed and successful SSH logins

sudo journalctl -u sshd
# 📚 View SSH logs from the systemd journal for more detailed log information

sudo grep -i "invalid user" /var/log/auth.log
# 🚨 Look for invalid user login attempts in SSH logs

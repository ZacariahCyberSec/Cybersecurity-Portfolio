with open("log.txt") as f:
    logs = f.readlines()

# Count failed logins per user
user_failures = {}
ip_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[5]
        ip = parts[-1]

        # Count by user
        if username in user_failures:
            user_failures[username] += 1
        else:
            user_failures[username] = 1

        # Count by IP
        if ip in ip_failures:
            ip_failures[ip] = ip_failures.get(ip, 0) + 1

# Build report
report = ""

report += "👤 Failed login attempts by username:\n\n"
for user, count in user_failures.items():
    report += f"{user}: {count}\n"

report += "\n🚨 Possible brute force IPs (3+ failures):\n\n"
for ip, count in ip_failures.items():
    if count >= 3:
        report += f"{ip}: {count} failed attempts\n"

# Save report
with open("risk_alerts_report.txt", "w") as f:
    f.write(report)

print(report)
print("✅ Summary report saved as 'risk_alerts_report.txt'")

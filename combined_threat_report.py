with open("log.txt") as f:
    logs = f.readlines()

user_failures = {}
ip_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[5]  # e.g. "user"
        ip = parts[-1]

        # Track failures by user
        if username in user_failures:
            user_failures[username] += 1
        else:
            user_failures[username] = 1

        # Track failures by IP
        if ip in ip_failures:
            ip_failures[ip] += 1
        else:
            ip_failures[ip] = 1

# Write to a single report
with open("combined_threat_report.txt", "w") as f:
    f.write("👤 Failed login attempts by username:\n\n")
    for user, count in user_failures.items():
        f.write(f"{user}: {count}\n")

    f.write("\n🚨 Possible brute force IPs (3+ failures):\n\n")
    for ip, count in ip_failures.items():
        if count >= 3:
            f.write(f"{ip}: {count} failed attempts\n")

print("\n✅ Combined threat report saved as 'combined_threat_report.txt'")

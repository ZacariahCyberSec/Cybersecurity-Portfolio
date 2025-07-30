with open("log.txt") as f:
    logs = f.readlines()

ip_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        ip = parts[-1]
        if ip in ip_failures:
            ip_failures[ip] += 1
        else:
            ip_failures[ip] = 1

output = "🚨 Possible brute force attempts (3+ failures):\n\n"

for ip, count in ip_failures.items():
    if count >= 3:
        output += f"{ip}: {count} failed attempts\n"

print(output)

# Save to file
with open("bruteforce_report.txt", "w") as report:
    report.write(output)

print("✅ Brute force report saved as 'bruteforce_report.txt'")

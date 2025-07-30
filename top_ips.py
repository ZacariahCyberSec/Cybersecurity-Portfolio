with open("log.txt") as f:
    logs = f.readlines()

ip_counts = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        ip = parts[-1]
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

print("🚨 Top IP addresses with most failed logins:\n")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip}: {count}")
with open("top_ips_report.txt", "w") as report:
    report.write("🚨 Top IP addresses with most failed logins:\n\n")
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        report.write(f"{ip}: {count}\n")
print("\n✅ Report saved as 'top_ips_report.txt'")

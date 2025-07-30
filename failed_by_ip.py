with open("log.txt") as f:
    logs = f.readlines()

failed_by_ip = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        ip = parts[-1]

        if ip in failed_by_ip:
            failed_by_ip[ip] += 1
        else:
            failed_by_ip[ip] = 1

with open("ip_report.txt", "w") as report:
    report.write("Failed login attempts grouped by IP:\n\n")
    for ip, count in failed_by_ip.items():
        report.write(f"{ip}: {count}\n")

print("✅ Report saved as 'ip_report.txt'")

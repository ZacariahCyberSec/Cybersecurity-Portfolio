with open("log.txt") as f:
    logs = f.readlines()

output = "🕒 Failed login attempts with timestamps:\n\n"

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        timestamp = parts[0] + " " + parts[1]
        username = parts[6]
        ip = parts[-1]
        output += f"{timestamp} | user: {username} | IP: {ip}\n"

with open("timeline_report.txt", "w") as report:
    report.write(output)

print("✅ Timeline report saved as 'timeline_report.txt'")

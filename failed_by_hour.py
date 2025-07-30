with open("log.txt") as f:
    logs = f.readlines()

failed_by_hour = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        # Assuming the format is: "Jul 29 02:45:12 login failed for user..."
        if len(parts) >= 3:
            time_part = parts[2]  # Example: "02:45:12"
            hour = time_part.split(":")[0]  # Extract "02"

            if hour in failed_by_hour:
                failed_by_hour[hour] += 1
            else:
                failed_by_hour[hour] = 1

with open("hourly_report.txt", "w") as report:
    report.write("🕒 Failed login attempts by hour:\n\n")
    for hour, count in sorted(failed_by_hour.items()):
        report.write(f"{hour}:00 - {count} attempts\n")

print("✅ Hourly report saved as 'hourly_report.txt'")

with open("log.txt") as f:
    logs = f.readlines()

user_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[6]  # Correct index for username
        if username in user_failures:
            user_failures[username] += 1
        else:
            user_failures[username] = 1

with open("failed_by_user_report.txt", "w") as report:
    report.write("👤 Failed login attempts by username:\n\n")
    for user, count in user_failures.items():
        report.write(f"{user}: {count}\n")

print("✅ Report saved as 'failed_by_user_report.txt'")

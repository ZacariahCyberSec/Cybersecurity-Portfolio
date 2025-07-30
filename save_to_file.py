with open("log.txt") as f:
    logs = f.readlines()

user_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[6]
        user_failures[username] = user_failures.get(username, 0) + 1

# Save results to a file
with open("report.txt", "w") as report:
    report.write("👤 Failed login attempts by username:\n\n")
    for user, count in user_failures.items():
        report.write(f"{user}: {count}\n")

print("✅ Report saved as 'report.txt'")

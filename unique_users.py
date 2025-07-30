with open("log.txt") as f:
    logs = f.readlines()

unique_users = set()

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[5]
        unique_users.add(username)

report = "Unique users with failed logins:\n\n"
for user in unique_users:
    report += f"{user}\n"

with open("unique_users_report.txt", "w") as out:
    out.write(report)

print("✅ Report saved as 'unique_users_report.txt'")

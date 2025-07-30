with open("log.txt") as f:
    logs = f.readlines()

user_failures = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[5]  # index 5 holds username
        user_failures[username] = user_failures.get(username, 0) + 1

# Filter users with 3 or more failed attempts
bruteforce_users = {user: count for user, count in user_failures.items() if count >= 3}

report_lines = ["Possible brute force attempts (3+ failures):\n"]
if bruteforce_users:
    for user, count in bruteforce_users.items():
        report_lines.append(f"{user}: {count}\n")
else:
    report_lines.append("No users with 3 or more failed attempts.\n")

with open("bruteforce_report.txt", "w") as report_file:
    report_file.writelines(report_lines)

print("✅ Report saved as 'bruteforce_report.txt'")

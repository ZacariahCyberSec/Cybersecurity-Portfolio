with open("log.txt") as f:
    logs = f.readlines()

user_counts = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        username = parts[5]
        if username in user_counts:
            user_counts[username] += 1
        else:
            user_counts[username] = 1

most_common = max(user_counts, key=user_counts.get)

print("🔥 Most common failed login username:\n")
print(f"{most_common}: {user_counts[most_common]}")

with open("most_common_user_report.txt", "w") as f:
    f.write("Most common failed login username:\n\n")
    f.write(f"{most_common}: {user_counts[most_common]}")

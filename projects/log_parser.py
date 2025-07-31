import datetime

# Load the log file (adjust if your path is different)
log_file_path = "logs/sample_syslog.txt"

# Dictionaries to track brute force attempts
user_attempts = {}
ip_attempts = {}

# Threshold for what counts as suspicious
threshold = 5

# Read the log file line by line
with open(log_file_path, 'r') as file:
    for line in file:
        if "FAILED" in line.upper():
            parts = line.split()
            for i, word in enumerate(parts):
                if word.lower() == "user":
                    user = parts[i + 1]
                    user_attempts[user] = user_attempts.get(user, 0) + 1
                if word.count('.') == 3:
                    ip = word
                    ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

# Generate report
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"🔐 Brute Force Summary Report - {now}\n\n"

report += "Suspicious usernames:\n"
for user, count in user_attempts.items():
    if count > threshold:
        report += f"- {user} (failed {count} times)\n"

report += "\nSuspicious IPs:\n"
for ip, count in ip_attempts.items():
    if count > threshold:
        report += f"- {ip} ({count} attempts)\n"

# Save report
with open("projects/log_report.txt", "w") as output:
    output.write(report)

print("✅ Brute force scan complete. Report saved to log_report.txt")

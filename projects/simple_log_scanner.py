# simple_log_scanner.py

log_file = "../log.txt"

with open(log_file, "r") as file:
    lines = file.readlines()

suspicious = [line for line in lines if "failed" in line.lower()]

print(f"🔍 Total suspicious entries: {len(suspicious)}\n")

for entry in suspicious:
    print(entry.strip())

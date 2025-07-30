with open("log.txt") as f:
    logs = f.readlines()

failed_logins = 0

print("🔍 Failed login attempts:\n")

for line in logs:
    if "failed" in line.lower():
        print("• " + line.strip())
        failed_logins += 1

print(f"\n📌 Total failed logins: {failed_logins}")

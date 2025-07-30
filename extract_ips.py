with open("log.txt") as f:
    logs = f.readlines()

print("📡 IP addresses with failed logins:\n")

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        ip_address = parts[-1]  # last word is the IP
        print(ip_address)

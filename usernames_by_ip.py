with open("log.txt") as f:
    logs = f.readlines()

attempts_by_ip = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        ip = parts[-1]          # IP is last item
        username = parts[6]     # Username is at index 6

        if ip not in attempts_by_ip:
            attempts_by_ip[ip] = []

        attempts_by_ip[ip].append(username)

print("🕵️‍♂️ Failed login attempts grouped by IP:\n")

for ip, users in attempts_by_ip.items():
    print(f"{ip}: {', '.join(users)}")

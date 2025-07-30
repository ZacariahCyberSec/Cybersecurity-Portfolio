with open("log.txt") as f:
    logs = f.readlines()

total_failed = 0
failed_by_ip = {}
failed_by_user = {}
failed_by_date = {}
failed_by_hour = {}
brute_force_candidates = {}

for line in logs:
    if "failed" in line.lower():
        total_failed += 1
        parts = line.strip().split()
        date = parts[0] + " " + parts[1]
        hour = parts[2].split(":")[0] + ":00"
        user = parts[5]
        ip = parts[-1]

        # Count by IP
        failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

        # Count by user
        failed_by_user[user] = failed_by_user.get(user, 0) + 1

        # Count by date
        failed_by_date[date] = failed_by_date.get(date, 0) + 1

        # Count by hour
        failed_by_hour[hour] = failed_by_hour.get(hour, 0) + 1

        # For brute force check
        key = f"{user}@{ip}"
        brute_force_candidates[key] = brute_force_candidates.get(key, 0) + 1

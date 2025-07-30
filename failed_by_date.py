# Step 1: Analyze failed login attempts by date

with open("log.txt") as f:
    logs = f.readlines()

failed_by_date = {}

for line in logs:
    if "failed" in line.lower():
        parts = line.strip().split()
        # Assuming date is the first two parts, e.g. "Jul 29"
        date = parts[0] + " " + parts[1]
        
        if date in failed_by_date:
            failed_by_date[date] += 1
        else:
            failed_by_date[date] = 1

print("Failed login attempts by date:\n")
for date, count in failed_by_date.items():
    print(f"{date}: {count}")

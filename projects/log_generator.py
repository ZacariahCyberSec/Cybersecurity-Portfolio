from datetime import datetime, timedelta
import random

users = ["user", "admin", "guest", "for"]
ips = ["192.168.1.5", "172.16.0.9", "10.0.0.8"]

log_lines = []
now = datetime.now()

for _ in range(50):
    timestamp = (now - timedelta(minutes=random.randint(0, 300))).strftime("%b %d %H:%M:%S")
    ip = random.choice(ips)
    user = random.choice(users)
    line = f"{timestamp} localhost sshd[1999]: Failed password for {user} from {ip} port 22 ssh2"
    log_lines.append(line)

with open("log.txt", "w") as file:
    file.write("\n".join(log_lines))

print("✅ Generated sample log.txt")

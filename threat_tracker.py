import requests
import datetime
import os

# Setup log folder
os.makedirs("logs", exist_ok=True)

# Timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log VPN Identity
def log_vpn_identity():
    try:
        ip = requests.get("https://api.ipify.org").text
        dns = requests.get("https://dns.google/resolve?name=example.com").json()
        dns_info = dns.get("Answer", [{}])[0].get("data", "Unavailable")

        with open("logs/vpn_identity_log.txt", "a") as f:
            f.write(f"[{timestamp}] IP: {ip} | DNS: {dns_info}\n")
        print(f"[INFO] IP and DNS logged ✅")
    except Exception as e:
        print(f"[ERROR] Could not log IP/DNS: {e}")

# Fetch threat data from test source
def fetch_threats():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            threat_data = response.text
            report_file = f"logs/threat_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_file, "w") as report:
                report.write("=== Threat Tracker Report ===\n")
                report.write(f"Generated: {timestamp}\n\n")
                report.write(threat_data)
            print(f"[INFO] Threat data saved to {report_file}")
        else:
            print(f"[WARN] Unable to fetch threat data: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch threat data: {e}")

# Run the script
log_vpn_identity()
fetch_threats()

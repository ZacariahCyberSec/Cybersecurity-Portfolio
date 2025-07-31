import requests
import datetime

# List of known threat actor keywords to track
keywords = ["clop", "lockbit", "ransomware", "data breach", "leak site", "dark web"]

# Sample public feed (can be extended with others)
feeds = {
    "Cybersecurity News": "https://www.bleepingcomputer.com/feed/",
    "DarkFeed": "https://darkfeed.io/feed.xml"
}

def fetch_feed(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text.lower()  # Convert to lowercase for matching
    except Exception as e:
        return f"Failed to fetch: {e}"

def check_threats():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = [f"📅 Threat Tracker Report - {now}\n"]

    for name, url in feeds.items():
        report_lines.append(f"🔗 Checking: {name} ({url})")
        content = fetch_feed(url)

        if "failed to fetch" in content:
            report_lines.append(content)
            continue

        for kw in keywords:
            if kw in content:
                report_lines.append(f"⚠️ Alert: Found keyword '{kw}' in {name}")

    return "\n".join(report_lines)

# Save to file
report = check_threats()
with open("threat_tracker_report.txt", "w") as f:
    f.write(report)

print("✅ Threat tracker finished.\n")
print(report)

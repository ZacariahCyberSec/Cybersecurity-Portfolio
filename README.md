# 🛡️ Cybersecurity Portfolio by Tinashe Zacariah (ZacariahCyberSec)

Welcome to my hands-on Cybersecurity Portfolio built entirely using Python and Termux on Android. This project simulates a real-world Security Operations Center (SOC) environment where logs are analyzed for brute force attacks, failed logins, and threat alerts are generated and emailed automatically.

## 🚀 Overview

This portfolio demonstrates skills in:
- Log file parsing
- Brute-force attack detection
- Email alert automation
- Threat reporting
- Git & GitHub version control

---

## 📂 Project Files

| Script/Report File | Description |
|--------------------|-------------|
| `log.txt` | Sample log file with simulated failed login attempts |
| `failed_by_date.py` | Analyzes failed logins grouped by date |
| `failed_by_hour.py` | Tracks login failures by hour |
| `failed_by_ip.py` | Shows failed logins grouped by IP address |
| `failed_by_user.py` | Groups failed login attempts by username |
| `top_ips.py` | Detects top IPs with most failed logins |
| `most_common_user.py` | Detects usernames used most in failed logins |
| `unique_users.py` | Lists all unique users who had login failures |
| `detect_bruteforce.py` | Detects brute force IPs with 3+ failures |
| `risk_alerts.py` | Summarizes all threats in one report |
| `email_alert.py` | Sends alert email using yagmail and app password |
| `send_full_report.py` | Sends a full summary report via email |
| `.txt files` | Automatically saved reports from above scripts |

---

## 🔧 How to Run (Using Termux on Android)

1. Clone the repository:

```bash
git clone https://github.com/ZacariahCyberSec/Cybersecurity-Portfolio.git
cd Cybersecurity-Portfolio

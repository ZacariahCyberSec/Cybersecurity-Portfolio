 HEAD
## 🌐 Connect with Me

- 📫 LinkedIn: [linkedin.com/in/tinashe-zacariah](https://www.linkedin.com/in/tinashe-zacariah-nyandoro-787b9723a)
- 📁 GitHub: [github.com/ZacariahCyberSec](https://github.com/ZacariahCyberSec)
- ✉️ Email: [t.nyandoro@yahoo.com](mailto:t.nyandoro@yahoo.com)
- 📘 [View Full Wiki Documentation](https://github.com/ZacariahCyberSec/Cybersecurity-Portfolio/wiki)

> “Cybersecurity is not just about technology — it's about people, process, and passion.”  
> — Zacariah

# Threat Tracker Script

This Python script logs your current public IP address and DNS resolver while securely connected to Proton VPN, then fetches and saves threat intelligence data from an external feed.

## Features
- Logs IP & DNS (verifies VPN masking)
- Saves timestamped threat reports
- Python-based, mobile/Termux compatible
- Lightweight & portable for threat hunting

## Files Generated
- `logs/vpn_identity_log.txt`
- `logs/threat_report_YYYYMMDD_HHMMSS.txt`

## Usage
```bash
python threat_tracker.py
 45b6373 (Initial commit: threat_tracker.py with VPN log and threat feed)

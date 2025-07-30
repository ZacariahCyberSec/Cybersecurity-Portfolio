import yagmail

sender_email = "zacariah.cybersec@gmail.com"
app_password = "uohluigrogqtcsyp"  # Use your working app password
receiver_email = "zacariah.cybersec@gmail.com"  # Same or another

# Load the summary content from the file
with open("risk_alerts_report.txt", "r") as f:
    report_content = f.read()

yag = yagmail.SMTP(sender_email, app_password)
yag.send(
    to=receiver_email,
    subject="📊 Full Security Report Summary",
    contents=report_content
)

print("📧 Full security report sent!")

import yagmail

sender_email = "zacariah.cybersec@gmail.com"
app_password = "uohluigrogqtcsyp"  # No spaces, copy exactly
receiver_email = "zacariah.cybersec@gmail.com"  # Same or different email

yag = yagmail.SMTP(sender_email, app_password)
yag.send(
    to=receiver_email,
    subject="🚨 Security Alert",
    contents="Brute force login detected on your system."
)

print("📧 Email alert sent!")

import smtplib
from email.mime.text import MIMEText
import streamlit as st

def send_alerts(results, extra_email=None):
    smtp_user = st.secrets["email"]["smtp_username"]
    smtp_pass = st.secrets["email"]["smtp_password"]
    default_to = st.secrets["email"]["to_email"]
    recipients = [default_to]

    if extra_email and "@" in extra_email:
        recipients.append(extra_email)

    body = "\n\n".join([
        f"{item['title']}\nStore: {item['store']}\nBid: {item['current_bid']} ({item['bids']})\nTime Left: {item['time_left']}\n{item['url']}"
        for item in results
    ])

    msg = MIMEText(body)
    msg["Subject"] = "🔔 BidRL Auction Watcher – New Matches"
    msg["From"] = smtp_user
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, recipients, msg.as_string())

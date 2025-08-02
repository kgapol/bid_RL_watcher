import smtplib
from email.mime.text import MIMEText
import streamlit as st

def send_alerts(results):
    smtp_user = st.secrets['email']['smtp_username']
    smtp_pass = st.secrets['email']['smtp_password']
    to_email = st.secrets['email']['to_email']

    body = '\n'.join([f"{item['title']} ({item['price']}) at {item['store']}" for item in results])
    msg = MIMEText(body)
    msg['Subject'] = 'BidRL Auction Watcher – New Matches'
    msg['From'] = smtp_user
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, [to_email], msg.as_string())
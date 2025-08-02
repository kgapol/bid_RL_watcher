# BidRL Auction Watcher

Searches all BidRL stores for matching auction items and emails alerts.

## Usage
- Deploy to [Streamlit Cloud](https://streamlit.io/cloud)
- Add secrets for Gmail in `secrets.toml`

## Required Secrets
```
[email]
smtp_username = "your-email@gmail.com"
smtp_password = "your-app-password"
to_email = "your-email@gmail.com"
```
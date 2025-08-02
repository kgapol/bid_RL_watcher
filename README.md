# BidRL Auction Watcher

Searches BidRL affiliate stores for auction listings matching keywords and sends alerts.

## Features
- Dynamic store discovery
- Prioritized stores
- Daily scraping via GitHub Action (planned)
- Streamlit app with manual refresh and email alerting

## Streamlit Secrets
```toml
[email]
smtp_username = "your@gmail.com"
smtp_password = "your-app-password"
to_email = "your@gmail.com"
```
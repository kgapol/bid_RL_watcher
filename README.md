# BidRL Auction Watcher

Searches all BidRL stores for matching auctions and emails results.

## Features
- Keyword search across all stores
- Image display
- Bid amount, number of bids, time left
- Email alerts (to secrets + optional email)

## Required Streamlit Secrets
```
[email]
smtp_username = "your@gmail.com"
smtp_password = "your-app-password"
to_email = "your@gmail.com"
```
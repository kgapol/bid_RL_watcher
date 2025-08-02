def run_search(keywords):
    # Simulated results (replace with real scraping logic)
    dummy_data = [
        {
            "title": "Winbot 880 Window Robot",
            "store": "Stockton",
            "current_bid": "$89",
            "bids": "4 bids",
            "time_left": "2 days",
            "url": "https://www.bidrl.com/auction/12345/item/67890",
            "image": "https://www.bidrl.com/images/items/winbot.jpg"
        },
        {
            "title": "Reverse Osmosis Water Filter",
            "store": "Sacramento",
            "current_bid": "$45",
            "bids": "2 bids",
            "time_left": "1 day",
            "url": "https://www.bidrl.com/auction/98765/item/43210",
            "image": "https://www.bidrl.com/images/items/ro_filter.jpg"
        }
    ]
    return [item for item in dummy_data if any(k in item["title"].lower() for k in keywords)]

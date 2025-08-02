import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from settings import PRIORITIZED_STORES, MAX_AUCTIONS_PER_STORE, OUTPUT_FILE

def discover_store_urls():
    url = "https://www.bidrl.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select("a[href*='/affiliate/']")
    stores = {}
    for link in links:
        name = link.text.strip()
        href = link.get("href")
        if name and href:
            stores[name] = href
    return stores

def parse_auctions(store_name, store_url):
    res = requests.get(store_url)
    soup = BeautifulSoup(res.text, "html.parser")
    cards = soup.select("div.auction-item")
    results = []
    for card in cards[:MAX_AUCTIONS_PER_STORE]:
        title = card.select_one("h4 a")
        url = title.get("href") if title else ""
        full_url = f"https://www.bidrl.com{url}" if url else ""
        image = card.select_one("img")
        image_url = image.get("src") if image else ""
        bids = card.select_one(".bids")
        bid_text = bids.text.strip() if bids else "0 bids"
        bid_price = card.select_one(".price")
        price_text = bid_price.text.strip() if bid_price else "$0"
        time_left = card.select_one(".time-left")
        time_str = time_left.text.strip() if time_left else "Unknown"
        close_dt = "Unknown"
        if "ends in" in time_str.lower():
            delta = time_str.lower().replace("ends in", "").strip()
            try:
                d, h = [int(part.strip().split()[0]) for part in delta.split(",")]
                close_dt = (datetime.now() + timedelta(days=d, hours=h)).strftime("%b %d, %Y at %I:%M %p")
                time_str = f"{d} days, {h} hours"
            except:
                pass
        results.append({
            "title": title.text.strip() if title else "Unknown",
            "store": store_name,
            "current_bid": price_text,
            "bids": bid_text,
            "time_left": time_str,
            "close_time": close_dt,
            "url": full_url,
            "image": image_url
        })
    return results

def refresh_auctions():
    stores = discover_store_urls()
    all_data = []
    for store in sorted(stores.keys(), key=lambda x: x not in PRIORITIZED_STORES):
        store_url = stores[store]
        try:
            print(f"Scraping: {store}")
            auctions = parse_auctions(store, store_url)
            all_data.extend(auctions)
        except Exception as e:
            print(f"Error scraping {store}: {e}")
    with open(OUTPUT_FILE, "w") as f:
        json.dump(all_data, f)

def run_search(keywords):
    try:
        with open(OUTPUT_FILE, "r") as f:
            auctions = json.load(f)
    except:
        auctions = []
    return [a for a in auctions if any(k in a["title"].lower() for k in keywords)]

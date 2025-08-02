# settings.py

# Stores to prioritize (will be scraped first or highlighted in UI)
PRIORITIZED_STORES = [
    "Modesto",
    "Stockton",
    "Fresno"
]

# Max auctions per store to scrape
MAX_AUCTIONS_PER_STORE = 100

# Where to store the cached auction file
OUTPUT_FILE = "data/auctions.json"

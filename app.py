import streamlit as st
import json
import os
from search_engine import run_search, refresh_auctions
from email_alerts import send_alerts

st.set_page_config(page_title="BidRL Auction Watcher", layout="wide")
st.title("🔍 BidRL Auction Watcher")

keywords = st.text_input("Enter keywords (comma-separated):", value="osmosis, winbot, robot")
extra_email = st.text_input("Send copy of alerts to (optional email):", value="")

col1, col2 = st.columns([1, 3])
refresh = col1.button("🔄 Refresh Auctions (Manual)")
run_button = col2.button("Run Watch Now")

if refresh:
    with st.spinner("Scraping all stores live..."):
        refresh_auctions()
        st.success("Auction data refreshed!")

if run_button:
    with st.spinner("Searching auctions..."):
        keyword_list = [k.strip().lower() for k in keywords.split(",") if k.strip()]
        results = run_search(keyword_list)
        if results:
            st.success(f"Found {len(results)} matching auctions!")
            for item in results:
                cols = st.columns([1, 2])
                if item["image"] and "no_image" not in item["image"]:
                    cols[0].image(item["image"], use_container_width=True)
                else:
                    cols[0].write("🖼 No image available")
                cols[1].markdown(f"""
                ### [{item['title']}]({item['url']})
                - **Store**: {item['store']}
                - **Current Bid**: {item['current_bid']}
                - **Bids**: {item['bids']}
                - **Time Left**: {item['time_left']}
                - **Closes**: {item['close_time']}
                """)
            send_alerts(results, extra_email)
        else:
            st.warning("No matching items found.")

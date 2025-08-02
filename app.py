import streamlit as st
from search_engine import run_search
from email_alerts import send_alerts

st.set_page_config(page_title="BidRL Auction Watcher", layout="wide")
st.title("🔍 BidRL Auction Watcher")

keywords = st.text_input("Enter keywords (comma-separated):", value="osmosis, winbot, robot")
extra_email = st.text_input("Send copy of alerts to (optional email):", value="")

run_button = st.button("Run Watch Now")

if run_button:
    with st.spinner("Searching auctions..."):
        keyword_list = [k.strip().lower() for k in keywords.split(",") if k.strip()]
        results = run_search(keyword_list)
        if results:
            st.success(f"Found {len(results)} matching auctions!")

            for item in results:
                cols = st.columns([1, 2])
                if item["image"] and not item["image"].endswith("no_image.png"):
                    cols[0].image(item["image"], use_column_width=True)
                else:
                    cols[0].write("🖼 No image available")
                cols[1].markdown(f"""
                ### [{item['title']}]({item['url']})
                - **Store**: {item['store']}
                - **Current Bid**: {item['current_bid']}
                - **Bids**: {item['bids']}
                - **Time Left**: {item['time_left']}
                """)
            send_alerts(results, extra_email)
        else:
            st.warning("No matching items found.")

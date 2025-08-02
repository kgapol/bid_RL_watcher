# Streamlit frontend app

import streamlit as st
from search_engine import run_search
from email_alerts import send_alerts

st.title("BidRL Auction Watcher")

keywords = st.text_input("Enter keywords (comma-separated):", value="osmosis, winbot, robot")
run_button = st.button("Run Watch Now")

if run_button:
    st.write("🔍 Searching...")
    results = run_search([k.strip() for k in keywords.split(',')])
    if results:
        st.success(f"Found {len(results)} matching items.")
        send_alerts(results)
    else:
        st.info("No matching items found.")
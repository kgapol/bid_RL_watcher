
import streamlit as st
import json

st.title("BidRL Auction Watcher")

with open("stores.json", "r") as f:
    store_list = json.load(f)

st.download_button(
    label="Download Store List (JSON)",
    data=json.dumps(store_list, indent=2),
    file_name="stores.json",
    mime="application/json"
)

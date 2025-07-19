import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EcoSort - Coins", layout="wide")
st.title("🪙 Coin Info")

with open("coin.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)

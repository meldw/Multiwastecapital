import streamlit as st
import streamlit.components.v1 as components
import os
import sys

# Biar bisa import model dari root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_vlm import classify_image_from_file
from model_llm import get_bot_reply

st.set_page_config(page_title="EcoSort UI", layout="wide")
st.title("🌱 EcoSort Interface")

# Render halaman HTML UI (pastikan file ecosort_ui.html ada di public/)
with open("public/cwastemel_ui.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1300, scrolling=True)

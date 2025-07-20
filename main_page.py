#only for vlm show
'''
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modul.model_vlm import classify_image_from_file
import tempfile
from PIL import Image

hf_token = st.secrets["HF_TOKEN"]

uploaded_file = st.file_uploader("Upload gambar")
if uploaded_file:
    image = Image.open(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        image.save(temp.name)
        result = classify_image_from_file(temp.name, token=hf_token)
    st.write(f"Hasil klasifikasi: {result}")

'''

#only for llm
'''
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modul.model_llm import get_bot_reply

st.set_page_config(page_title="Chatbot Satvika", page_icon="💬")
st.title("🤖 Chatbot Satvika (Streamlit Edition)")

# Inisialisasi riwayat obrolan
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input dari user
user_input = st.text_input("Tanya ke chatbot:")

# Proses jawaban jika ada input
if user_input:
    with st.spinner("Bot sedang menjawab..."):
        reply = get_bot_reply(user_input)
        st.session_state.chat_history.append(("🧑 Kamu", user_input))
        st.session_state.chat_history.append(("🤖 Bot", reply))

# Tampilkan riwayat obrolan
for speaker, text in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {text}")
'''

import streamlit as st
import streamlit.components.v1 as components
import os
import sys

st.set_page_config(page_title="EcoSort UI", layout="wide")
st.title("🌱 EcoSort Interface")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Add New
def render_page(page):
    if page == 'home':
        print("ini abaikan")
        with open("public/cwastemel_ui.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=1300, scrolling=True)
    elif page == 'coins':
        # st.write("Welcome to the Coins Page!")
        print("ini abaikan")
        with open("public/coin.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=1300, scrolling=True)
    elif page == 'history':
        # st.write("Welcome to the History Page!")
        print("ini abaikan")
        with open("public/history.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=1300, scrolling=True)

def page_navigation_handler(msg):
    if msg['type'] == 'set_page':
        st.session_state.page = msg['page']

# Sidebar for navigation
page_selection = st.sidebar.selectbox(
    "Select a Page",
    ("Home", "Coins", "History")  # Sidebar options
)

# Update the page content based on sidebar selection
if page_selection == "Home":
    st.session_state.page = 'home'
elif page_selection == "Coins":
    st.session_state.page = 'coins'
elif page_selection == "History":
    st.session_state.page = 'history'

# Render content based on the selected page
render_page(st.session_state.page)
# render_page(st.session_state.page)

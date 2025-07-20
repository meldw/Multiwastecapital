import streamlit as st
import streamlit.components.v1 as components
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from modul.model_vlm import classify_image_from_file
from modul.model_llm import get_bot_reply

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
        # Bagian Upload dan VLM
        st.subheader("🖼️ Klasifikasi Sampah (VLM)")
        uploaded_file = st.file_uploader("Upload gambar sampah", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            # Simpan sementara gambar
            with open("temp.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Tampilkan preview gambar
            st.image("temp.jpg", caption="Gambar yang di-upload", use_column_width=True)

            # Klasifikasi dengan model VLM
            hasil_klasifikasi = classify_image_from_file("temp.jpg")
            st.success(f"♻️ Hasil klasifikasi: **{hasil_klasifikasi}**")

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

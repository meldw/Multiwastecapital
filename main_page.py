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

# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define a function to display content based on the selected page
def render_page(page):
    if page == 'home':
        st.write("Welcome to the Home Page!")
        # You can include other content for Home here.
    elif page == 'coins':
        st.write("Welcome to the Coins Page!")
        # You can include other content for Coins here.
    elif page == 'history':
        st.write("Welcome to the History Page!")
        # You can include other content for History here.

# Display the HTML navigation bar (with the modified button elements)
with open("public/cwastemel_ui.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1300, scrolling=True)

# Add buttons for navigation in Streamlit (they control which page is displayed)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Home'):
        st.session_state.page = 'home'

with col2:
    if st.button('Coins'):
        st.session_state.page = 'coins'

with col3:
    if st.button('History'):
        st.session_state.page = 'history'

# Render content based on the selected page
render_page(st.session_state.page)

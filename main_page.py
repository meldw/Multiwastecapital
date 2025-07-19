import streamlit as st
import streamlit.components.v1 as components
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_vlm import classify_image_from_file
from model_llm import get_bot_reply

st.set_page_config(page_title="EcoSort UI", layout="wide")
st.title("🌱 EcoSort Interface")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Add New
def render_page(page):
    if page == 'home':
        st.write("Welcome to the Home Page!")
    elif page == 'coins':
        st.write("Welcome to the Coins Page!")
    elif page == 'history':
        st.write("Welcome to the History Page!")

# Add New
with open("public/cwastemel_ui.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1300, scrolling=True)

def page_navigation_handler(msg):
    if msg['type'] == 'set_page':
        st.session_state.page = msg['page']

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Home'):
        st.session_state.page = 'home'
        st.experimental_rerun()  # Trigger a rerun to reflect changes immediately

with col2:
    if st.button('Coins'):
        st.session_state.page = 'coins'
        st.experimental_rerun()  # Trigger a rerun to reflect changes immediately

with col3:
    if st.button('History'):
        st.session_state.page = 'history'
        st.experimental_rerun()  # Trigger a rerun to reflect changes immediately

# Render content based on the selected page
render_page(st.session_state.page)

# Handle the pages click
# message = st.query_params ()

# Check Params
# if "page" in message:
#     st.session_state.page = message["page"][0]
#     st.experimental_rerun()

# Render item pages
# render_page(st.session_state.page)

# # Add New
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button('Home'):
#         st.session_state.page = 'home'
# with col2:
#     if st.button('Coins'):
#         st.session_state.page = 'coins'
# with col3:
#     if st.button('History'):
#         st.session_state.page = 'history'

# # Add New
# render_page(st.session_state.page)

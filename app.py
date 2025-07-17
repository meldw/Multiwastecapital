
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sampah Bercuan", layout="centered")

# ===== Custom CSS untuk mempercantik tombol dan teks =====
st.markdown("""
<style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 10px;
    }

    .description {
        font-size: 18px;
        text-align: center;
        color: #444444;
        margin-bottom: 30px;
    }

    .button-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }

    .stButton > button {
        background-color: #2E8B57;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 12px 20px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #276c48;
    }
</style>
""", unsafe_allow_html=True)

# ===== Title and Description =====
st.markdown('<div class="main-title">👋 Selamat Datang di Sampah Bercuan!</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Aplikasi ini membantu kamu mengenali jenis sampah, berkonsultasi lewat chatbot, dan memantau coin serta histori transaksi.</div>', unsafe_allow_html=True)

st.markdown("### 🔍 Pilih fitur yang ingin kamu akses:")

# ===== Tiga Kolom Tombol =====
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🖼️ Deteksi Sampah + Chat"):
        st.switch_page("pages/main_page.py")

with col2:
    if st.button("💰 Coin & Investasi"):
        st.switch_page("pages/coin_page.py")

with col3:
    if st.button("📜 Riwayat Transaksi"):
        st.switch_page("pages/history_page.py")






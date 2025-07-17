import streamlit as st

st.set_page_config(page_title="Sampah Bercuan", layout="centered")

# ===== Custom CSS untuk background dan elemen lainnya =====
st.markdown("""
<style>
    body {
        background: linear-gradient(to bottom right, #e0f7e9, #ffffff);
    }

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

    .stButton > button {
        background-color: #2E8B57;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 12px 20px;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #276c48;
    }

    /* Atur seluruh halaman */
    .block-container {
        background: linear-gradient(to bottom right, #e0f7e9, #ffffff);
        padding: 2rem;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ===== Title dan Deskripsi =====
st.markdown('<div class="main-title">👋 Selamat Datang di Sampah Bercuan!</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Aplikasi ini membantu kamu mengenali jenis sampah, berkonsultasi lewat chatbot, dan memantau coin serta histori transaksi.</div>', unsafe_allow_html=True)

st.markdown("### 🔍 Pilih fitur yang ingin kamu akses:")

# ===== Tombol Navigasi =====
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






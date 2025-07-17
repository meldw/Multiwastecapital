
#we try use html gabung 3 halaman

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sampah Bercuan", layout="centered")

st.title("👋 Selamat Datang di Sampah Bercuan!")

st.markdown("""
Aplikasi ini membantu kamu mengenali jenis sampah, berkonsultasi lewat chatbot, dan memantau coin serta histori transaksi.
""")

st.markdown("### 🔍 Pilih fitur yang ingin kamu akses:")

# Buat 3 tombol sebagai gateway ke 3 halaman
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





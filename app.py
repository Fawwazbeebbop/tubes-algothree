import streamlit as st
import time

st.set_page_config(
    page_title="Sistem Kasir Greedy",
    page_icon="💰",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #f9fafb;
}

.title {
    text-align: center;
    color: #1f2937;
}

.card {
    background-color: #99C5F1;
    padding: 10px;
    border-radius: 12px;
    margin-top: 7px;
    margin-bottom: 7px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.result-title {
    color: #2563eb;
    font-weight: bold;
}

.time {
    color: #16a34a;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

from recursive import greedy_recursive
from iterative import greedy_iterative

COINS = [5000, 2000, 1000, 500, 200, 100]

st.markdown("<h1 class='title'>💰 Sistem Kasir</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='title'>Perbandingan Algoritma Greedy Iteratif & Rekursif</h4>", unsafe_allow_html=True)

st.divider()

total_belanja = st.number_input("Total Belanja (Rp)", min_value=0, step=100)
uang_dibayar = st.number_input("Uang Dibayar (Rp)", min_value=0, step=100)

if st.button("Hitung Kembalian"):
    if uang_dibayar < total_belanja:
        st.error("❌ Uang dibayar kurang dari total belanja!")
    else:
        kembalian = uang_dibayar - total_belanja
        st.success(f"✅ Kembalian: Rp {kembalian}")

        start = time.perf_counter()
        iteratif_result = greedy_iterative(kembalian, COINS)
        iteratif_time = time.perf_counter() - start

        start = time.perf_counter()
        rekursif_result = greedy_recursive(kembalian, COINS)
        rekursif_time = time.perf_counter() - start
        
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<p class='result-title'>🔁 Greedy Iteratif</p>", unsafe_allow_html=True)
        st.write(iteratif_result)
        st.markdown(f"<p class='time'>⏱ Waktu Eksekusi: {iteratif_time:.8f} detik</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<p class='result-title'>🔂 Greedy Rekursif</p>", unsafe_allow_html=True)
        st.write(rekursif_result)
        st.markdown(f"<p class='time'>⏱ Waktu Eksekusi: {rekursif_time:.8f} detik</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

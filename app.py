import streamlit as st
import time

from greedy.iterative import greedy_iterative
from greedy.recursive import greedy_recursive

st.set_page_config(page_title="Sistem Kasir Greedy", page_icon="💰")

COINS = [1000, 500, 200, 100]

# Statis data
ITEMS = {
    "Beras 5kg": {"price": 65000, "img": "img/beras.jpg"},
    "Minyak Goreng": {"price": 18000, "img": "img/minyak.jpg"},
    "Gula Pasir": {"price": 14000, "img": "img/gula.jpg"},
    "Telur 1kg": {"price": 28000, "img": "img/telor.jpg"},
    "Mie Instan": {"price": 3500, "img": "img/mie.jpg"},
    "Susu UHT": {"price": 7000, "img": "img/susu.jpg"},
    "Kopi": {"price": 12000, "img": "img/kopi.jpg"},
    "Teh": {"price": 8000, "img": "img/teh.jpg"},
    "Sabun Mandi": {"price": 6000, "img": "img/sabun.jpg"},
    "Deterjen": {"price": 15000, "img": "img/deterjen.jpg"}
}

st.title("Sistem Kasir Sederhana")

left_col, right_col = st.columns([2, 1])

total_belanja = 0
jumlah_barang = {}

with left_col:
    st.markdown("### 🛒 Daftar Barang")

    for item, data in ITEMS.items():
        col_img, col_input = st.columns([1, 3])

        with col_img:
            st.image(data["img"], width=70)

        with col_input:
            qty = st.number_input(
                f"{item} (Rp {data['price']})",
                min_value=0,
                step=1,
                key=item
            )
            jumlah_barang[item] = qty
            total_belanja += qty * data["price"]

with right_col:
    st.markdown("### 💵 Ringkasan Transaksi")
    st.success(f"Total Belanja: Rp {total_belanja}")

    uang_dibayar = st.number_input("Uang Dibayar (Rp)", min_value=0, step=100)

    if st.button("Hitung Kembalian"):
        if uang_dibayar < total_belanja:
            st.error("Uang dibayar kurang!")
        else:
            kembalian = uang_dibayar - total_belanja
            st.success(f"Kembalian: Rp {kembalian}")

            start = time.perf_counter()
            hasil_iteratif = greedy_iterative(kembalian, COINS)
            waktu_iteratif = time.perf_counter() - start

            start = time.perf_counter()
            hasil_rekursif = greedy_recursive(kembalian, COINS)
            waktu_rekursif = time.perf_counter() - start

            st.markdown("#### 🔁 Greedy Iteratif")
            st.write(hasil_iteratif)
            st.caption(f"Waktu: {waktu_iteratif:.8f} detik")

            st.markdown("#### 🔂 Greedy Rekursif")
            st.write(hasil_rekursif)
            st.caption(f"Waktu: {waktu_rekursif:.8f} detik")

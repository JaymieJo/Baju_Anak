import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Toko Baju Bayi")

# Data baju bayi (kombinasi URL dan gambar lokal)
baju_bayi = [
    {"Nama": "Baju Bayi Motif Hewan", "Harga": 100000, "Gambar": "images/baby_animal.jpg"},
    {"Nama": "Baju Bayi Motif Bunga", "Harga": 95000, "Gambar": "images/baby_flower.jpg"},
    {"Nama": "Baju Bayi Motif Mobil", "Harga": 105000, "Gambar": "images/baby_car.jpg"},
    {"Nama": "Baju Bayi Motif Buah", "Harga": 110000, "Gambar": "images/baby_fruit.jpg"}, 
    {"Nama": "Baju Bayi Motif Kartun", "Harga": 120000, "Gambar": "images/baby_cartoon.jpg"},
    {"Nama": "Baju Bayi Motif Polkadot", "Harga": 90000, "Gambar": "images/baby_polkadot.jpg"}, 
    {"Nama": "Baju Bayi Motif Pelangi", "Harga": 115000, "Gambar": "images/baby_rainbow.jpg"},
    {"Nama": "Baju Bayi Motif Bintang", "Harga": 100000, "Gambar": "images/baby_star.jpg"},
    {"Nama": "Baju Bayi Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/baby_space.jpg"},
]

# Inisialisasi total harga
total_harga = 0

# Menampilkan katalog dan pilihan jumlah
for baju in baju_bayi:
    col1, col2 = st.columns([1, 3])

    with col1:
        try:
            # Coba ambil gambar dari URL
            if baju["Gambar"].startswith("http"):
                response = requests.get(baju["Gambar"])
                img = Image.open(BytesIO(response.content))
            else:
                # Jika gambar lokal
                img = Image.open(baju["Gambar"])

            st.image(img, use_column_width=True)
        except Exception as e:
            st.error(f"Gagal memuat gambar untuk {baju['Nama']}")

    with col2:
        st.subheader(baju["Nama"])
        st.write(f"Harga: Rp {baju['Harga']:,}")
        jumlah = st.number_input(f"Jumlah untuk {baju['Nama']}", min_value=0, max_value=10, step=1, key=baju["Nama"])
        total_harga += jumlah * baju["Harga"]
        
    # Menampilkan total harga
st.markdown("## Total Harga")
st.write(f"*Rp {total_harga:,}*")

# Tombol beli
if st.button("Beli Sekarang"):
    st.success("Terima kasih atas pembelian Anda!")

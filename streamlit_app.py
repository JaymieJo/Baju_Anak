import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Judul aplikasi
st.title("Katalog Toko Baju Bayi")

# Deskripsi halaman
st.write("Selamat datang di toko baju online kami! Di sini Anda dapat menemukan berbagai macam baju dengan harga terjangkau.")

# Buat sidebar
with st.sidebar:
    # Kategori baju
    kategori = st.selectbox("Kategori", ["Semua", "Kaos", "Kemeja", "Celana", "Rok"])

    # Rentang harga
    harga_min, harga_max = st.slider("Rentang Harga", 0, 100, (0, 100))

    # Ukuran baju
    ukuran = st.multiselect("Ukuran", ["S", "M", "L", "XL", "XXL"])

    # Warna baju
    warna = st.multiselect("Warna", ["Merah", "Biru", "Hijau", "Kuning", "Hitam", "Putih"])

# Keranjang belanja
keranjang = []

# Tambahkan baju ke keranjang
def add_to_cart(baju):
    keranjang.append(baju)

# Hapus baju dari keranjang
def remove_from_cart(baju):
    keranjang.remove(baju)

# Filter data baju
if kategori != "Semua":
    data = data[data["Kategori"] == kategori]
if harga_min > 0 or harga_max < 100:
    data = data[(data["Harga"] >= harga_min) & (data["Harga"] <= harga_max)]
if len(ukuran) > 0:
    data = data[data["Ukuran"].isin(ukuran)]
if len(warna) > 0:
    data = data[data["Warna"].isin(warna)]

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

# Checkout
def checkout():
    st.write("Terima kasih telah berbelanja di toko kami!")
    st.write("Total pesanan Anda adalah Rp{sum(baju['Harga'] for baju in keranjang)}")
    st.write("Silakan lakukan pembayaran ke rekening berikut:")
    st.write("Nama Bank: Bank ABC")
    st.write("Nomor Rekening: 1234567890")
    st.write("Atas Nama: Toko Baju Online")


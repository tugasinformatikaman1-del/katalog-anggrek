import streamlit as st
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Katalog Orchids Rafeyfara", layout="wide")

# 2. CSS UNTUK TAMPILAN PROFESIONAL
st.markdown("""
    <style>
    [data-testid="stImage"] img[src*="Banner"] {
        max-height: 400px; 
        object-fit: contain;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    [data-testid="column"] img {
        height: 250px; 
        object-fit: contain;
        background-color: #fcfcfc;
        border-radius: 12px;
        border: 1px solid #eee;
    }
    .nama-anggrek {
        font-size: 18px; font-weight: bold; text-align: center; margin-top: 10px; color: #1b5e20;
    }
    .status-tanaman {
        font-size: 14px; text-align: center; color: #666; font-style: italic;
    }
    .harga-anggrek {
        font-size: 19px; font-weight: 800; text-align: center; color: #e91e63; margin-bottom: 5px;
    }
    .info-box {
        background-color: #f0f7f0; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. JUDUL & BANNER
st.title("🌸 Katalog Orchids Rafeyfara")
if os.path.exists("Banner.png"):
    st.image("Banner.png", use_container_width=True)

# 4. INFORMASI PENGIRIMAN
st.markdown("""
    <div class="info-box">
        <strong>📍 Informasi Pengiriman:</strong><br>
        • Tanaman sehat, akar jalan, packing aman dengan kardus tebal.<br>
        • <em>Bisa kirim ke seluruh Indonesia.</em>
    </div>
    """, unsafe_allow_html=True)

# 5. MENU UTAMA
tabs = st.tabs(["🛍️ Katalog Produk", "🩺 Klinik & Nutrisi Anggrek"])

with tabs[0]:
    # Sesuaikan pilihan menu
    menu = st.selectbox("Pilih Jenis Koleksi:", 
        ["Anggrek Dendrobium", "Anggrek Bulan", "Anggrek Vanda", "Anggrek Onsidium", "Anggrek Paphiopedilum", "Anggrek Hutan"])

    st.divider()

    # Tips Perawatan
    tips_perawatan = {
        "Anggrek Dendrobium": "☀️ Suka matahari (50-70%). 💧 Siram 1-2 hari sekali. 🧪 Pupuk Tinggi P untuk bunga.",
        "Anggrek Bulan": "☁️ Teduh. 💧 Siram 2x seminggu. 🧪 Pupuk bunga cair 10 hari sekali.",
        "Anggrek Vanda": "☀️ Suka banyak cahaya. 💧 Siram akar pagi & sore. 🧪 Rendam akar dengan pupuk 2x seminggu.",
        "Anggrek Onsidium": "🌤️ Terang tapi sejuk. 💧 Jaga kelembapan media. 🧪 Pupuk NPK seimbang.",
        "Anggrek Paphiopedilum": "☁️ Lembap & Teduh. 💧 Media tidak boleh kering. 🧪 Pupuk organik dosis rendah.",
        "Anggrek Hutan": "🌲 Habitat asli (Lembap). 💧 Siram air hujan. 🧪 Hindari pupuk kimia berlebih."
    }

    def tampilkan_katalog(list_anggrek, jenis):
        cols = st.columns(4)
        for i, item in enumerate(list_anggrek):
            with cols[i % 4]:
                # Cek file foto
                if os.path.exists(item['foto']):
                    st.image(item['foto'], use_container_width=True)
                    st.markdown(f"<div class='nama-anggrek'>{item['nama']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='status-tanaman'>{item['status']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='harga-anggrek'>Rp {item['harga']:,}</div>".replace(",", "."), unsafe_allow_html=True)
                    with st.popover("Cara Perawatan"):
                        st.info(tips_perawatan[jenis])
                else:
                    st.error(f"Foto '{item['foto']}' tidak ditemukan. Cek nama filenya!")

    # 6. LOGIKA DATA (PASTIKAN NAMA FILE SESUAI DAFTAR DI KOMPUTER)
    if menu == "Anggrek Dendrobium":
        data = [
            {"foto": "dendro1.JPG", "nama": "Dendro Keriting", "status": "Dewasa", "harga": 65000},
            {"foto": "dendro2.JPG", "nama": "Dendro Putih", "status": "Berbunga", "harga": 60000}
        ]
        tampilkan_katalog(data, menu)

    elif menu == "Anggrek Bulan":
        data = [
            {"foto": "bulan1.JPG", "nama": "Bulan Putih", "status": "Knop", "harga": 125000},
            {"foto": "bulan2.JPG", "nama": "Bulan Totol", "status": "Mekar", "harga": 130000}
        ]
        tampilkan_katalog(data, menu)

    elif menu == "Anggrek Vanda":
        # Sesuai gambar: vanda1.JPG, vanda2.JPG, vanda3.JPG
        data = [
            {"foto": "vanda1.JPG", "nama": "Vanda Ungu Totol", "status": "Gantung", "harga": 450000},
            {"foto": "vanda2.JPG", "nama": "Vanda Biru Langit", "status": "Koleksi", "harga": 500000},
            {"foto": "vanda3.JPG", "nama": "Vanda Spesies", "status": "Dewasa", "harga": 550000}
        ]
        tampilkan_katalog(data, menu)

    elif menu == "Anggrek Onsidium":
        # Sesuai gambar: onsidium1.JPG, onsidium2.JPG, dsb
        data = [
            {"foto": "onsidium1.JPG", "nama": "Onsi Golden Shower", "status": "Rimbun", "harga": 185000},
            {"foto": "onsidium2.JPG", "nama": "Onsi Kuning", "status": "Siap Bunga", "harga": 190000}
        ]
        tampilkan_katalog(data, menu)

    elif menu == "Anggrek Paphiopedilum":
        # Sesuai gambar: paphiopedilum1.JPG, paphiopedilum2.JPG
        data = [
            {"foto": "paphiopedilum1.JPG", "nama": "Paphio Kantong 1", "status": "Rawatan", "harga": 300000},
            {"foto": "paphiopedilum2.JPG", "nama": "Paphio Kantong 2", "status": "Koleksi", "harga": 325000}
        ]
        tampilkan_katalog(data, menu)

    elif menu == "Anggrek Hutan":
        # Sesuai dengan nama file asli di folder Anda
        data = [
            {"foto": "anggrek_hutan1.JPG", "nama": "Hutan Spesies 1", "status": "Rawatan", "harga": 400000},
            {"foto": "Anggrek_hutan2.JPG", "nama": "Hutan Spesies 2", "status": "Langka", "harga": 450000}
        ]
        tampilkan_katalog(data, menu)

# --- TAB 2: KLINIK & NUTRISI ---
with tabs[1]:
    st.subheader("🧪 Rahasia Anggrek Cepat Berbunga")
    st.write("Gunakan pupuk tinggi P (Fosfor) seminggu sekali dan pastikan sinar matahari cukup.")
    st.divider()
    st.subheader("🩺 Identifikasi Penyakit")
    st.error("Busuk Hitam: Potong bagian busuk, oleskan fungisida.")
    st.warning("Kutu Putih: Lap dengan alkohol 70% atau semprot insektisida.")

# 9. KONTAK
st.divider()
st.link_button("📲 Hubungi Admin via WhatsApp", "https://wa.me/628123456789")
st.caption("© 2024 Orchids Rafeyfara")
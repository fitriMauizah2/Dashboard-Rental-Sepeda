import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dashboard/day.csv")

# Konversi kolom tanggal ke format datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Mapping angka bulan ke nama bulan
month_names = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}
df['month_name'] = df['mnth'].map(month_names)

# Sidebar untuk filter bulan
st.sidebar.title("Filter Data")
selected_month = st.sidebar.selectbox("Pilih Bulan", df['month_name'].unique())

# Filter data berdasarkan bulan yang dipilih
df_filtered = df[df['month_name'] == selected_month]

# Judul dashboard
st.title("Dashboard Rental Sepeda")
st.write("Visualisasi Data Penyewaan Sepeda")

# Menampilkan DataFrame
st.subheader("Dataset Bike Rental (Filtered)")
st.dataframe(df_filtered)

# Visualisasi tren penyewaan sepeda
st.subheader("📊 Tren Penyewaan Sepeda per Hari")
fig, ax = plt.subplots()
ax.plot(df_filtered['dteday'], df_filtered['cnt'], marker='o', linestyle='-')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title(f"Tren Peminjaman Sepeda di {selected_month}")
plt.xticks(rotation=45)
st.pyplot(fig)

# Footer
st.markdown(
    """
    ---
     **Catatan:**  
    - Data ini merupakan hasil analisis penggunaan sepeda berdasarkan dataset Bike Rental.  
    - Dashboard ini dibuat menggunakan **Streamlit** untuk memudahkan visualisasi tren penggunaan sepeda.  
    """
)

# Bike Rental Analysis Dashboard

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti hari kerja vs akhir pekan dan kondisi cuaca. Hasil analisis divisualisasikan dalam dashboard interaktif menggunakan Streamlit.

## Setup Environment

### Menggunakan Annaconda

Jika menggunakan Anaconda, jalankan perintah berikut di terminal/cmd:  

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt


### Menggunakan Terminal

mkdir submission
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt


## Struktur Folder

submission 
├───dashboard 
    │ ├───day.csv 
    │ └───dashboard.py 
├───notebook.ipynb 
├───README.md 
├───requirements.txt 
└───url.txt

## Cara Menjalankan Dashboard

1. Pastikan Python dan Streamlit sudah terinstall.
2. Jalankan perintah berikut di terminal:
    streamlit run dashboard/dashboard.py
3. Dashboard akan terbuka di browser.



## Link Dashboard Online

Jika dashboard sudah di-deploy ke Streamlit Cloud, tambahkan linknya di sini.

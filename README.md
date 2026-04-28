# Bike Sharing Dataset - Analisis Data & Dashboard

Proyek analisis data penyewaan sepeda dari dataset **Capital Bikeshare** (Washington D.C., 2011-2012) yang mencakup Exploratory Data Analysis (EDA), visualisasi, dan interactive dashboard.

---

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Struktur Folder](#struktur-folder)
- [Requirement](#requirement)
- [Dicoding Collection Dashboard](#dicoding-collection-dashboard-)
- [Cara Menjalankan Notebook](#cara-menjalankan-notebook)
- [Cara Menjalankan Dashboard](#cara-menjalankan-dashboard)
- [Insight & Kesimpulan](#insight--kesimpulan)

---

## ✨ Fitur Utama

### 1. **Exploratory Data Analysis (EDA)**

- Data gathering dan assessment
- Data cleaning (konversi tipe data, scaling nilai, mapping kategori)
- Statistik deskriptif dan analisis tren
- Identifikasi outlier dan missing values

### 2. **Visualisasi & Analysis**

- Pengaruh cuaca dan musim terhadap penyewaan sepeda
- Pola penggunaan berdasarkan jam (hari kerja vs akhir pekan)
- Segmentasi jam berdasarkan volume penyewaan
- Heatmap dan time series analysis

### 3. **Interactive Dashboard**

- Filter dinamis (tahun, musim, cuaca)
- Visualisasi KPI dan tren
- Perbandingan casual vs registered users
- Real-time analytics

---

## 📁 Struktur Folder

```
submission/
├── notebook.ipynb              # Jupyter Notebook dengan EDA lengkap
├── README.md                   # Dokumentasi proyek (file ini)
├── requirements.txt            # Library dependencies
├── dashboard/
│   ├── dashboard.py           # Streamlit dashboard application
│   └── main_data.csv          # Data yang di-export untuk dashboard
└── data/
    ├── day.csv                # Dataset harian (731 baris, 2011-2012)
    └── hour.csv               # Dataset per jam (17.379 baris, 2011-2012)
```

---

## 🔧 Requirement

**Python Version:** 3.8 atau lebih tinggi

### Library yang Digunakan:

```
streamlit==1.28.0
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
numpy==1.24.3
```

---

## 🎯 Dicoding Collection Dashboard ✨

Panduan lengkap untuk menjalankan proyek analisis data dan dashboard interaktif.

### Setup Environment - Anaconda

```bash
# Buat environment baru dengan Python 3.9
conda create --name main-ds python=3.9

# Aktifkan environment
conda activate main-ds

# Install dependencies
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal (Pipenv)

```bash
# Buat folder proyek
mkdir proyek_analisis_data
cd proyek_analisis_data

# Initialize pipenv dan install dependencies
pipenv install

# Aktifkan virtual environment
pipenv shell

# Install requirements
pip install -r requirements.txt
```

### Run Streamlit App

```bash
# Navigasi ke folder dashboard
cd dashboard

# Jalankan streamlit application
streamlit run dashboard.py
```

Dashboard akan terbuka di: **http://localhost:8501**

---

## 📖 Cara Menjalankan Notebook

### 1. **Setup Environment**

**Windows:**

```bash
# Buka Command Prompt atau PowerShell dan navigasi ke folder proyek
cd "path/to/Proyek Analisis Data"

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate
```

**macOS/Linux:**

```bash
cd "path/to/Proyek Analisis Data"
python3 -m venv venv
source venv/bin/activate
```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Jalankan Notebook**

**Opsi A: Menggunakan Jupyter Notebook**

```bash
pip install jupyter
jupyter notebook notebook.ipynb
```

**Opsi B: Menggunakan VS Code**

- Buka file `notebook.ipynb` di VS Code
- Klik tombol "Run All" atau jalankan setiap cell secara berurutan

**Opsi C: Menggunakan Google Colab**

- Upload file `notebook.ipynb` ke Google Drive
- Buka di Google Colab
- Upload juga folder `data/` jika menggunakan Colab

### 4. **Output Notebook**

- Semua visualisasi akan ditampilkan secara inline
- File `dashboard/main_data.csv` akan dibuat otomatis saat cell export data dijalankan

---

## 🚀 Cara Menjalankan Dashboard

### Prasyarat:

Pastikan **notebook sudah dijalankan sampai selesai** sehingga file `dashboard/main_data.csv` sudah terbuat.

### Menjalankan Dashboard:

**Windows:**

```bash
cd "path/to/Proyek Analisis Data"
venv\Scripts\activate
cd dashboard
streamlit run dashboard.py
```

**macOS/Linux:**

```bash
cd "path/to/Proyek Analisis Data"
source venv/bin/activate
cd dashboard
streamlit run dashboard.py
```

### Dashboard Akan Terbuka di:

```
http://localhost:8501
```

### Fitur Dashboard:

✅ **Sidebar Filters:**

- Filter berdasarkan Tahun (2011, 2012)
- Filter berdasarkan Musim (Spring, Summer, Fall, Winter)
- Filter berdasarkan Kondisi Cuaca (Clear, Mist, Rain)

✅ **Visualisasi Utama:**

- KPI Card: Total penyewaan, rata-rata per hari
- Trend penyewaan per waktu
- Perbandingan casual vs registered users
- Analisis per musim dan cuaca
- Distribusi penyewaan per jam

---

## 📊 Insight & Kesimpulan

### **Pertanyaan 1: Pengaruh Cuaca dan Musim**

**Temuan Utama:**

1. **Musim Gugur (Fall)** memiliki rata-rata penyewaan tertinggi: **5.644 per hari**
   - Musim Semi (Spring) terendah: **2.649 per hari**
   - Perbedaan: **213% lebih tinggi** di musim gugur

2. **Cuaca Cerah** menghasilkan penyewaan **2x lebih tinggi** (5.002 per hari)
   - Cuaca hujan ringan: 2.673 per hari (47% lebih rendah)
   - Faktor cuaca adalah penentu utama minat pengguna

3. **Pertumbuhan Signifikan 2011 → 2012:**
   - Total penyewaan naik **64%**
   - Menunjukkan peningkatan adopsi layanan bike sharing

---

### **Pertanyaan 2: Pola Penggunaan Hari Kerja vs Akhir Pekan**

**Temuan Utama:**

1. **Hari Kerja (Workday)** - Pola Bimodal (2 puncak):
   - **Puncak Pagi:** Jam 8:00 (474 penyewaan) - komuter ke kantor
   - **Puncak Sore:** Jam 17:00-18:00 (575 penyewaan) - pulang kerja
   - Perbedaan: **22% lebih tinggi** sore hari

2. **Akhir Pekan (Weekend)** - Pola Unimodal (1 puncak):
   - **Puncak:** Jam 14:00 (419 penyewaan) - rekreasi siang hari
   - Distribusi lebih merata sepanjang hari
   - Volume **27% lebih rendah** dibanding hari kerja

3. **Jam-jam Kritis (High Volume):**
   - 6 jam dengan volume tertinggi: **11:00-14:00 dan 17:00-19:00**
   - Ideal untuk: Optimasi distribusi sepeda dan promosi
   - Jam 00:00-07:00 (Low Volume) ideal untuk: Maintenance & cleaning

---

## 💡 Rekomendasi Action Item

### **1. Strategi Distribusi Sepeda**

- ✅ Hari kerja: Pastikan ketersediaan tinggi di residential areas (06:00-08:00) dan CBD (16:00-19:00)
- ✅ Akhir pekan: Distribusikan ke area wisata & taman (10:00-16:00)
- ✅ Jam 00:00-07:00: Waktu ideal untuk perawatan armada

### **2. Strategi Promosi Musiman**

- ✅ **Musim Gugur & Panas:** Kampanye intensif (minat tinggi)
- ✅ **Musim Semi & Dingin:** Promo diskon untuk menjaga loyalitas

### **3. Optimasi Pricing**

- ✅ Dynamic pricing pada jam puncak (sore hari & akhir pekan)
- ✅ Diskon off-peak untuk meratakan demand

---

## 📝 Dataset Information

**Sumber Data:** Capital Bikeshare System, Washington D.C. USA  
**Periode:** 1 Januari 2011 - 31 Desember 2012 (2 tahun)  
**Total Records:** 17.379 observations (hourly), 731 observations (daily)

**Kolom Utama:**

- `dteday`: Tanggal observasi
- `season`: Musim (1=Spring, 2=Summer, 3=Fall, 4=Winter)
- `weathersit`: Kondisi cuaca (1-4)
- `temp`: Suhu (normalized 0-1)
- `hum`: Kelembaban (normalized 0-1)
- `windspeed`: Kecepatan angin (normalized 0-1)
- `casual`: Pengguna casual
- `registered`: Pengguna registered
- `cnt`: Total penyewaan (target variable)

---

## 📧 Informasi Autor

**Nama:** Putu Krisna Udayana  
**Email:** krisnaudayana05@gmail.com  
**ID Dicoding:** krisna_udayana

---

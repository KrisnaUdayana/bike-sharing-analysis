# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Title
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis Pola Penyewaan Sepeda Berdasarkan Waktu, Cuaca, dan Musim")

# Load data
@st.cache_data
def load_data():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'main_data.csv')
    df = pd.read_csv(data_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Data")

selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=df['year'].unique(),
    default=df['year'].unique()
)

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season_label'].unique(),
    default=df['season_label'].unique()
)

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=df['weather_label'].unique(),
    default=df['weather_label'].unique()
)

# Filter data
filtered_df = df[
    (df['year'].isin(selected_year)) &
    (df['season_label'].isin(selected_season)) &
    (df['weather_label'].isin(selected_weather))
]

# Metrics
st.subheader("📊 Statistik Utama")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata per Hari", f"{filtered_df['cnt'].mean():.0f}")
with col3:
    st.metric("Pengguna Terdaftar", f"{filtered_df['registered'].sum():,}")
with col4:
    st.metric("Pengguna Kasual", f"{filtered_df['casual'].sum():,}")

# Visualisasi 1: Tren Penyewaan per Tahun
st.subheader("📈 Tren Penyewaan per Tahun")
fig, ax = plt.subplots(figsize=(12, 6))
yearly_data = filtered_df.groupby('year')['cnt'].sum().reset_index()
colors = ['#FF6B6B', '#4ECDC4']
ax.bar(yearly_data['year'], yearly_data['cnt'], color=colors, edgecolor='black')
ax.set_xlabel('Tahun', fontsize=12)
ax.set_ylabel('Total Penyewaan', fontsize=12)
ax.set_title('Total Penyewaan Sepeda per Tahun', fontsize=14, fontweight='bold')
for i, v in enumerate(yearly_data['cnt']):
    ax.text(yearly_data['year'][i], v + 5000, f'{v:,}', ha='center', fontweight='bold')
st.pyplot(fig)

# Visualisasi 2: Pengaruh Musim dan Cuaca
st.subheader("🌤️ Pengaruh Musim dan Cuaca")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 5))
    season_data = filtered_df.groupby('season_label')['cnt'].mean().sort_values()
    season_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    ax.barh(season_data.index, season_data.values, color=season_colors, edgecolor='black')
    ax.set_xlabel('Rata-rata Penyewaan', fontsize=12)
    ax.set_title('Rata-rata Penyewaan per Musim', fontsize=12, fontweight='bold')
    for i, v in enumerate(season_data.values):
        ax.text(v + 100, i, f'{int(v):,}', va='center', fontweight='bold')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 5))
    weather_data = filtered_df.groupby('weather_label')['cnt'].mean().sort_values()
    weather_colors = ['#4CAF50', '#FFC107', '#F44336']
    ax.barh(weather_data.index, weather_data.values, color=weather_colors, edgecolor='black')
    ax.set_xlabel('Rata-rata Penyewaan', fontsize=12)
    ax.set_title('Rata-rata Penyewaan per Kondisi Cuaca', fontsize=12, fontweight='bold')
    for i, v in enumerate(weather_data.values):
        ax.text(v + 100, i, f'{int(v):,}', va='center', fontweight='bold')
    st.pyplot(fig)

# Visualisasi 3: Tren Bulanan
st.subheader("📅 Tren Penyewaran Bulanan")
fig, ax = plt.subplots(figsize=(12, 6))
monthly_data = filtered_df.groupby('month')['cnt'].mean().reset_index()
ax.plot(monthly_data['month'], monthly_data['cnt'], marker='o', linewidth=2, markersize=8, color='#FF6B6B')
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Rata-rata Penyewaan', fontsize=12)
ax.set_title('Rata-rata Penyewaan per Bulan', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des'])
ax.grid(True, alpha=0.3)
for i, v in enumerate(monthly_data['cnt']):
    ax.text(monthly_data['month'][i], v + 50, f'{int(v):,}', ha='center', fontsize=9)
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("**Dashboard by Bike Sharing Analysis** | Data 2011-2012")
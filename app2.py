import os
import pickle
import joblib
import streamlit as st
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
import base64
import csv
import time
import requests
from bs4 import BeautifulSoup
import io
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
import numpy as np
import folium
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor

from PIL import Image

# Konfigurasi halaman harus berada di bagian awal script
st.set_page_config(
    page_title="Maètala Scientist",
    layout="wide",
    page_icon="🌏"
)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Maètala Scientist',
        [
            'Home',
            'Data Description',
            'Analytics',
            'Clustering Visualization',
            'Simulasi',
            'About Us'
        ],
        menu_icon='globe',
        icons=['house', 'clipboard-data', 'graph-up', 'bi-diagram-2-fill', 'bi-play-fill', 'people'],
        default_index=0
    )

# Load Dataset
@st.cache_data
# Dataset Describe
def load_data():
  dataset_path = "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/dataset/dataset_baruku.csv"
  data = pd.read_csv(dataset_path)
  return data

# Dataset Train Mix (categorical and numeric)
def load_data2():
  dataset_path2 = "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/dataset/dataset_desc.csv"
  data = pd.read_csv(dataset_path2)
  return data

# All Numeric Dataset Train
def load_data3():
  dataset_path3 = "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/dataset/dataset_baru.csv"
  data = pd.read_csv(dataset_path3)
  return data
    
# Home Page
if selected == 'Home':
  from PIL import Image

  # URL gambar logo GreatEdu
  image_url = "https://github.com/lutfijulpian/MaetalaSciencetist/blob/main/foto/logo%20starcore.png?raw=true"

  # Mengunduh gambar
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))

  # Menyimpan gambar ke buffer
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")

  # Mengonversi gambar menjadi string base64
  img_str6 = base64.b64encode(buffered.getvalue()).decode()

  # Load the image logo Tut Wuri Handay
  image_url = "https://github.com/lutfijulpian/MaetalaSciencetist/blob/main/foto/logo%20komifo.png?raw=true"

  # Mengunduh gambar
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))

  # Menyimpan gambar ke buffer
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")

  # Mengonversi gambar menjadi string base64
  img_str3 = base64.b64encode(buffered.getvalue()).decode()

  #image_path = "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/logo komifo.png"
  #image = Image.open(image_path)
  #buffered = io.BytesIO()
  #image.save(buffered, format="PNG")
  #img_str3 = base64.b64encode(buffered.getvalue()).decode()

  # Load the image logo Batik Nasional
  image_url = "https://github.com/lutfijulpian/MaetalaSciencetist/blob/main/foto/logomtla.png?raw=true"

  # Mengunduh gambar
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))

  # Menyimpan gambar ke buffer
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")

  # Mengonversi gambar menjadi string base64
  img_str2 = base64.b64encode(buffered.getvalue()).decode()

  # Load the image for air
  image_url = "https://github.com/lutfijulpian/MaetalaSciencetist/blob/main/foto/gempa_bumi.jpg?raw=true"

  # Mengunduh gambar
  response = requests.get(image_url)
  image = Image.open(io.BytesIO(response.content))

  # Menyimpan gambar ke buffer
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")

  # Mengonversi gambar menjadi string base64
  img_str4 = base64.b64encode(buffered.getvalue()).decode()


  st.markdown(
      f"""
      <style>
      .header {{
          display: flex;
          justify-content: space-between;
      }}
      .kumlogo {{
          display: flex;
          background-position: center;
          margin-top: 40px;
      }}
      .logo3 {{
          background-image: url("data:image/jpeg;base64,{img_str6}");
          background-size: contain;
          background-repeat: no-repeat;
          width: 150px;
          height: 80px;
          margin-right: 20px;
      }}
      .logo2 {{
          background-image: url("data:image/jpeg;base64,{img_str3}");
          background-size: contain;
          background-repeat: no-repeat;
          width: 50px;
          height: 45px;
      }}
      .logo4 {{
          background-image: url("data:image/jpeg;base64,{img_str2}");
          background-size: contain;
          background-repeat: no-repeat;
          width: 40px;
          height: 45px;
      }}
      .main-content {{
          display: flex;
          justify-content: space-between;
          border-radius: 40px;
          margin-top: 60px;
      }}
      .header .title h1 {{
      }}
      .fotodas{{
          display: flex;
          justify-content: space-between;
      }}
      .des{{
          flex: 1;
          margin-left: 10px;
          text-align: justify;
      }}
      .description {{
          border-radius: 10px;
          margin-top: 20 px;
      }}
      .air {{
          flex: 1;
          background-image: url("data:image/jpeg;base64,{img_str4}");
          background-size: cover;
          background-repeat: no-repeat;
          margin-top: 20 px;
          border-radius: 10px;
      }}
      .objective {{
          flex: 1;
          padding: 20px;
          border-radius: 10px;
          background-color: #f5f5f1;
          margin-right: 10px;
          width: 50%;
          box-shadow: 0px 4px 10px rgba(0, 110, 46, 0.7);
          color: #000000;  /* Warna teks menjadi hitam */
      }}
      .benefit {{
          flex: 1;
          padding: 20px;
          border-radius: 10px;
          background-color: #D9FAEE;
          width: 50%;
      }}
      </style>
      """,
      unsafe_allow_html=True
  )

  st.markdown(
    """
        <div class="header">
            <div class="title">
                <h1>JavaQuake Insight</h1>
            </div>
            <div class="kumlogo">
                <div class="logo4"></div>
                <div class="logo2"></div>
                <div class="logo3"></div>
            </div>
        </div>
      <hr style="margin: 20px 0; border-top: 1px solid #ddd;">
      <div class="main-content">
          <div class="description">
            <div class = "fotodas">
              <div class ="air"></div>
              <p class = "des">Pelayanan publik selama ini menjadi bagian penting di mana negara diwakili pemerintah berinteraksi dengan masyarakat (Rahmadana ect al., 2020).
               Dalam konteks mitigasi dan informasi gempa bumi, sistem pelayanan publik harus mampu menyediakan mekanisme yang cepat dan tepat untuk mengurangi dampak bencana.
                Dalam menghadapi bencana alam, tindakan pencegahan selalu lebih baik daripada penanganan, oleh karenanya upaya mitigasi bencana di Indonesia merupakan hal yang 
                krusial dilakukan untuk menciptakan lingkungan yang lebih aman dan tahan bencana bagi generasi mendatang (Maulana & Andriansyah, 2024)</p>
            </div>
              <p style="text-align: justify;">Gempa bumi merupakan salah satu bencana alam yang sering terjadi di Indonesia, sebuah negara yang terletak di wilayah cincin api
               Pasifik (Tantyoko ect al., 2023). Kepulauan Indonesia terletak pada pertemuan 3 lempeng utama dunia yaitu lempeng Australia, Eurasia, dan Pasifik (Murtianto, 2010).
                Oleh karena itu, penting bagi pemerintah dan masyarakat untuk meningkatkan sistem mitigasi dan kesiapsiagaan bencana agar dapat mengurangi risiko dan dampak yang ditimbulkan 
                oleh gempa bumi, serta memastikan keselamatan dan kesejahteraan masyarakat.</p>
              <div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>
                <div class="objective"> 
                  <h4 style="text-align: center; color: #000000;">Objective</h4>
                  <p style="font-size: 0.8em; text-align: justify;">
                      <span><b>1. Meningkatkan pemahaman tentang kualitas air</b></span><br>
                      Melalui analisis prediktif, tujuan utama adalah meningkatkan pemahaman tentang faktor-faktor yang memengaruhi kualitas air di berbagai lokasi. Hal ini akan membantu dalam mengidentifikasi sumber polusi dan potensi risiko terhadap kesehatan manusia dan lingkungan.<br>
                      <span><b>2. Peningkatan responsibilitas lingkungan</b></span><br>
                      Dengan memprediksi kualitas air secara akurat, tujuan ini adalah untuk memberikan solusi yang dapat meningkatkan tanggung jawab lingkungan dalam pengelolaan sumber daya air. Hal ini dapat mencakup upaya untuk mengurangi polusi air, mengoptimalkan penggunaan air, dan meminimalkan dampak negatif terhadap ekosistem air.<br>
                      <span><b>3. Mendukung keberlanjutan lingkungan</b></span><br>
                      Melalui pemahaman yang lebih baik tentang kualitas air, tujuan ini adalah untuk mendukung upaya-upaya dalam menjaga keberlanjutan lingkungan. Hal ini dapat mencakup pengelolaan air yang lebih efisien, perlindungan habitat air, dan pemulihan ekosistem air yang terganggu.<br>
                      <span><b>4. Peningkatan kesehatan masyarakat</b></span><br>
                      Dengan memantau kualitas air secara berkala dan melakukan prediksi yang akurat, tujuan ini adalah untuk melindungi kesehatan masyarakat dari risiko yang berkaitan dengan konsumsi air yang tercemar. Hal ini akan membantu dalam mengurangi risiko penyakit terkait air dan meningkatkan kualitas hidup masyarakat secara keseluruhan.
                  </p>
                </div>
              </div>
          </div>
      </div>
  """,
  unsafe_allow_html=True
  )

  # Footer
  st.markdown("""
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
      <div style="display: flex; align-items: flex-start; font-size: 15px;">
          <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
          <div style="font-size: 15px; color: #4C4D50;">
              Universitas Siliwangi<br>
              Informatika<br>
          </div>
      </div>
  </div>
  """, unsafe_allow_html=True)

  st.markdown("""
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
  <div style="display: flex; flex-direction: column;">
      <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
          <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
              <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
              2024 <span style="margin-left: 2px"><b>Maètala Scientist</b></span>. All Rights Reserved
          </div>
          <div style="font-size: 14px; margin: 0; color: #4C4D50;">
              TSA Batch 2 | 2024
          </div>
      </div>
  </div>
  """, unsafe_allow_html=True)

  # Data Description Page
if selected == 'Data Description':
  from PIL import Image

  # Set the background image
  st.markdown(
      f"""
      <style>
      </style>
      """,
      unsafe_allow_html=True
  )

  st.markdown('<h1>Dataset Description</h1>', unsafe_allow_html=True)
  st.markdown('---')
  st.markdown("""Dataset yang kami gunakan diambil dari <a href="https://www.kaggle.com/datasets/kekavigi/earthquakes-in-indonesia/data">https://www.kaggle.com/datasets/kekavigi/earthquakes-in-indonesia/data</a>. 
  dan Repositori Gempa (Preliminary Earthquake Catalog) yang dikelola oleh BMKG Indonesia. Ini berisi data kejadian gempa bumi dari 1 November 2008 hingga 30 September
  2024, tetapi mungkin tidak akurat untuk beberapa kejadian gempa bumi terakhir yang tercatat. Ada 11 variabel dalam dataset ini, masing-masing dengan nama deskriptif.
  Variabel yang dikumpulkan dalam dataset ini adalah:

  1. eventID : Kode identitas kejadian unik
  2. datetime : Mengacu pada waktu (Waktu asal) ketika gempa bumi terjadi
  3. latitude : Koordinat lintang geografis episentrum gempa (6N, -11S)
  4. longitude : Koordinat bujur geografis episentrum gempa (95W, 141E)
  5. magnitude : Nilai yang menunjukkan besarnya kekuatan gempa
  6. mag_type : Jenis besaran gempa seperti Mlv, Mw, MwP, dll
  7. depth : Kedalaman gempa, tempat di dalam bumi dimana gempa terjadi
  8. phasecount : Jumlah stasiun fase kedatangan gempa bumi
  9. azimuth_gap : Celah azimuthal adalah sudut maksimum yang memisahkan dua stasiun seismik yang berdekatan, keduanya diukur dari episentrum gempa bumi. Jika celah azimuthal lebih dari 180°, akurasi lokasi menurun secara signifikan. Kemampuan deteksi jaringan dapat dievaluasi berdasarkan hubungan antara magnitudo dan jarak pengamatan.
  10. location : Nama lokasi episentrum gempa mengacu pada Wilayah Flinn-Engdahl (F-E). Wilayah F-E terdiri dari serangkaian zona seismik yang berdekatan yang menutupi permukaan Bumi. Dalam seismologi, zona ini merupakan standar untuk melokalisasi gempa bumi. Skema ini diusulkan pada tahun 1965 oleh Edward A.
  11. agency : BMKG, lembaga resmi yang bertugas dalam penyediaan informasi gempa bumi
  </div>""", unsafe_allow_html=True)
  st.markdown('<div>Berikut Dataset yang digunakan dalam prediksi kualitas air ini :</div>', unsafe_allow_html=True)

  df = load_data()

  st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #046335;
    }
    </style>
  """, unsafe_allow_html=True)

  # Dropdownlist untuk memilih kategori
  option = st.selectbox('Select Category:', ['All Data', 'Very Poor', 'Poor', 'Standard', 'Good','Very Good'])

  # Filter data berdasarkan kategori yang dipilih
  if option == 'All Data':
      st.dataframe(df.sort_values(by='water_quality'), width=1050)
      st.write(f"Total Data: {len(df)}")
  elif option == 'Very Poor':
      verypoor_df = df[df['water_quality'] == 'Very Poor'].sort_values(by='water_quality')
      st.dataframe(verypoor_df, width=1050)
      st.write(f"Total Data VeryPoor: {len(verypoor_df)}")
  elif option == 'Poor':
      poor_df = df[df['water_quality'] == 'Poor'].sort_values(by='water_quality')
      st.dataframe(poor_df, width=1050)
      st.write(f"Total Data Poor: {len(poor_df)}")
  elif option == 'Standard':
      standard_df = df[df['water_quality'] == 'Standard'].sort_values(by='water_quality')
      st.dataframe(standard_df, width=1050)
      st.write(f"Total Data Standard: {len(standard_df)}")
  elif option == 'Good':
      good_df = df[df['water_quality'] == 'Good'].sort_values(by='water_quality')
      st.dataframe(good_df, width=1050)
      st.write(f"Total Data Good: {len(good_df)}")
  else:
      verygood_df = df[df['water_quality'] == 'Very Good'].sort_values(by='water_quality')
      st.dataframe(verygood_df, width=1050)
      st.write(f"Total Data VeryGood: {len(verygood_df)}")

  # Footer
  st.markdown("""
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
      <div style="display: flex; align-items: flex-start; font-size: 15px;">
          <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
          <div style="font-size: 15px; color: #4C4D50;">
              Universitas Siliwangi<br>
              Informatika<br>
          </div>
      </div>
  </div>
  """, unsafe_allow_html=True)

  st.markdown("""
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
  <div style="display: flex; flex-direction: column;">
      <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
          <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
              <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
              2024 <span style="margin-left: 2px"><b>Maètala Scientist</b></span>. All Rights Reserved
          </div>
          <div style="font-size: 14px; margin: 0; color: #4C4D50;">
              TSA Batch 2 | 2024
          </div>
      </div>
  </div>
  """, unsafe_allow_html=True)

if selected == 'Analytics':
    from PIL import Image
    import streamlit as st
    import leafmap.foliumap as leafmap
    import plotly.graph_objects as go

    # Memuat font League Spartan
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400&display=swap');
        .plotly .text { font-family: 'League Spartan', sans-serif; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Definisi label, ukuran, dan count untuk pie chart
    labels = ['Pagi', 'Siang', 'Sore', 'Fajar', 'Malam']
    sizes = [23.66, 26.98, 25.87, 12.79, 10.70]

    # Cari indeks dari data dengan nilai terbesar
    max_index = sizes.index(max(sizes))

    # Warna untuk setiap bagian pie chart
    colors = ['#2db488', '#db9942', '#e65695', '#605dc8', '#892fc1']

    # Membuat pie chart menggunakan plotly dan menonjolkan bagian terbesar
    fig_pie = go.Figure(data=[go.Pie(
        labels=labels,  # Tambahkan labels
        values=sizes,
        hoverinfo='label+percent+value',  # Menampilkan label, persentase, dan nilai
        textinfo='label+percent',  # Menampilkan label dan persentase
        textfont_size=14,
        textfont=dict(family='League Spartan', color='white'),  # Mengatur font dan warna teks
        marker=dict(line=dict(color='black', width=2)),
        pull=[0.1 if i == max_index else 0 for i in range(len(sizes))],  # Menonjolkan data terbesar
        marker_colors=colors  # Mengatur warna
    )])

    # Menambahkan judul dan layout untuk pie chart
    fig_pie.update_layout(
        legend_title="Waktu Sehari",
        margin=dict(t=50, l=0, r=0, b=0),
        font=dict(family='League Spartan', color='white')  # Mengatur font untuk judul dan legenda
    )

    # Data contoh: magnitudo gempa bumi dalam persen
    labels_bar = ['Minor', 'Mikro', 'Ringan', 'Sedang', 'Besar', 'Mayor', 'Kuat']
    magnitudes = [46.78, 38.21, 12.13, 2.06, 0.36, 0.05, 0.14]  # Persentase magnitudo gempa

    # Warna khusus untuk masing-masing bar
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF3', '#F3FF33', '#FF33A8']

    # Membuat bar chart menggunakan plotly dan menambahkan keterangan persentase pada masing-masing bar
    fig_bar = go.Figure(data=[go.Bar(
        x=labels_bar,
        y=magnitudes,
        text=[f'{val:.2f}%' for val in magnitudes],  # Menampilkan persentase sebagai teks di atas bar
        textposition='auto',  # Posisi teks akan otomatis diatur agar tampil rapi
        marker_color=colors,  # Warna batang khusus untuk tiap bar
        marker_line_color='rgba(0, 0, 0, 1)',  # Warna garis batas batang
        marker_line_width=1.5
    )])

    # Menambahkan judul dan layout untuk bar chart
    fig_bar.update_layout(
        title_text="Kekuatan Gempa Bumi Berdasarkan Magnitudo",
        xaxis_title="Klasifikasi Gempa",
        yaxis_title="Persentase",  # Ubah label yaxis menjadi 'Persentase'
        yaxis=dict(range=[0, 50]),  # Rentang sumbu y disesuaikan hingga 50
        margin=dict(t=50, l=0, r=0, b=0)
    )

    # Data untuk chart di col3 (misal: intensitas gempa di berbagai wilayah)
    labels_col3 = ['Dangkal', 'Sedang', 'Dalam']
    intensities = [85.41, 13.17, 0.88]  # Contoh data intensitas

    # Membuat bar chart untuk col3
    fig_col3 = go.Figure(data=[go.Bar(
        x=labels_col3,
        y=intensities,
        text=[f'{val}%' for val in intensities],  # Tampilkan teks persentase di atas bar
        textposition='auto',
        marker_color='#FF5733',  # Warna batang
        marker_line_color='rgba(0, 0, 0, 1)',  # Warna garis batas
        marker_line_width=1.5
    )])

    # Menambahkan judul dan layout untuk chart di col3
    fig_col3.update_layout(
        title_text="Intensitas Gempa Berdasarkan Kedalaman",
        xaxis_title="kategori kedalaman",
        yaxis_title="Count",
        yaxis=dict(range=[0, 50]),  # Rentang sumbu y disesuaikan
        margin=dict(t=50, l=0, r=0, b=0)
    )

    # Membuat kontainer untuk pie chart, bar chart, dan tambahan chart di col3
    with st.container():
        st.header("Distribusi Java Quake")

        # Menggunakan 2 kolom untuk menyandingkan pie chart dan bar chart
        col1, col2 = st.columns(2)

        # Kontainer untuk pie chart
        with col1:
            st.write("Pie chart berikut menunjukkan proporsi kejadian gempa bumi dalam rentang waktu yang berbeda selama 10 tahun terakhir.")
            # Tampilkan pie chart interaktif di Streamlit
            st.plotly_chart(fig_pie, use_container_width=True)

        # Kontainer untuk bar chart
        with col2:
            st.write("Bar chart berikut menunjukkan kekuatan gempa bumi berdasarkan magnitudo masing-masing kejadian.")
            # Tampilkan bar chart di Streamlit
            st.plotly_chart(fig_bar, use_container_width=True)

        # Kontainer untuk chart baru di bawah kolom 1 dan 2
        st.write("Bar chart ini menggambarkan pengelompokan kategori kedalaman gempa bumi, yaitu dangkal, sedang, dan dalam, berdasarkan rentang kedalaman tertentu")
        # Tampilkan chart baru di Streamlit
        st.plotly_chart(fig_col3, use_container_width=True)




    # Footer
    st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
        <div style="display: flex; align-items: flex-start; font-size: 15px;">
            <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
            <div style="font-size: 15px; color: #4C4D50;">
                Universitas Siliwangi<br>
                Informatika<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <div style="display: flex; flex-direction: column;">
        <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
            <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
                <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
                2024 <span style="margin-left: 2px"><b>Maètala Scientist</b></span>. All Rights Reserved
            </div>
            <div style="font-size: 14px; margin: 0; color: #4C4D50;">
                TSA Batch 2 | 2024
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Analytics Page 
if selected == 'Clustering Visualization':
    from PIL import Image

    import streamlit as st
    import leafmap.foliumap as leafmap
    import pandas as pd
    import geopandas as gpd

    # Judul halaman
    st.title("Clustering Visualization - Simulasi Gempa Bumi")
    st.markdown('---')

    # Buat peta dengan pusat dan level zoom yang ditentukan
    m = leafmap.Map(center=[-2.5489, 118.0149], zoom=5)

    # Load data kota dan wilayah dari URL
    cities_url = 'https://raw.githubusercontent.com/lutfijulpian/MaetalaSciencetist/refs/heads/main/df1.csv'
    regions_url = 'https://raw.githubusercontent.com/arvelqi/indonesia_json_maps/refs/heads/master/indonesia.json'

    # Load file CSV untuk kota ke dalam DataFrame pandas
    cities = pd.read_csv(cities_url)

    # Load file GeoJSON untuk wilayah ke dalam GeoDataFrame
    regions = gpd.read_file(regions_url)

    # Tambahkan wilayah GeoJSON ke peta
    m.add_gdf(regions, layer_name='Indonesian Regions')

    # Group by latitude and longitude to count how many times an earthquake occurred at each point
    earthquake_counts = cities.groupby(['latitude', 'longitude']).size().reset_index(name='count')

    # Merge the counts back to the original dataframe to have the 'count' column
    cities_with_counts = pd.merge(cities, earthquake_counts, on=['latitude', 'longitude'])

    # Kategorikan nilai magnitudo
    def categorize_magnitude(magnitude):
        if magnitude < 4.0:
            return 'Low'
        elif 4.0 <= magnitude < 7.0:
            return 'Medium'
        else:
            return 'High'  

    # Terapkan fungsi kategorisasi
    cities_with_counts['magnitude_category'] = cities_with_counts['magnitude'].apply(categorize_magnitude)

    # Tambahkan titik ke peta menggunakan dataset kota yang telah difilter
    m.add_points_from_xy(
        cities_with_counts,
        x="longitude",
        y="latitude",
        color_column='magnitude_category',  # Kolom warna yang baru ditambahkan
        icon_names=['fa-window-close-o ', 'fa-exclamation-triangle', 'fa-exclamation-triangle'],  # Ikon untuk kategori
        spin=True,
        add_legend=True,
        info_columns=['latitude', 'longitude', 'count'],  # Menampilkan jumlah kejadian gempa ('count') di info
    )

    # Tampilkan peta di Streamlit
    m.to_streamlit()

    # Import libraries
    import streamlit as st
    import pandas as pd
    import folium
    from folium.plugins import MarkerCluster
    from scipy.spatial import ConvexHull
    from geopy.distance import geodesic
    from streamlit_folium import folium_static

    # Baca data dari URL GitHub
    url = "https://raw.githubusercontent.com/lutfijulpian/MaetalaSciencetist/refs/heads/main/tempDF2.csv"
    tempDf2 = pd.read_csv(url)

    # Filter interaktif
    st.sidebar.title("Filter Data")
    year_range = st.sidebar.slider("Pilih Rentang Tahun", 
                                  int(tempDf2['year'].min()), 
                                  int(tempDf2['year'].max()), 
                                  (int(tempDf2['year'].min()), int(tempDf2['year'].max())))

    magnitude_range = st.sidebar.slider("Pilih Rentang Magnitudo", 
                                        float(tempDf2['magnitude'].min()), 
                                        float(tempDf2['magnitude'].max()), 
                                        (float(tempDf2['magnitude'].min()), float(tempDf2['magnitude'].max())))

    depth_range = st.sidebar.slider("Pilih Rentang Kedalaman", 
                                    float(tempDf2['depth'].min()), 
                                    float(tempDf2['depth'].max()), 
                                    (float(tempDf2['depth'].min()), float(tempDf2['depth'].max())))

    clusters = st.sidebar.multiselect("Pilih Cluster", 
                                      options=tempDf2['cluster'].unique(), 
                                      default=tempDf2['cluster'].unique())

    # Filter data berdasarkan input pengguna
    filtered_data = tempDf2[
        (tempDf2['year'] >= year_range[0]) & 
        (tempDf2['year'] <= year_range[1]) &
        (tempDf2['magnitude'] >= magnitude_range[0]) & 
        (tempDf2['magnitude'] <= magnitude_range[1]) &
        (tempDf2['depth'] >= depth_range[0]) & 
        (tempDf2['depth'] <= depth_range[1]) &
        (tempDf2['cluster'].isin(clusters))
    ]

    # Hitung centroid
    centroids = filtered_data.groupby('cluster')[['latitude', 'longitude']].mean()

    cluster_stats = filtered_data.groupby('cluster').agg({
        'depth': ['min', 'max', 'count'],
        'magnitude': ['min', 'max'],
        'year': ['min', 'max']
    }).reset_index()

    # Inisialisasi peta folium
    m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=5)

    # Buat Marker Cluster untuk titik gempa
    marker_cluster = MarkerCluster().add_to(m)

    # Tambahkan setiap titik gempa ke peta
    for idx, row in filtered_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Cluster: {row['cluster']}, Magnitude: {row['magnitude']}, Depth: {row['depth']}, Tahun: {row['year']}",
            icon=folium.Icon(color='blue' if row['cluster'] != -1 else 'red')
        ).add_to(marker_cluster)

    # Hitung luas cluster
    def calculate_polygon_area(coords):
        if coords[0] != coords[-1]:
            coords.append(coords[0])

        total_area = 0.0
        for i in range(len(coords) - 1):
            latlon1 = coords[i]
            latlon2 = coords[i + 1]
            edge_length = geodesic(latlon1, latlon2).kilometers
            total_area += edge_length

        return total_area

    # Tambahkan centroid cluster beserta statistik tambahan ke popup
    for idx, row in centroids.iterrows():
        stats = cluster_stats[cluster_stats['cluster'] == idx]
        depth_min = stats['depth']['min'].values[0] if not stats.empty else 0
        depth_max = stats['depth']['max'].values[0] if not stats.empty else 0
        magnitude_min = stats['magnitude']['min'].values[0] if not stats.empty else 0
        magnitude_max = stats['magnitude']['max'].values[0] if not stats.empty else 0
        event_count = int(stats['depth']['count'].values[0]) if not stats.empty else 0
        year_min = int(stats['year']['min'].values[0]) if not stats.empty else 0
        year_max = int(stats['year']['max'].values[0]) if not stats.empty else 0

        cluster_points = filtered_data[filtered_data['cluster'] == idx][['latitude', 'longitude']].values
        if len(cluster_points) > 2:
            hull = ConvexHull(cluster_points)
            hull_points = cluster_points[hull.vertices]
            hull_polygon = [[point[0], point[1]] for point in hull_points]
            cluster_area = calculate_polygon_area(hull_polygon)
        else:
            cluster_area = 0

        popup_text = (f"Centroid of Cluster {idx}<br>"
                      f"Jumlah Gempa: {event_count}<br>"
                      f"Rentang Kedalaman: {depth_min:.2f} km - {depth_max:.2f} km<br>"
                      f"Rentang Magnitudo: {magnitude_min:.2f} - {magnitude_max:.2f}<br>"
                      f"Rentang Tahun: {year_min} - {year_max}<br>"
                      f"Luas Cluster: ± {cluster_area:.2f} km²")

        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup_text,
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(m)

    # Tambahkan convex hull boundaries untuk setiap cluster
    cluster_counts = filtered_data['cluster'].value_counts()

    def get_color(event_count):
        if event_count < 10:
            return '#FFFF66'
        elif 10 <= event_count <= 15:
            return '#FFA500'
        else:
            return '#FF0000'

    for cluster_id in filtered_data['cluster'].unique():
        if cluster_id != -1:
            cluster_points = filtered_data[filtered_data['cluster'] == cluster_id][['latitude', 'longitude']].values
            if len(cluster_points) > 2:
                hull = ConvexHull(cluster_points)
                hull_points = cluster_points[hull.vertices]
                hull_polygon = [[point[0], point[1]] for point in hull_points]

                event_count = cluster_counts[cluster_id]
                color_hex = get_color(event_count)

                folium.Polygon(
                    locations=hull_polygon,
                    color=color_hex,
                    fill=True,
                    fill_opacity=0.4
                ).add_to(m)

    # Tampilkan peta dalam Streamlit
    st.title("Peta Cluster Gempa Bumi")
    st.write("Peta ini menunjukkan lokasi gempa bumi berdasarkan cluster yang telah dianalisis.")

    # Tambahkan CSS untuk membuat peta responsif
    st.markdown(
        """
        <style>
        .leaflet-container {
            width: 100% !important;
            height: 600px;  /* Atur tinggi sesuai kebutuhan */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Render the map
    folium_static(m)

    # Footer
    st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
        <div style="display: flex; align-items: flex-start; font-size: 15px;">
            <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
            <div style="font-size: 15px; color: #4C4D50;">
                Universitas Siliwangi<br>
                Informatika<br>
                Badan Pusat Statistik
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <div style="display: flex; flex-direction: column;">
        <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
            <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
                <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
                2024 <span style="margin-left: 2px"><b>Fun-tastic Four</b></span>. All Rights Reserved
            </div>
            <div style="font-size: 14px; margin: 0; color: #4C4D50;">
                SIB Cycle 6 | 2024
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
# About Us Page
if selected == 'Simulasi':
    from PIL import Image
    
    # Judul halaman
    st.title('Simulasi Sistem Early Warning Gempa - Siliwangi QuakeGuard')
    st.markdown('---')

    # Judul video
    st.header('Simulasi Sistem Peringatan Dini Gempa Bumi')

    # Penjelasan video
    st.write('Video berikut merupakan simulasi dari **Siliwangi QuakeGuard**, sebuah sistem peringatan dini gempa bumi yang menggabungkan teknologi terkini dan filosofi kebijaksanaan Siliwangi. \
    Sistem ini dirancang untuk mendeteksi aktivitas seismik secara real-time dan memberikan peringatan dini kepada masyarakat agar dapat melakukan evakuasi tepat waktu. \
    Dalam video ini, Anda akan melihat bagaimana sistem ini bekerja dalam memberikan notifikasi dan informasi terkait dengan potensi gempa.')

    # URL video dari YouTube
    VIDEO_URL = "https://youtu.be/YE28v3kcUVs"

    # Tampilkan video di Streamlit
    st.video(VIDEO_URL)

    # Footer
    st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
        <div style="display: flex; align-items: flex-start; font-size: 15px;">
            <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
            <div style="font-size: 15px; color: #4C4D50;">
                Universitas Siliwangi<br>
                Informatika<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <div style="display: flex; flex-direction: column;">
        <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
            <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
                <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
                2024 <span style="margin-left: 2px"><b>Maètala Scientist</b></span>. All Rights Reserved
            </div>
            <div style="font-size: 14px; margin: 0; color: #4C4D50;">
                TSA Batch 2 | 2024
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# About Us Page
if selected == 'About Us':
    from PIL import Image
    
    st.title('About Us')
    st.markdown('---')
    from PIL import Image

    # Jalur gambar dari Google Drive
    ICON_RED = "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/Kiriman_Instagram_Diskon_Hari_Batik_Nasional_Kolase_Krem_Hitam-removebg-preview (1).png"

    # Menampilkan gambar dari Google Drive
    image = Image.open(ICON_RED)

    # Mengonversi gambar menjadi base64 untuk dimasukkan dalam HTML
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div style="margin-bottom: 20px;">
                <img src="data:image/png;base64,{img_str}" alt="Maètala Scientist Logo" width="300"/>
            </div>
            <div style="max-width: 600px;">
                <p style="font-size: 16px; margin-top: 10px; text-align: justify;">
                    Logo "Maètala Scientist" menggabungkan filosofi tanah dan ilmu pengetahuan. "Maètala," 
                    dari bahasa Sanskerta, berarti "tanah" atau "bumi," melambangkan kehidupan dan kelestarian 
                    alam. Lekukan hitam mewakili dinamika kehidupan dan lapisan geologis bumi, simbol aliran energi 
                    alami. Warna kuning melambangkan vitalitas, cahaya matahari, dan harapan, menunjukkan optimisme 
                    serta semangat menjaga bumi. Nama "Scientist" menegaskan fokus ilmiah untuk memahami dan melindungi 
                    bumi serta lingkungan. Secara keseluruhan, logo ini menggambarkan komitmen ilmiah dalam menjaga keseimbangan 
                    alam dan keberlanjutan lingkungan bagi generasi mendatang.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    team_members = [
    {
        "name": "Mohammad Faikar Natsir",
        "image_id": "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/beras.jpg",
        "role": "Modeller",
        "email": "kkkk",
        "description": ""
    },
    {
        "name": "Fedro Rizkyana Padila",
        "image_id": "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/Fedro.JPG",
        "role": "Data Analisis",
        "email": "kkkk",
        "description": "Bertanggungjawab"
    },
    {
        "name": "Lutfi Julpian",
        "image_id": "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/Lutfi.jpg",
        "role": "Visualization",
        "email": "lutfijulpian@gmail.com",
        "description": "Lutfi bertanggung jawab untuk menciptakan visualisasi data yang intuitif dan informatif. Ia membantu mengubah data mentah menjadi cerita yang menarik."
    },
    {
        "name": "Arif Muhammad Rifai",
        "image_id": "/content/drive/MyDrive/BPS (Harga Beras)/FINAL/foto/Arif.jpg",
        "role": "Modeller",
        "email": "kkkk",
        "description": "Bertanggung Jawab"
    },
    ]

    image_width = 200
    image_height = 200

    for member in team_members:
        cols = st.columns([1, 4])
        if 'image_id' in member:
            image = Image.open(member["image_id"])
            image = image.resize((image_width, image_height))
            cols[0].image(image, use_column_width=False)
            st.write('<style>div.Widget.row-widget.stRadio>div{flex-direction:column;}</style>', unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown(f"""
            <div style='margin-top: 25px; background-color: #f5f5f1; padding: 10px; border-radius: 5px; color: #000000;'>
                <strong>{member['name']}</strong>
                <br>
                <em>{member['role']}</em>
                <br>
                <em>{member['email']}</em>
                <br><br>
                {member['description']}
            </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 10px;">
        <div style="display: flex; align-items: flex-start; font-size: 15px;">
            <i class="material-icons" style="font-size: 25px; margin-right: 5px; color: #4C4D50 ;">location_on</i>
            <div style="font-size: 15px; color: #4C4D50;">
                Universitas Siliwangi<br>
                Informatika<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <div style="display: flex; flex-direction: column;">
        <hr style="border-top: 1px solid #ddd; margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
            <div style="display: flex; align-items: center; font-size: 15px; color: #4C4D50;">
                <i class="far fa-copyright" style="font-size: 20px; margin-right: 5px;"></i>
                2024 <span style="margin-left: 2px"><b>Maètala Scientist</b></span>. All Rights Reserved
            </div>
            <div style="font-size: 14px; margin: 0; color: #4C4D50;">
                TSA Batch 2 | 2024
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

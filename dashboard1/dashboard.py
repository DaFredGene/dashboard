import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Proyek Analis Data-Air Quality Dataset')
st.header('Pertanyaan 1')
st.subheader('Diantara Aotizhongxin, Changping, dan Dingling, daerah manakah yang memiliki kadar O3 tinggi sedangkan SO2, NO2, dan CO rendah sehingga cocok untuk dibentuknya sebuah perkebunan kangkung yang memanfaatkan teknologi ozon sebagai disinfektan dan sterilisasi bakteri?')
st.header('Pertanyaan 2')
st.subheader('Jika proses panen kangkung memakan waktu 1 bulan lamanya dengan kondisi temperatur optimal 25°C hingga 30°C dan curah hujan yang tinggi, pada bulan apakah sebaiknya siklus panen dilakukan?')
st.text('Silahkan Pilih Tab dibawah ini untuk melihat jawaban')
jawaban1, jawaban2 = st.tabs(["Jawaban Pertanyaan1", "Jawaban Pertanyaan 2"])
with jawaban1:
    st.header('Jawab Pertanyaan 1')
    st.write('Apa Relasi antara O3 dengan SO2, NO2, dan CO?')
    df_visual2 = pd.read_csv('https://github.com/DaFredGene/dashboard/blob/400d06836c09ec2e94a85ed40b15ef40f9e94540/dashboard1/df_visual.csv')
    df_visual1 = df_visual2.iloc[6:]
    df_visual = df_visual2.iloc[1:4]
    st.image("https://i.ibb.co/yBFMsGw/FBFE19-FC-9-DA5-401-C-B19-D-5-C4317-CF414-B.jpg")
    
    with st.expander("Klik, untuk penjelasan tabel korelasi"):
        st.write(''' Dari korelasi antara O3 dengan SO2, NO2, dan CO tersebut, kita bisa melihat bahwa korelasinya negatif,
                 artinya, semakin tinggi kadar O3 maka semakin rendah kadar dari SO2, NO2, dan CO tersebut,
                 dari relasi ini lah, kita dapat membuat keputusan berdasarkan presentase kadar dari setiap unsur.
                 ''')
        colors = ['#D33000', '#E03000', '#E69C9C']
    col = ['SO2', 'NO2', 'CO']
    explode = (0, 0, 0.1)
    labels = ['Aotizhongxin', 'Changping', 'Dingling']

    fig, axes = plt.subplots(nrows=1, ncols=len(df_visual[col]), figsize=(15, 5)) #akan ada error disini tapi tetap akan berjalan
    for i, kandungan in enumerate(df_visual[col]):
        axes[i].pie(df_visual[kandungan],
                    labels=labels,
                    colors=colors,
                    autopct='%1.1f%%',
                    explode=explode)
        axes[i].set_title(kandungan)

    plt.suptitle("Presentase Kadar Unsur Berbahaya", fontsize=20, y=1.1)
    plt.tight_layout()

    st.pyplot(fig)
    st.write(df_visual2.iloc[0:4])

    with st.expander("Klik, untuk penjelasan pie chart"):
        st.write(''' Dari pie chart tersebut, terlihat jika presentase kandungan SO2, NO2, dan CO dar 
                 daerah Dingling lebih kecil dibandingkan kedua daerah lainnya, berdasarkan nilai
                 korelasi sebelumnya, dapat dibuat sebuah hipotesis bahwa O3 dari daerah Dingling
                 akan bernilai lebih besar dari kedua daerah lainnya, hipotesis akan dibuktikan dibawah.
                 ''')
    colors = ['#4E632E', '#556B2F', '#8FBC8F']
    colO3 = 'O3'
    explode = (0, 0, 0.05)
    data_values = df_visual[colO3].values.flatten()
    st.title("Presentase Kadar Unsur O3")
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(data_values,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            explode=explode)
    ax.set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
    with st.expander("Klik, untuk penjelasan pie chart"):
        st.write(''' Dari pie chart tersebut, terlihat jika presentase kandungan O3 lebih besar dibandingkan
                 dengan SO2, NO2, dan CO. Hal ini sudah sesuai dengan hipotesis sebelumnya, jadi kesimpulan untuk
                 pertanyaan 1 sudah dapat diambil.
                 ''')
    st.header('Kesimpulan: ')
    st.subheader('Daerah Dingling merupakan daerah yang memiliki kandungan O3 tertinggi dan juga kandungan SO2, NO2, dan CO terendah.')
    st.subheader('Oleh sebab itu daerah DINGLING, merupakan daerah yang paling cocok untuk dibentuknya sebuah perkebunan kangkung yang memanfaatkan teknologi ozon sebagai disinfektan dan sterilisasi bakteri.')

with jawaban2:
    st.header('Jawab Pertanyaan 2')
    st.subheader('Temperatur dan curah hujan merupakan hal penting dalam perkebunan, mari kita analisis kapan waktu terbaik untuk melakukan proses penanaman hingga panen')
    rainfreq = df_visual2['SO2'][6:].to_list()
    for i in range(len(rainfreq)):
        rainfreq[i] = int(rainfreq[i])
    months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    df_visual3 = pd.DataFrame({
    'rainfreq': rainfreq,
    'months': months})
    fig, ax = plt.subplots()
    ax.bar(df_visual3['months'], df_visual3['rainfreq'], color='blue')
    ax.set_ylabel('Frekuensi Hujan (jam)')
    ax.set_title('Kategori Hujan berdasarkan Bulan')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    with st.expander("Klik, untuk penjelasan bar chart"):
        st.write(''' Dari bar chart tersebut, terlihat jika curah hujan pada bulan Juli merupakan yang tertinggi di daerah Dingling.
                 ''')
    dingin = df_visual2['NO2'][6:].to_list()
    for i in range(len(dingin)):
        dingin[i] = int(dingin[i])
    optimal = df_visual2['CO'][6:].to_list()
    for i in range(len(optimal)):
        optimal[i] = int(optimal[i])
    panas = df_visual2['O3'][6:].to_list()
    for i in range(len(panas)):
        panas[i] = int(panas[i])
    fig, ax = plt.subplots()
    ax.bar(months, dingin, color='blue', label='Dingin')
    ax.bar(months, optimal, bottom = dingin, color = 'green', label = 'Optimal')
    ax.bar(months, panas, bottom=np.add(dingin, optimal), color='red', label='Panas')
    ax.set_ylabel('Total jam kondisi temperatur')
    ax.set_title('Temperature Categories by Month')
    plt.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)
    with st.expander("Klik, untuk penjelasan bar chart"):
        st.write(''' Dari bar chart tersebut, kita bisa melihat bahwa suhu optimal pada bulan Juli lebih lama 
                 dibandingkan dengan bulan lain, hal ini linear dengan curah hujan pada bulan Juli yang dijelaskan sebelumnya
                 ''')
    st.header('Kesimpulan: ')
    st.subheader('Bulan Juli merupakan bulan terbaik untuk penanaman kangkung')
    st.subheader('Hal ini karena, curah hujan bulan Juli merupakan yang tertinggi dan jumlah temperatur Optimal(25°C- 30°C)')


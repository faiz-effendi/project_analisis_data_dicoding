import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_season_to_total_df(df):
  season_to_total_df = df.groupby(by='season').agg({
    'instant': 'nunique',
    'casual': 'sum',
    'registered': 'sum',
    'total_book': 'sum',
  }).sort_values(by='total_book', ascending=False).reset_index()

  return season_to_total_df

def create_temp_to_total_df(df):
  temp_to_total_df = df[['temp', 'total_book']]

  return temp_to_total_df

df = pd.read_csv('day_cleaned.csv')
season_to_total_df = create_season_to_total_df(df)
temp_to_total_df = create_temp_to_total_df(df)

st.header('Dashboard Analisis Peminjaman Sepeda')

with st.container():
  st.subheader('Bagaimana tren penyewaan sepeda keseluruhan bervariasi antara musim?')

  colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

  fig, ax = plt.subplots(figsize=(20, 10))

  sns.barplot(y='casual', x='season', data=season_to_total_df.sort_values(by='casual', ascending=False), palette=colors, ax=ax)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.set_title("Peminjaman oleh pengguna casual", loc="center", fontsize=32)
  ax.tick_params(axis ='x', labelsize=24)
  st.pyplot(fig)

  sns.barplot(y='registered', x='season', data=season_to_total_df.sort_values(by='registered', ascending=False), palette=colors, ax=ax)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.set_title("Peminjaman oleh pengguna terdaftar", loc="center", fontsize=32)
  ax.tick_params(axis ='x', labelsize=24)
  st.pyplot(fig)

  sns.barplot(y='total_book', x='season', data=season_to_total_df.sort_values(by='total_book', ascending=False), palette=colors, ax=ax)
  ax.set_ylabel(None)
  ax.set_xlabel(None)
  ax.set_title("Peminjaman Total", loc="center", fontsize=32)
  ax.tick_params(axis ='x', labelsize=24)
  st.pyplot(fig)

temp_to_total_df['temp'] = temp_to_total_df.temp.apply(lambda temp: 'cold' if temp < 0.439 else ('hot' if temp > 0.682 else 'ideal') )
temp_to_total_df = temp_to_total_df.groupby(by='temp').total_book.sum().sort_values(ascending=False).reset_index()

with st.container():
  st.header('Pengaruh apa yang diberikan oleh suhu dan kelembapan lingkungan pada jumlah peminjaman sepeda?')
  colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
  fig, ax = plt.subplots(figsize=(20, 10))

  sns.barplot(
      x='temp',
      y='total_book',
      data=temp_to_total_df.sort_values(by='total_book', ascending=False),
      palette = colors
  )

  ax.set_title('Number of Total Order Based on Temp Type', loc='center', fontsize=32)
  ax.set_xlabel(None)
  ax.set_ylabel(None)
  ax.tick_params(axis='x', labelsize=24)
  st.pyplot(fig)
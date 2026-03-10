import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Vehicle Listings Dashboard",
    page_icon="🚗",
    layout="wide"
)

car_data = pd.read_csv('vehicles_us.csv')

if 'is_4wd' in car_data.columns:
    car_data['is_4wd'] = car_data['is_4wd'].fillna(0)

st.header('Vehicle Listings Dashboard')

st.write(
    'Este aplicativo web permite explorar dados de anúncios de venda de carros '
    'nos Estados Unidos usando visualizações interativas.'
)

st.subheader('Prévia dos dados')
st.dataframe(car_data.head())

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a coluna odometer')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando gráfico de dispersão entre odometer e price')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
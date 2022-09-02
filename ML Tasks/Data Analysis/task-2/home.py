import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
pic1 = Image.open('audience.jpg')

pic = Image.open('20424689.jpg')


st.set_page_config(page_title="Home", page_icon="")
st.title("Streamlit Application")
st.image(pic)
df=pd.read_csv('data.csv')
st.sidebar.image(image=pic1)
st.title("Let me find a PUB")
option=st.selectbox('select an option',['First five rows','Satistics of Data'])
if option == 'First five rows':
    st.subheader('Dataset')
    st.dataframe(df.head())
if option == 'Satistics of Data':
    st.subheader('stats')
    st.dataframe(df.describe())



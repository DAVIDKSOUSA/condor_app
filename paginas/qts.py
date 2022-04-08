#importar bibliotecas
import streamlit as st
from PIL import Image

#chamada da pagina
def qts():
    #st.write('___')
    #st.image(load_image_from_local("asset/images/chef-transformer-transparent.png"), width=300)
    st.markdown(
        "<h3 style='text-align: center; color:#003366; font-size:40px;'><b>QTS de 11 a 15 de abril de 2022<b></h3>",
        unsafe_allow_html=True)
    image = Image.open('qts/8-14.jpg')
    st.image(image)
    #st.image('/Users/davidsousa/condor_app/qts/8-14.jpg', use_column_width='always')
    st.write('___')
    st.markdown(
        "<h3 style='text-align: center; color:#003366; font-size:40px;'><b>QTS de 11 a 15 de abril de 2022<b></h3>",
        unsafe_allow_html=True)
    image = Image.open('qts/8-14.jpg')
    st.image(image)
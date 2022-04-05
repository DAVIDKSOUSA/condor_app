#importar bibliotecas
import streamlit as st
from PIL import Image


#chamada da pagina
def qts():
    #st.write('___')
    #st.image(load_image_from_local("asset/images/chef-transformer-transparent.png"), width=300)
    st.title('QTS da Semana')
    image = Image.open('qts/qts.png')
    st.image(image)
    ###############
    st.write('___')
    st.title('QTS da Semana')
    image = Image.open('qts/qts.png')
    st.image(image)
    ##############
    st.write('___')
    st.title('QTS da Semana')
    image = Image.open('qts/qts.png')
    st.image(image)


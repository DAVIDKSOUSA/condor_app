#importar bibliotecas
import streamlit as st
from PIL import Image

#chamada da pagina
def qts():
    #st.write('___')
    #st.image(load_image_from_local("asset/images/chef-transformer-transparent.png"), width=300)
    st.markdown(
        "<h3 style='text-align: center; color:grey; font-size:40px;'><b>QTS de 02 a 06 de maio de 2022<b></h3>",
        unsafe_allow_html=True)
    image = Image.open('qts/2-6.jpg')
    st.image(image)
    #st.image('/Users/davidsousa/condor_app/qts/8-14.jpg', use_column_width='always')

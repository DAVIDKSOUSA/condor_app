#importar bibliotecas
import streamlit as st
from PIL import Image


#chamada da pagina
def qts():
    st.write('___')
    image = Image.open('qts.png')

    st.image('/Users/davidsousa/condor_app/qts/qts.png', output_format='PNG')
    #st.image(width= , )
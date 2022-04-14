#importar bibliotecas
import streamlit as st
from streamlit_option_menu import option_menu

#definir pagina
def documentos():
    pagina = option_menu(
        menu_title="Dowloads",
        options=['Aulas', 'Manuais', 'MAPIL/STUDY GUIDE', 'OI C-99'],
        menu_icon='person',
        default_index=0,
        orientation='vertical'
    )

    if pagina == 'Aulas':

        st.header('Aulas Ground')

        with open("aulas/1 AIRPLANE DESCRIPTION.ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="1 AIRPLANE DESCRIPTION",
                           data=PDFbyte,
                           file_name="1 AIRPLANE DESCRIPTION.ppt",
                           mime='application/octet-stream')

        with open("aulas/2 APU.ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="2 APU",
                           data=PDFbyte,
                           file_name="2 APU.ppt",
                           mime='application/octet-stream')

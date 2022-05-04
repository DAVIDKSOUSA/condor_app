#importar bibliotecas
import streamlit as st
from streamlit_option_menu import option_menu

#definir pagina

#https://towardsdatascience.com/display-and-download-pdf-in-streamlit-a-blog-use-case-5fc1ac87d4b1
def documentos():
    pagina = option_menu(
        menu_title="Downloads",
        options=['Aulas','OI C-99', 'Manuais EMB-145'],
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
        with open("aulas/3 FIRE PROTECTION (BMR_RCD).ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="3 FIRE PROTECTION",
                           data=PDFbyte,
                           file_name="3 FIRE PROTECTION (BMR_RCD).ppt",
                           mime='application/octet-stream')

        with open("aulas/4 POWERPLANT (VAG_BMR).pptx", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="4 POWERPLANT",
                           data=PDFbyte,
                           file_name="4 POWERPLANT (VAG_BMR).pptx",
                           mime='application/octet-stream')

        with open("aulas/5 HYDRAULIC SYSTEM (VAG_BMR).ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="5 HYDRAULIC SYSTEM",
                           data=PDFbyte,
                           file_name="5 HYDRAULIC SYSTEM (VAG_BMR).ppt",
                           mime='application/octet-stream')

        with open("aulas/6 LANDING GEAR AND BREAKES (RCD_VAG).ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="6 LANDING GEAR AND BREAKES",
                           data=PDFbyte,
                           file_name="6 LANDING GEAR AND BREAKES (RCD_VAG).ppt",
                           mime='application/octet-stream')

        with open("aulas/7 FLIGHT CONTROLS (RCD_VAG).ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="7 FLIGHT CONTROLS (RCD_VAG)",
                           data=PDFbyte,
                           file_name="7 FLIGHT CONTROLS (RCD_VAG).ppt",
                           mime='application/octet-stream')
        with open("aulas/8 FMS  (RCD_VAG).ppt", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="8 FMS",
                           data=PDFbyte,
                           file_name="8 FMS  (RCD_VAG).ppt",
                           mime='application/octet-stream')

    if pagina == 'OI C-99':
        st.header('OI C-99')

        with open("aulas/OI C99 compilada.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="OI C99 compilada",
                           data=PDFbyte,
                           file_name="OI C99 compilada.pdf",
                           mime='application/octet-stream')


    if pagina == 'Manuais EMB-145':

        st.header('Manuais EMB-145')

        with open("manuais/Manual FMS.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Manual FMS",
                           data=PDFbyte,
                           file_name="Manual FMS.pdf",
                           mime='application/octet-stream')
        with open("manuais/AFM145-1152-02-REV84-FULL-VOL1.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="AFM145-1152-02-REV84-FULL-VOL1",
                           data=PDFbyte,
                           file_name="AFM145-1152-02-REV84-FULL-VOL1.PDF",
                           mime='application/octet-stream')

        with open("manuais/AFM145-1152-02-REV84-FULL-VOL2.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="AFM145-1152-02-REV84-FULL-VOL2",
                           data=PDFbyte,
                           file_name="AFM145-1152-02-REV84-FULL-VOL2.PDF",
                           mime='application/octet-stream')
        with open("manuais/AOM-1114-71-REV43-FULL.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="AOM-1114-71-REV43-FULL",
                           data=PDFbyte,
                           file_name="AOM-1114-71-REV43-FULL.PDF",
                           mime='application/octet-stream')
        with open("manuais/DDPM-1179-01-REV13-FULL.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="DDPM-1179-01-REV13-FULL",
                           data=PDFbyte,
                           file_name="DDPM-1179-01-REV13-FULL.PDF",
                           mime='application/octet-stream')
        with open("manuais/MMEL145-1113-REV14-FULL.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="MMEL145-1113-REV14-FULL",
                           data=PDFbyte,
                           file_name="MMEL145-1113-REV14-FULL.PDF",
                           mime='application/octet-stream')

        with open("manuais/QRH145-1167-02-ANAC-REV16-FULL.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="QRH145-1167-02-ANAC-REV16-FULL",
                           data=PDFbyte,
                           file_name="QRH145-1167-02-ANAC-REV16-FULL.PDF",
                           mime='application/octet-stream')

        with open("manuais/SOP145-1489-REV09-FULL.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="SOP145-1489-REV09-FULL",
                           data=PDFbyte,
                           file_name="SOP145-1489-REV09-FULL.PDF",
                           mime='application/octet-stream')
        with open("manuais/WB145-1160-CTA.PDF", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="WB145-1160-CTA",
                           data=PDFbyte,
                           file_name="WB145-1160-CTA.PDF",
                           mime='application/octet-stream')


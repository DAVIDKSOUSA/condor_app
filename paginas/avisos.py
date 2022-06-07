#importar bibliotecas
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

##animacao
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_hu7gcd3w.json')

#chamada da pagina
def avisos():
    #st.set_page_config(
    #    page_title="Chef Transformer",
    #    page_icon="🍲",
    #    layout="wide",
    #    initial_sidebar_state="expanded"
    #)

    image = Image.open('images/condor guerreiro colorido.png')
    st.sidebar.image(image)


    st.write('---')
    coluns = st.columns(2)
    image = Image.open('images/bolacha.png')
    coluns[0].image(image, width=300)
    coluns[1].markdown("<h1 style='text-align:center ; color:grey; font-size:20px;'><b>1º/2º GT - Primeiro Esquadrão do Segundo Grupo de Transporte<b></h1>",
                unsafe_allow_html=True)
    coluns[1].markdown("<h1 style='text-align:center ; color:grey; font-size:18px;'><b>Missão<b></h1>",
                unsafe_allow_html=True)
    coluns[1].write('Manter o efetivo preparado para empregar seus meios aéreos com SEGURANÇA, EFICIENCIA e EFICÁCIA.')
    st.write('---')

    def p_title(title):
        st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>',
                    unsafe_allow_html=True)

    p_title('AVISOS:')
    # st.text('')
    # st.write(' - Reunião/Prestação de Contas de Fiscais de Contrato e CONREC - 12/05/22 às 13h30.'
    #          )
    #
    # image = Image.open('qts/IMG_4341.jpg')
    # st.image(image)
    #
    # with open("qts/IMG_4341.jpg", "rb") as pdf_file:
    #     PDFbyte = pdf_file.read()
    #
    # st.download_button(label='Baixar Documento',
    #                    data=PDFbyte,
    #                    file_name="IMG_4341.jpg",
    #                    mime='application/octet-stream')
    #
    # st.write('---')

    #st.text('')
    #st.markdown("<h1 style='text-align: center; color:grey; font-size:23px;'><b>Faça uma análise completa da sua "
    #            "carteira de investimentos de forma<b></h1>",
    #            unsafe_allow_html=True)
    #st.markdown("<h3 style='text-align: center; color:grey; font-size:30px;'><b>SIMPLES, OBJETIVA e RÁPIDA!<b></h3>",
    #            unsafe_allow_html=True)
    #st.text('')
    #st.write(
    #    'ALTIVO E GLORIOSO\n'
    #    'VOAMOS COM LOUVOR\n'
    #    'SEGURO E EFICIENTE\n'
    #    'NAS ASAS DO CONDOR.'
    #)
    #st.write('---')
    #st.write(':point_left: Use o menu ao lado e selecione uma funcionalidade.')
    #st.write('---')
    # with st.container():
    #     left_column, right_column = st.columns(2)
    #     with left_column:
    #         def p_title(title):
    #             st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>',
    #                         unsafe_allow_html=True)
    #         p_title('AVISOS:')
    #         st.text('')
    #         st.write(' - Reunião/Prestação de Contas de Fiscais de Contrato e CONREC - 12/05/22 às 13h30.'
    #         )
    #
    #         image = Image.open('qts/IMG_4341.jpg')
    #         st.image(image)
    #
    #         with open("qts/IMG_4341.jpg", "rb") as pdf_file:
    #             PDFbyte = pdf_file.read()
    #
    #         st.download_button(label='Visualizar Documento',
    #                            data=PDFbyte,
    #                            file_name="IMG_4341.jpg",
    #                            mime='application/octet-stream')


        #     p_title('AVISOS:')
        #     #st.write(
        #     #    'INSERIR AVISO'
        #     #)
        #     st.write('##')
        #     st.write('Mídias Sociais (não oficial) :')
        #     st.markdown(
        #         """
        #         :point_right:\t[![YouTube Channel Condor](https://img.shields.io/youtube/channel/subscribers/UCyZh6LEoaABxkgpCP2F5ZBQ?style=social&logo=youtube)](https://www.youtube.com/channel/UCyZh6LEoaABxkgpCP2F5ZBQ)
        #         """
        #     )
        #     st.markdown(
        #         """
        #         :point_right:\t[![Instagram](https://img.shields.io/badge/Condor_altivo-E4405F?logo=instagram&style=social)](https://www.instagram.com/condor_altivo/)
        #         """
        #     )
        # with right_column:
        #     st_lottie(lottie_coding, quality='high', height=300, key='coding')
        #

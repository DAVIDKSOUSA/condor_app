#baixar as bibliotecas
import streamlit as st
from streamlit_option_menu import option_menu

#importar paginas
import paginas.avisos as av
import paginas.qts as qts
import paginas.relprev as rp
import paginas.faltas as ft
import paginas.indisp as id
import paginas.documentos as dc

st.set_page_config(page_title="Aplicativo Esquadrão Condor",
                   page_icon='🛩',
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items={'Get help': None,
                               "Report a Bug": None,
                               "About": None
                                }
                   )
#ocultar o menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#pagina com navegation bar
pagina = option_menu(
        "ESQUADRÃO CONDOR", ["Avisos", 'Relprev', 'QTS', 'Formulários', 'Faltas', 'Documentos'],
        icons=['pin', 'cast', 'table', 'list-task', 'person-check', 'cloud-download', ],
    menu_icon="house",
    default_index=0,
    orientation='horizontal'
    # site com icones: https://icons.getbootstrap.com
)

if pagina == 'Avisos':
    av.avisos()

if pagina == 'QTS':
    qts.qts()

if pagina == 'Faltas':
    ft.faltas()

if pagina == 'Relprev':
    rp.relprev()

if pagina == 'Formulários':
    id.indisp()

if pagina == 'Documentos':
    dc.documentos()





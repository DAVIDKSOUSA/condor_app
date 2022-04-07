#baixar as bibliotecas
import streamlit as st
from streamlit_option_menu import option_menu

#importar paginas
import paginas.inicio as ic
#import paginas.avisos as av
import paginas.qts as qts
import paginas.relprev as rp
import paginas.faltas as ft
import paginas.indisp as id

##ocultar o menu
#hide_menu_style = """
#    <style>
#    #MainMenu {visibility: hidden; }
#    footer {visibility: hidden;}
#    </style>
#    """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

#pagina com navegation bar
#st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")
# site com icones: https://icons.getbootstrap.com
pagina = option_menu(
        "CONDOR APP", ["Avisos", 'Relprev', 'QTS', 'Documentos', 'Formulários', 'Faltas', 'Diversos'],
        icons=['pin', 'cast', 'table', 'cloud-download', 'list-task', 'person-check'],
    menu_icon="house",
    default_index=0,
    #menu_title= "CONDOR",
    #options=['Início', 'Avisos', 'QTS', 'RELPREV', 'Faltas', 'Indiponibilidade Mensal'],
    #menu_icon='cast',
    #default_index=0,
    orientation='horizontal'
)

if pagina == 'Início':
    ic.inicio()

#if pagina == 'Avisos':
#    av.avisos()

if pagina == 'QTS':
    qts.qts()

if pagina == 'Faltas':
    ft.faltas()

if pagina == 'Relprev':
    rp.relprev()

if pagina == 'Formulários':
    id.indisp()





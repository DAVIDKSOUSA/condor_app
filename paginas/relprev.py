#importar bibliotecas

from __future__ import print_function
import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

from streamlit_option_menu import option_menu
#chamada da pagina

def relprev():

    # pagina = option_menu(
    #     menu_title="Formulários",
    #     options=['Mensal', 'CML'],
    #     menu_icon='cast',
    #     default_index=0,
    #     orientation='vertical'
    # )

    SCOPE = "https://www.googleapis.com/auth/spreadsheets"
    SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    SHEET_NAME = "relprev"
    GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"

    @st.experimental_singleton(suppress_st_warning=True)
    def connect_to_gsheet():
        # Create a connection object.
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=[SCOPE],
        )

        # Create a new Http() object for every request
        def build_request(http, *args, **kwargs):
            new_http = google_auth_httplib2.AuthorizedHttp(
                credentials, http=httplib2.Http()
            )
            return HttpRequest(new_http, *args, **kwargs)

        authorized_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        service = build(
            "sheets",
            "v4",
            requestBuilder=build_request,
            http=authorized_http,
        )
        gsheet_connector = service.spreadsheets()
        return gsheet_connector

    # Ten David

    def get_data(gsheet_connector) -> pd.DataFrame:
        values = (
            gsheet_connector.values()
                .get(
                spreadsheetId=SPREADSHEET_ID,
                range=f"{SHEET_NAME}!A:D",
            )
                .execute()
        )

        df = pd.DataFrame(values["values"])
        df.columns = df.iloc[0]
        df = df[1:]
        return df

    def add_row_to_gsheet(gsheet_connector, row) -> None:
        gsheet_connector.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:D",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        ).execute()

    # st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")
    st.markdown("<h1 style='text-align:center ; color:red; font-size:30px;'><b>RELPREV - Relato de Prevenção<b></h1>",
                        unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center ; color:black; font-size:15px;'><b>Sua atitude pode salvar vidas!<b></h2>",
                unsafe_allow_html=True)

    gsheet_connector = connect_to_gsheet()

    # texto sidebar
    st.sidebar.markdown("<h1 style='text-align:center ; color:red; font-size:30px;'><b>ATENÇÃO !<b></h1>",
                        unsafe_allow_html=True)
    st.sidebar.write(
        "É vedado o uso do RELPREV para o trato de assuntos caracterizados como DENÚNCIA,  tais como, violações intencionais da regulamentação em vigor, contravenções penais ou crimes relacionados à atividade aérea.")
    st.sidebar.markdown("<h3 style='text-align:center ; color:black; font-size:30px;'><b>Avisos<b></h3>",
                unsafe_allow_html=True)
    st.sidebar.write("1. O RELPREV destina-se, tão somente, ao registro das circunstâncias que constituam ou possam vir a constituir uma situação com potencial de risco à atividade aérea, com o objetivo exclusivo de prevenir ocorrências aeronáuticas.")
    st.sidebar.write("2. O RELPREV está baseado nos princípios da voluntariedade, sigilo e não punibilidade.")
    st.sidebar.write("3. De acordo com as regulamentações brasileiras, este relato (ou parte dele) somente será usado para a prevenção de acidentes aeronáuticos, a fim de aumentar a segurança operacional. Este relato não precisa ser identificado. Caso o relator se identifique, o mesmo será informado sobre as medidas adotadas.")

    st.sidebar.write("Cadastrar Ricardo/Whatsapp.")

    form = st.form(key="annotation")

    with form:
        st.subheader('DADOS GERAIS DA OCORRÊNCIA')
        comment = st.text_area("Local:")
        cols = st.columns(3)
        data = cols[0].date_input("Data:")
        time = cols[1].time_input("Horário:")
        timeutc = cols[2].time_input("Horário - UTC:")
        pessoal = st.text_area("Pessoal envolvido e/ou aeronave:")
        situacao = st.text_area("Situação:")
        st.subheader('IDENTIFICAÇÃO')
        cols = st.columns(3)
        nome = cols[0].text_area("Nome:")
        posto = cols[1].selectbox('Posto/Graduação:', ['', 'Brig', 'Cel', 'Ten Cel', 'Maj', 'Cap', 'Ten', 'SO', '1S', '2S', '3S', 'CB', 'TF', 'SD'])
        tipo = cols[2].selectbox('Tipo de Relator:', ['', 'Tripulante', 'Manutenção', 'ATS', 'Pessoal de Apoio ao Solo', 'Anônimo'])
        cols = st.columns(3)
        email = cols[0].text_area("E-mail:")
        telefone = cols[1].text_area("Telefone:")
        secao = cols[2].text_area("Seção:")
        feedback = st.radio("Deseja Receber Feedback:", ['Sim', 'Não'])

        submitted = st.form_submit_button(label="Salvar e enviar Relprev")

    if submitted:
        add_row_to_gsheet(
            gsheet_connector,
            [[str(comment), str(data), str(time), str(timeutc),
              str(pessoal), str(situacao), str(posto),
              str(nome), str(email), str(telefone), str(secao), str(tipo), str(feedback)]],
        )
        st.success("Registro realizado.")
        st.balloons()

    # expander = st.expander("Registros")
    # with expander:
    #     st.write(f"Abrir planilha no [Google Sheet]({GSHEET_URL})")
    #     st.dataframe(get_data(gsheet_connector))






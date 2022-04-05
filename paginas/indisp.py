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

def indisp():
    st.write('___')
    pagina = option_menu(
        menu_title="Formulários",
        options=['Mensal', 'CML'],
        menu_icon='cast',
        default_index=0,
        orientation='vertical'
    )



    SCOPE = "https://www.googleapis.com/auth/spreadsheets"
    SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    SHEET_NAME = "indisponibilidade"
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
    st.title("RETIRADA DE FALTAS")

    gsheet_connector = connect_to_gsheet()

    # texto sidebar
    st.sidebar.write(
        f"Esta página é permitida somente para o efetivo da Seção de Apoio do 1/2GT, somente usuários com e-mail \n"
        f"cadastrados podem modificar a [Planilha de Retirada de Faltas]({GSHEET_URL})."
    )
    st.sidebar.write(
        "Caso haja demandas procure algum militar do Apoio.\n"

    )
    st.sidebar.write(
        "Att, Ten David"
    )

    form = st.form(key="annotation")

    with form:
        st.title('Ten David')
        # cols = st.columns((1, 1))
        # author = cols[0].text_input("Ten David")
        cols = st.columns(2)
        motivo = cols[0].radio(
            "Motivo:", ["Presente", "Voo", "Sobreaviso", "Dispensado", "Férias", "Outro"], index=0
        )

        date = cols[1].date_input("Data")
        time = cols[1].time_input("Horário")
        comment = st.text_area("Comentários")
        submitted = st.form_submit_button(label="Registrar")

    if submitted:
        add_row_to_gsheet(
            gsheet_connector,
            [[str(motivo), str(comment), str(date), str(time)]],
        )
        st.success("Registro realizado.")
        st.balloons()

    expander = st.expander("Registros")
    with expander:
        st.write(f"Abrir planilha no [Google Sheet]({GSHEET_URL})")
        st.dataframe(get_data(gsheet_connector))






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
from PIL import Image

#chamada da pagina

def indisp():
    st.write('___')
    pagina = option_menu(
        menu_title="Formulários",
        options=['Indisponibilidade Mensal', 'CML'],
        menu_icon='cast',
        default_index=0,
        orientation='vertical'
    )

#sidebar

    image = Image.open('images/condor guerreiro colorido.png')
    st.sidebar.image(image)
    st.sidebar.markdown(
        "<h3 style='text-align: center; color:grey; font-size:30px;'><b>ORIENTAÇÕES<b></h3>",
        unsafe_allow_html=True)
    st.sidebar.write("1. A indisponibilidades mensal deve ser inserida até o dia 11 de cada mês.")
    st.sidebar.write("2. Os militares que prestarem serviço no CML devem inserir os dias referente ao mês anterior até o dia 3 de cada mês.")

#chamada de página
    if pagina == 'Indisponibilidade Mensal':
        SCOPE = "https://www.googleapis.com/auth/spreadsheets"
        SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
        SHEET_NAME = "mensal"
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

        def get_data(gsheet_connector) -> pd.DataFrame:
            values = (
                gsheet_connector.values()
                    .get(
                    spreadsheetId=SPREADSHEET_ID,
                    range=f"{SHEET_NAME}!A:E",
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
                range=f"{SHEET_NAME}!A:E",
                body=dict(values=row),
                valueInputOption="USER_ENTERED",
            ).execute()

        st.markdown("<h1 style='text-align: center; color:grey; font-size:2Opx;'><b>INDISPONIBILIDADE MENSAL<b></h1>",
                    unsafe_allow_html=True)
        gsheet_connector = connect_to_gsheet()

        form = st.form(key="annotation")

        with form:
            cols = st.columns(2)
            author = st.text_input("Posto/Grad/Nome de Guerra:")
            cols = st.columns(2)
            motivo = cols[0].radio(
                "Motivo:", ["Férias", "Serviço", "Dispensa", "Curso", "Outro (descrever motivo)"], index=0
            )
            cols[1].write("Data  ( ANO/MÊS/DIA ):")
            date1 = cols[1].date_input("De:")
            date2 = cols[1].date_input("Até:")
            comment = st.text_area("Descrição:", height=100)
            submitted = st.form_submit_button(label="Salvar e Registrar")

        if submitted:
            add_row_to_gsheet(
                gsheet_connector,
                [[str(author), str(motivo), str(comment), str(date1), str(date2)]],
            )
            st.success("Registro realizado.")
            st.balloons()

        expander = st.expander("Conferir registro")
        with expander:
            st.write(f"Abrir planilha no [Google Sheet]({GSHEET_URL})")
            st.dataframe(get_data(gsheet_connector))

    if pagina == 'CML':
        SCOPE = "https://www.googleapis.com/auth/spreadsheets"
        SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
        SHEET_NAME = "cml"
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

        def get_data(gsheet_connector) -> pd.DataFrame:
            values = (
                gsheet_connector.values()
                    .get(
                    spreadsheetId=SPREADSHEET_ID,
                    range=f"{SHEET_NAME}!A:E",
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
                range=f"{SHEET_NAME}!A:E",
                body=dict(values=row),
                valueInputOption="USER_ENTERED",
            ).execute()

        st.markdown("<h1 style='text-align: center; color:grey; font-size:2Opx;'><b>Serviço no CML<b></h1>",
                    unsafe_allow_html=True)
        gsheet_connector = connect_to_gsheet()

        form = st.form(key="annotation")

        with form:
            author = st.text_input("Posto/Grad/Nome de Guerra:")
            cols = st.columns(2)
            saram = cols[0].text_area("SARAM:", height=100)
            dias = cols[0].slider(label= 'Quantidade de dias:', max_value=30 , min_value=1)
            cols[1].write("Data  ( ANO/MÊS/DIA ):")
            date1 = cols[1].date_input("De:")
            date2 = cols[1].date_input("Até:")
            submitted = st.form_submit_button(label="Salvar e Registrar")

        if submitted:
            add_row_to_gsheet(
                gsheet_connector,
                [[str(author), str(saram), str(date1), str(date2), str(dias)]],
            )
            st.success("Registro realizado.")
            st.balloons()

        expander = st.expander("Conferir registro")
        with expander:
            st.write(f"Abrir planilha no [Google Sheet]({GSHEET_URL})")
            st.dataframe(get_data(gsheet_connector))
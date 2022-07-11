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

def faltas():
    # texto sidebar
    SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"


    #sidebar com imagem do Esquadrão
    # image = Image.open('images/condor guerreiro colorido.png')
    # st.sidebar.image(image)
    # st.sidebar.write(
    #     f"Esta página é permitida somente para o efetivo da Seção de Apoio do 1/2GT."
    #
    # )

    # st.sidebar.write(
    #     "Caso haja demandas procure algum militar do Apoio.\n"
    # )
    # st.sidebar.write(
    #     "Att, Ten David"
    # )

    pagina = option_menu(
        menu_title="Retirada de Faltas",
        options=['Oficiais', 'Graduados', 'Praças', ],
        menu_icon='person',
        default_index=0,
        orientation='vertical'
    )

    if pagina == 'Oficiais':

        def check_password():
            """Returns `True` if the user had a correct password."""

            def password_entered():
                """Checks whether a password entered by the user is correct."""
                if (
                        st.session_state["username"] in st.secrets["passwords"]
                        and st.session_state["password"]
                        == st.secrets["passwords"][st.session_state["username"]]
                ):
                    st.session_state["password_correct"] = True
                    del st.session_state["password"]  # don't store username + password
                    del st.session_state["username"]
                else:
                    st.session_state["password_correct"] = False

            if "password_correct" not in st.session_state:
                # First run, show inputs for username + password.
                st.text_input("Usuário:", on_change=password_entered, key="username")
                st.text_input(
                    "Senha:", type="password", on_change=password_entered, key="password"
                )
                return False
            elif not st.session_state["password_correct"]:
                # Password not correct, show input + error.
                st.text_input("Username", on_change=password_entered, key="username")
                st.text_input(
                    "Password", type="password", on_change=password_entered, key="password"
                )
                st.error("😕 Usuário ou senha incorreto")
                return False
            else:
                # Password correct.
                return True

        if check_password():

            SCOPE = "https://www.googleapis.com/auth/spreadsheets"
            SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
            SHEET_NAME = "oficiais"
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

            # st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")
            st.title("OFICIAIS")

            gsheet_connector = connect_to_gsheet()

            form = st.form(key="annotation")

            efetivo = ['TC DAVIDSON', 'MJ ROELES', 'CP DALLA CORTE', 'CP RAFAEL', 'CP ROBERTHA',
                        'CP MOREIRA', 'CP RICARDO', 'CP BLUMER',
                        'CP FIALHO', 'CP ALENCAR', 'TEN DAVID', 'TEN FILGUEIRAS', 'TEN ANCHIETA',
                        'TEN LUIZ CLÁUDIO', 'TEN GABRIEL', 'TEN MOURA']

            for i in efetivo:
                with form:
                    cols = st.columns(2)
                    nome = cols[0].subheader(i)
                    motivo = cols[0].radio(
                        "Motivo:", [" _______ ", "Presente", "Serviço", "Voo", "Sobreaviso", "Dispensado", "Férias", "Atrasado", "Outro"],
                        index=0, key=i
                    )
                    date = cols[1].date_input("Data", key=i)
                    time = cols[1].radio(
                        "Horário:", ["Dia", "Tarde", "Noite"], index=0, key=i)
                    comment = st.text_area("Comentários", key=i)
                    submitted = st.form_submit_button(label='REGISTRAR\n' + i)

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

    if pagina == 'Graduados':

        def check_password2():
            """Returns `True` if the user had a correct password."""

            def password_entered2():
                """Checks whether a password entered by the user is correct."""
                if (
                        st.session_state["username"] in st.secrets["passwords2"]
                        and st.session_state["password"]
                        == st.secrets["passwords2"][st.session_state["username"]]
                ):
                    st.session_state["password_correct"] = True
                    del st.session_state["password"]  # don't store username + password
                    del st.session_state["username"]
                else:
                    st.session_state["password_correct"] = False

            if "password_correct" not in st.session_state:
                # First run, show inputs for username + password.
                st.text_input("Usuário:", on_change=password_entered2, key="username")
                st.text_input(
                    "Senha:", type="password", on_change=password_entered2, key="password"
                )
                return False
            elif not st.session_state["password_correct"]:
                # Password not correct, show input + error.
                st.text_input("Username", on_change=password_entered2, key="username")
                st.text_input(
                    "Password", type="password", on_change=password_entered2, key="password"
                )
                st.error("😕 Usuário ou senha incorreto")
                return False
            else:
                # Password correct.
                return True

        if check_password2():
            #st.button("Entrar")
            #st.write("Autenticação realizada com sucesso")


            SCOPE = "https://www.googleapis.com/auth/spreadsheets"
            SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
            SHEET_NAME = "graduados"
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

            # st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")
            st.title("Graduados")

            gsheet_connector = connect_to_gsheet()

            form = st.form(key="annotation")

            efetivo = ['SO CAIO', '1S MEIRELES', '1S LUIZ ALBERTO', '1S FAUSTINO', '1S RONILSON',
                        '2S CASTANHEIRA', '2S CARVALHO', '2S AZEVEDO', '2S WOLBERTH', '3S ESTEVES']

            for i in efetivo:
                with form:
                    cols = st.columns(2)
                    nome = cols[0].subheader(i)
                    motivo = cols[0].radio(
                        "Motivo:",
                        [" _______ ", "Presente", "Serviço", "Voo", "Sobreaviso", "Dispensado", "Férias", "Atrasado", "Outro"],
                        index=0, key=i
                    )
                    date = cols[1].date_input("Data", key=i)
                    time = cols[1].radio(
                        "Horário:", ["Dia", "Tarde", "Noite"], index=0, key=i)
                    comment = st.text_area("Comentários", key=i)
                    submitted = st.form_submit_button(label='REGISTRAR\n' + i)

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

    if pagina == 'Praças':

        def check_password():
            """Returns `True` if the user had a correct password."""

            def password_entered():
                """Checks whether a password entered by the user is correct."""
                if (
                        st.session_state["username"] in st.secrets["passwords3"]
                        and st.session_state["password"]
                        == st.secrets["passwords3"][st.session_state["username"]]
                ):
                    st.session_state["password_correct"] = True
                    del st.session_state["password"]  # don't store username + password
                    del st.session_state["username"]
                else:
                    st.session_state["password_correct"] = False

            if "password_correct" not in st.session_state:
                # First run, show inputs for username + password.
                st.text_input("Usuário:", on_change=password_entered, key="username")
                st.text_input(
                    "Senha:", type="password", on_change=password_entered, key="password"
                )
                return False
            elif not st.session_state["password_correct"]:
                # Password not correct, show input + error.
                st.text_input("Username", on_change=password_entered, key="username")
                st.text_input(
                    "Password", type="password", on_change=password_entered, key="password"
                )
                st.error("😕 Usuário ou senha incorreto")
                return False
            else:
                # Password correct.
                return True

        if check_password():
        #     st.write("Autenticação realizada com sucesso")
        #     #st.button("Entrar")

            SCOPE = "https://www.googleapis.com/auth/spreadsheets"
            SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
            SHEET_NAME = "pracas"
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

            # st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")
            st.title("Praças")

            gsheet_connector = connect_to_gsheet()

            form = st.form(key="annotation")


            efetivo = [ 'S1 L. SIQUEIRA', 'S1 SILVA MOURA',
                       'S2 VALENTINO', 'S2 ARANHA', 'S2 LUAN SOARES', 'S2 SILVA BARBOSA', 'S2 LEVI GOMES', 'S2 COSTA VITOR']

        for i in efetivo:
            with form:
                cols = st.columns(2)
                nome = cols[0].subheader(i)
                motivo = cols[0].radio(
                    "Motivo:",
                    [" _______ ", "Presente", "Serviço", "Voo", "Sobreaviso", "Dispensado", "Férias", "Atrasado", "Outro"],
                    index=0, key=i
                )
                date = cols[1].date_input("Data", key=i)
                time = cols[1].radio(
                    "Horário:", ["Dia", "Tarde", "Noite"], index=0, key=i)
                comment = st.text_area("Comentários", key=i)
                submitted = st.form_submit_button(label='REGISTRAR\n' + i)

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

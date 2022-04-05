#conexao com Google Sheets
#importar bibliotecas
#from __future__ import print_function
import streamlit as st
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import google_auth_httplib2
import httplib2
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.http import HttpRequest

def faltas():
    # If modifying these scopes, delete the file token.json.
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    #ID da planilha
    SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    SHEET_NAME = 'david'
    GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"

    def connect_to_gsheet():
        creds = None
    #executa o login na ferramenta
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPE)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPE)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

    #         # Call the Sheets API
    # #ler informacoes no google sheets
    #         sheet = service.spreadsheets()
    #         result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    #                                     range=SHEET_NAME).execute()
    #         values = result.get('values', [])
    #         print(values)
    # #adicionar/editar ou editar valores no google sheets
    #         valores_adicionar = [
    #             ['sextou', 's2'],
    #             ['jantarzinho', 'amorzao'],
    #             ['pipoquinha', 's2']
    #         ]
    #         result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
    #                                        range='Página1!A1:B13', valueInputOption='USER_ENTERED',
    #                                        body={'values': valores_adicionar}).execute()
    #         print()
    #verificacao de valores nulos
        #     if not values:
        #         print('No data found.')
        #         return
        #
        #     print('Name, Major:')
        #     for row in values:
        #         # Print columns A and E, which correspond to indices 0 and 4.
        #         print('%s, %s' % (row[0], row[4]))
        except HttpError as err:
            print(err)

    if __name__ == '__connect_to_gsheet__':
        connect_to_gsheet()

    # @st.experimental_singleton()
    # def connect_to_gsheet():
    #     # Create a connection object.
    #     credentials = service_account.Credentials.from_service_account_info(
    #         st.secrets["gcp_service_account"],
    #         scopes=[SCOPE],
    #     )
    #
    #     # Create a new Http() object for every request
    #     def build_request(http, *args, **kwargs):
    #         new_http = google_auth_httplib2.AuthorizedHttp(
    #             credentials, http=httplib2.Http()
    #         )
    #         return HttpRequest(new_http, *args, **kwargs)
    #
    #     authorized_http = google_auth_httplib2.AuthorizedHttp(
    #         credentials, http=httplib2.Http()
    #     )
    #     service = build(
    #         "sheets",
    #         "v4",
    #         requestBuilder=build_request,
    #         http=authorized_http,
    #     )
        gsheet_connector = service.spreadsheets()
        return gsheet_connector

    # def get_data(gsheet_connector) -> pd.DataFrame:
    #     values = (
    #         gsheet_connector.values()
    #             .get(
    #             spreadsheetId=SPREADSHEET_ID,
    #             range=f"{SHEET_NAME}",
    #         )
    #             .execute()
    #     )
    #
    #     df = pd.DataFrame(values["values"])
    #     df.columns = df.iloc[0]
    #     df = df[1:]
    #     return df

    def add_row_to_gsheet(gsheet_connector, row) -> None:
        gsheet_connector.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:G",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        ).execute()



    st.title("Retirada de Faltas")

    gsheet_connector = connect_to_gsheet()

    st.sidebar.write(
        f"This app shows how a Streamlit app can interact easily with a [Google Sheet]({GSHEET_URL}) to read or store data."
    )

    st.sidebar.write(
        f"[Read more](https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet) about connecting your Streamlit app to Google Sheets."
    )

    form = st.form(key="annotation")

    with form:
        cols = st.columns((1,1))
        author = cols[0].text_input("Ten David")
        motivo = cols[1].selectbox(
            "Motivo:", ["Presente", "Voo", "Sobreaviso", "Dispensado", "Férias", "Outro"], index=2
        )
        cols = st.columns(2)
        date = cols[0].date_input("Data")
        time = cols[1].time_input("Horário")
        comment = st.text_area("Comentários")
        submitted = st.form_submit_button(label="Registrar")

    if submitted:
        add_row_to_gsheet(
            gsheet_connector,
            [[author, motivo, comment, str(date), time]],
        )
        st.success("Registro realizado.")
        st.balloons()

    # expander = st.expander("Registros")
    # with expander:
    #     st.write(f"Abrir Planilha [Google Sheet]({GSHEET_URL})")
    #     st.dataframe(get_data(gsheet_connector))
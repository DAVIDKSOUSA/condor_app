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
import plotly.express as px

#chamada da pagina

def horas():
    st.write('___')
    pagina = option_menu(
        menu_title="Pau de Sebo",
        options=['Pilotos', 'Mecânicos', 'Comissários'],
        menu_icon='plane',
        default_index=0,
        orientation='vertical'
    )

    if pagina == "Pilotos":
        df = pd.read_excel('aulas/horas.xlsx',
                           sheet_name='pilotos',
                           usecols='A:B',
                           header=0)
        st.dataframe(df)

        bar_chart = px.bar(df,
                           x="NOME",
                           y="HORAS",
                           template='plotly_white',
                           title='HORAS VOADAS PILOTOS - ATUALIZADO (26/04/2022)')
        st.plotly_chart(bar_chart)

    if pagina == "Mecânicos":
        df = pd.read_excel('aulas/horas.xlsx',
                           sheet_name='mecanicos',
                           usecols='A:B',
                           header=0)
        st.dataframe(df)

        bar_chart = px.bar(df,
                           x="NOME",
                           y="HORAS",
                           template='plotly_white',
                           title='HORAS VOADAS MECÂNICOS - ATUALIZADO (26/04/2022)')
        st.plotly_chart(bar_chart)

    if pagina == "Comissários":
        df = pd.read_excel('aulas/horas.xlsx',
                           sheet_name='comissarios',
                           usecols='A:B',
                           header=0)
        st.dataframe(df)

        bar_chart = px.bar(df,
                           x="NOME",
                           y="HORAS",
                           template='plotly_white',
                           title='HORAS VOADAS COMISSÁRIOS - ATUALIZADO (26/04/2022)')
        st.plotly_chart(bar_chart)



# SCOPE = "https://www.googleapis.com/auth/spreadsheets"
    # SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    # SHEET_NAME = "horas"
    # GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
    #
    # @st.experimental_singleton(suppress_st_warning=True)
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
    #     gsheet_connector = service.spreadsheets()
    #     return gsheet_connector
    #
    # def get_data(gsheet_connector) -> pd.DataFrame:
    #     values = (
    #         gsheet_connector.values()
    #             .get(
    #             spreadsheetId=SPREADSHEET_ID,
    #             range=f"{SHEET_NAME}!A:B",
    #         )
    #             .execute()
    #     )
    #
    #     df = pd.DataFrame(values["values"])
    #     df.columns = df.iloc[0]
    #     df = df[1:]
    #     return df
    #
    # def add_row_to_gsheet(gsheet_connector, row) -> None:
    #     gsheet_connector.values().append(
    #         spreadsheetId=SPREADSHEET_ID,
    #         range=f"{SHEET_NAME}!A:B",
    #         body=dict(values=row),
    #         valueInputOption="USER_ENTERED",
    #     ).execute()
    #
    # #st.markdown("<h1 style='text-align: center; color:grey; font-size:2Opx;'><b>Pau de Sebo<b></h1>",
    # #            unsafe_allow_html=True)
    # gsheet_connector = connect_to_gsheet()
    #
    # if pagina == 'Pilotos':
    #         SCOPE = "https://www.googleapis.com/auth/spreadsheets"
    #         SPREADSHEET_ID = '1Q9A-rSoxYxNRL4smyyaFnNWlRX9Mvp3RmxEhHiipEd8'
    #         SHEET_NAME = "horas"
    #         GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
    #
    #         @st.experimental_singleton(suppress_st_warning=True)
    #         def connect_to_gsheet():
    #             # Create a connection object.
    #             credentials = service_account.Credentials.from_service_account_info(
    #                 st.secrets["gcp_service_account"],
    #                 scopes=[SCOPE],
    #             )
    #
    #             # Create a new Http() object for every request
    #             def build_request(http, *args, **kwargs):
    #                 new_http = google_auth_httplib2.AuthorizedHttp(
    #                     credentials, http=httplib2.Http()
    #                 )
    #                 return HttpRequest(new_http, *args, **kwargs)
    #
    #             authorized_http = google_auth_httplib2.AuthorizedHttp(
    #                 credentials, http=httplib2.Http()
    #             )
    #             service = build(
    #                 "sheets",
    #                 "v4",
    #                 requestBuilder=build_request,
    #                 http=authorized_http,
    #             )
    #             gsheet_connector = service.spreadsheets()
    #             return gsheet_connector
    #
    #         def get_data(gsheet_connector) -> pd.DataFrame:
    #             values = (
    #                 gsheet_connector.values()
    #                     .get(
    #                     spreadsheetId=SPREADSHEET_ID,
    #                     range=f"{SHEET_NAME}!A:B",
    #                 )
    #                     .execute()
    #             )
    #
    #             df = pd.DataFrame(values["values"])
    #             df.columns = df.iloc[0]
    #             df = df[1:]
    #             return df
    #
    #         def add_row_to_gsheet(gsheet_connector, row) -> None:
    #             gsheet_connector.values().append(
    #                 spreadsheetId=SPREADSHEET_ID,
    #                 range=f"{SHEET_NAME}!A:B",
    #                 body=dict(values=row),
    #                 valueInputOption="USER_ENTERED",
    #             ).execute()
    #
    #         # st.markdown("<h1 style='text-align: center; color:grey; font-size:2Opx;'><b>Pau de Sebo<b></h1>",
    #         #            unsafe_allow_html=True)
    #         gsheet_connector = connect_to_gsheet()
    #         st.write(f"Abrir planilha no [Google Sheet]({GSHEET_URL})")
    #         fig = pd.DataFrame(get_data(gsheet_connector))
    #         st.dataframe(fig)
    #
    #
    #         credentials = service_account.Credentials.from_service_account_info(
    #             st.secrets["gcp_service_account"],
    #             scopes=[SCOPE],
    #         )
    #
    #         def build_request(http, *args, **kwargs):
    #             new_http = google_auth_httplib2.AuthorizedHttp(
    #                 credentials, http=httplib2.Http()
    #             )
    #             return HttpRequest(new_http, *args, **kwargs)
    #
    #         authorized_http = google_auth_httplib2.AuthorizedHttp(
    #             credentials, http=httplib2.Http()
    #         )
    #
    #         service = build(
    #             "sheets",
    #             "v4",
    #             requestBuilder=build_request,
    #             http=authorized_http,
    #         )
    #
    #         sheet = service.spreadsheets()
    #         result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="horas!A:B").execute()
    #         values = result.get('values', [])
    #
    #         # df = pd.DataFrame(values, index="TEMPO")
    #         #df1 = df.set_index("TEMPO")
    #
    #         #df2 = pd.Series(df, index="TEMPO")
    #
    #         # st.dataframe(df)
    #
    #
    #         # bar_chart = px.bar(df1, x='NOME', y= df1.index, text_auto=True)
    #         # st.plotly_chart(bar_chart, use_container_width=True, sharing='streamlit')
    #
    #         st.write('___')







#importar bibliotecas
import streamlit as st
from streamlit_lottie import st_lottie
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
    # st.image('/Users/davidsousa/Prophet/Capa_Home.png', use_column_width='always')
    st.write('---')
    st.markdown("<h3 style='text-align: center; color:blue; font-size:50px;'><b>ESQUADRÃO CONDOR<b></h3>",
                unsafe_allow_html=True)
    st.write('---')
    st.text('')
    st.markdown("<h1 style='text-align: center; color:grey; font-size:23px;'><b>Faça uma análise completa da sua "
                "carteira de investimentos de forma<b></h1>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color:grey; font-size:30px;'><b>SIMPLES, OBJETIVA e RÁPIDA!<b></h3>",
                unsafe_allow_html=True)
    st.text('')
    st.write(
        'O processo de alocação patrimonial, apesar de ser simples não é fácil. Devido à quantidade exarcebada de infor'
        'mações que temos, muitas vezes, o investidor fica na dúvida em relação à composição da sua '
        'carteira de investimentos. Neste contexto '
        'o SMART PORTFOLIO '
        'foi concebido com a intenção de auxiliar no processo de alocação patrimonial. O aplicativo não irá te mostrar '
        'em qual classe de ativo financeiro investir, contudo uma vez definida a classe de ativo será possível '
        'identificar uma alocação eficiente, '
        'onde pode-se esperar um menor risco (volatilidade), para um maior retorno.'
    )
    st.write('---')
    st.write(':point_left: Use o menu ao lado e selecione uma funcionalidade.')
    st.write('---')
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            def p_title(title):
                st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>',
                            unsafe_allow_html=True)

            st.text('')
            p_title('Qual objetivo do SMART PORTFOLIO ?')
            st.text('')
            st.write(
                'Realizar a analise de ativos financeiros e o comportamento de um portifólio de investimentos através de '
                'análise de dados.'
            )
            p_title('Quem deve utilizar o SMART PORTFOLIO ?')
            st.write(
                'Investidores que querem realizar uma análise independente da sua carteira de investimentos ou algum ativo'
                ' específico'
            )
            st.write('##')
            st.write(
                '''
                Link das Mídias Sociais:
                '''
            )
            st.markdown(
                """
                [![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCHi_qOCcC_KeMu18cOyHtQg?style=social)](https://www.youtube.com/channel/UCHi_qOCcC_KeMu18cOyHtQg)
                """
                # [![Star](https: // img.shields.io / github / stars / dlopezyse / Synthia.svg?logo = instagram & style = social)](https: // gitHub.com / dlopezyse / Synthia)
                # [![DFGDFG](https: // img.shields.io / github / stars / dlopezyse / Synthia.svg?logo = linkedin & style = social)](https: // www.linkedin.com / in / david-sousa-ab6826198 /)
            )

        with right_column:
            st_lottie(lottie_coding, quality='high', height=300, key='coding')


import pandas as pd
import streamlit as st

from Ferramentas.Tratamento import padronizando

# Configurando o titulo da pagina
st.set_page_config(page_title='Finanças',page_icon='computer') 

# Formatando com Markdown

st.markdown("""
# Curva ABC            
           
""")


def exibir():
    ''' Função para apresentação de dados '''
    try:
        # Exibindo informações
        st.subheader('Informações do Data Frame')

        #Capturando o arquivo
        arquivo_upload = st.file_uploader('Arquivos', type=['csv'])

        if arquivo_upload is not None:
            
            df = padronizando(arquivo_upload)
            st.success('Arquivo enviado com sucesso')
            st.subheader(arquivo_upload.name)
            st.dataframe(df)

        else:
            st.info('Aguardando o arquivo csv')

    except Exception as e:
        st.error(f'Erro em exibir: {e}')

def main():
    ''' Função principal do programa '''

    # Configuração Geral
    st.set_page_config(page_title='Curva ABC', layout='wide', initial_sidebar_state='collapsed')

    exibir()

if __name__ == '__main__':
    main()
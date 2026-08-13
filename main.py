import pandas as pd
import streamlit as st

from Ferramentas.Tratamento import padronizando

# Configurando o titulo da pagina
st.set_page_config(page_title='Finanças',page_icon='computer') 

# Formatando com Markdown

st.markdown("""
# Curva ABC            
           
""")


def main():
    ''' Função principal do programa '''

    # Configuração Geral
    st.set_page_config(page_title='Curva ABC', layout='wide', initial_sidebar_state='collapsed')

    try:

        #Capturando o arquivo
        arquivo_upload = st.file_uploader('Arquivos', type=['csv'])

        if arquivo_upload is not None:
            
            df = padronizando(arquivo_upload)
            st.success('Arquivo enviado com sucesso')
            st.subheader(arquivo_upload.name)

            # --- Cards ---
            card_faturamento, card_estoque, card_ruptura = st.columns(3)

            
            faturamento_total = df['faturamento_total'].sum()
            card_faturamento.metric('Faturamento Total', faturamento_total, border=True)

            estoque_total = df['estoque_atual'].sum()
            card_estoque.metric('Estoque Atual Total', estoque_total, border=True)

            ruptura_flags = df.query('Flag_Ruptura_Critica == 1 ')['Flag_Ruptura_Critica'].count()
            card_ruptura.metric('Ruptura Crítica de Produtos', ruptura_flags, border=True)


            # --- Abas --- isso pode virar filtro e colocar um dataframe que acompanha os filtros
            curva_a,curva_b, curva_c = st.tabs(['Curva A','Curva B','Curva C'])

            with curva_a:
                st.info('Curva A')
                st.dataframe(df)
            with curva_b:
                st.info('Curva B')

            with curva_c:
                st.info('Curva C')

        else:
            st.info('Aguardando o arquivo csv')

    except Exception as e:
        st.error(f'Erro ao enviar o arquivo: {e}')

if __name__ == '__main__':
    main()
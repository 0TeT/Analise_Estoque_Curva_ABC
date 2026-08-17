import pandas as pd
import streamlit as st

from Ferramentas.Tratamento import padronizando, Filtrando_curva

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
            
            df_padronizado = padronizando(arquivo_upload)
            st.success('Arquivo enviado com sucesso')
            st.subheader(arquivo_upload.name)

            # --- Cards ---
            card_faturamento, card_estoque, card_ruptura = st.columns(3)

            
            faturamento_total = df_padronizado['faturamento_total'].sum()
            exibir_faturamento = f'R$ {faturamento_total:,.2f}'
            card_faturamento.metric('Faturamento Total', exibir_faturamento, border=True)

            estoque_total = df_padronizado['estoque_atual'].sum()
            exibir_estoque = f'{estoque_total:,.0f}'
            card_estoque.metric('Estoque Atual Total', exibir_estoque, border=True)

            ruptura_flags = df_padronizado.query('Flag_Ruptura_Critica == 1 ')['Flag_Ruptura_Critica'].count()
            card_ruptura.metric('Ruptura Crítica de Produtos', ruptura_flags, border=True)


            # --- Abas --- 
            curva_abc, curva_a, curva_b, curva_c = st.tabs(['Curva ABC','Curva A','Curva B','Curva C'])

            # Cada Aba é um Filtro que mostra apenas o DataFrame de cada filtro
            with curva_abc:
                # Contruir um Botão para baixa o arquivo atual
                st.dataframe(df_padronizado)
            with curva_a:
                tipo_curva = 'Curva_A'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva)
                st.dataframe(df_curva,hide_index=True)
            with curva_b:
                tipo_curva = 'Curva_B'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva)
                st.dataframe(df_curva,hide_index=True)
            with curva_c:
                tipo_curva = 'Curva_C'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva)
                st.dataframe(df_curva,hide_index=True)

        else:
            st.info('Aguardando o arquivo csv')

    except Exception as e:
        st.error(f'Erro ao enviar o arquivo: {e}')

if __name__ == '__main__':
    main()
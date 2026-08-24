import io
import pandas as pd
import streamlit as st

from Ferramentas.Tratamento import padronizando, Filtrando_curva
from Ferramentas.Grafico import pareto, analise_categoria

# Formatando com Markdown


st.set_page_config(page_title='Curva ABC', layout='wide', initial_sidebar_state='collapsed',page_icon='📦')
# Configuração Geral

st.markdown("""
# Curva ABC            
           
""")

@st.cache_data(show_spinner=False)
def kpis_filtrados(base):
    ''' Função para atualizar os filtros'''
    try:
        filtrado_df = base.copy()
        # --- Cards ---
        card_faturamento, card_estoque, card_ruptura = st.columns(3)

        faturamento_total = filtrado_df['faturamento_total'].sum()
        exibir_faturamento = f'R$ {faturamento_total:,.2f}'
        card_faturamento.metric('Faturamento Total', exibir_faturamento, border=True)

        estoque_total = filtrado_df['estoque_atual'].sum()
        exibir_estoque = f'{estoque_total:,.0f}'
        card_estoque.metric('Estoque Atual Total', exibir_estoque, border=True)

        ruptura_flags = filtrado_df.query('Flag_Ruptura_Critica == 1 ')['Flag_Ruptura_Critica'].count()
        card_ruptura.metric('Ruptura Crítica de Produtos', ruptura_flags, border=True)
    except Exception as e:
        return st.error(f'Erro nos Filtros dos Cards: {e}')


def botao_download(base):
    ''' Função que vai baixar os aquivo'''
    try:
        relatorio = base.copy()
        xlsx,csv = st.columns(2)

        with xlsx:
            with st.spinner('Gerando Arquivo em Excel...'):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as write:
                    relatorio.to_excel(write, index=False)
                buffer.seek(0)
                relatorio_excel = buffer.getvalue()

            st.download_button(
                label="Baixar Relatorio em XLS",
                data=relatorio_excel,
                file_name='Relatorio.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                use_container_width=True,
                key="btn_download_xlsx"
            )

        with csv:
            relatorio_csv = relatorio.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Baixar Relatorio em CSV",
                data=relatorio_csv,
                file_name='Relatorio.csv',
                mime='text/csv',
                use_container_width=True,
                key="btn_download_csv"
                
            )
        
    except Exception as e:
        return st.error(f'Erro em baixar o arquivo: {e}')
def main():
    ''' Função principal do programa '''


    try:

        #Capturando o arquivo
        arquivo_upload = st.file_uploader('Arquivos', type=['csv'])

        if arquivo_upload is not None:
            
            df_padronizado = padronizando(arquivo_upload)
            st.success('Arquivo enviado com sucesso')
            st.subheader(arquivo_upload.name)

            # --- Abas --- 
            curva_abc, curva_a, curva_b, curva_c, grafico_comparacao, grafico_categoria = st.tabs(['Curva ABC','Curva A','Curva B','Curva C', 'Graficos de Comparação', 'Grafico de Categoria'])

            # Cada Aba é um Filtro que mostra apenas o DataFrame de cada filtro
            with curva_abc:
                botao_download(df_padronizado)
                kpis_filtrados(df_padronizado)
                st.dataframe(df_padronizado)
            with curva_a:
                tipo_curva = 'Curva_A'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva)
                kpis_filtrados(df_curva)
                st.dataframe(df_curva,hide_index=True)
            with curva_b:
                tipo_curva = 'Curva_B'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva) 
                kpis_filtrados(df_curva)
                st.dataframe(df_curva,hide_index=True)
            with curva_c:
                tipo_curva = 'Curva_C'
                df_curva = Filtrando_curva(df_padronizado,tipo_curva)
                kpis_filtrados(df_curva)
                st.dataframe(df_curva,hide_index=True)
            with grafico_comparacao:
                st.plotly_chart(pareto(df_padronizado.head(20)), use_container_width=True)
            with grafico_categoria:
                st.plotly_chart(analise_categoria(df_padronizado), use_container_width=True)


        else:
            st.info('Aguardando o arquivo csv')

    except Exception as e:
        st.error(f'Erro ao enviar o arquivo: {e}')

if __name__ == '__main__':
    main()
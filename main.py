import pandas as pd
import streamlit as st

# Configurando o titulo da pagina
st.set_page_config(page_title='Finanças',page_icon='computer') 

# Formatando com Markdown

st.markdown("""
# Curva ABC            
           
""")

# Capturando o arquivo
arquivo_upload = st.file_uploader(label="Faça Upload dos dados", type=['csv'])

if arquivo_upload is not None:

    # Leitura com Pandas
    df_surjo = pd.read_csv(arquivo_upload)

    # Formatando pelo proprio streamlit, apenas visualmente
    format_colunas = {"preco_venda":st.column_config.NumberColumn("preco_venda", format="R$ %f")}

    # Exibindo os dados
    st.dataframe(df_surjo, hide_index=True, column_config=format_colunas)

    variavel = st.expander()# para esconder a informação
    variavel.dataframe(df_surjo)
    variavel.line_chart(df_surjo)
    variavel.bar_chart(df_surjo)

    v1, v2, v3 = st.tab(['nome1','nome2','nome3'])
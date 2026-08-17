import numpy as np
import pandas as pd


def curva(pocentagem):
    ''' Função para atribuir a curva de cada produto'''

    if pocentagem <= 0.80:
        return 'A'
    elif pocentagem <= 0.95:
        return 'B'
    else:
        return 'C'

def padronizando(base):
    ''' Função para padronizar o DataFrame Recebido '''

    # Lendo arquivo CSV
    base_surja = pd.read_csv(base).copy()

    # Removendo duplicadas
    base_surja.drop_duplicates(subset='codigo_produto', keep='last', inplace=True)

    # Tratando valores nulos
    base_surja['estoque_atual'] = base_surja['estoque_atual'].fillna(0)
    base_surja['categoria'] = base_surja['categoria'].fillna('Não Classificado')


    # Tratando formatação e tipagem

    base_surja['preco_venda'] = (
        base_surja['preco_venda']
        .astype(str)
        .str.replace('R$', '', regex=False)
        .str.strip()
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )

    base_surja['preco_venda'] = pd.to_numeric(base_surja['preco_venda'], errors='coerce')

    base_surja['custo_unitario'] = (
        base_surja['custo_unitario']
        .astype(str)
        .str.replace('R$', '', regex=False)
        .str.strip()
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )

    base_surja['custo_unitario'] = pd.to_numeric(base_surja['custo_unitario'], errors='coerce')

    # Padronizando categorias
    base_surja['categoria'] = base_surja['categoria'].str.strip().str.replace('&','e').str.title()


    # Trantando valores negativos
    base_surja['estoque_atual'] = base_surja['estoque_atual'].clip(lower=0).astype(int)
    base_surja['unidades_vendidas_90d'] = base_surja['unidades_vendidas_90d'].clip(lower=0).astype(int)

    # Contruindo Outliers

    # Declarando Quartil
    Q1 = base_surja['preco_venda'].quantile(0.25)
    Q2 = base_surja['preco_venda'].quantile(0.75)

    # Calculando a Amplitude Interquartil
    IQR = Q2 - Q1

    # Tolerancia
    Limite_inferior = Q1 - 1.5 *IQR
    Limite_superior = Q2 + 1.5 *IQR

    # Tratando Outliers
    mediana_preco = base_surja.loc[base_surja['preco_venda'] <= Limite_superior, 'preco_venda'].median()
    base_surja.loc[base_surja['preco_venda'] > Limite_superior, 'preco_venda'] = mediana_preco

    base_limpa = regra_negocio(base_surja)

    return base_limpa 

def regra_negocio(base):
    ''' Função para tratar a Regra do negocio '''

    # Criando a coluna 'faturamento_total'
    base['faturamento_total'] = base['preco_venda'] * base['unidades_vendidas_90d']

    # Ordenando DataFrame
    base = base.sort_values(by='faturamento_total', ascending=False).reset_index(drop=True) 

    # Faturamento em percentual individual
    faturamento_geral = base['faturamento_total'].sum() 
    base['porcentagem_faturamento'] = base['faturamento_total'] / faturamento_geral 

    # Faturamento acumulado
    base['porcentagem_acumulado'] = base['porcentagem_faturamento'].cumsum()

    # Categorizando Curvas
    base['curva'] = base['porcentagem_acumulado'].apply(curva)

    # Criando Vendas Diaria, Cobertura de Estoque
    base['vendas_diaria'] = (base['unidades_vendidas_90d'] / 90)
    base['cobertura_estoque'] = (base['estoque_atual'] / base['vendas_diaria']).replace([np.inf, -np.inf],0).fillna(0).astype(int)

    # Flagando Ruptura
    base['Flag_Ruptura_Critica'] = np.where(
        (base['curva'] == 'A') & ((base['cobertura_estoque'] < 7)),
        1,
        0
    )

   
    return base

def Filtrando_curva(base, tipo_curvas):
    ''' Filtrando Curvas'''

    try:
        
        base = base[['codigo_produto','categoria','custo_unitario','preco_venda','unidades_vendidas_90d','estoque_atual','faturamento_total','curva','vendas_diaria','cobertura_estoque']]
        if tipo_curvas == 'Curva_A':
            base = base.query('curva == "A"')
            
            return base

        elif tipo_curvas == 'Curva_B':
            base = base.query('curva == "B"')
            return base
        elif tipo_curvas == 'Curva_C':
            base = base.query('curva == "C"')
            return base
        else:
            raise Exception
    except Exception as e:
        return f'Erro na filtragem: {e}'
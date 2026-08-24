# 📦 Gestão de Estoque & Análise de Curva ABC (Supply Chain)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=flat&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?style=flat&logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat&logo=streamlit)

Aplicação interativa desenvolvida em **Python** e **Streamlit** para automação do pipeline de ETL, classificação de catálogo via **Curva ABC** e controle preventivo de **Ruptura Crítica de Estoque**.

---

## 🎯 Objetivo do Projeto

Transformar dados brutos e não padronizados de vendas/estoque em um painel executivo e operacional que auxilie gerentes de suprimentos e analistas de logística a:

1. Identificar os produtos de maior impacto financeiro (**Curva A**).
2. Monitorar a cobertura de estoque em dias.
3. Antecipar rupturas críticas com base no perfil de demanda de cada item.

---

## 🏗️ Arquitetura e Estrutura de Pastas

O projeto foi construído de forma **modular**, separando o pipeline de tratamento de dados (ETL), a construção visual dos gráficos e a interface de usuário do dashboard:

```text
├── Ferramentas/
│   ├── Tratamento.py       # Funções de limpeza, tratamento de moeda, IQR e regras de negócio
│   └── Grafico.py          # Funções de renderização de gráficos do Plotly
├── main.py                 # Aplicação principal em Streamlit (interface do usuário)
├── .gitignore              # Configuração para ignorar arquivos desnecessários (__pycache__, envs)
└── README.md               # Documentação técnica do repositório
```

---

## 🧠 Regras de Negócio e Metodologia Aplicada

### 1. Tratamento de Dados (ETL & Outliers)
* **Limpeza e Tipagem:** Remoção de duplicatas, padronização de categorias de texto e conversão segura de moedas (exemplo: `R$ 1.250,50` para `1250.50`).
* **Tratamento de Outliers:** Aplicação do método da **Amplitude Interquartil (IQR)** sobre a coluna de preços de venda, substituindo discrepâncias pela mediana dos preços válidos.

### 2. Classificação Curva ABC
O faturamento total individual é calculado multiplicando o Preço de Venda pelas Unidades Vendidas. Em seguida, os produtos são ordenados de forma decrescente para apuração do percentual acumulado:
* **Classe A:** Representam até **80%** do faturamento acumulado (Alta prioridade).
* **Classe B:** Representam os **15%** seguintes (de 80% a 95%) do faturamento acumulado (Média prioridade).
* **Classe C:** Representam os **5%** finais (de 95% a 100%) do faturamento acumulado (Baixa prioridade/Cauda longa).

### 3. Matriz de Ruptura Crítica por Nível de Serviço
A cobertura de estoque em dias é calculada dividindo o `Estoque Atual` pela `Venda Diária Média`. A flag de **Ruptura Crítica (`1`)** é acionada preventivamente segundo os critérios:

| Classe da Curva ABC | Critério de Cobertura | Status Acionado |
| :--- | :--- | :--- |
| **Curva A** | Cobertura menor que 7 dias | Ruptura Crítica |
| **Curva B** | Cobertura menor que 5 dias | Ruptura Crítica |
| **Curva C** | Cobertura menor que 3 dias | Ruptura Crítica |

---

## 📊 Funcionalidades do Dashboard (Streamlit)

* **Upload Flexível de Dados:** Leitura automatizada de arquivos `.csv`.
* **Cards de KPIs em Tempo Real:** Faturamento Total, Volume de Estoque e Total de Produtos em Ruptura Crítica.
* **Gráfico de Pareto Interativo:** Visualização de duplo eixo Y (Faturamento em R$ vs. % Acumulado).
* **Análise Comparativa por Categoria:** Barras agrupadas comparando Estoque Atual x Unidades Vendidas em 90 dias.
* **Exportação Dinâmica:** Módulo de download direto do relatório tratado em formatos **XLSX (Excel)** ou **CSV**.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.

### Passos

1. **Clone este repositório:**
```bash
git clone https://github.com/0TeT/Analise_Estoque
cd Analise_Estoque
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate
```

3. **Instale as dependências necessárias:**
```bash
pip install pandas numpy streamlit plotly xlsxwriter
```

4. **Execute a aplicação Streamlit:**
```bash
streamlit run main.py
```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Plotly Express, Plotly Graph Objects
* **Interface & Dashboard:** Streamlit
* **Motor de Exportação:** XlsxWriter
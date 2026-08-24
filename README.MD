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

O projeto foi construído de forma **modular**, separando o pipeline de tratamento de dados (ETL), a construção visual dos gráficos e a interface de usuário do dashboard.

```text
├── Ferramentas/
│   ├── Tratamento.py       # Funções de limpeza, tratamento de moeda, IQR e regras de negócio
│   └── Grafico.py          # Funções de renderização de gráficos do Plotly
├── main.py                 # Aplicação principal em Streamlit (interface do usuário)
├── .gitignore              # Configuração para ignorar arquivos desnecessários (__pycache__, envs)
└── README.md               # Documentação técnica do repositório


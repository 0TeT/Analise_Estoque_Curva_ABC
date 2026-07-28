# 🚀 Guia de Execução: Análise de Curva ABC e Gestão de Estoque

---

## 📌 Etapa 1: Limpeza e Tratamento de Dados (*Data Cleaning*)

- [ ] **1. Remoção de Duplicatas**
  - Identificar e remover registros 100% idênticos usando `.drop_duplicates()`.

- [ ] **2. Padronização de Texto (`categoria`)**
  - Remover espaços extras no início e no fim do texto com `.str.strip()`.
  - Converter textos para *Title Case* (ex: `"eletronicos"` -> `"Eletrônicos"`).
  - Unificar variações de escrita (ex: transformar `"Alimentos & Bebidas"` em `"Alimentos e Bebidas"` usando `.str.replace()`).

- [ ] **3. Tratamento e Conversão de Moedas**
  - Identificar colunas com formato brasileiro (ex: `"R$ 45,90"`).
  - Remover o prefixo `"R$ "`, substituir vírgula por ponto (`,` -> `.`) e converter a coluna para o tipo `float`.

- [ ] **4. Tratamento de Valores Ausentes (`NaN`)**
  - Preencher valores ausentes na coluna `categoria` com a string `"Não Classificado"`.
  - Preencher valores nulos em `estoque_atual` (ex: preencher com `0` ou aplicar a mediana da categoria).

- [ ] **5. Aplicação de Regras de Negócio e Outliers**
  - Identificar e corrigir valores inconsistentes (ex: vendas ou estoques com números negativos $< 0$).
  - Tratar preços com erros de digitação (ex: o produto discrepante de $R\$ 99.999,00$).

---

## 📌 Etapa 2: Regras de Negócio, Curva ABC e Métricas de Estoque

- [ ] **1. Faturamento Total**
  - Criar a coluna `faturamento_total` ($\text{Preço} \times \text{Unidades Vendidas}$).

- [ ] **2. Classificação da Curva ABC**
  - Ordenar o DataFrame pelo `faturamento_total` em ordem decrescente.
  - Calcular a porcentagem do faturamento individual e a porcentagem acumulada com `.cumsum()`.
  - Definir a regra de classificação:
    - **Classe A:** Responde por até 80% do faturamento acumulado.
    - **Classe B:** Responde pelos próximos 15% (de 80% até 95%).
    - **Classe C:** Responde pelos últimos 5% (de 95% até 100%).

- [ ] **3. Indicadores de Estoque**
  - **Média de Vendas Diárias:** $\text{Vendas 90 dias} \div 90$.
  - **Cobertura de Estoque (em dias):** $\text{Estoque Atual} \div \text{Venda Diária}$.
  - **Flag de Ruptura Crítica:** Identificar produtos da Classe A com cobertura inferior a 7 dias de estoque.

---

## 📌 Etapa 3: Visualização de Dados (Matplotlib / Seaborn)

- [ ] **1. Gráfico de Pareto (Curva ABC)**
  - Criar um gráfico combinado: barras representando o faturamento individual por produto e uma linha no eixo secundário mostrando o acumulado percentual.

- [ ] **2. Análise por Categoria**
  - Construir um gráfico de barras comparando o volume de vendas x estoque atual segmentado por categoria de produtos.

---

## 📌 Etapa 4: Dashboard Interativo (Streamlit)

- [ ] **1. Cartões de Métricas (KPIs)**
  - Exibir no topo do dashboard: Faturamento Total, Total de Itens em Estoque e Quantidade de Produtos em Ruptura Crítica.

- [ ] **2. Filtros Dinâmicos**
  - Adicionar uma barra lateral (*sidebar*) para filtrar os dados por Categoria e por Classe ABC (A, B, C).

- [ ] **3. Tabelas Interativas**
  - Exibir a tabela tratada e permitir o download ou a ordenação direta na tela.
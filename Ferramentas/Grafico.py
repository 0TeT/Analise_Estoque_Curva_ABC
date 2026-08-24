import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def pareto(base):
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(
        go.Bar(
            x=base['codigo_produto'].astype(str),
            y=base['faturamento_total'],
            name='Faturamento (R$)',
            marker_color='royalblue',
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=base['codigo_produto'].astype(str),
            y=base['porcentagem_acumulado'] * 100,
            mode='lines+markers',
            name='% Acumulado',
            line=dict(color='firebrick',width=3),
        ),
        secondary_y=True
    )

    fig.update_layout(
        title_text="<b>Gráfico de Pareto:</b> Top produtos x Faturamento Acumulado",
        xaxis_title="Código do Produto",
    )

    fig.update_yaxes(title_text="Faturamento Total (R$)", secondary_y=False)

    fig.update_yaxes(
        title_text="% Acumulado", secondary_y=True
    )

    return fig

def analise_categoria(base):
    fig = px.bar(
    base,
    x='categoria',
    y=['estoque_atual','unidades_vendidas_90d'],
    barmode='group',
    title='<b>Análise por Categoria:</b> Volume de Estoque x Vendas (90 dias)',
    labels={
        "value":"Quantidade (Unidade)",
        "categoria":"Categoria",
        "variable":"Métrica"
    }
    )
    return fig

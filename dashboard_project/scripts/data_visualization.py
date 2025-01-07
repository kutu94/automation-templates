import plotly.express as px


def grafico_ventas_diarias(df):
    """Crea un gráfico de barras para ventas diarias."""
    fig = px.bar(
        df,
        x='Fecha',
        y='Ventas',
        title='Ventas Diarias',
        labels={'Fecha': 'Día', 'Ventas': 'Monto en USD'}
    )
    return fig

def grafico_stock_productos(df):
    """Crea un gráfico de barras para niveles de stock."""
    fig = px.bar(
        df,
        x='Producto',
        y='Stock',
        title='Niveles de Stock por Producto',
        labels={'Producto': 'Nombre del Producto', 'Stock': 'Unidades Disponibles'},
        color='Stock'
    )
    return fig

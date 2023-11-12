import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

avocado = pd.read_csv('data/avocado.csv')

app = Dash()

app.layout = html.Div([
    html.H1('Avocado Prices Dashboard'),
    dcc.Dropdown(id='geo-dropdown',
                 options=avocado['geography'].unique(),
                 value='New York'),
    dcc.Graph(id='price-graph')
])


@app.callback(
    Output('price-graph', 'figure'),
    Input('geo-dropdown', 'value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado.query('geography == @selected_geography')
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)

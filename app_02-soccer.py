import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

soccer = pd.read_csv('data/fifa_soccer_players.csv')

app = Dash(external_stylesheets=[dbc.themes.GRID])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    dbc.Row([
        dbc.Col(html.P(['Source: ',
                        html.A('Sofifa',
                               href='https://sofifa.com',
                               target='_blank')])),
        dbc.Col([html.Label('Player name: '),
                 dcc.Dropdown(
                     options=soccer['long_name'].unique(),
                     value=soccer['long_name'].unique()[0]
                 )])])
])

if __name__ == '__main__':
    app.run_server(debug=True)

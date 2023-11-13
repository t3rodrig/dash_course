import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

soccer = pd.read_csv('data/fifa_soccer_players.csv')

avg_age = soccer['age'].mean()
avg_height = soccer['height_cm'].mean()
avg_weight = soccer['weight_kg'].mean()

cards = dbc.Row([
    dbc.Col(dbc.Card([
        html.H4('Avg. Age'),
        html.H5(f'{round(avg_age, 1)} years')
    ], body=True, style={'textAlign': 'center', 'color': 'white'},
        color='lightblue')),
    dbc.Col(dbc.Card([
        html.H4('Avg. Height'),
        html.H5(f'{round(avg_height, 1)} cm')
    ], body=True, style={'textAlign': 'center', 'color': 'white'},
        color='blue')),
    dbc.Col(dbc.Card([
        html.H4('Avg. weight'),
        html.H5(f'{round(avg_weight, 1)} kg')
    ], body=True, style={'textAlign': 'center', 'color': 'white'},
        color='darkblue'))
])

navbar = dbc.NavbarSimple(
    brand='Soccer Players Dashboard',
    children=[
        html.Img(src='https://uptime.com/media/website_profiles/sofifa.com.png',
                 height=20),
        html.A('Data Source',
               href='https://sofifa.com',
               target='_blank',
               style={'color': 'black'})
    ],
    color='primary',
    fluid=True
)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([navbar, html.Br(), cards])

if __name__ == '__main__':
    app.run_server(debug=True)

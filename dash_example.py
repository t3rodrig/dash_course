import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

happiness = pd.read_csv("world_happiness.csv")

app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report',
                   target='_blank')]),
    dcc.Dropdown(id='country-dropdown',
                 options=happiness['country'].unique(),
                 value='United States'),
    dcc.Graph(id='happiness-graph')
])


@app.callback(
    Output('happiness-graph','figure'),
    Input('country-dropdown','value')
)
def update_graph(selected_country):
    filtered_happiness = happiness.query('country == @selected_country')
    line_fig = px.line(filtered_happiness,
                       x='year', y='happiness_score',
                       title=f'Happiness Score in {selected_country}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)

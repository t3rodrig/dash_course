import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, Input, Output

electricity = pd.read_csv('data/electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

app = Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(year_min, year_max+1)}),
    dcc.Graph(id='map-graph'),
    dash_table.DataTable(id='price-info',
                         data=electricity.to_dict('records'))
])


@app.callback(
    Output('map-graph', 'figure'),
    Input('year-slider', 'value')
)
def update_map_graph(selected_years):
    filtered_electricity = electricity.query(
        '(Year >= @selected_years[0]) and (Year <= @selected_years[1])'
    )
    avg_price_electricity = filtered_electricity.groupby('US_State')[
        'Residential Price'].mean().reset_index()

    map_fig = px.choropleth(avg_price_electricity,
                            locations='US_State',
                            locationmode='USA-states',
                            color='Residential Price',
                            scope='usa',
                            color_continuous_scale='reds')
    return map_fig


if __name__ == '__main__':
    app.run_server(debug=True)

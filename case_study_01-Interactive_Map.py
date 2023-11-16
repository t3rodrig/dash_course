import pandas as pd
from dash import Dash, html, dcc

electricity = pd.read_csv('data/electricity.csv')

app = Dash()

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(year_min, year_max+1)})
])

if __name__ == '__main__':
    app.run_server(debug=True)

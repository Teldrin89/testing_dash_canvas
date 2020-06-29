# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_canvas as dc
from dash.dependencies import Input, Output, State
import vtk_python_script as vps
# import vtk

asset_style = ['assets/style.css']
js_script = [
    {'src': 'https://unpkg.com/vtk.js@14.10.1/dist/vtk.js'}]

app = dash.Dash(
    __name__, 
    external_stylesheets=asset_style)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python
    '''),
    dcc.RangeSlider(id="slider", className="slider"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.H5("Dash Cnavas testing"),
    # dc.DashCanvas(id='canvas-1')
    # html.Canvas(id="html-canvas"),
    html.Iframe(
        src="https://kitware.github.io/vtk-js/examples/GeometryViewer/GeometryViewer.html",
        height=300,
        width=600),
    dcc.Loading(
        html.Button(id="test-button")
    )
    
])

@app.callback(
    Output('test-button', 'children'),
    [Input('test-button', 'n_clicks')]
)
def testing_button(clicks):
    print("number of clicks {}".format(clicks))
    print()
    output  = "Start"
    if clicks is None:
        output = "Button"
    else:
        output = "Button {}".format(clicks)
        # vps.main()
    
    return output

if __name__ == '__main__':
    app.run_server(debug=True)
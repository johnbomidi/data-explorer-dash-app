from dash import html, dcc

def serve_layout():

    return html.Div([
                    dcc.Loading(dcc.Store(id='store'), fullscreen=True, type="dot"),
                    dcc.Upload(
                                id='upload-data',
                                children=html.Div([
                                    'Drag and Drop or ',
                                    html.A('Select a File')
                                ]),
                                style={
                                    'width': '100%',
                                    'height': '60px',
                                    'lineHeight': '60px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin': '10px',
                                    # 'backgroundColor': '#1E1E1E'
                                },
                                # Allow multiple files to be uploaded
                                multiple=False
                            ),
                    html.Div(id='after-upload-children', hidden=True,
                                children=[
                                        html.Div(id='selectors', 
                                            # style={'color': '#1E1E1E'}, 
                                            children=
                                            [
                                                html.Div(html.Label(["Select Index Column", dcc.Dropdown(id="plot-index-selection", 
                                                # style={'backgroundColor': '#1E1E1E'}
                                                # style={'width': '49%', 'display': 'inline-block'},
                                                )]),style={'width': '31%', 'display': 'inline-block'},),
                                                html.Div(html.Label(
                                                    [
                                                        "Select Columns to Plot",
                                                        dcc.Dropdown(id="plot-selection", 
                                                        # style={'backgroundColor': '#1E1E1E'}, 
                                                        # style={'width': '49%', 'display': 'inline-block'},
                                                        multi=True),
                                                    ]
                                                ),style={'width': '69%', 'display': 'inline-block'},),
                                                html.Label(
                                                    [
                                                        "Select Start/End Plot Indices: ",
                                                        dcc.Input(id="start-index", 
                                                                    # type="text", 
                                                                    debounce=True, 
                                                                    style={'marginRight':'10px', 'marginTop':'10px', }),
                                                        dcc.Input(id="end-index", 
                                                                # type="text", 
                                                                debounce=True,
                                                                style={'marginRight':'10px', 'marginTop':'10px', }),
                                                    ]
                                                )
                                            ]
                                         ),
                                        html.Div(id='chart', children=
                                                    [
                                                        dcc.Graph(id='exploration-plot', 
                                                        # config={'displayModeBar': True},
                                                        config={'displayModeBar': False}, 
                                                        animate=True)
                                                    ]
                                                ),
                                        html.Div(id='range-slider-selector', children=
                                                [dcc.RangeSlider(
                                                    id='range-slider',
                                                    # min=0,
                                                    # max=20,
                                                    # step=0.5,
                                                    # value=[5, 15]
                                                )]
                                            ),
                                        html.Div(id='output-data-upload'),

                                    ]
                            ),
                    
                    ])

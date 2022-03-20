
from dash_extensions.enrich import Output, Input, State, ServersideOutput

from _app.gen import parse_contents, find_closest
from _app.update import update_dropdown, update_marks, update_table, update_graph

from dash import callback_context
from dash.exceptions import PreventUpdate
import pandas as pd


def register_callbacks(app):
    @app.callback(ServersideOutput("store", "data"), Input('upload-data', 'contents'), 
                    [State('upload-data', 'filename'),
                State('upload-data', 'last_modified'),],
                memoize=True)
    def query_data(contents, filename, date):        
        print('query_data')
        df = parse_contents(contents, filename, date)
        return df

    @app.callback([Output('plot-index-selection', 'options'),
                Output('plot-index-selection', 'value'),
                Output('after-upload-children', 'hidden')],
                [Input("store", "data"),],)
    def update_index_selector(df):
        print('update_index_selector')
        options, value = update_dropdown(df)
        return options, value[0], False


    @app.callback([Output('plot-selection', 'options'),
                Output('plot-selection', 'value'),
                Output('range-slider', 'min'),
                Output('range-slider', 'max'),
                Output('range-slider', 'marks')
                ],
                [Input('plot-index-selection', 'value'),
                # Input("store", "data"),
                ], [State("store", "data"),
                State('plot-selection', 'value'),
                State('range-slider', 'marks')])
    def update_plot_selector(index, df, columns, marks):
        print('update_plot_selector')
        # options, value = update_dropdown(df, index=index)
        options, value = update_dropdown(df.set_index(index))
        if (columns is not None) and (set(columns) <= set(df.columns.to_list())):
            value = [col for col in columns if col != index]
        # (int(len(df[index])/4))
        marks = update_marks(df[index])
        print (marks)  
        return options, value, 0, len(df[index])-1, marks

    @app.callback([Output('range-slider', 'value'),
                Output('start-index', 'value'),
                Output('end-index', 'value')],
                [Input('range-slider', 'value'),
                Input('plot-index-selection', 'value'),
                Input('start-index', 'value'),
                Input('end-index', 'value'),
                 # Input("store", "data"),
                ], State("store", "data"),
                #   prevent_initial_call=True
                )
    def update_range_selector(slider_range, index, start_range, end_range, df):
        print('update_range_selector')
        ctx = callback_context
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        # (slider_range is not None) and 
        if (trigger_id == 'range-slider'):            
            start_range_index, end_range_index = max(0, slider_range[0]), min(len(df[index])-1, slider_range[1])            
            start_range, end_range = df[index][start_range_index], df[index][end_range_index]
        # ((start_range is not None) or (end_range is not None)) and 
        elif ((trigger_id == 'start-index') or (trigger_id == 'end-index')): 
            print(index)           
            if index in df.select_dtypes(include = ['datetime']).columns.to_list():
                print('its a datetime index')
                start_range, end_range = pd.to_datetime(start_range), pd.to_datetime(end_range)
            else:
                start_range, end_range = float(start_range), float(end_range)
            start_range, end_range = max(df[index].min(), start_range), min(df[index].max(), end_range)
            start_range_index, end_range_index = find_closest(start_range, df, index),  find_closest(end_range, df, index, return_lower=False)
            # start_range, end_range = int(start_range), int(end_range)
        # elif (not start_range) or (not end_range):
        else:
            # print('setting initial ranges')
            # intial_index_iloc = min(len(df[index])-1, 10)
            intial_index_iloc = int(len(df[index])/2.5)
            start_range, end_range = df[index][0], df[index][intial_index_iloc]
            start_range_index, end_range_index = 0, intial_index_iloc
        print(start_range_index, end_range_index)
        if end_range_index < start_range_index:
                raise PreventUpdate
        slider_range = [start_range_index, end_range_index]
        # print(trigger_id)
        # print(slider_range, start_range, end_range)

        return slider_range, start_range, end_range


    @app.callback(Output('output-data-upload', 'children'),
                [Input('range-slider', 'value'),],
                [State('plot-index-selection', 'value'),
                State("store", "data"),
                State('upload-data', 'filename'),
                ])
    def update_output(slider_range, index, df, filename):
        print('update_output')
        # df = df.loc[(df[index]>=slider_range[0]) & (df[index]<=slider_range[1])]
        df = df.loc[slider_range[0]:slider_range[1]]
        children = update_table(df, filename)
        return children


    @app.callback(Output('exploration-plot', 'figure'),
                [Input('plot-selection', 'value'),
                Input('range-slider', 'value'),
                Input('plot-index-selection', 'value'),
                 # Input("store", "data"),
                ], [State("store", "data"),
                ],)
    def update_plot(columns, slider_range, index, df):
        # if (not index) or (not columns) or (not slider_range):
        #     raise PreventUpdate
        print('update_plot')
        print(columns, index)
        if (index is not None) and (columns is not None) and (slider_range is not None):
            # df = df.loc[(df[index]>=slider_range[0]) & (df[index]<=slider_range[1])]
            df = df.loc[slider_range[0]:slider_range[1]]
            figure = update_graph(df, index, columns)
            return figure
import plotly.graph_objects as go

from dash import html, dash_table
from _app.gen import check_non_default_index, monotonic_cols_in_df, numeric_cols_in_df, datetime_strcols_in_df

def get_options(list_options):
    dict_list = []
    for i in list_options:
        dict_list.append({'label': i, 'value': i})
    return dict_list


# def update_dropdown(df, index=None):
def update_dropdown(df):
    # datetime_strcols, numeric_cols = datetime_strcols_in_df(df, return_numeric_cols=True)
    if check_non_default_index(df):
        cols = df.select_dtypes(include = ['number', 'datetime']).columns.to_list()
        # cols = [col for col in df.columns if col not in df.select_dtypes(exclude = ['number', 'datetime']).columns.to_list()] 
        # columns = numeric_cols[numeric_cols].index.to_list()
        # columns = df.columns[numeric_cols_in_df(df)]
        # value = [df.index.name]
    else:
        monotonic_cols = monotonic_cols_in_df(df)
        cols = monotonic_cols[monotonic_cols].index.to_list()
        # index_cols = datetime_strcols | (numeric_cols & monotonic_cols_in_df(df))
        # columns = index_cols[index_cols].index.to_list()
        # columns = df.columns[numeric_cols_in_df(df) & monotonic_cols_in_df(df)]
        # value = [columns[0]]

    # if index is not None:
    #     columns = df.columns[~df.columns.isin([index])]
    # else:
    #     columns = df.columns
    options = get_options(cols)
    value = [cols[0]]
    return options, value
#     return [dcc.Dropdown(id=id, multi=multi, 
#                      style={'backgroundColor': '#1E1E1E'},
# #                      className='stockselector',
#                      value=value, options=options,
#                     )]


def update_marks(index_series, n_marks=4):
    series_len = len(index_series)
    return {i:{'label':str(index_series.iloc[i]), 
            # 'style':{'transform':'rotate(-90deg)'}
            } for i in range(0, series_len) if ((i%(int(series_len/n_marks)) == 0) or (i==series_len-1))}


def update_table(df, filename):
    return html.Div([
        html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

#         html.Hr(),  # horizontal line

#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
    ])




def update_graph(df, index, columns):
    trace1 = []
    df_sub = df
    layout = go.Layout(
                #   colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                #   template='plotly_dark',
                  #   paper_bgcolor='rgba(0, 0, 0, 0)',
                #   plot_bgcolor='rgba(0, 0, 0, 0)',
                #   plot_bgcolor='#1E1E1E',
                #   paper_bgcolor='#1E1E1E',
                #   margin={'b': 15},
                  hovermode='x unified',
                #   height=650,
                  dragmode='select',
                  autosize=True,
                #   title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub[index].min(), df_sub[index].max()], 'showgrid':False},
                #   yaxis = dict(
                #                 anchor='free',
                #                 # side='left',
                #                 # overlaying='y',s
                #                 showticklabels=False,
                #                 showgrid=False,
                #                 zeroline=False,
                #                 visible=False),

              )
    for icol, column in enumerate(columns):
        yAxisName = f'yaxis{icol + 1}' if icol > 0 else 'yaxis'
        yNumber = f'y{icol+1}' if icol > 0 else 'y'
        trace1.append(go.Scattergl(x=df_sub[index],
                                    y=df_sub[column],
                                    mode='lines',
                                    opacity=0.7,
                                    name=column,
                                    yaxis=yNumber
                                    #  textposition='bottom center'
                                    ))
        if icol == 0:            
            axis_dict = dict(title=column,
                             side='left',
                             anchor='free',
                             showticklabels=False,
                             showgrid=False,
                             zeroline=False,
                             visible=False
                            )
        else:
            axis_dict = dict(title=column,
                            overlaying='y',
                            side='left',
                            anchor='free',
                            showticklabels=False,
                            showgrid=False,
                            zeroline=False,
                            visible=False
                            )
        layout[yAxisName] = axis_dict
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': layout,
              }

    return figure

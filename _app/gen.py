import base64
import io

import pandas as pd
from dash import html


def check_non_default_index(df):
    if not ((type(df.index) == pd.RangeIndex) and (df.index.name is None)):
        return True
    else:
        return False

 
def numeric_cols_in_df(df):
    numeric_cols = ~ df.apply(lambda s: pd.to_numeric(s, errors='coerce').isna().all())
    return numeric_cols


def datetime_strcols_in_df(df, return_numeric_cols=False):
    numeric_cols = numeric_cols_in_df(df)
    datetime_strcols = ~ df.loc[:, ~numeric_cols].apply(lambda s: pd.to_datetime(s, errors='coerce').isna().all())
    datetime_strcols = (~ numeric_cols ) & datetime_strcols
    if return_numeric_cols:
        return datetime_strcols, numeric_cols
    else:
        return datetime_strcols

def monotonic_cols_in_df(df):
    monotonic_cols = df.apply(lambda s: s.is_monotonic)
    return monotonic_cols


def find_closest(value, df, colname, return_lower='True'):
    if check_non_default_index(df):
        df = df.reset_index()
    exactmatch = df[df[colname] == value]
    if not exactmatch.empty:
        return exactmatch.index[0]
    elif return_lower:
        lowerneighbour_ind = df[df[colname] < value][colname].idxmax()
        return lowerneighbour_ind
    else:
        upperneighbour_ind = df[df[colname] > value][colname].idxmin()
        return upperneighbour_ind


def convert_to_numeric_datetime(df):
    datetime_strcols, numeric_cols = datetime_strcols_in_df(df, return_numeric_cols=True)
    numeric_colnames = numeric_cols[numeric_cols].index
    datetime_strcolnames = datetime_strcols[datetime_strcols].index
    df[numeric_colnames] = df[numeric_colnames].apply(lambda s: pd.to_numeric(s, errors='coerce'))
    df[datetime_strcolnames] = df[datetime_strcolnames].apply(lambda s: pd.to_datetime(s, errors='coerce'))
    return df



def parse_contents(contents, filename, date, convert_numeric_datetime=True):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    
    df = convert_to_numeric_datetime(df)
    
    return df
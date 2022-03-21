
from dash_extensions.enrich import Dash

from _app.layout import serve_layout
from _app.callback import register_callbacks


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(prevent_initial_callbacks=True, 
            external_stylesheets=external_stylesheets
            )

register_callbacks(app)

app.layout = serve_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
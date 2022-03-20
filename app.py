
from dash_extensions.enrich import Dash

from _app.layout import serve_layout
from _app.callback import register_callbacks


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]


# Server definition

app = Dash(prevent_initial_callbacks=True, 
            external_stylesheets=external_stylesheets
            )

# HEADER
# ======


# COMPONENTS
# ==========

# Your components go here.


# INTERACTION
# ===========

# Your interaction goes here.
register_callbacks(app)

# APP LAYOUT
# ==========

app.layout = serve_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
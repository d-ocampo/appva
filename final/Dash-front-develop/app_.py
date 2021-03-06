
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                # these meta_tags ensure content is scaled correctly on different devices
                # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ],
                assets_external_path='./', 
                )
app.title = 'Visual Analytics - ESPACE'

app.config.suppress_callback_exceptions=True

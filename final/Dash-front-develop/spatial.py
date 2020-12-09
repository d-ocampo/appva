import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64

# Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px
import json

from layouts import ans, cod_reg, cod_dep ,dict_base, CRN

# Data
padding_top = -430
df_comunas = pd.read_csv(
    "Data/geoplot/Pronósticos STDM.csv", sep=";", encoding="ISO-8859-1")

with open('Data/geoplot/comunas.geojson') as f:
    geojson = json.load(f)


# Spatial Model

fig_spatial = px.choropleth(df_comunas, geojson=geojson, color="Observado",
                            locations="Nombre Comuna", featureidkey="properties.NMS",  hover_name="Nombre Comuna",
                            animation_frame="Fecha",   labels="Nombre Comuna",
                            projection="mercator")
fig_spatial.update_geos(fitbounds="locations", visible=False)
fig_spatial.update_layout(margin={"r": 0, "t": 140, "l": 0, "b": 0})

fig_spatial['layout']['sliders'][0]['pad']['t'] = padding_top
fig_spatial['layout']['updatemenus'][0]['pad']['t'] = padding_top


# Bars

df_comunas = df_comunas.sort_values(by=['Pronóstico'],  ascending=False)
padding_top = -300

fig_bars = px.bar(df_comunas, x="Nombre Comuna", y="Pronóstico",
                  animation_frame="Fecha", barmode="group", color="Nombre Comuna")

fig_bars.update_layout(margin={"r": 0, "t": 140, "l": 0, "b": 0})
fig_bars['layout']['sliders'][0]['pad']['t'] = padding_top
fig_bars['layout']['updatemenus'][0]['pad']['t'] = padding_top

# lines

fig_lines = px.line(df_comunas, x="Fecha", y="Pronóstico", line_group="Nombre Comuna",
                    facet_col_wrap=3, facet_col="Nombre Comuna", width=1000, height=900, color="Nombre Comuna")


# ---------------------------------------------------------------------------- Spatial Model
spatial = html.Div([

      dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    html.H3("Cluster Analysis",
                                            className="card-title"),
 
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
            ),
        ],
    ),
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Region", "value": 0},
                                            {"label": "Department", "value": 1}
                                        ],
                                        value=0,
                                        id="cluster base",
                                        # switch=True,
                                        # className="md",
                                        style={'display': 'inline-block'}
                                    ),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": dict_base[i], "value": i} for i in dict_base.keys()
                                        ],
                                        value=0,
                                        id="cluster option",
                                        # switch=True,
                                        # className="md",
                                        style={'display': 'inline-block'}
                                    ),

                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
            ),
        ],
    ),


      dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    html.H3("Time Cluster Analysis",
                                            className="card-title"),
                                    dcc.Slider(
                                        min=min(ans),
                                        max=max(ans),
                                        step=None,
                                        marks={
                                            i: i for i in ans
                                        },
                                        value=ans[0],
                                        id='cluster slider',
                                        included=False
                                    ), 
                                    dcc.Graph(id='cluster time'),
 
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
            ),
        ],
    ),

      dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    html.H3("Zone Cluster Analysis",
                                            className="card-title"),
                                    dcc.Dropdown(
                                        clearable=False,
                                        # className="float-right",
                                        id="cluster list",
                                        style=dict(
                                            width='50%',
                                            verticalAlign="middle", 
                                            # position = "fixed",
                                            # top      = "0px",
                                            # right    = "0px"
                                        )
                                    ),
                                    dcc.Dropdown(
                                        clearable=False,
                                        # className="float-right",
                                        id="cluster ans",
                                        options=[
                                            {'label': i, 'value': i} for i in ans
                                        ],
                                        style=dict(
                                            width='50%',
                                            verticalAlign="middle", 
                                            # position = "fixed",
                                            # top      = "0px",
                                            # right    = "0px"
                                        )
                                    ),
                                    dcc.Graph(id='cluster zone'),
 
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
            ),
        ],
    ),


],
    className='container',
)


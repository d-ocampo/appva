import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64

# Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px
import json

from layouts import top_cards

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

    top_cards,

    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5("Number of Covid-19 cases per comuna",
                                            className="card-title"),
                                    dbc.Alert(
                                        "Spatial Model is a model can predict the numbers of infected people for COVID throught the time. Please select the  date to visualize.", color="info", dismissable=True,),

                                    dcc.Graph(figure=fig_spatial,
                                              id='spatial_model'),
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
                                    html.H5("Number of Covid-19 cases per comuna (Bars)",
                                            className="card-title"),
                                    dbc.Alert(
                                        " Please select the  date to visualize.", color="info", dismissable=True,),

                                    dcc.Graph(figure=fig_bars,
                                              id='spatial_model_bars'),
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
                                    html.H5("Number of Covid-19 cases per comuna  through time",
                                            className="card-title"),
                                    dbc.Alert(
                                        "The following graph shows the prediction cases by commune in a line plot.", color="info", dismissable=True,),
                                    dcc.Graph(figure=fig_lines,
                                              id='spatial_model_lines'),
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


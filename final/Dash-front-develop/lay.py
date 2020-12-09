import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
from app_ import app
from dash import callback_context as ctx


from dash.dependencies import Input, Output, State
# Data analytics library

import os
import pandas as pd
import numpy as np
import plotly.express as px
import json

# Risk Model --------------------------------------------------------------------------

# Layout definition

risk = html.Div([



    dbc.Card(

        dbc.CardBody([


            html.Iframe(width="100%", height="5500", 
  src="https://observablehq.com/embed/@jftorresp/paris-french-demographic-and-services-storyline?cell=title&cell=text1&cell=container&cell=title2&cell=text2&cell=viewof+tab&cell=title3&cell=text3&cell=graph5&cell=title4&cell=text4&cell=graph2&cell=title5&cell=text5&cell=graph1&cell=title6&cell=text6&cell=graph4&cell=title7&cell=text7&cell=codes&cell=tit&cell=text8&cell=table2&cell=title8&cell=text9&cell=graph3&cell=ape_codes", style ={"border-width": "0px"})

        ],
        ),
        outline=True,
#        ,
    ),

],
    className='container',
)

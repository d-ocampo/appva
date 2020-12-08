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


dia_fallecidos = pd.read_csv("Data/mortalidad_dia.csv")
semana_fallecidos = pd.read_csv("Data/mortalidad_semana.csv")
dia_positivos = pd.read_csv("Data/casos_positivos_dia.csv")
semana_positivos = pd.read_csv("Data/casos_positivos_semana.csv")
edad_egresos_fallecidos = pd.read_csv("Data/edad_egresos_fallecidos.csv")
sexo_egresos = pd.read_csv("Data/sexo_egresos.csv")
comor_day = pd.read_csv("Data/comorbilidades_dia.csv", delimiter = ";")
#comor_week = pd.read_csv("Data/comorbilidades_semana.csv")


# Figuras
fig_dia_fallecidos = px.line(dia_fallecidos, x="day", y="cases")
fig_dia_fallecidos_acu = px.line(dia_fallecidos, x="day", y="cases_cummulative")

fig_semana_fallecidos = px.line(semana_fallecidos, x="week", y="cases")
fig_semana_fallecidos_acu = px.line(
    semana_fallecidos, x="week", y="cases_cummulative")

fig_dia_positivos = px.line(dia_positivos, x="day", y="cases")
fig_dia_positivos_acu = px.line(dia_positivos, x="day", y="cases_cummulative")

fig_semana_positivos = px.line(semana_positivos, x="week", y="cases")
fig_semana_positivos_acu = px.line(
    semana_positivos, x="week", y="cases_cummulative")


edad_mortalidad = px.bar(edad_egresos_fallecidos,
                          x="Age", y="Identification", color="Status")

fig_edad_mortalidad = px.line(edad_egresos_fallecidos,
                          x="Age", y="Identification", color="Status")

fig_comor_day = px.line(comor_day, x="Day", y= "Diabetes")

figura3 = px.bar(sexo_egresos, x='Sex', y="Identification", color='Status')




# Risk Model --------------------------------------------------------------------------

# Layout definition

risk = html.Div([



    dbc.Card(

        dbc.CardBody([
            html.H1("Risk Of Death Predictor"),
            dbc.Alert(
                "Select comorbilities and age for calculated risk of death by COVID-19",
                id="alert-prediction-death",
                dismissable=True,
                fade=False,
                is_open=True,
                color = "primary",
            ),
        ],
        ),
        color="primary",
        outline=True,
        style={"margin": "0.5rem auto 0.75rem"},
    ),

    dbc.Card(

        dbc.CardBody([

            
            dbc.Label("Age ", html_for="slider", style = {"font-size":"24px"}),

            html.I(className="fa fa-question-circle",
                   id="tooltip-target-age",
                   style={"padding": "1rem"}, ),





            html.Div([

                dcc.Slider(id="slider-age", min=0, max=100, step=1, value=5,
                           marks={
                               0: '0',
                               5: '5',
                               10: '10',
                               15: '15',
                               20: '20',
                               25: '25',
                               30: '30',
                               35: '35',
                               40: '40',
                               45: '45',
                               50: '50',
                               55: '55',
                               60: '60',
                               65: '65',
                               70: '70',
                               75: '75',
                               80: '80',
                               85: '85',
                               90: '90',
                               95: '95',
                               100: '100'

                           }
                           ),
            ]
            ),


        ],
        ),

        color="primary",
        outline=True,
    ),

    #dbc.Button("?", )

   


    dbc.Row(
        [
            dbc.Col(

                dbc.Card(

                    dbc.CardBody([
                        dbc.FormGroup(
                            [
                                dbc.Label("Comorbidities", style = {"font-size":"24px"}),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-comorbidities",
                                       style={"padding": "1rem"}, ),
                                dbc.Checklist(
                                    options=[
                                        {"label": "Diabetes",
                                         "value": 'DIA'},
                                        {"label": "Heart disease",
                                         "value": 'EFC'},
                                        {"label": "Cancer",
                                         "value": 'CAN'},
                                        {"label": "Obesity",
                                         "value": 'OBS'},
                                        {"label": "Renal insufficiency",
                                         "value": 'IFR'},
                                    ],
                                    value=[],
                                    id="switches-input-comorbidities",
                                    switch=True,
                                ),


                            ]
                        ),
                        
                    ],
                    style = { "margin": "0.45rem 0 0"},
                    ),
                    color="primary",
                    outline=True,
                    style={"margin": "0.25rem auto 1.5rem"},
                    className = "h-100", 
                    
                ),

                className = "col-3",
                style={"padding": "0.25rem 0 0"},
                #width=3,
                #lg=3
            ),




            dbc.Col([

                    dbc.Card(
                        dbc.CardBody([

                            dbc.Label("Risk Prediction of Death", style = {"font-size":"24px"}),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-risk-death",
                                       style={"padding": "1rem"}, ),
                            dbc.Progress(id ="progress", style = {"height" : "50px", "vertical-align": "middle"}, 
                                        #  bar_style={"display":"flex", "font-size": "18px"}
                                         ),


                        ]),

                        color="primary",
                        outline=True,
                        style={"margin": "0.5rem auto 0.5rem"},


                    ),


                    dbc.Card(
                    dbc.CardBody([

                        dbc.Label("Risk Classificaction", style = {"font-size":"24px"}),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-risk-classification",
                                       style={"padding": "1rem"}, ),

                        dbc.Row([

                            dbc.Col([
                                dbc.Card(

                                    dbc.CardBody([

                                        html.I(className="fa fa-frown-o fa-2",
                                        id="tooltip-target-high-risk",
                                        style={"padding": "1rem", "font-size": "4em"}, ),

                                        html.P("High Risk: 80 - 100%", className = "mb-0", style = {"font-size": "15px"})

                                    ],
                                    className = "d-flex align-items-center",
                                    
                                ),       
                            color="danger",
                            outline=True,
                            style={"margin": "0.5rem auto 0.5rem"},

                                ),

                            ],
                            
                            ),




                            dbc.Col([

                                dbc.Card(

                                    dbc.CardBody([

                                        html.I(className="fa fa-meh-o fa-2",
                                        id="tooltip-target-meh-risk",
                                        style={"padding": "1rem", "font-size": "4em"}, ),


                                        html.P("Medium Risk: 60 - 79 %", className = "mb-0", style = {"font-size": "15px"})

                                    ],
                                    className = "d-flex align-items-center",
                                    ),

                                color="warning",
                                outline=True,
                                style={"margin": "0.5rem auto 0.5rem"},    
                                ),

                                
                                


                            ]),

                            dbc.Col([

                                dbc.Card(


                                    dbc.CardBody([

                                            html.I(className="fa fa-smile-o fa-2",
                                            id="tooltip-target-smile-risk",
                                            style={"padding": "1rem", "font-size": "4em"}, ),


                                            html.P("Low Risk: 0 - 59%", className = "mb-0", style = {"font-size": "15px"})

                                        ],
                                        className = "d-flex align-items-center",
                                    ),

                                    color="success",
                                    outline=True,
                                    style={"margin": "0.5rem auto 0.5rem"},    

                                 ),



                            ]),



                        ]),

                        dbc.Alert(
                            "Today more than ever we must stand firm and fight together to prevent the Covid-19 pandemic worldwide. Protection and quedarns at home is essential. - ILGA World",
                            id="alert-prediction-risk",
                            dismissable=True,
                            fade=False,
                            is_open=True,
                            color = "warning",
                            style = {"font-weight" : "700"}
                        ),


                    ]),

                    color="primary",
                    outline=True,
                    style={"margin": "0 auto"},


                ),





                    ],
                    #width=9,
                    #lg=9,

                    style={"padding": "0.25rem 0rem 0 0.5rem"},



                    ),


           

        ],

         style={"margin": "0.25rem 0 1.5rem"},


    ),


    dbc.Row([


        dbc.Col([


            dbc.Card(

                dbc.CardBody([

                    html.H1("Deaths for age and comorbidites "),
                        dbc.Alert(
                            "Graphs about death people per age and comorbidities throught time",
                            id="alert-prediction-death",
                            dismissable=True,
                            fade=False,
                            is_open=True,
                            color="primary",
                        ),






                    dbc.Col(

                        dbc.Card(

                            dbc.CardBody([

                                dbc.Label("Deaths per age", style = {"font-size":"24px"}),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-edad-fallecidos",
                                       style={"padding": "1rem"}, ),

                                dcc.Graph(figure=fig_edad_mortalidad,
                                        id='edad_fallecidos'),

                            ]),

                        ),

                    ),


                    dbc.Col(

                        dbc.Card(

                            dbc.CardBody([


                                dbc.Label("Deaths per comorbidites throught time", style = {"font-size":"24px"}),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-comorbidities-fallecidos",
                                       style={"padding": "1rem"}, ),


                                dcc.Graph(figure=fig_comor_day,
                                        id='comor_day'),

                            ]),

                        ),

                    ),






                ]),


                color="warning",
                outline=True,



            ),



        ]),

    ]),

    # Tooltips

    dbc.Tooltip(
        "Select your age with the slider",
        target="tooltip-target-age",
    ),

    dbc.Tooltip(
        "Select the cormobilites that you have",
        target="tooltip-target-comorbidities",
    ),

    dbc.Tooltip(
        "Probability of death by COVID-19 per comorbidities and age ",
        target="tooltip-target-risk-death",
    ),

    dbc.Tooltip(
        "Risk probability classification of death for the model",
        target="tooltip-target-risk-classification",
    ),

    dbc.Tooltip(
        "Axis y: People death and axis x: Age number",
        target="tooltip-target-edad-fallecidos",
    ),

    dbc.Tooltip(
        "Axis y: Death People and axis x: Comorbidities, It is possible select each comorbidities click-on in variable option",
        target="tooltip-target-comorbidities-fallecidos",
    ),



],
    className='container',
)

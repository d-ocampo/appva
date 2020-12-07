import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
from app_ import app
from dash import callback_context as ctx

from dash.dependencies import Input, Output, State
# Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px
import json

# CSVS

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

fig_comor_day = px.line(comor_day, x="Day", y= ["Diabetes","Cancer", "Obesity", "Heart Disease", "Renal Insufficiency"])

figura3 = px.bar(sexo_egresos, x='Sex', y="Identification", color='Status')




top_cards = dbc.Row([
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("add_alert", className="material-icons"),
                                  className="float-right rounded w-40 danger text-center "),
                        html.H5(
                            "Total Cases", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("17007"),
                    ],

                    className="pt-2 pb-2 box "
                ),
            ],
            color="danger",
            outline=True,
            #style={"width": "18rem"},
        ),
        ],
            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [

                dbc.CardBody(
                    [html.Span(html.I("mood", className="material-icons"),
                               className="float-right rounded w-40 primary text-center "),
                        html.H5(
                            "Total Recovered", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("15122"),

                     ],

                    className="pt-2 pb-2 box"
                ),
            ],
            color="success",
            outline=True,
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("error", className="material-icons"),
                                  className="float-right rounded w-40 accent text-center "),
                        html.H5(
                            "Total Actives", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("1177"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            color="info",
            outline=True,
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("local_hospital", className="material-icons"),
                                  className="float-right rounded w-40 warn text-center "),
                        html.H5(
                            "Total Deaths", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("702"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            color="warning",
            outline=True,
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),


    ],
        className="mt-1 mb-2"

    )


home = html.Div([
    dbc.Jumbotron(
        [
            html.Img(src="/assets/images/bga_rojo.png",
                     className="img-fluid")
        ], className="text-center"),


    dbc.Row(

        dbc.Col([

            html.I(className="fa fa-bars",
                   id="tooltip-target-home",
                   style={"padding": "1rem", "transform" : "rotate(90deg)", "font-size": "2rem", "color": "#999999"}, ),

            html.P('"The Coronavirus has changed the planet, modifying the way we live and the way we interact with other people. In Colombia the impact has not been made waiting, and municipalities like Bucaramanga are looking for new and better ways to face the current situation. That is why information becomes our main asset and data visualization methods, the best tool to facilitate decision-making."',
            style = { "font-color": "#666666", "font-size": "16px", "margin": "3rem auto 0", "padding": "0 12rem"}, className="text-muted"
            
            ),


            html.Hr(style = {"width" : "100px", "border": "3px solid #999999", "background-color": "#999999", "margin": "3rem auto"}),

        ],
        style = {"text-align": "center"},
        ),
    ),

    dbc.Container(
        [

            dbc.CardGroup([
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/images/dashboard.jpeg", top=True),
                        dbc.CardBody(
                            [
                                html.H3("Dashboard", style = {"color": "#66666"}),
                                html.P(
                                    "Here you can find graphs, data analysis and comments about COVID-19 in Bucaramanga City.",
                                    className="card-text", style = {"font-size": "15px"},
                                ),
                                dbc.Button(
                                    "Dashboard", color="primary", href="/page-5"),
                            ],
                            className="text-center"
                        ),
                    ],
                    style={"width": "18rem", "margin": "0 1rem 0 0"},
                ),
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/images/spatial_model.jpeg", top=True),
                        dbc.CardBody(
                            [

                                html.H3("Spatial Model", style = {"color": "#66666"}),

                                html.P(
                                    "Spatial Model is a model can predict the numbers of infected people for COVID throught the time.",
                                    className="card-text", style = {"font-size": "15px"},
                                ),
                                dbc.Button("Spatial Model",
                                           color="primary", href="/page-2"),
                            ],
                            className="text-center"
                        ),
                    ],
                    style={"width": "18rem"},
                ),

                dbc.Card(
                    [
                        dbc.CardImg(
                            src="/assets/images/risk_death.jpeg", top=True),
                        dbc.CardBody(

                            [  html.H3("Risk of Death", style = {"color": "#66666"}),

                                html.P(
                                    "Model for calculated the probability of death due to COVID-19 and their relations with comorbidities and age.",
                                    className="card-text", style = {"font-size": "15px"},
                                ),

                                dbc.Button("Risk Death Model", color="primary",
                                           href="/page-3", style={"align": "center"}),
                            ],
                            className="text-center"
                        ),
                    ],
                    style={"width": "18rem", "margin": "0 0 0 1rem"},                )

            ]),

            html.Hr(style = {"width" : "100px", "border": "3px solid #999999", "background-color": "#999999", "margin": "3rem auto"}),

            dbc.Row(


                dbc.Col(
                
               
                html.H1("PARTNERS"),
                style = {"align": "center", "color": "#66666", "margin" : "0 auto 2rem"},
                className="text-center",


                ),

            ),

            dbc.Row ([

                dbc.Col (

                    html.Img(src="/assets/images/mintic.jpeg", className="img-fluid"),
                    className = "d-flex justify-content-center align-items-center",


                ),

                dbc.Col (

                    html.Img(src="/assets/images/alcaldia_bmanga.png", className="img-fluid"),
                    className = "d-flex justify-content-center align-items-center",



                ),


                dbc.Col (

                    html.Img(src="/assets/images/correlation.jpeg", className="img-fluid"),
                    className = "d-flex justify-content-center align-items-center",



                ),

                


            ], 
            style = {"padding" : "0 0 5rem"}),
        ]

    )

])

dashboard = html.Div([

    top_cards,



    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    dbc.ButtonGroup([
                                        dbc.Button(
                                            "Daily", id="pos_daily", className="btn btn-outline b-info  text-black"),
                                        dbc.Button(
                                            "Weekly", id="pos_weekly", className="btn btn-outline b-info  text-black"),
                                    ],
                                        className="float-right d-none d-lg-flex btn-group-sm btn-group",
                                        id="but_positive"
                                    ),

                                    dbc.Checklist(
                                        options=[
                                            {"label": "Cummulative", "value": 1},
                                        ],
                                        value=[],
                                        id="pos_cum",
                                        switch=True,
                                        className="md",
                                    ),


                                    html.H5("Positive cases",
                                            className="card-title"),

                                    dcc.Graph(
                                        id='positives'),
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
                                    dbc.ButtonGroup([
                                        dbc.Button(
                                            "Daily", id="death_daily", className="btn btn-outline b-info  text-black"),
                                        dbc.Button(
                                            "Weekly", id="death_weekly", className="btn btn-outline b-info  text-black"),
                                    ],
                                        className="float-right d-none d-lg-flex btn-group-sm btn-group"
                                    ),

                                    dbc.Checklist(
                                        options=[
                                            {"label": "Cummulative", "value": 1},
                                        ],
                                        value=[],
                                        id="death_cum",
                                        switch=True,
                                        className="md",
                                    ),
                                    html.H5("Deaths",
                                            className="card-title"),
                                    dcc.Graph(
                                        figure=fig_dia_fallecidos, id='death'),
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
                                    html.H5("Number of Covid-19 cases by age",
                                            className="card-title"),

                                    dcc.Graph(figure=edad_mortalidad,
                                              id='spatial_model_lines'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3", lg="6", sm="12", md="auto"
            ),

            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5("Status by sex",
                                            className="card-title"),

                                    dcc.Graph(figure=figura3,
                                              id='spatial_model_lines'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3", lg="6", sm="12", md="auto"
            ),
        ],
    ),


],
    className='container',
)


# Risk Model --------------------------------------------------------------------------

# Layout definition

risk = html.Div([

    #Top definition 
    top_cards,
    


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
                            dbc.Progress(id ="progress", style = {"height" : "50px", "vertical-align": "middle"}, bar_style={"display":"flex", "font-size": "18px"}),


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


aboutus = html.Div([

    dbc.CardDeck([

        dbc.Card([

            html.Div([

                 dbc.CardImg(src="assets/images/profiles/Alejandro.jpeg",
                             top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                 dbc.CardBody([
                     html.H4("Alejandro Ospina",
                             className="card-title m-a-0 m-b-xs"),
                     html.Div([
                         html.A([
                                html.I(className="fa fa-linkedin"),
                                html.I(className="fa fa-linkedin cyan-600"),
                                ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/alejandro-ospina-cortés-317125158/"),

                         html.A([
                             html.I(className="fa fa-envelope"),
                             html.I(className="fa fa-envelope red-600"),
                         ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:aospinacortes@gmail.com"),

                     ], className="block clearfix m-b"),
                     html.P(
                         "Mathematician, Analytics Analyst at Accenture",
                         className="text-muted",
                     ),

                 ]

                 ),

                 ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                 dbc.CardImg(src="/assets/images/profiles/Fabian_gamboa.jpeg",
                             top=True, className="img-circle" , style = {"margin-top": "1.125rem"}),
                 dbc.CardBody([
                     html.H4("Fabian Gamboa",
                             className="card-title m-a-0 m-b-xs"),
                     html.Div([
                         html.A([
                                html.I(className="fa fa-linkedin"),
                                html.I(className="fa fa-linkedin cyan-600"),
                                ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/fabian-gamboa-01900b155"),

                         html.A([
                             html.I(className="fa fa-envelope"),
                             html.I(className="fa fa-envelope red-600"),
                         ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:fagamboas@unal.edu.co"),

                     ], className="block clearfix m-b"),
                     html.P(
                         "Economist, Campaign's Structure Analyst, Seguros Bolívar.",
                         className="text-muted",
                     ),

                 ]

                 ),

                 ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Fabian.jpeg",
                            top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                    html.H4("Fabian Pallares",
                            className="card-title m-a-0 m-b-xs"),
                    html.Div([
                        html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/fabian-pallares-jaimes-643118164/"),

                        html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:fabianpallares23@gmail.com"),

                    ], className="block clearfix m-b"),
                    html.P(
                        "Systems Engineering Student. Emphasis on Information and Management Systems",
                        className="text-muted",
                    ),

                ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Jhon.jpeg",
                            top=True, className="img-circle",  style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                    html.H4("Jhon Alexis Parra",
                             className="card-title m-a-0 m-b-xs"),
                    html.Div([
                        html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/jhon-alexis-parra-abril-0a935515a/"),

                        html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:jhalpaab@gmail.com"),

                    ], className="block clearfix m-b"),
                    html.P(
                        "MSc in Business Student, Electronic Engineer and Business Administrator.",
                        className="text-muted",
                    ),

                ]

                ),

            ],
                className="opacity_1",
            ),


        ],
            className="text-center",

        ),




    ]),
    html.Br(),
    dbc.CardDeck([

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Jimmy.jpeg",
                            top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                 html.H4("Jimmy Pulido",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                          html.I(className="fa fa-linkedin"),
                          html.I(className="fa fa-linkedin cyan-600"),
                          ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/jimmy-pulido-arias-0639411b3/"),

                     html.A([
                         html.I(className="fa fa-envelope"),
                         html.I(className="fa fa-envelope red-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:jiapulidoar@gmail.com"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Computer System Engineering Student.",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),



        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Luz.jpeg",
                            top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                 html.H4("Luz Dary Vanegas",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                            ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/luz-dary-vanegas-penagos-a8517958"),

                     html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                            ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:luzdaryvanegaspenagos@gmail.com"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Economist,  Statistician Especialist, Fraud Prevention Lead in PayU",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Wilmer.jpeg",
                            top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                 html.H4("Wilmer Pineda",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                         html.I(className="fa fa-linkedin"),
                         html.I(className="fa fa-linkedin cyan-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/wilmer-pineda-85ab7262"),

                     html.A([
                         html.I(className="fa fa-envelope"),
                         html.I(className="fa fa-envelope red-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:wpinedar@unal.edu.co"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Mathematician, MSc in Mathematics, PhD (c) in Statistics. Professor at Universidad Santo Tomás . Data Scientist at the Superintendencia de Servicios Públicos.",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([


                 dbc.CardImg(src="/assets/images/profiles/bucaramanga.jpeg",
                             top=True, style = {"margin-top": "1.125rem"}),
                 dbc.CardBody([

                     html.P(
                         "Greetings to Bucaramanga Town Hall.",
                         className="text-muted",
                     ),

                 ]

                 ),

                 ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),




    ]),


])


@app.callback(
    Output('positives', 'figure'),
    [Input('pos_daily', 'n_clicks'),
     Input('pos_weekly', 'n_clicks'), Input('pos_cum', 'value')])
def update_posfig(pos_daily, pos_weekly, pos_cum):
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if(len(pos_cum) == 1):
        if(button_id == "pos_daily"):
            return fig_dia_positivos_acu
        elif(button_id == "pos_weekly"):
            return fig_semana_positivos_acu
        return fig_dia_positivos_acu

    if(button_id == "pos_daily"):
        return fig_dia_positivos
    elif(button_id == "pos_weekly"):
        return fig_semana_positivos

    return fig_dia_positivos



@app.callback(
    Output('death', 'figure'),
    [Input('death_daily', 'n_clicks'),
     Input('death_weekly', 'n_clicks'), Input('death_cum', 'value')])
def update_deathfig(pos_daily, pos_weekly, pos_cum):
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if(len(pos_cum) == 1):
        if(button_id == "death_daily"):
            return fig_dia_fallecidos_acu
        elif(button_id == "death_weekly"):
            return fig_semana_fallecidos_acu
        return fig_dia_fallecidos_acu

    if(button_id == "death_daily"):
        return fig_dia_fallecidos
    elif(button_id == "death_weekly"):
        return fig_semana_fallecidos

    return fig_dia_fallecidos
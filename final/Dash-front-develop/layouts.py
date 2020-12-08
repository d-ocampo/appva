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


#Resources

ans=[1968, 1975, 1982, 1990, 1999, 2006, 2011, 2016]

cod_dep={
    "01":"Ain",
"02":"Aisne",
"03":"Allier",
"04":"Alpes-de-Haute-Provence",
"05":"Hautes-Alpes",
"06":"Alpes-Maritimes",
"07":"Ardèche",
"08":"Ardennes",
"09":"Ariège",
"10":"Aube",
"11":"Aude",
"12":"Aveyron",
"13":"Bouches-du-Rhône",
"14":"Calvados",
"15":"Cantal",
"16":"Charente",
"17":"Charente-Maritime",
"18":"Cher",
"19":"Corrèze",
"21":"Côte-d'Or",
"22":"Côtes-d'Armor",
"23":"Creuse",
"24":"Dordogne",
"25":"Doubs",
"26":"Drôme",
"27":"Eure",
"28":"Eure-et-Loir",
"29":"Finistère",
"2A":"Corse-du-Sud",
"2B":"Haute-Corse",
"30":"Gard",
"31":"Haute-Garonne",
"32":"Gers",
"33":"Gironde",
"34":"Hérault",
"35":"Ille-et-Vilaine",
"36":"Indre",
"37":"Indre-et-Loire",
"38":"Isère",
"39":"Jura",
"40":"Landes",
"41":"Loir-et-Cher",
"42":"Loire",
"43":"Haute-Loire",
"44":"Loire-Atlantique",
"45":"Loiret",
"46":"Lot",
"47":"Lot-et-Garonne",
"48":"Lozère",
"49":"Maine-et-Loire",
"50":"Manche",
"51":"Marne",
"52":"Haute-Marne",
"53":"Mayenne",
"54":"Meurthe-et-Moselle",
"55":"Meuse",
"56":"Morbihan",
"57":"Moselle",
"58":"Nièvre",
"59":"Nord",
"60":"Oise",
"61":"Orne",
"62":"Pas-de-Calais",
"63":"Puy-de-Dôme",
"64":"Pyrénées-Atlantiques",
"65":"Hautes-Pyrénées",
"66":"Pyrénées-Orientales",
"67":"Bas-Rhin",
"68":"Haut-Rhin",
"69":"Rhône",
"70":"Haute-Saône",
"71":"Saône-et-Loire",
"72":"Sarthe",
"73":"Savoie",
"74":"Haute-Savoie",
"75":"Paris",
"76":"Seine-Maritime",
"77":"Seine-et-Marne",
"78":"Yvelines",
"79":"Deux-Sèvres",
"80":"Somme",
"81":"Tarn",
"82":"Tarn-et-Garonne",
"83":"Var",
"84":"Vaucluse",
"85":"Vendée",
"86":"Vienne",
"87":"Haute-Vienne",
"88":"Vosges",
"89":"Yonne",
"90":"Territoire de Belfort",
"91":"Essonne",
"92":"Hauts-de-Seine",
"93":"Seine-Saint-Denis",
"94":"Val-de-Marne",
"95":"Val-d'Oise",
"971":"Guadeloupe",
"972":"Martinique",
"973":"Guyane",
"974":"La Réunion",
"FF" : "faute de frappe"
}

cod_reg={
    "01":"Guadeloupe",
    "02":"Martinique",
    "03":"Guyane",
    "04":"La Réunion",
    "11":"Île-de-France",
    "24":"Centre-Val de Loire",
    "27":"Bourgogne-Franche-Comté",
    "28":"Normandie",
    "32":"Hauts-de-France",
    "44":"Grand Est",
    "52":"Pays de la Loire",
    "53":"Bretagne",
    "75":"Nouvelle-Aquitaine",
    "76":"Occitanie",
    "84":"Auvergne-Rhône-Alpes",
    "93":"Provence-Alpes-Côte d'Azur",
    "94":"Corse",
    "FF" : "faute de frappe"
}


## Códigos de variables
cod_sexe={
    1 : "Homme",
    2 : "Femme"
    }

cod_stat={
    "A" : "Marié",
    "B" : "Non marié"
    }

cod_natio={
    "000" : "Français de naissance",
    "001" : "Français par acquisition",
    "1IT" : "Italiens",
    "1ES" : "Espagnols",
    "1PT" : "Portugais",
    "2**" : "Autres nationalités d'Europe",
    "3DZ": "Algériens",
    "3MA" : "Marocains",
    "3TN": "Tunisiens",
    "3**" : "Autres nationalités d'Afrique",
    "4TR": "Turcs",
    "***" : "Autres nationalités"
    }

cod_dipl={
    "A" : "Aucun diplôme ou au mieux BEPC - brevet des collèges ou DNB",
    "B" : "CAP - BEP",
    "C" : "Baccalauréat (général - techno - pro)",
    "D" : "Diplôme d'études supérieures",
    "*" : "Personnes de moins de 15 ans (17 ans pour le RP 1975) ou étudiants - élèves"
    }

cod_typ={
    1 : "Actifs ayant un emploi",
    2 : "Chômeurs",
    3 : "Étudiants ou élèves",
    4 : "Militaires du contingent",
    5 : "Anciens actifs",
    6 : "Autres inactifs"
    }

cod_nes={
    1 : "Agriculture",
    2 : "Industrie",
    3 : "BTP",
    4 : "Tertiaire",
    9 : "Inactifs ou chômeurs"
    }

cod_csp={
    1 : "Agriculteurs",
    2 : "Artisans-commerçants-chefs d'entreprise",
    3 : "Cadres et professions intellectuelles supérieures",
    4 : "Professions intermédiaires",
    5 : "Employés",
    6 : "Ouvriers",
    8 : "Anciens actifs",
    9 : "Inactifs et chômeurs n'ayant jamais travaillé"
    }


dict_variables={
    'SEXE' :list(cod_sexe.values()),
    'STAT_CONJ':list(cod_stat.values()),
    'NATIO':list(cod_natio.values()),
    'DIPL': list(cod_dipl.values()),
    'TYP_ACT':list(cod_typ.values()),
    'NES4':list(cod_nes.values()),
    'CSP':list(cod_csp.values())
    }


nombre_variables={
    "SEXE" : "Sexe",
    "STAT_CONJ" : "Statut conjugal",
    "NATIO" : "Nationalité regroupée",
    "DIPL" : "Diplôme regroupé",
    "TYP_ACT" : "Type d'activité (en 6 postes)",
    "NES4" : "Secteur d'activité(en 4 postes)",
    "CSP" : "Catégorie socioprofessionnelle (en 8 postes)"
}

# CSVS

ruta='Data/'

os.listdir(ruta)

data=[]
#Listar los archivos separados
for archivo in os.listdir(ruta):
    if 'RESUMEN' in archivo:
        data.append(archivo)

#Resúmen de región
RN=pd.read_csv(ruta+data[1],sep=';')
RRE=pd.read_csv(ruta+data[0],sep=';')
RT=pd.read_csv(ruta+data[2],sep=';')
RRA=pd.read_csv(ruta+data[3],sep=';')


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




top_cards = dbc.Row([
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        # html.Span(html.I("add_alert", className="material-icons"),
                        #           className="float-right rounded w-40 danger text-center "),
                        html.H5(
                            "Year of census", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4(id="year census"),
                    ],

                    className="pt-2 pb-2 box "
                ),
            ],
            # color="danger",
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
                        html.H5(
                            "Total Population of France", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4(id="total population"),

                     ],

                    className="pt-2 pb-2 box"
                ),
            ],
            # color="success",
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
                        html.H5(
                            "Place", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4(id="place"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            # color="info",
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
                        html.H5(
                            "Name", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4(id="name of place"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            # color="warning",
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
            html.Img(src="/assets/images/francebanner.webp",
                     className="img-fluid")
        ], className="text-center"),


    dbc.Row(

        dbc.Col([
#banner del home
            html.I(className="fa fa-bars",
                   id="tooltip-target-home",
                   style={"padding": "1rem", "transform" : "rotate(90deg)", "font-size": "2rem", "color": "#999999"}, ),
# Descripción del problema
            html.P('''
                   Fast changes in population causes many issues for municipalities to fulfill inhabitants 
                   needs. Municipalities evolve, increasing or decreasing population and services. 
                   Stakeholders need to foresight demographic evolution to conceive public policies. 
                   They could face new problems that other municipalities have already resolved in the past,
                   but data about their evolution is often sparse and incomplete. In France consistent census
                   data is available, but tools for analyzing demographic data series are rare. We propose a 
                   visual tool for municipalities, which helps stakeholders to have a look on the trajectories followed 
                   by other municipalities and find the ones that have, or had in the past, a similar development, to 
                   understand their future evolution. In order to compare different French municipalities, we consider 
                   harmonized historical census data from 1968 to 2016. This visual tool should give the possibility to 
                   choose different multivariate comparison methods for data series.
                   ''',
            style = { "font-color": "#666666", "font-size": "16px", "margin": "1rem auto 0", "padding": "0 12rem"}, className="text-muted"
            
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
                                    '''Here you can find graphs, data analysis and comments about 
                                    france census during 1968 and 2016
                                    
                                    ''',
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
                                    '''Cluster Model is a model that groups the municipalities of France by euclidean distance
                                    of similarity during the years of the census''',
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

                # dbc.Card(
                #     [
                #         dbc.CardImg(
                #             src="/assets/images/risk_death.jpeg", top=True),
                #         dbc.CardBody(

                #             [  html.H3("Risk of Death", style = {"color": "#66666"}),

                #                 html.P(
                #                     "Model for calculated the probability of death due to COVID-19 and their relations with comorbidities and age.",
                #                     className="card-text", style = {"font-size": "15px"},
                #                 ),

                #                 dbc.Button("Risk Death Model", color="primary",
                #                            href="/page-3", style={"align": "center"}),
                #             ],
                #             className="text-center"
                #         ),
                #     ],
                #     style={"width": "18rem", "margin": "0 0 0 1rem"},                
                #     )

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

                    html.Img(src="/assets/images/uniandes.png", className="img-fluid"),
                    className = "d-flex justify-content-center align-items-center",


                ),

                dbc.Col (

                    html.Img(src="/assets/images/unicote.png", className="img-fluid"),
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

                                    dcc.Dropdown(
                                        clearable=False,
                                        # className="float-right",
                                        id="name list",
                                        style=dict(
                                            width='50%',
                                            verticalAlign="middle", 
                                            # position = "fixed",
                                            # top      = "0px",
                                            # right    = "0px"
                                        )
                                    ),

                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Region", "value": 1},
                                            {"label": "Department", "value": 0}
                                        ],
                                        value=0,
                                        id="base select",
                                        # switch=True,
                                        className="md",
                                    ),
                                    dcc.Slider(
                                        min=min(ans),
                                        max=max(ans),
                                        step=None,
                                        marks={
                                            i: i for i in ans
                                        },
                                        value=ans[0],
                                        id='dash slider'
                                    ),  

                                    html.H5("Drill down analysis",
                                            className="card-title"),

                                    dcc.Graph(
                                        id='dash drill'),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": nombre_variables[i], "value": i} for i in nombre_variables.keys()
                                        ],
                                        value="SEXE",
                                        id="variable",
                                        # switch=True,
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
                                    html.H5("Regions Analysis",
                                            className="card-title"),

                                    dcc.Graph(figure=edad_mortalidad,
                                              id='dash region'),
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
                                    html.H5("Time Analysis",
                                            className="card-title"),

                                    dcc.Graph(figure=figura3,
                                              id='dash time'),
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




aboutus = html.Div([

    dbc.CardDeck([

        dbc.Card([

            html.Div([

                 dbc.CardImg(src="assets/images/profiles/ocampo.jpeg",
                             top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                 dbc.CardBody([
                     html.H4("David Ocampo",
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

                 dbc.CardImg(src="/assets/images/profiles/juan.jpeg",
                             top=True, className="img-circle" , style = {"margin-top": "1.125rem"}),
                 dbc.CardBody([
                     html.H4("Juan Felipe Torres",
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

                dbc.CardImg(src="/assets/images/profiles/quinonez.jpeg",
                            top=True, className="img-circle", style = {"margin-top": "1.125rem"}),
                dbc.CardBody([
                    html.H4("Juan David Quiñonez",
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
                        "Statistician",
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


# @app.callback(
#     Output('positives', 'figure'),
#     [Input('pos_daily', 'n_clicks'),
#      Input('pos_weekly', 'n_clicks'), Input('base select', 'value')])
# def update_posfig(pos_daily, pos_weekly, base select):
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]

#     if(len(base select) == 1):
#         if(button_id == "pos_daily"):
#             return fig_dia_positivos_acu
#         elif(button_id == "pos_weekly"):
#             return fig_semana_positivos_acu
#         return fig_dia_positivos_acu

#     if(button_id == "pos_daily"):
#         return fig_dia_positivos
#     elif(button_id == "pos_weekly"):
#         return fig_semana_positivos

#     return fig_dia_positivos



# @app.callback(
#     Output('death', 'figure'),
#     [Input('death_daily', 'n_clicks'),
#      Input('death_weekly', 'n_clicks'), Input('death_cum', 'value')])
# def update_deathfig(pos_daily, pos_weekly, base select):
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]

#     if(len(base select) == 1):
#         if(button_id == "death_daily"):
#             return fig_dia_fallecidos_acu
#         elif(button_id == "death_weekly"):
#             return fig_semana_fallecidos_acu
#         return fig_dia_fallecidos_acu

#     if(button_id == "death_daily"):
#         return fig_dia_fallecidos
#     elif(button_id == "death_weekly"):
#         return fig_semana_fallecidos

#     return fig_dia_fallecidos
from layouts import home, dashboard, aboutus, risk, RN, RRE, RT, RRA

from app_ import app
from spatial import spatial
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import math

##Graph libraries
import plotly.express as px
import plotly.graph_objects as go


server = app.server

# Resources

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


# end resources


# Top bar
top_navbar = dbc.Navbar(
    [
        #Nombre de cada página, 
        dbc.NavbarBrand(["Visual Analytics"],
                        id="top_title", className="ml-2 wd"),

    ],
    color="white",
    sticky="top",
    id="topBar",
    style={'z-index': 1}
)

# end top bar

sidebar_header = dbc.Row(
    [
        dbc.Col(

            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col([html.Img(src="/assets/images/uniandes.png",
                                         className="img-fluid w-50 text-center w-75 pt-5")], className="text-center"),
                       
                        dbc.Col([html.Img(src="/assets/images/unicote.png",
                                         className="img-fluid w-50 text-center w-75 pt-5")], className="text-center"),                    
                        ],
                    align="center",
                    no_gutters=True,
                    className="justify-content-center"
                ),
                href="#",

            ),
            
        ),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(255,255,255,.5)",
                    "border-color": "rgba(255,255,255,.1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="rigth",
        ),
    ]
)

sidebar = dbc.Navbar([html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be

        dbc.Collapse(
            dbc.Nav(
                [

             
                    dbc.NavLink( [  html.Span(html.I("home", className="material-icons"),
                                           className="nav-icon"),  html.Span("Home", className="nav-text") 
                                           ], href="/", id="page-1-link", className="nav-header"),

                    dbc.NavLink([html.Span(html.I("dashboard", className="material-icons"),
                                           className="nav-icon"),  html.Span("Dashboard", className="nav-text")
                                           ], href="/page-5", id="page-5-link", className="nav-header"),

                     dbc.NavLink([html.Span(html.I("map", className="material-icons"),
                                           className="nav-icon"),  html.Span("Cluster Model", className="nav-text")
                                           ], href="/page-2", id="page-2-link", className="nav-header"),

                    #  dbc.NavLink([html.Span(html.I("favorite", className="material-icons"),
                    #                        className="nav-icon"),  html.Span("Risk of death", className="nav-text")
                    #                        ], href="/page-3", id="page-3-link", className="nav-header"),


                    dbc.NavLink([html.Span(html.I("supervisor_account", className="material-icons"),
                                           className="nav-icon"),  html.Span("About us", className="nav-text")
                                           ], href="/page-4", id="page-4-link", className="nav-header"),

                     ],
                vertical=True,
                navbar=True
            ),
            id="collapse",
        ),
    ],

),

],
    color="#d7af60",
    dark=True,
    id="sidebar",
    className="mm-show",
)

content = html.Div(id="page-content")
content2 = html.Div([top_navbar,  content], id="content")
app.layout = html.Div([dcc.Location(id="url"),  sidebar, content2])


# fin Navbar

## Modelo de riesgo según enfermedad
@app.callback(
    [dash.dependencies.Output('progress', 'value'),
    dash.dependencies.Output('progress', 'children')],
    [dash.dependencies.Input('slider-age', 'value'),
    dash.dependencies.Input('switches-input-comorbidities', 'value'),
    ])
def update_output(slider, switches):
    diabetes = 0
    heart_disasse = 0
    cancer = 0
    obesity = 0
    renal= 0

    if "DIA" in switches:
        diabetes = 1
    if "EFC" in switches:
        heart_disasse = 1
    if "CAN" in switches:
        cancer = 1
    if "OBS" in switches:
        obesity = 1
    if "IFR" in switches:
        renal = 1

    probability = 1 / (1 + (math.e ** (-(-2.0283 + (0.0804*(slider-70)) + (0.6025*diabetes) + (0.8621*cancer) + (1.4573*obesity) + (1.3140*renal) + (1.3140*heart_disasse)))))
    probability = round(probability * 100) 

    return probability, f"{probability } %" if probability  >= 5 else ""


# Establecer ruta de las páginas
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return home
    elif pathname == "/page-5":
        return dashboard
    elif pathname == "/page-2":
        return spatial
    elif pathname == "/page-3":
        return risk
    elif pathname == "/page-4":
        return aboutus
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output("top_title", "children"), [Input("url", "pathname")])
def update_topTitle(pathname):
    if pathname in ["/", "/home"]:
        return "Paris - French demographic and services storyline"
    elif pathname == "/page-5":
        return "Dashboard"
    elif pathname == "/page-2":
        return "Cluster Model"
    elif pathname == "/page-3":
        return "Risk of Death"
    elif pathname == "/page-4":
        return "About us"



##############################################
#### Visual Analytics ########################
##############################################


###### Dash Board ################

#Cambiar el valor de las tarjetas - lugar 
@app.callback(
    Output("place", "children"),
    [Input("base select", "value")],
)
def place(value):
    if value==1:
        return "Region"
    else: 
        return "Department"


#Cambiar el valor del dropdown 
@app.callback(
    Output("name list", "options"),
    [Input("base select", "value")],
)
def list_names(value):
    if value==1:
        return [{'label': cod_reg[i], 'value': i} for i in cod_reg.keys()]
    else: 
        return [{'label': cod_dep[i], 'value': i} for i in cod_dep.keys()] 

#Cambiar el nombre de la tarjeta 
@app.callback(
    Output("name of place", "children"),
    [Input("name list", "value"),
     Input("base select", "value"),],
)
def list_names(value,terrain):
    if terrain==1:
        return cod_reg[value]
    else: 
        return cod_dep[value]
    
#Cambiar el nombre de la tarjeta de año 
@app.callback(
    Output("year census", "children"),
    [Input("dash slider", "value")],
)
def list_names(value):
    return value

# Gráfico de drill down en el dash board

@app.callback(
    Output("dash drill", "figure"),
    [Input("dash slider", "value"),
     Input("base select", "value"),
     Input("name list", "value")
     ],
)
def list_names(year, base,terreno):
    prueba=RN[RN['ANS']==int(year)]
    # print(year,base,terreno,len(prueba))
 
    var='SEXE'
    if base==1:
        x=dict_variables[var]
        y=prueba[prueba['REGION']==cod_reg[terreno]][dict_variables[var]].values.tolist()[0]
    print(x,y)
    fig = go.Figure([go.Bar(x=x, y=y)])
    return fig



if __name__ == "__main__":
    app.run_server(debug=False)
    

# Images etc

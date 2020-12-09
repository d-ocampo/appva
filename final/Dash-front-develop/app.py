from layouts import home, dashboard, aboutus,  RN, RRE, RT, RRA, dict_variables,cod_dep, cod_reg,cod_csp,cod_dep,cod_dipl,cod_natio,cod_nes,cod_reg,cod_sexe, cod_stat,cod_typ, dict_variables,nombre_variables,dict_base,nombre_variables, seleccion_base
from lay import  risk

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

                     dbc.NavLink([html.Span(html.I("favorite", className="material-icons"),
                                           className="nav-icon"),  html.Span("Exploration", className="nav-text")
                                           ], href="/page-3", id="page-3-link", className="nav-header"),


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
    if value==0:
        return "Region"
    else: 
        return "Department"


#Cambiar el valor del dropdown 
@app.callback(
    Output("name list", "options"),
    [Input("base select", "value")],
)
def list_names(value):
    if value==0:
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
    if terrain==0:
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
    [Output("dash drill", "figure"),
     Output("total population", "children")],
    [Input("dash slider", "value"),
     Input("base select", "value"),
     Input("name list", "value"),
     Input("variable", "value"),
     Input("option select", "value")
     ],
)
def bar_graph(year, base,terreno,var,opcion):
    df=seleccion_base(int(base),int(opcion))
    prueba=df[df['ANS']==int(year)]
    # print(year,base,terreno,len(prueba))
    total=round(prueba[dict_variables["SEXE"]].sum().sum())
    total="{:,}".format(int(total))
    print(year, base,terreno,var,opcion)
    # print(cod_dep[terreno])
    if int(base)==0:
        x=dict_variables[var]
        y=prueba[prueba['REGION']==cod_reg[terreno]][dict_variables[var]].values.tolist()[0]
    else:
        x=dict_variables[var]
        y=prueba[prueba['REGION']==cod_dep[terreno]][dict_variables[var]].values.tolist()[0]
    fig = go.Figure([go.Bar(x=x, y=y)])
    return fig, total


#Gráfico de comparación de región

@app.callback(
    Output("dash region", "figure"),
    [Input("dash slider", "value"),
     Input("base select", "value"),
     Input("name list", "value"),
     Input("variable", "value"),
     Input("option select", "value")
     ],
)
def region_graph(year, base,terreno,var,opcion):
    df=seleccion_base(int(base),int(opcion))
    prueba=df[dict_variables[var]+['ANS','REGION']]
    prueba=prueba[prueba['ANS']==int(year)]
    fig = px.bar(prueba, y=dict_variables[var], x='REGION')
    return fig

#Gráfico de línea de tiempo

@app.callback(
    Output("dash time", "figure"),
    [Input("dash slider", "value"),
     Input("base select", "value"),
     Input("name list", "value"),
     Input("variable", "value"),
     Input("option select", "value")
     ],
)
def time_graph(year, base,terreno,var,opcion):
    df=seleccion_base(int(base),int(opcion))
    if int(base)==0:
        fig = px.line(df[df['REGION']==cod_reg[terreno]].sort_values(by=['ANS']), x="ANS", y=dict_variables[var])
    else:
        fig = px.line(df[df['REGION']==cod_dep[terreno]].sort_values(by=['ANS']), x="ANS", y=dict_variables[var])      
    return fig

#Cambiar nombre de la selección de la base
@app.callback(
    Output("seleccion analisis", "children"),
    [Input("base select", "value"),
     Input("option select", "value")
     ],
)
def analysis_name(base,opcion):
    if int(base)==0:
        text='Analysis of "Region de '+ dict_base[opcion]+'"'
    else:
        text='Analysis of "Deparment de '+ dict_base[opcion]+'"'      
    return text







if __name__ == "__main__":
    app.run_server(debug=False)
    

# Images etc

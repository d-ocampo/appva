import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)
server = app.server


app.layout = html.Div([
    # Banner display
    html.Div([
    ],
        className="banner"
    ),

    # Body
    html.Div([
        html.H2('Contexto'),
        html.P('''
               El Sistema General de Regalías
               está basado en el principio de descentralización y de autonomía de las entidades 
               territoriales, que busca una distribución más equitativa, garantizando el uso 
               de los recursos con eficiencia y probidad
               '''),
        html.P('''
               Este visualizador está basado en la información que concierne a la distribución
               de valores girados a los diferentes Departamentos, Entidades y Rubros a los que se les
               asignó recursos durante el año 2020            
               '''),
        html.A('Para más información del Sistema General de Regalías (SGR), click acá',
               href='http://www.eiticolombia.gov.co/es/informes-eiti/informe-2016/distribucion-y-seguimiento-de-ingresos/sistema-general-de-regalias-sgr/',
               style={'text-align':'left'}),
        html.H2('Análisis'),
        html.P('''
               En la base de datos que corresponde a la distribución de las regalías se encuentran variables 
               que permiten identificar a dónde se han generado los pagos, estas incluyen el rubro, 
               la entidad y el departamento
               '''),
        html.P('''
               Para el análisis se tomaron 60.160 registros que corresponden a todos los giros realizados durante 
               el año 2020 y que cuenta con la información de: CodigoDepartamento, NombreDepartamento, FechaGiro, NumeroGiro,
               IdentificacionEntidad, NombreEntidad, Rubro, ValorNetoGiroSGR,
               ValorPagadoGiroSGR, en las cuales se pretende establecer en qué se gastaron 3.9 billones de pesos del SGR, para esto
               se realizó el análisis sobre 34 registros de Departamento, 1.028 entidades, y 3.841 rubros declarados
               '''),
        html.P('''
               En el tratamiento de datos se estandarizaron los tipos de rubros según en el nombre, los rubros que presentaban
               una recurrencia menor a 29 ejecuciones se estableció como otro tipo de rubro por no ser tan recurrente. Para las
               diferentes entidades se estableció el tipo de entidad (Agencia,Municipio, etc...) para entender mejor el gasto en 
               estas 
               '''),
        html.H2('Enfoque Visualization Analysis & Design'),
        html.H4('¿What?'),
        html.Li('Tipos de Datos: Los items son las entidades y departamentos del SGR, y los atributos las variables que conciernen a la información financiera de pagos de estos'),       
        html.Li('Tipos de Dataset: El tipo de datos es una tabla en el que se contienen los items y atributos mencionados anteriormente'),
        html.Li('Disponibilidad de datos: A pesar de que los datos se encuentran disponbles a descarga y aparentemente son estáticos, el SGR funciona todo el año y la base se debe estar alimentando por lo tanto es dinámica'),
        html.H4('¿Why?'),
        html.Li('Consumir: Se realizó un descubrimiento de información obteniendo los resumenes más importantes de la data a consultar'),
        html.Li('Buscar: Al no conocer el objetivo pero sí la ubicación de los datos se hizo un proceso de observación de la información'),
        html.Li('Consultar: Se realizaron comparaciones frente a los diferentes actores a analizar, así como se resumió información vital para la investigación como lo fue la suma de valores girados'), 
        html.H4('¿How?'),
        html.Li('Arreglar: Para realizar una idea concreta y poder analizar los diferentes actores involucrados en el SGR fue necesario separar los datos como se menciona en el párrafo de análisis'),
        html.Li('Manipular: La data tuvo que ser transformada para una mejor interpretación y realizar análisis más concretos como en el caso de los rubos y el tipo de entidad'),
        html.Li('Reducir: Se debió realizar agregación por entidad y departamento para establecer dónde estaban los recursos destinados del SGR'),
 

    ],
        className="content",
    )


])


external_css = [
    # "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",  # Normalize the CSS
    # "https://fonts.googleapis.com/css?family=Open+Sans|Roboto"  # Fonts
    # "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    # "https://cdn.rawgit.com/xhlulu/0acba79000a3fd1e6f552ed82edb8a64/raw/dash_template.css"  # For production
]

for css in external_css:
    app.css.append_css({"external_url": css})

# Running the server
if __name__ == '__main__':
    app.run_server(debug=False,host='0.0.0.0')

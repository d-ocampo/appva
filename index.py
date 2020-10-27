import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import plotly.express as px

import pandas as pd
import os
import numpy as np

from assets.figs import figuras , figuras_dep

# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

#ruta de ejecución
path=os.getcwd()

#establecer archivos de clusters
clusters=[]
for i in os.listdir(path+'/assets/data/'):
    if 'cluster' in i:
        clusters.append(i)
        

#crear data sets completo y por departamento y región 
data=pd.DataFrame()
data_dep=pd.DataFrame()
data_reg=pd.DataFrame()
for i in range(len(clusters)):
    df=pd.read_csv(path+'/assets/data/'+clusters[i],sep=';')
    df['entidad']=clusters[i].split('cluster_')[1][:-4]
    df['ANS']=df['ID'].apply(lambda x: x.split('-')[0])
    data=data.append(df)
    if 'DEP' in clusters[i]:
        df['DEP']=df['ID'].apply(lambda x: x.split('-')[1])
        data_dep=data_dep.append(df)
    else:
        df['REG']=df['ID'].apply(lambda x: x.split('-')[1])
        data_reg=data_reg.append(df)
# diccionario de variables de francia
dep_nombres=pd.read_excel(path+'/assets/data/Diccionario Variables France.xlsx',
                          sheet_name='Departamentos')
dep_nombres.ID = dep_nombres.ID.astype('str')

#diccionario de regiones de francia
reg_nombres=pd.read_excel(path+'/assets/data/Diccionario Variables France.xlsx',
                          sheet_name='Region')
reg_nombres.ID = reg_nombres.ID.astype('str')


def departamento(codigo):
    dep=dep_nombres[dep_nombres['ID']==codigo]['Departamento']
    try:
        indice=dep.index.to_list()[0]
        return dep[indice]
    except:
        return 'S/C'
    
def region(codigo):
    dep=reg_nombres[reg_nombres['ID']==codigo]['Region']
    try:
        indice=dep.index.to_list()[0]
        return dep[indice]
    except:
        return 'S/C'
    
    
data_dep['Departamento']=data_dep['DEP'].apply(lambda x: departamento(x))

    
data_reg['Region']=data_reg['REG'].apply(lambda x: region(x))

variables=[]
for i in data_dep.columns:
    if '_' in i:
        value='_'.join(i.split('_')[:-1])
        variables.append(value)

variables=unique(variables)

var_nombres=pd.read_excel(path+'/assets/data/Varmod_RP19682016_Esp.xlsx',
                          sheet_name='Esp')

def varfr(codigo):
    vn=var_nombres[var_nombres['VAR']==codigo]['VARFR']
    indice=vn.index.to_list()[0]
    return vn[indice]


variables.remove('AGE')
entidades=list(data_dep.entidad.unique())
deps=list(data_dep.Departamento.unique())



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
        dcc.RadioItems(
            id='check',
            options=[{'label': varfr(i), 'value': i} for i in entidades],
            value=entidades[0],
            labelStyle={'display': 'inline-block'}
        ),  
        dcc.Dropdown(
            id='drop',
            options=[{'label': varfr(i), 'value': i} for i in variables],
            value=variables[0],
            clearable=False
        ),  
        dcc.Graph(id='graph-bar'),
        dcc.Dropdown(
            id='drop-dep',
            options=[{'label': i, 'value': i} for i in deps],
            value=deps[15],
            clearable=False        
        ),
        dcc.Graph(id='graph-bar-dep'),
        html.H3('Clusters'),
        dcc.Graph(id='graph-clusters',
                  figure=px.parallel_categories(data_reg, dimensions=['CLUSTER', 'Region','ANS'])
        ),  
        html.H3('ObservableHQ'),
        html.Iframe(src=app.get_asset_url("prueba.html"), width = 900, height = 450),
    ],
        className="content",
    )
])

#actualizar gráfico
@app.callback(
    dash.dependencies.Output('graph-bar', 'figure'),
    [dash.dependencies.Input('check', 'value'),
     dash.dependencies.Input('drop', 'value')])
def update_output(entidad, variable):
    fig =figuras(data_dep,entidad,variable)
    return fig

#actualizar gráfico
@app.callback(
    dash.dependencies.Output('graph-bar-dep', 'figure'),
    [dash.dependencies.Input('check', 'value'),
     dash.dependencies.Input('drop', 'value'),
     dash.dependencies.Input('drop-dep', 'value')])
def update_output(entidad, variable,departamento):
    fig =figuras_dep(data_dep,departamento,entidad,variable)
    return fig


# Running the server
if __name__ == '__main__':
   app.run_server(host='0.0.0.0', port=8051)
	# app.run_server(debug=True)


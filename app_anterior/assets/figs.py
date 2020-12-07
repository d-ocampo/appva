#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 03:55:39 2020

@author: davidsaw
"""
import plotly.graph_objs as go

def figuras(data_dep,entidad, variable):
    
    df=data_dep[data_dep['entidad']==entidad]
    varfig=[]
    for i in df.columns:
        if variable in i:
            varfig.append(i)
            
    fig = go.Figure(data=go.Scatter(x=df['ANS'],
                                    y=df[varfig[0]],
                                    mode='markers',
                                    text=df['Departamento'],
                                    name=varfig[0].split('_')[-1]))
    fig.add_trace(go.Scatter(x=df['ANS'],
                            y=df[varfig[1]],
                            mode='markers',
                            text=df['Departamento'],
                            name=varfig[1].split('_')[-1]))
    
    
    if len(varfig)>2:
        for i in range(2,len(varfig)-1):
            fig.add_trace(go.Scatter(x=df['ANS'],
                                        y=df[varfig[i]],
                                        mode='markers',
                                        text=df['Departamento'],
                                        name=varfig[i].split('_')[-1]))
               
    return fig


def figuras_dep(data_dep,departamento,entidad, variable):
    
    df=data_dep[data_dep['entidad']==entidad]
    df=df[df['Departamento']==departamento]
    
    varfig=[]
    for i in df.columns:
        if variable in i:
            varfig.append(i)
            
    fig = go.Figure(data=go.Scatter(x=df['ANS'],
                                    y=df[varfig[0]],
                                    mode='lines',
                                    text=df['Departamento'],
                                    name=varfig[0].split('_')[-1]))
    fig.add_trace(go.Scatter(x=df['ANS'],
                            y=df[varfig[1]],
                            mode='lines',
                            text=df['Departamento'],
                            name=varfig[1].split('_')[-1]))
    
    
    if len(varfig)>2:
        for i in range(2,len(varfig)-1):
            fig.add_trace(go.Scatter(x=df['ANS'],
                                        y=df[varfig[i]],
                                        mode='lines',
                                        text=df['Departamento'],
                                        name=varfig[i].split('_')[-1]))
               
    return fig






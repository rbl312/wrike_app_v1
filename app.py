# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import data
from plotly.graph_objs import *

def get_pillar():
    '''Returns the list of divisions that are stored in the database'''
    pillars = list(data.L1['pillar_title'].sort_values(axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last').unique())
    return pillars

def onLoad_pillar_options():
    '''Actions to perform upon initial page load'''

    pillar_options = (
        [{'label': pillar, 'value': pillar}
        for pillar in get_pillar()]
        )
    return pillar_options


def plot_graph(df, idx, col, val, g_title, sp):

    if sp == 'NA':
        pass
    else:
        df = df[df['pillar_title'] == sp]

    pv1 = pd.pivot_table(df, index=[idx], columns=[col], values=[val], aggfunc='count', fill_value=0)
    
    if('Completed' not in pv1['id']):
        pv1['id','Completed'] = 0

    if('Delayed' not in pv1['id']):
        pv1['id','Delayed'] = 0

    if('On Hold' not in pv1['id']):
        pv1['id','On Hold'] = 0

    if('Requested' not in pv1['id']):
        pv1['id','Requested'] = 0

    if('Work In Progress' not in pv1['id']):
        pv1['id','Work In Progress'] = 0

    if('Future' not in pv1['id']):
        pv1['id','Future'] = 0

    if('Rejected' not in pv1['id']):
        pv1['id','Rejected'] = 0

    trace1 = go.Bar(x=pv1.index, y=pv1[(val, 'Completed')], name='Completed',marker=Marker(color='rgb(33,150,243)'))
    trace2 = go.Bar(x=pv1.index, y=pv1[(val, 'Delayed')], name='Delayed',marker=Marker(color='rgb(233,30,99)'))
    trace3 = go.Bar(x=pv1.index, y=pv1[(val, 'On Hold')], name='On Hold',marker=Marker(color='rgb(158,158,158)'))
    trace4 = go.Bar(x=pv1.index, y=pv1[(val, 'Requested')], name='Requested',marker=Marker(color='rgb(158,158,158)'))
    trace5 = go.Bar(x=pv1.index, y=pv1[(val, 'Work In Progress')], name='Work In Progress',marker=Marker(color='rgb(255,152,0)'))
    trace6 = go.Bar(x=pv1.index, y=pv1[(val, 'Future')], name='Future',marker=Marker(color='rgb(63,81,181)'))
    trace7 = go.Bar(x=pv1.index, y=pv1[(val, 'Rejected')], name='Rejected',marker=Marker(color='rgb(121,85,72)'))

    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
    layout = go.Layout(title=g_title,  font=dict(family='Helvetica', size=12, color='rgb(0,80,115)'), 
    barmode='stack', height=800,
            yaxis=dict(
                        autotick=False,
                        ticks='outside',
                        tick0=0,
                        dtick=10,
                        ticklen=8,
                        tickwidth=1,
                        tickcolor='#000'
                        ))

    return go.Figure(data=data, layout=layout)



def plot_user_graph(df, idx, col, val, g_title, sp):

    if sp == 'NA':
        pass
    else:
        df = df[df['pillar_title'] == sp]

    pv1 = pd.pivot_table(df, index=[idx], columns=[col], values=[val], aggfunc='count', fill_value=0)

    if('Rizen Yamauchi' not in pv1['id']):
        pv1['id','Rizen Yamauchi'] = 0

    if('Abhishek Pradhan Shrestha' not in pv1['id']):
        pv1['id','Abhishek Pradhan Shrestha'] = 0

    if('Ritika Lohadiya' not in pv1['id']):
        pv1['id','Ritika Lohadiya'] = 0

    if('Matthew Danna' not in pv1['id']):
        pv1['id','Matthew Danna'] = 0

    if('Nicole Arra' not in pv1['id']):
        pv1['id','Nicole Arra'] = 0

    if('Batul Arsiwala' not in pv1['id']):
        pv1['id','Batul Arsiwala'] = 0

    if('Ryan Lund' not in pv1['id']):
        pv1['id','Ryan Lund'] = 0


    if('Reshmi Vaidhyanathan' not in pv1['id']):
        pv1['id','Reshmi Vaidhyanathan'] = 0

    if('Jack Xia' not in pv1['id']):
        pv1['id','Jack Xia'] = 0

    if('John Fegan' not in pv1['id']):
        pv1['id','John Fegan'] = 0

    if('Cameron Petersen' not in pv1['id']):
        pv1['id','Cameron Petersen'] = 0

    if('Myrna Alba' not in pv1['id']):
        pv1['id','Myrna Alba'] = 0


    trace11 = go.Bar(x=pv1.index, y=pv1[('id', 'Rizen Yamauchi')], name='Rizen Yamauchi',marker=Marker(color='rgb(240,98,146)'))
    trace21 = go.Bar(x=pv1.index, y=pv1[('id', 'Abhishek Pradhan Shrestha')], name='Abhishek Pradhan Shrestha',marker=Marker(color='rgb(186,104,200)'))
    trace31 = go.Bar(x=pv1.index, y=pv1[('id', 'Ritika Lohadiya')], name='Ritika Lohadiya',marker=Marker(color='rgb(192,202,51)'))
    trace41 = go.Bar(x=pv1.index, y=pv1[('id', 'Matthew Danna')], name='Matthew Danna',marker=Marker(color='rgb(251,192,45)'))
    trace51 = go.Bar(x=pv1.index, y=pv1[('id', 'Nicole Arra')], name='Nicole Arra',marker=Marker(color='rgb(121,134,203)'))
    trace61 = go.Bar(x=pv1.index, y=pv1[('id', 'Batul Arsiwala')], name='Batul Arsiwala',marker=Marker(color='rgb(77,182,172)'))
    trace71 = go.Bar(x=pv1.index, y=pv1[('id', 'Ryan Lund')], name='Ryan Lund',marker=Marker(color='rgb(67,160,71)'))

    trace81 = go.Bar(x=pv1.index, y=pv1[('id', 'Reshmi Vaidhyanathan')], name='Reshmi Vaidhyanathan',marker=Marker(color='rgb(30,136,229)'))
    trace91 = go.Bar(x=pv1.index, y=pv1[('id', 'Jack Xia')], name='Jack Xia',marker=Marker(color='rgb(216,27,96)'))
    trace101 = go.Bar(x=pv1.index, y=pv1[('id', 'John Fegan')], name='John Fegan',marker=Marker(color='rgb(57,73,171)'))
    trace111 = go.Bar(x=pv1.index, y=pv1[('id', 'Cameron Petersen')], name='Cameron Petersen',marker=Marker(color='rgb(0,172,193)'))
    trace121 = go.Bar(x=pv1.index, y=pv1[('id', 'Myrna Alba')], name='Myrna Alba',marker=Marker(color='rgb(229,115,115)'))

    data = [trace11, trace21, trace31, trace41, trace51, trace61, trace71, trace81, trace91, trace101, trace111, trace121]
    layout = go.Layout(title=g_title,  font=dict(family='Helvetica', size=12, color='rgb(0,80,115)'), 
    barmode='stack', height=800,
            yaxis=dict(
                        autotick=False,
                        ticks='outside',
                        tick0=0,
                        dtick=10,
                        ticklen=8,
                        tickwidth=1,
                        tickcolor='#000'
                        ))

    return go.Figure(data=data, layout=layout)



pv1 = pd.pivot_table(data.L1, index=['pillar_title'], columns=["Current_status"], values=['id'], aggfunc='count', fill_value=0)

if('Completed' not in pv1['id']):
    pv1['id','Completed'] = 0

if('Delayed' not in pv1['id']):
    pv1['id','Delayed'] = 0

if('On Hold' not in pv1['id']):
    pv1['id','On Hold'] = 0

if('Requested' not in pv1['id']):
    pv1['id','Requested'] = 0

if('Work In Progress' not in pv1['id']):
    pv1['id','Work In Progress'] = 0

if('Future' not in pv1['id']):
    pv1['id','Future'] = 0

if('Rejected' not in pv1['id']):
    pv1['id','Rejected'] = 0

trace1 = go.Bar(x=pv1.index, y=pv1[('id', 'Completed')], name='Completed',marker=Marker(color='rgb(33,150,243)'))
trace2 = go.Bar(x=pv1.index, y=pv1[('id', 'Delayed')], name='Delayed',marker=Marker(color='rgb(233,30,99)'))
trace3 = go.Bar(x=pv1.index, y=pv1[('id', 'On Hold')], name='On Hold',marker=Marker(color='rgb(158,158,158)'))
trace4 = go.Bar(x=pv1.index, y=pv1[('id', 'Requested')], name='Requested',marker=Marker(color='rgb(158,158,158)'))
trace5 = go.Bar(x=pv1.index, y=pv1[('id', 'Work In Progress')], name='Work In Progress',marker=Marker(color='rgb(255,152,0)'))
trace6 = go.Bar(x=pv1.index, y=pv1[('id', 'Future')], name='Future',marker=Marker(color='rgb(63,81,181)'))
trace7 = go.Bar(x=pv1.index, y=pv1[('id', 'Rejected')], name='Rejected',marker=Marker(color='rgb(121,85,72)'))


pv2 = pd.pivot_table(data.L1, index=['pillar_title'], columns=["full_name"], values=['id'], aggfunc='count', fill_value=0)

# print(pv2)

trace11 = go.Bar(x=pv2.index, y=pv2[('id', 'Rizen Yamauchi')], name='Rizen Yamauchi',marker=Marker(color='rgb(240,98,146)'))
trace21 = go.Bar(x=pv2.index, y=pv2[('id', 'Abhishek Pradhan Shrestha')], name='Abhishek Pradhan Shrestha',marker=Marker(color='rgb(186,104,200)'))
trace31 = go.Bar(x=pv2.index, y=pv2[('id', 'Ritika Lohadiya')], name='Ritika Lohadiya',marker=Marker(color='rgb(192,202,51)'))
trace41 = go.Bar(x=pv2.index, y=pv2[('id', 'Matthew Danna')], name='Matthew Danna',marker=Marker(color='rgb(251,192,45)'))
trace51 = go.Bar(x=pv2.index, y=pv2[('id', 'Nicole Arra')], name='Nicole Arra',marker=Marker(color='rgb(121,134,203)'))
trace61 = go.Bar(x=pv2.index, y=pv2[('id', 'Batul Arsiwala')], name='Batul Arsiwala',marker=Marker(color='rgb(77,182,172)'))
trace71 = go.Bar(x=pv2.index, y=pv2[('id', 'Ryan Lund')], name='Ryan Lund',marker=Marker(color='rgb(67,160,71)'))

trace81 = go.Bar(x=pv2.index, y=pv2[('id', 'Reshmi Vaidhyanathan')], name='Reshmi Vaidhyanathan',marker=Marker(color='rgb(30,136,229)'))
trace91 = go.Bar(x=pv2.index, y=pv2[('id', 'Jack Xia')], name='Jack Xia',marker=Marker(color='rgb(216,27,96)'))
trace101 = go.Bar(x=pv2.index, y=pv2[('id', 'John Fegan')], name='John Fegan',marker=Marker(color='rgb(57,73,171)'))
trace111 = go.Bar(x=pv2.index, y=pv2[('id', 'Cameron Petersen')], name='Cameron Petersen',marker=Marker(color='rgb(0,172,193)'))
trace121 = go.Bar(x=pv2.index, y=pv2[('id', 'Myrna Alba')], name='Myrna Alba',marker=Marker(color='rgb(229,115,115)'))


app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='BAnDS Management Report'),
    html.Div(children='''Team Bandwidth and Management Report'''),
    dcc.Graph(
        id='example-graph',
        figure={
        'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7],
        'layout':
        go.Layout(title='Number of Tasks by Pillar',font=dict(family='Helvetica', size=12, color='rgb(0,80,115)'), barmode='stack', height=800,
            yaxis=dict(
                        autotick=False,
                        ticks='outside',
                        tick0=0,
                        dtick=20,
                        ticklen=8,
                        tickwidth=1,
                        tickcolor='#000'
                        )
            )
        }),


    html.Div([
    html.Label('Select Pillar',
     className='drop-down-label'),
    dcc.Dropdown(id='selected_pillar',
        options=onLoad_pillar_options())], className='two columns', id='drop-down-list'),



    html.Div(
     dcc.Graph(
        id='second-graph'
        ),
     className='nine columns', id='table-div'
     ),

    html.Div(
     dcc.Graph(
        id='third-graph',
        figure={
        'data': [trace11, trace21, trace31, trace41, trace51, trace61, trace71, trace81, trace91, trace101, trace111, trace121],
        'layout':
        go.Layout(title='Number of Tasks by Pillar/User',font=dict(family='Helvetica', size=12, color='rgb(0,80,115)'), barmode='stack', height=800,
            yaxis=dict(
                        autotick=False,
                        ticks='outside',
                        tick0=0,
                        dtick=20,
                        ticklen=8,
                        tickwidth=1,
                        tickcolor='#000'
                        ))
        }),

     className='nine columns', id='table-div'
     ),

    html.Div([
    html.Label('Select Pillar',
    className='drop-down-label'),
    dcc.Dropdown(id='selected_pillar2',
    options=onLoad_pillar_options())], className='two columns', id='drop-down-list'),

     html.Div(
     dcc.Graph(
        id='fourth-graph'
        # figure={
        # 'data': [trace11, trace21, trace31, trace41, trace51, trace61, trace71, trace81, trace91, trace101, trace111, trace121],
        # 'layout':
        # go.Layout(title='Number of Tasks by Pillar/User',font=dict(family='Helvetica', size=12, color='rgb(0,80,115)'), barmode='stack')
        # }
        ),

     className='nine columns', id='table-div'
     ),


], className='six columns', )

@app.callback(
    Output(component_id='second-graph', component_property='figure'),
    [
        Input(component_id='selected_pillar', component_property='value')
    ]
)

def load_graph(selected_pillar):
    return plot_graph(df=data.L2, idx='project_title', col="Current_status", val='id', g_title='Number of Tasks by Project',sp=selected_pillar)


@app.callback(
    Output(component_id='fourth-graph', component_property='figure'),
    [
        Input(component_id='selected_pillar2', component_property='value')
    ]
)
def load_user_graph(selected_pillar2):
    return plot_user_graph(df=data.L1, idx='project_title', col="full_name", val='id', g_title='Number of Tasks by Project/User',sp=selected_pillar2)

if __name__ == '__main__':
    app.run_server(debug=True, port=8030)
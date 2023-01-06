import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from utils.utils import tipo1

def simple_time_series(data: pd.DataFrame, x, y, xl, yl):
    fig = px.line(data, x=x, y=y,
                    title='',
                    labels={'contador': 'Conteo', x:xl, y:yl})
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(mode='markers+lines')
    fig.update_layout(yaxis_tickformat=',.0f')
    fig.update_xaxes(tickangle=330)

    return fig


def bars_plot_contador(data: pd.DataFrame, x, xl):

    data = tipo1(data, 'stockcode')

    fig = px.bar(data, y='proporcion', x=x, 
                    title = '',
                    hover_data=['contador'],
                    labels = {x:xl, 'contador': 'Units', 'proporcion':'Proportion'},
                )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(yaxis_tickformat='.1%')  
    
    return fig


def simple_bars_plot(data: pd.DataFrame, x, y, xl, yl):

    fig = px.bar(data, x=x, y=y,
                    title = '',
                    hover_data=['contador'],
                    labels = {x:xl, y:yl, 'contador': 'Units', 'proporcion':'Proportion'},
                )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    
    return fig

# Funcion grafico de pie en una dimension
def grafico_circulo(data, variable, centro):
    
    '''Ingresa un df y retorna un grafico de pie'''
    
    df_tipo = tipo1(data, variable)

    labels = list(df_tipo[variable])
    fig = go.Figure(data=[go.Pie(labels = labels, values = df_tipo['contador'], name='', 
                                 # marker_colors=human_sequence2h,
                                 direction='clockwise', sort=False)])
    fig.update_traces(hole=.5, hoverinfo="label+percent+value+name", textinfo='label')
    fig.update_layout(
        title_text='',
        annotations=[dict(text=centro, x=0.5, y=0.5, font_size=18, showarrow=False)])
    fig.update_layout(showlegend=False)
    
    return fig


def grafico_circulo2(data, x, y):
     
    '''Ingresa un df y retorna un grafico de pie doble'''

    data = data.groupby([x, y]).sum()
    data = data.reset_index()
    
    fig = px.sunburst(data, path=[x, y], values='units', 
                      title = '',
                      color_discrete_sequence = ['#9386f2','#90dde0','#ff514e'])
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})


    return fig


# def rfm_graph(data: pd.DataFrame):

#     fig = px.box(data, y='recency', color='group', 
#                 title = 'RFM Recency',
#                 category_orders={'group': ['1','2','3','4','5','6','7','8']},
#                 color_discrete_map={'1':'#684cf6','2':'#90dde0','3':'#447FF5','4':'#78e591','5':'#1e5274',
#                                     '6':'#FFE343','7':'#9EFF43','8':'#4AC3FF'},
#                 labels={'recency':'Recency', 
#                         'frequency':'Frequency', 
#                         'monetary':'Monetary', 
#                         'group':'Group',
#                         'segment':'Segment'
#                         })
#     return fig
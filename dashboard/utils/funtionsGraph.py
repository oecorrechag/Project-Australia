import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def simple_time_series(data: pd.DataFrame, x, y, xl, yl):
    fig = px.line(data, x=x, y=y,
                    title='',
                    labels={'contador': 'Conteo', x:xl, y:yl})
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(mode='markers+lines')
    fig.update_layout(yaxis_tickformat=',.0f')
    fig.update_xaxes(tickangle=330)
    return fig


def simple_bars_plot(data: pd.DataFrame, x, y, xl, yl):
    fig = px.bar(data, x=x, y=y,
                    title = '',
                    hover_data=['contador'],
                    labels = {x:xl, y:yl, 'contador': 'Units', 'proporcion':'Proportion'},
                )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig


def grafico_circulo(data: pd.DataFrame, variable, centro):
    
    '''Ingresa un df y retorna un grafico de pie'''
    
    labels = list(data[variable])
    fig = go.Figure(data=[go.Pie(labels = labels, values = data['contador'], name='', 
                                 direction='clockwise', sort=False)])
    fig.update_traces(hole=.5, hoverinfo="label+percent+value+name", textinfo='label')
    fig.update_layout(
        title_text='',
        annotations=[dict(text=centro, x=0.5, y=0.5, font_size=18, showarrow=False)])
    fig.update_layout(showlegend=False)
    return fig


def grafico_circulo2(data: pd.DataFrame, x, y, val):
     
    '''Ingresa un df y retorna un grafico de pie doble'''

    data = data.groupby([x, y]).sum()
    data = data.reset_index()
    fig = px.sunburst(data, path=[x, y], values=val, 
                      title = '',
                      )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig


def recency_graph(data: pd.DataFrame):
    
    labels={'recency':'Recency', 
            'frequency':'Frequency',
            'monetary':'Monetary', 
            'model':'Segment'}

    colours = {'1':'#684cf6','2':'#90dde0','3':'#447FF5','4':'#78e591','5':'#1e5274','6':'#FFE343',
               '7':'#9EFF43','8':'#4AC3FF'}

    orders = ['0','1','2','3','4','5','6','7','8']

    data['model'] = data['model'].astype(str)

    fig_recency = px.box(data, y='recency', color='model', 
                         title = 'Recency',
                         category_orders={'model': orders},
                         color_discrete_map=colours,
                         labels=labels)
    fig_recency.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_recency


def frequency_graph(data: pd.DataFrame):

    labels={'recency':'Recency', 
            'frequency':'Frequency',
            'monetary':'Monetary', 
            'model':'Segment'}

    colours = {'1':'#684cf6','2':'#90dde0','3':'#447FF5','4':'#78e591','5':'#1e5274','6':'#FFE343',
               '7':'#9EFF43','8':'#4AC3FF'}

    orders = ['0','1','2','3','4','5','6','7','8']

    data['model'] = data['model'].astype(str)

    fig_frequency = px.box(data, y='frequency', color='model', 
                           title = 'Frequency',
                           category_orders={'model': orders},
                           color_discrete_map=colours,
                           labels=labels)
    fig_frequency.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_frequency


def monetary_graph(data: pd.DataFrame):

    labels={'recency':'Recency', 
            'frequency':'Frequency',
            'monetary':'Monetary', 
            'model':'Segment'}

    colours = {'1':'#684cf6','2':'#90dde0','3':'#447FF5','4':'#78e591','5':'#1e5274','6':'#FFE343',
               '7':'#9EFF43','8':'#4AC3FF'}

    orders = ['0','1','2','3','4','5','6','7','8']

    data['model'] = data['model'].astype(str)

    fig_monetary = px.box(data, y='monetary', color='model', 
                title = 'Monetary',
                category_orders={'model': orders},
                color_discrete_map=colours,
                labels=labels)
    fig_monetary.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_monetary


def rfm_graph(data: pd.DataFrame, model):

    labels={'recency':'Recency', 
            'frequency':'Frequency',
            'monetary':'Monetary', 
            model:'Segment'}

    colours = {'1':'#684cf6','2':'#90dde0','3':'#447FF5','4':'#78e591','5':'#1e5274','6':'#FFE343',
               '7':'#9EFF43','8':'#4AC3FF'}

    orders = ['0','1','2','3','4','5','6','7','8']

    fig_recency = px.box(data, y='recency', color=model, 
                         title = 'RFM Recency',
                         category_orders={model: orders},
                         color_discrete_map=colours,
                         labels=labels)
    fig_recency.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig_frequency = px.box(data, y='frequency', color=model, 
                           title = 'RFM Frequency',
                           category_orders={model: orders},
                           color_discrete_map=colours,
                           labels=labels)
    fig_frequency.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    fig_monetary = px.box(data, y='monetary', color=model, 
                title = 'RFM Monetary',
                category_orders={model: orders},
                color_discrete_map=colours,
                labels=labels)
    fig_monetary.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    return fig_recency, fig_frequency, fig_monetary


def snake(data: pd.DataFrame):
    '''Esta funcion recibe un dataframe que contengan la recencia, frecuencia y monetario.
       A continuación escala las variables y genera el grafico
    '''

    fig = px.line(data, x="variable", y="value", color='model', 
              title = 'Parallel plot by segment',
              category_orders={'model':['1','2','3','4','5','6','7','8','9']},
              color_discrete_map={'1':'#684cf6', '2':'#9386f2', '3':'#90dde0', '4':'#78e591', '5':'#1e5274'},
              labels = {'variable': 'Variable', 'value': 'Value', 'model':'Segment'},        
              hover_data=['recency','frequency','monetary'])
    fig.update_traces(mode='markers+lines')
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(
        tickvals=['recency_s','frequency_s','monetary_s'],
        ticktext=['Recencia', 'Frecuencia', 'Monetario'])
    fig.update_traces(
        hovertemplate="<br>".join([
            "Variable: %{x}",
            "Scale value: %{y:,.2f}",
            "Recency: %{customdata[0]:,.0f}",
            "Frequency: %{customdata[1]:,.0f}",
            "Monetary: %{customdata[2]:,.0f}",
        ])
    )
    
    return fig

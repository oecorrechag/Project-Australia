import plotly.express as px

def barras(dataframe, x, y, color):

    '''Esta funcion recibe un dataframe, dos variables a graficar en x e y, una variable para colorear'''

    return px.bar(dataframe, x=x, y=y, color=color, barmode="group")


def lineas(dataframe, x, y, color):

    '''Esta funcion recibe un dataframe, dos variables a graficar en x e y, una variable para colorear'''

    return px.line(dataframe, x=x, y=y, color=color)

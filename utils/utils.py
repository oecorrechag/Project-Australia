
# Funcion tipo1
def tipo1(df, variable):
    
    '''Funcion ingresa un dataframe y una variable, retornara proporciones'''
    
    salida = df.loc[:,[variable]]
    salida.insert(1, 'contador', 1)
    salida['proporcion'] = (salida['contador'] / len(salida))
    salida = salida.groupby([variable]).sum()
    salida = salida.reset_index()
    salida['proporcion'] = round(salida['proporcion'],5)
    salida = salida.sort_values(by=['proporcion'], ascending=False)
    
    return salida

def tipo1B(df, variable):
    """
    Función que calcula y retorna las proporciones de una variable en un dataframe.

    Parámetros:
        df (pandas.DataFrame): El dataframe que contiene la variable.
        variable (str): El nombre de la variable a analizar.

    Retorna:
        pandas.DataFrame: Un dataframe con las proporciones de la variable.
    """

    proporciones = df.groupby(variable).size().to_frame(name='contador')
    proporciones['proporcion'] = proporciones['contador'] / len(df)
    proporciones['proporcion'] = proporciones['proporcion'].apply(lambda x: f"{x:.5f}")
    proporciones = proporciones.sort_values(by='proporcion', ascending=False)

    mensaje = f"Proporciones de '{variable}':\n{proporciones}"
    return mensaje

# Funcion tipo1
def tipo1(df, variable):
    
    '''Funcion ingresa un dataframe y una variable, retornara un grafico'''
    
    salida = df.loc[:,[variable]]
    salida.insert(1, 'contador', 1)
    salida['proporcion'] = (salida['contador'] / len(salida))
    salida = salida.groupby([variable]).sum()
    salida = salida.reset_index()
    salida['proporcion'] = round(salida['proporcion'],5)
    salida = salida.sort_values(by=['proporcion'], ascending=False)
    
    return salida
    
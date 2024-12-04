import pandas as pd
from mypackage import dir
from mypackage.transforms import non_sex, diff_date, convert_variables


# Environment variables
modality = 'p'
project = 'australian'
data = dir.make_dir_line(modality, project) 
raw = data('raw')
processed = data('processed')


# Función para cargar datos
def cargar_datos(table_name: str) -> pd.DataFrame:
    df = pd.read_csv(raw / f'{table_name}.csv', sep = ',', decimal = '.', header = 0)
    print(f'Loaded table: {table_name}')
    return df

# Función para transformar los datos clientes
def transformar_datos_clientes(df: pd.DataFrame) -> pd.DataFrame:
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], format='%Y-%m-%d', errors = 'coerce')
    df = convert_variables(df, ['id_cliente', 'sexo'], 'str')
    df = non_sex(df, 'sexo')
    df = diff_date(df, "fecha_nacimiento", 'now')
    return df

# Función para transformar los datos productos
def transformar_datos_productos(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={'precio':'valor', 'production':'procentaje_produccion'}, inplace=True)
    df['valor_produccion'] = (df['valor'] * df['procentaje_produccion'])/100
    return df

# Función para transformar los datos ventas
def transformar_datos_ventas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.loc[:,['id_factura', 'fecha', 'id_cliente', 'id_producto', 'quantity', 'id_store', 'discount', 'per_discount2']]
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors = 'coerce')
    df = convert_variables(df, ['id_factura', 'id_cliente', 'id_store', 'discount'], 'str')
    df.drop_duplicates(inplace=True)
    return df

# Función para cargar los datos en la base de datos
def cargar_en_db(df: pd.DataFrame, table_name: str) -> None:
    df.to_parquet(processed/f'{table_name}.parquet.gzip', compression='gzip')
    print(f'Saved table: {table_name}')

if __name__ == '__main__':

    # ETL clientes
    clientes = cargar_datos('df_clientes')
    clientes_transformadas = transformar_datos_clientes(clientes)
    cargar_en_db(clientes_transformadas, 'clientes')

    # ETL productos
    productos = cargar_datos('df_productos')
    productos_transformadas = transformar_datos_productos(productos)
    cargar_en_db(productos_transformadas, 'productos')

    # ETL ventas
    ventas = cargar_datos('df_ventas')
    ventas_transformadas = transformar_datos_ventas(ventas)
    cargar_en_db(ventas_transformadas, 'ventas')

    # Create dataset
    productos = productos.loc[:,['id_producto', 'category', 'valor', 'valor_produccion']]
    df = ventas.merge(productos, on = ['id_producto'])
    df['total_factura'] = df['valor'] * df['quantity']
    df = df.loc[:,['id_factura', 'fecha', 'id_cliente', 'quantity', 'valor', 'total_factura']]
    df = df.dropna()
    cargar_en_db(df, 'dataset')
    
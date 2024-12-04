import pandas as pd
import datetime as dt

from sklearn.ensemble import IsolationForest

from mypackage import dir
from mypackage.rfm import calculate_rfm

iso_forest = IsolationForest(contamination=0.1, random_state=42)

# Environment variables
modality = 'p'
project = 'australian'
data = dir.make_dir_line(modality, project) 
processed = data('processed')


# Función para cargar datos
def cargar_datos(table_name: str) -> pd.DataFrame:
    df = pd.read_parquet(processed / f'{table_name}.parquet.gzip')
    print(f'Loaded table: {table_name}')
    return df

# Función para cargar los datos en la base de datos
def cargar_en_db(df: pd.DataFrame, table_name: str) -> None:
    df.to_parquet(processed/f'{table_name}.parquet.gzip', compression='gzip')
    print(f'Saved table: {table_name}')

def get_month(x): return dt.datetime(x.year, x.month, 1) 

def get_dates(df, col):
    year = df[col].dt.year
    month = df[col].dt.month
    day = df[col].dt.day
    return year, month, day

if __name__ == '__main__':

    df = cargar_datos('dataset')
    # dividir data para drift
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors = 'coerce')
    df = df[df['fecha']<'2024-1-1']
    df = df[df["total_factura"] > 0.0]
    # transformaciones
    df = df.sort_values(by=['fecha'], ascending=True)
    df['anomaly'] = iso_forest.fit_predict(df.loc[:,['quantity', 'valor', 'total_factura']])
    df = df[df['anomaly'] == 1].drop(columns='anomaly')

    df["InvoiceMonth"] = df["fecha"].apply(get_month)
    df["CohortMonth"] = df.groupby("id_cliente")["InvoiceMonth"].transform("min")

    invoice_year, invoice_month, invoice_day = get_dates(df, "InvoiceMonth")
    cohort_year, cohort_month, cohort_day = get_dates(df, "CohortMonth")
    year_diff = invoice_year - cohort_year
    month_diff = invoice_month - cohort_month
    df["CohortIndex"] = 12 * year_diff + month_diff + 1

    rfm = calculate_rfm(dataframe=df, 
                        val_id_customer='id_cliente', 
                        val_id_facture='id_factura', 
                        val_money='total_factura', 
                        val_date='fecha')
    cltv = rfm.copy()
    cltv["monetary"] = cltv["monetary"] / cltv["frequency"] 
    cltv = cltv[(cltv['frequency'] > 1)]
    # dividir para tener semanas
    cltv["live_purches"] = cltv["live_purches"] / 7
    cltv["tenure"] = cltv["tenure"] / 7

    cargar_en_db(df, 'cohortes')
    cargar_en_db(rfm, 'rfm')
    cargar_en_db(cltv, 'cltv')

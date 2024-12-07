import pandas as pd
from sklearn.ensemble import IsolationForest
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

from mypackage import dir
from mypackage.rfm import calculate_rfm

# Environment variables
modality = 'p'
project = 'australian'
data = dir.make_dir_line(modality, project) 
processed = data('processed')
models = data('models')
outputs = data('outputs')

iso_forest = IsolationForest(contamination=0.1, random_state=42)

# Función para cargar datos
def cargar_datos(table_name: str) -> pd.DataFrame:
    df = pd.read_parquet(processed / f'{table_name}.parquet.gzip')
    print(f'Loaded table: {table_name}')
    return df

if __name__ == '__main__':

    reference = cargar_datos('rfm')
    reference = reference.loc[:,['recency', 'live_purches', 'tenure', 'frequency', 'monetary']]
    current = cargar_datos('dataset')
    current['fecha'] = pd.to_datetime(current['fecha'], format='%Y-%m-%d', errors = 'coerce')
    df_post_2024 = current[current['fecha']>='2024-1-1']
    clientes_post_2024 = df_post_2024['id_cliente'].unique()
    current = current[current['id_cliente'].isin(clientes_post_2024)]
    current = current[current["total_factura"] > 0.0]
    current['anomaly'] = iso_forest.fit_predict(current.loc[:,['quantity', 'valor', 'total_factura']])
    current = current[current['anomaly'] == 1].drop(columns='anomaly')
    current = current.sort_values(by=['fecha'], ascending=True)
    current = calculate_rfm(dataframe=current, 
                        val_id_customer='id_cliente', 
                        val_id_facture='id_factura', 
                        val_money='total_factura', 
                        val_date='fecha')
    current = current.loc[:,['recency', 'live_purches', 'tenure', 'frequency', 'monetary']]


    report = Report(metrics=[
        DataDriftPreset(drift_share=0.3), 
    ])
    report.run(reference_data=reference, 
            current_data=current
            )

    report.save_html(str(outputs/'rfm_driff.html'))


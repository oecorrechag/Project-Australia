import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from mypackage import dir


# Environment variables
modality = 'p'
project = 'australian'
data = dir.make_dir_line(modality, project) 
processed = data('processed')
models = data('models')


# Función para cargar datos
def cargar_datos(table_name: str) -> pd.DataFrame:
    df = pd.read_parquet(processed / f'{table_name}.parquet.gzip')
    print(f'Loaded table: {table_name}')
    return df

# Función para cargar los datos en la base de datos
def cargar_en_db(df: pd.DataFrame, table_name: str) -> None:
    df.to_parquet(models/f'{table_name}.parquet.gzip', compression='gzip')
    print(f'Saved table: {table_name}')

if __name__ == '__main__':

    df = cargar_datos('cohortes')

    cohort_data = df.groupby(["CohortIndex", "CohortMonth"])["id_cliente"].nunique().reset_index()
    cohort_pivot = cohort_data.pivot(index = "CohortMonth", columns = "CohortIndex", values = "id_cliente")

    cohort_sizes = cohort_pivot.iloc[:, 0]

    retention = cohort_pivot.divide(cohort_sizes, axis = 0)
    retention.index = retention.index.strftime("%Y-%m")
    cargar_en_db(retention, 'retention')

    churn = 1 - retention
    cargar_en_db(churn, 'churn')

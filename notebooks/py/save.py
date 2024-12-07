import pandas as pd


from mypackage import dir


modality = 'p'
project = 'australian'
data = dir.make_dir_line(modality, project) 
processed = data('processed')
models = data('models')
outputs = data('outputs')


# Función para cargar y guardar los parquets como csv
def comvert_parquet(original: str, table_name: str) -> None:
    df = pd.read_parquet(original / f'{table_name}.parquet.gzip')
    df.to_csv(outputs/f'{table_name}.csv', encoding = 'utf-8-sig', index = False)
    print(f'Saved table: {table_name}')

if __name__ == '__main__':
    comvert_parquet(processed, 'cltv')
    comvert_parquet(models, 'segmentacion')

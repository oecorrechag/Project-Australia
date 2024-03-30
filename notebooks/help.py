import pandas as pd
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

def calculate_time_between_purchases(dataframe: pd.DataFrame, customer_id_column: str, date_column: str) -> pd.DataFrame:
  """
  Calculates the minimum, average and maximum days between purchases in a DataFrame.

  Args:
    dataframe: DataFrame with the purchases. It must have a column with the purchase date.
    customer_id_column: String, column name for customer ID.
    date_column: String, column name for purchase date.

  Returns:
    New DataFrame with the following columns:
      - 'Time_Min': Minimum time between purchases.
      - 'Time_Average': Average time between purchases.
      - 'Time_Max': Maximum time between purchases.
  """

  # Sort the DataFrame by customer and date
  dataframe[date_column] = pd.to_datetime(dataframe[date_column])
  dataframe = dataframe.sort_values(by=[customer_id_column, date_column])

  # Calculate the time difference between purchases for each customer
  dataframe['Time_Between_Purchases'] = dataframe.groupby(customer_id_column)[date_column].diff().dt.days

  # Calculate statistics
  stats = dataframe.groupby(customer_id_column)['Time_Between_Purchases'].agg(['min', 'mean', 'max'])

  # Create a new DataFrame with the results
  results_df = pd.DataFrame(stats)
  results_df.columns = ['Time_Min', 'Time_Average', 'Time_Max']
  results_df['Time_Average'] = round(results_df['Time_Average'], 0)
  results_df = results_df.reset_index()

  return results_df


def cluster_summary(dataframe: pd.DataFrame, column_group: str, sta: str =True, statistics_list=None) -> pd.DataFrame:
    """
    Computes fundamental statistical measures within specified groups, offering flexibility and readability.

    Args:
        dataframe (pd.DataFrame): The input DataFrame.
        column_group (str): Column to group.
        statistics_list (list, optional): List of statistical measures to compute.
            Defaults to ['mean', 'median', 'min', 'max', 'std'].

    Returns:
        pd.DataFrame: A DataFrame with the specified statistical measures.
    """

    if sta is True:
       numeric_columns = dataframe.select_dtypes(include=['number']).columns
       numeric_columns = [col for col in numeric_columns if col not in dataframe.select_dtypes(include=['object']).columns]
       dataframe[numeric_columns] = scaler.fit_transform(dataframe[numeric_columns])
        
    if statistics_list is None:
        statistics_list = ['mean', 'median', 'min', 'max', 'std']  # Include standard deviation by default

    def g(df):
        return df.groupby(column_group).agg(statistics_list)

    resume = g(dataframe.copy())  # Avoid modifying original DataFrame
    resume.columns = resume.columns.map('_'.join)  # Concise column renaming

    return resume.reset_index().rename(columns={column_group: 'category'}).melt(id_vars='category', var_name='statistic', value_name='value')

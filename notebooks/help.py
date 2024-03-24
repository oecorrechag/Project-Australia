import pandas as pd

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

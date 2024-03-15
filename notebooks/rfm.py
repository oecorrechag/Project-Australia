import pandas as pd

def calculate_rfm(dataframe, val_id_customer, val_id_facture, val_money, val_date):
    """Calculates RFM.

    Args:
        dataframe: Pandas DataFrame containing customer purchase data.
        val_id_customer: String, column name for customer ID.
        val_id_facture: String, column name for invoice ID.
        val_money: String, column name for purchase amount.
        val_date: String, column name for purchase date.

    Returns:
        Pandas DataFrame with RFM score and RFM groups.
    """

    max_date = dataframe[val_date].dt.date.max()
    TODAY = max_date + pd.DateOffset(1)

    rfm = (
        dataframe.groupby(val_id_customer)
        .agg(
            recency=(val_date, lambda date: (TODAY - date.max()).days),
            frequency=(val_id_facture, lambda num: num.nunique()),
            monetary=(val_money, lambda price: price.sum()),
        )
        .reset_index()
    )

    rfm.columns = [val_id_customer, 'recency', 'frequency', 'monetary']

    return rfm

import pandas as pd

def cut_rfm(dataset):
    """Calculates RFM scores and segments customers into groups.

    Args:
        dataset (pd.DataFrame): Pandas DataFrame containing customer purchase data.
            Columns should include 'recency', 'frequency', and 'monetary_value'.

    Returns:
        pd.DataFrame: The original DataFrame with added columns:
            - 'recency_rank': Rank of recency (ascending = more recent).
            - 'frequency_rank': Rank of frequency (ascending = more frequent).
            - 'monetary_value_rank': Rank of monetary value (ascending = higher value).
            - 'r_quartile': RFM score quartile for recency (1 = least recent, 5 = most recent).
            - 'f_quartile': RFM score quartile for frequency (1 = least frequent, 5 = most frequent).
            - 'm_quartile': RFM score quartile for monetary value (1 = lowest value, 5 = highest value).
            - 'rfm_score': Concatenated RFM score quartiles (e.g., '321' for R=3, F=2, M=1).
            - 'segment': Customer segment based on RFM score (descriptive labels).
            - 'group': Customer segment based on RFM score (numerical codes).
    """

    # Rank columns with appropriate ascending/descending order
    dataset["recency_rank"] = dataset["recency"].rank(ascending=False)  # Less recent = higher rank
    dataset["frequency_rank"] = dataset["frequency"].rank(ascending=True)  # More frequent = higher rank
    dataset["monetary_value_rank"] = dataset["monetary"].rank(ascending=True)  # Higher value = higher rank

    # Create RFM score quartiles using pandas.qcut for even distribution
    dataset['r_quartile'] = pd.qcut(dataset['recency_rank'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    dataset['f_quartile'] = pd.qcut(dataset['frequency_rank'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    dataset['m_quartile'] = pd.qcut(dataset['monetary_value_rank'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')

    # Combine RFM quartiles into a single score string
    dataset['rfm_score'] = dataset[['r_quartile', 'f_quartile', 'm_quartile']].astype(str).sum(axis=1)

    # Segment mapping dictionary with more descriptive and consistent labels
    seg_map = {
        r'[1-2][1-2][1-2]': 'Hibernating',
        r'[3][3][3]': 'About to Sleep',
        r'[3][1-2][1-2-3]': 'About to Sleep',
        r'[1-2-3][3][1-2]': 'About to Sleep',
        r'[1-2][3][1-2-3]': 'About to Sleep',
        r'[1-2][1-2-3][3]': 'About to Sleep',     
        r'[4-5][1-2-3][1-2-3]': 'New Customers',  
        r'[4-5][4-5][1-2-3]': 'Low Potential',      
        r'[1-2-3][4-5][1-2-3]': 'At Risk', 
        r'[3-4-5][1-2][4-5]': 'High New Customers', 
        r'[1-2][1-2][4-5]': 'Uniquely Promising Highs', 
        r'[1-2][3-4-5][4-5]': 'Need Attention', 
        r'[3-4-5][3][4-5]': 'High Potential', 
        r'[3][3-4-5][4-5]': 'High Potential',
        r'[4-5][4-5][4-5]': 'Champions'
    }

    seg_map2 = {
        r'Hibernating': '1',
        r'About to Sleep': '2',
        r'High New Customers': '6',
        r'New Customers': '3',
        r'Low Potential':'4',
        r'At Risk': '5',
        r'Uniquely Promising Highs': '7',
        r'Need Attention': '8',
        r'High Potential': '9',
        r'Champions': '10' 
    }

    dataset['group_rfm'] = dataset['rfm_score'].replace(seg_map, regex=True)
    dataset['segment_rfm'] = dataset['group_rfm'].replace(seg_map2, regex=True)

    return dataset

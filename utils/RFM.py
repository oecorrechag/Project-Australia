import pandas as pd
import numpy as np
import datetime as dt

def rfm_v1(dataset, id_customer, id_facture, date, money, 
           cut_r=None, cut_f=None, cut_m=None):
    '''This function recive:
        A dataframe, ID customer, ID facture, date, money,
        3 list to cut recency, frecuency, monetary,
        return rfm_score and 10 groups'''

    max_date = dataset[date].dt.date.max()
    TODAY = max_date + pd.DateOffset(1)

    # Calcular las letras del RFM
    rfm = dataset.groupby(id_customer).agg({date: lambda date: (TODAY - date.max()).days,
                                            id_facture: lambda num: num.nunique(),
                                            money: lambda price: price.sum()}).reset_index()
    rfm.columns=['id_customer','recency','frequency','monetary']

    df_aux = pd.DataFrame({'recency': rfm['recency'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99]),
                          'frequency': rfm['frequency'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99]),
                          'monetary': rfm['monetary'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99])
                        })

    if cut_r == None:
        rfm['r_quartile'] = pd.qcut(rfm['recency'], 5, [5, 4, 3, 2, 1])
    else:
        cut_bins, labels = cut_r, [5, 4, 3, 2, 1]
        rfm["r_quartile"] = pd.cut(rfm['recency'], bins = cut_bins, labels = labels)

    if cut_f == None:
        rfm['f_quartile'] = pd.qcut(rfm['frequency'], 5, [1, 2, 3, 4, 5])
    else:
        cut_bins, labels = cut_f, [1, 2, 3, 4, 5]
        rfm["f_quartile"] = pd.cut(rfm['frequency'], bins = cut_bins, labels = [1, 2, 3, 4, 5])

    if cut_m == None:
        rfm['m_quartile'] = pd.qcut(rfm['monetary'], 5, [1, 2, 3, 4, 5])
    else:
        cut_bins, labels = cut_m, [1, 2, 3, 4, 5]
        rfm["f_quartile"] = pd.cut(rfm['frequency'], bins = cut_bins, labels = [1, 2, 3, 4, 5])
        
    rfm['rfm_score'] = rfm.r_quartile.astype(str)+ rfm.f_quartile.astype(str) + rfm.m_quartile.astype(str)


    # partir los grupos con nombre
    seg_map = {
        r'[1-2][1-2][1-2]': 'Hibernating',

        r'[3][3][3]': 'About to Sleep',
        r'[3][1-2][1-2-3]': 'About to Sleep',
        r'[1-2-3][3][1-2]': 'About to Sleep',
        r'[1-2][3][1-2-3]': 'About to Sleep',
        r'[1-2][1-2-3][3]': 'About to Sleep',
                
        r'[4-5][1-2-3][1-2-3]': 'New Customers',
                
        r'[4-5][4-5][1-2-3]': 'Potential low', 
                
        r'[1-2-3][4-5][1-2-3]': 'At Risk', 
                
        r'[3-4-5][1-2][4-5]': 'New Customers higt', 
                
        r'[1-2][1-2][4-5]': 'Unique higt - Promising', 
                
        r'[1-2][3-4-5][4-5]': 'Need Attention', 
                
        r'[3-4-5][3][4-5]': 'Potential higt', 
        r'[3][3-4-5][4-5]': 'Potential higt',
                
        r'[4-5][4-5][4-5]': 'Champions'
        
    }


    seg_map2 = {
        r'Hibernating': '1',
        r'About to Sleep': '2',
        r'New Customers higt': '6',
        r'New Customers': '3',
        r'Potential low':'4',
        r'At Risk': '5',
        r'Unique higt - Promising': '7',
        r'Need Attention': '8',
        r'Potential higt': '9',
        r'Champions': '10'
        
    }

    rfm['segment'] = rfm['rfm_score'].replace(seg_map, regex=True)
    rfm['group'] = rfm['segment'].replace(seg_map2, regex=True)

    return rfm, df_aux


def rfm_v2(dataset, id_customer, id_facture, date, money, 
           cut_r=None, cut_f=None, cut_m=None,
           r_weight=1, f_weight=1, m_weight=1,
           n_groups=5
           ):
    '''This function recive:
        A dataframe, ID customer, ID facture, date, money,
        3 list to cut recency, frecuency, monetary,
        return rfm_score and 5 groups for defect'''

    max_date = dataset[date].dt.date.max()
    TODAY = max_date + pd.DateOffset(1)

    # Calcular las letras del RFM
    rfm = dataset.groupby(id_customer).agg({date: lambda date: (TODAY - date.max()).days,
                                            id_facture: lambda num: num.nunique(),
                                            money: lambda price: price.sum()}).reset_index()
    rfm.columns=['id_customer','recency','frequency','monetary']

    df_aux = pd.DataFrame({'recency': rfm['recency'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99]),
                          'frequency': rfm['frequency'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99]),
                          'monetary': rfm['monetary'].describe([0.01,0.05,0.10,0.25,0.50,0.60,0.75,0.90,0.95,0.99])
                        })


    if cut_r == None:
        rfm['r_quartile'] = pd.qcut(rfm['recency'], 5, [5, 4, 3, 2, 1])
    else:
        cut_bins, labels = cut_r, [5, 4, 3, 2, 1]
        rfm["r_quartile"] = pd.cut(rfm['recency'], bins = cut_bins, labels = labels)

    if cut_f == None:
        rfm['f_quartile'] = pd.qcut(rfm['frequency'], 5, [1, 2, 3, 4, 5])
    else:
        cut_bins, labels = cut_f, [1, 2, 3, 4, 5]
        rfm["f_quartile"] = pd.cut(rfm['frequency'], bins = cut_bins, labels = [1, 2, 3, 4, 5])

    if cut_m == None:
        rfm['m_quartile'] = pd.qcut(rfm['monetary'], 5, [1, 2, 3, 4, 5])
    else:
        cut_bins, labels = cut_m, [1, 2, 3, 4, 5]
        rfm["f_quartile"] = pd.cut(rfm['frequency'], bins = cut_bins, labels = [1, 2, 3, 4, 5])

    rfm['r_quartile'] = rfm['r_quartile'].astype(int)
    rfm['f_quartile'] = rfm['f_quartile'].astype(int)
    rfm['m_quartile'] = rfm['m_quartile'].astype(int)    
    rfm["rfm_score"] = ((rfm['r_quartile'] * (r_weight)) + (rfm['f_quartile'] * (f_weight)) + (rfm['m_quartile'] * (m_weight)))/3

    if n_groups == 5:
        # cur rfm_score
        conditions = [(rfm['rfm_score'] >= 4.5),   
                      ((rfm['rfm_score'] >= 4) & (rfm['rfm_score'] < 4.5)),
                      ((rfm['rfm_score'] >= 3) & (rfm['rfm_score'] < 4)),
                      ((rfm['rfm_score'] >= 2) & (rfm['rfm_score'] < 3)),
                      (rfm['rfm_score'] < 2)
                    ]
        values = ['1','2','3','4','5']
        rfm['group'] = np.select(conditions, values)
    else:
        rfm['group'] = pd.qcut(rfm['rfm_score'], n_groups, np.arange(1, n_groups+1, 1, dtype=int))
        rfm['group'] = rfm['group'].astype(str)


    return rfm, df_aux
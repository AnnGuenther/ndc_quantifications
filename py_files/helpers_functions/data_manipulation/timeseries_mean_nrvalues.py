# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam
Last updated in 02/2020
"""

# %%
"""
Calculate the mean over the first/last nrvalues available values.

INPUT: pd.DataFrame with rows == countries and columns == years.
OUTPUT: pd.DataFramw with rows == countries and columns == ['first_values', 'last_values'], 
with the mean over the last/first nrvalues.
"""

# %%
import pandas as pd
import numpy as np

# %%
def timeseries_mean_nrvalues(df, nrvalues):
    df_notnan = ~df.isnull()
    df_out = pd.DataFrame(index=df.index, columns=['first_values', 'last_values'])
    for row in df.index[~df.isnull().all(axis=1)]:
        df_row = df.loc[row, :]
        available_years = np.array(sorted(df_row.index[df_notnan.loc[row, :]]))
        df_out.loc[row, 'first_values'] = df_row[available_years[:nrvalues]].mean()
        df_out.loc[row, 'last_values'] = df_row[available_years[-nrvalues:]].mean()
    #endfor
    return df_out
#enddef
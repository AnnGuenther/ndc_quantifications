#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
"""
Read in a csv output file from the PRIMAPDB (used write_tables_to_csv_files_agu.m to write out the table).

# e.g., path_to_table_csv = Path('C:/Users/annikag/primap/ndcs/ndc_quantifications_in_python/' +
    'ndc_quantifications/data/preprocess/matlab/emi/CO2_IPC1_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')
"""

# %%
import pandas as pd
from os import path
import sys
from helpers_functions.classes_tables.create_table import create_table

# %%
def import_table_to_class_metadata_country_year_matrix(path_to_table_csv):
    # Check if file exists
    if path.isfile(str(path_to_table_csv)):
        # Get the rows of the data (starting with row with iso3 in column0).
        data_col0 = pd.read_csv(path_to_table_csv, usecols=[0], header=None)
        start_row_isos = [xx for xx in data_col0.index 
                          if data_col0.loc[xx, :][0].upper() == 'ISO3']
        data_meta = pd.read_csv(path_to_table_csv, 
                                skiprows=range(start_row_isos[0], len(data_col0)), 
                                index_col=0, header=None)
        table = create_table()
        # Put meta-data into class attributes.
        for sheet_info in data_meta.index:
            setattr(table, sheet_info, data_meta.loc[sheet_info, :].values[0])
        # endfor
        data_numeric = pd.read_csv(path_to_table_csv, 
                                   skiprows=range(start_row_isos[0]), 
                                   index_col=0)
        data_numeric.columns = [int(xx) for xx in data_numeric.columns]
        table.data = data_numeric
        table.__tablename_to_standard__()
        table.__name_to_standard__()
        return table
    else:
        sys.exit("import_table_to_class_metadata_country_year_matrix.py: non-existent " + str(path_to_table_csv) + ".")
    # endif
# enddef
# %%

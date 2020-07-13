# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def write_table_from_class_metadata_country_year_matrix(table, path_to_folder):
    """
    Write out a 'table' to a csv file. The table is actually a class with different 
    attributes that are written to the csv-file. First the not-numerical-data are written,
    followed by the numerical cydata (country/year matrix). Empty rows are deleted.
    
    Parameters
    ----------
    table : class
        One attribute 'data' holding a country-year matrix of timeseries.
        And additional meta-data.
    path_to_folder : str or Path
        Path to output. If it does not end on '.csv', the attribute 'tablename' is used as file-name.
    """
    # %%
    from pathlib import Path
    from helpers_functions.classes_tables.get_all_attributes_of_class import get_all_attributes_of_class
    import csv
    
    # %%
    get_keys = get_all_attributes_of_class(table)
    get_keys.remove('data')
    #
    path_to_file = (Path(path_to_folder, table.tablename + '.csv') if not str(path_to_folder).endswith('.csv') 
                    else Path(path_to_folder))
    with open(path_to_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for write_row in get_keys:
            writer.writerow([write_row, str(getattr(table, write_row))])
        # endfor
        writer.writerow(['ISO3'] + list(table.data.columns))
        table.data.drop(index=table.data.index[table.data.isnull().all(axis=1)], inplace=True)
        for write_row in table.data.index:
            writer.writerow([write_row] + list(table.data.loc[write_row, :]))
    # endwith
# enddef
# %%

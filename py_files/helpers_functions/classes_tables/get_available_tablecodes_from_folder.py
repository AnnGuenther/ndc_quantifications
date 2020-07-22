# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 05/2020.
"""

# %%
def get_available_tables_from_folder(path_to_folder, iso3, **kwargs):
    """
    Find tables in 'path_to_folder' that have data for a certain country (and year) available.
    
    Input:
        path_to_folder: string.
        iso3: string.
    
    Optional input:
        year: numerical value for year.
        categories: list with categories.
        entities: list with entities.
    """
    
    # %%
    import numpy as np
    import os
    from pathlib import Path
    import helpers_functions as hpf
    
    # %%
    #path_to_folder = Path('C://Users', 'annikag', 'primap', 'datatables_csv', 'proc_SSP2018_23Jul19')
    files = os.listdir(path_to_folder)
    for file in files:
        
        if file.endswith('.csv'):
            
            if 'categories' in kwargs.keys():
                if any([True if xx in file else False for xx in kwargs['categories']]):
                    use_it_cat = True
                else:
                    use_it_cat = False
            else:
                use_it_cat = True
            
            if 'entities' in kwargs.keys():
                if any([True if xx in file else False for xx in kwargs['entities']]):
                    use_it_ent = True
                else:
                    use_it_ent = False
            else:
                use_it_ent = True
            
            if (use_it_cat and use_it_ent):
                
                try:
                    table = hpf.import_table_to_class_metadata_country_year_matrix(
                        Path(path_to_folder, file)).data.reindex(index=[iso3])
                    if 'year' in kwargs.keys():
                        year = kwargs['year']
                        if not np.isnan(table.loc[iso3, year]):
                            print(f"{file} has data for {iso3} for year {year}.")
                    else:
                        available_years = [xx for xx in table.columns if not np.isnan(table.loc[iso3, xx])]
                        print(f"{file} has data for {iso3} (first year: {available_years[0]}, last year: {available_years[-1]}).")
                
                except:
                    pass
        
    # %%
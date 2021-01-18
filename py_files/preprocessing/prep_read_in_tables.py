# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def prep_read_in_tables(file, path_to_folder, database, meta):
    
    """
    **Read in all datatables in folder.**
    
    All read into class 'database', with the tablenames as attributes.
    *Replace AR4 strings by ''*
    (e.g., ``KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTORY_CRF2019.csv`` is read in 
    with tablename 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTORY_CRF2019').
    The *attributes are classes* again, with *attributes entity, category, 
    data, family, etc. (see meta.nomenclature.attrs)*.
    """
    
    # %%
    from warnings import warn
    from pathlib import Path
    import helpers_functions as hpf
    
    # %%
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(path_to_folder, file))
    
    # For emissions data in CO2eq, only read in the data if the GWP is given and it equals meta.gwps.default.
    if (table.family == 'emi' and not hasattr(table, 'gwp')):
        warn("preprocessing.py: " + file + " has no field GWP, even though it is emissions data. It is not read in.")
    elif (hasattr(table, 'gwp') and table.gwp.upper() != meta.gwps.default):
        warn("preprocessing.py: gwp for " + file + " is not supported (only " + meta.gwps.default + ")! It is not read in.")
    else:
        
        # Delete some attributes, and rename the others following the 'new' nomenclature (see meta.nomenclture.oldname_to_attr).
        for attr in hpf.get_all_attributes_of_class(table):
            if attr in meta.nomenclature.oldname_to_attr.keys():
                setattr(table, meta.nomenclature.oldname_to_attr[attr], getattr(table, attr))
            
            if attr not in meta.nomenclature.attrs:
                delattr(table, attr)
        
        # Change the unit to meta.units.default.
        table.__convert_unit__(meta.units.default[table.family], gwp=meta.gwps.default)
        
        # Store gases / baskets without the AR4 in the tablename.
        if meta.gwps.default in table.ent:
            table.ent = table.ent.replace(meta.gwps.default, '')
        
        table.__tablename_to_standard__()
        table.__name_to_standard__()
        
        # Columns are integers (years). Dismiss all years < 1990 and years > 2050.
        # Index: all EARTH-iso3s, without EU28.
        # For the PRIMAP totals save one version without eliminating the early years (used for the .md-files).
        if file == 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + ".csv":
            hpf.write_table_from_class_metadata_country_year_matrix(
                    table, Path(meta.path.preprocess, 'tables', table.tablename + "__allYears.csv"))
        
        table.__reindex__(years=range(1990, 1+min([2050, max(table.data.columns)])), isos=meta.isos.EARTH)
        
        setattr(database, table.tablename, table)
        
    return database

# %%

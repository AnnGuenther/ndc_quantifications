# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def combine_tables(how, tables, **kwargs):
    """
    Parameters
    ----------
    how : str
        'add', 'subtract', 'multiply' or 'divide'
    tables : list
        list of tables (tables are classes where 'data' are country-year matrices, and other attributes are metadata)
    
    OPTIONAL:
        only_if_all_have_values : boolean
            'True' if you only want to keep values for country+year when all tables are not NaN, else 'False'.
            Only interesting for add and subtract. Multiply and divide will give NaN.
        gwp : str
            If a GWP is given, emissions data are converted into CO2eq using this
            GWP (not possible for gas baskets), else meta.gwps.default is used.
            But if there is a gas basket in the tables, the GWP of this basket is used.
        new_attrs (dictionary with new names of attributes)
    """
    
    # %%
    import sys
    import pandas as pd
    from warnings import warn
    import helpers_functions as hpf
    from setup_metadata import setup_metadata
    
    # %%
    meta = setup_metadata()

    # %%
    # tables have to be created with create_table().
    if how not in ['add', 'subtract', 'multiply', 'divide']:
        sys.exit("combine_tables.py: the string for 'how' is not supported.")
    #endif
        
    # If one table has emissions values in CO2eq that cannot be converted into the wanted gwp,
    # use that gwp instead of the one in kwargs.
    gwp_prescribed = []
    baskets = ['HFCS', 'PFCS', 'FGASES', 'KYOTOGHG']
    for ind in range(len(tables)):
        if 'gwp' in hpf.get_all_attributes_of_class(tables[ind]):
            if any([xx in getattr(tables[ind], 'ent') for xx in baskets]):
                gwp_act = (getattr(tables[ind], 'gwp'))
                gwp_act = ('AR2' if gwp_act == 'SAR' else gwp_act)
                gwp_prescribed += [gwp_act]
        #endif
    #endfor
    
    if 'gwp' in kwargs.keys():
        gwp_wanted = kwargs['gwp']
        gwp_wanted = ('AR2' if gwp_act == 'SAR' else gwp_wanted)
    if len(set(gwp_prescribed)) > 1:
        sys.exit("combine_tables.py: the data have different GWPs and cannot be converted into each other.")
    elif len(set(gwp_prescribed)) == 1:
        gwp = gwp_prescribed[0]
        if ('gwp_wanted' in locals() and gwp != gwp_wanted):
            warn("combine_tables.py: the GWP of the basket (" + gwp + \
                 ") is used, instead of the provided GWP " + gwp_wanted + ".")
        else:
            print("combine_tables.py: the GWP of the basket (" + gwp + ") is used.")
        #endif
    elif 'gwp' in kwargs.keys():
        gwp = kwargs['gwp']
    else:
        gwp = meta.gwps.default
    #endif
    
    if 'new_attrs' in kwargs.keys():
        new_attrs = kwargs['new_attrs']
    else:
        new_attrs = {}
    #endif
    
    if how == 'add':
        operator = "+"
    elif how == 'subtract':
        operator = "-"
    elif how == 'multiply':
        operator = "*"
    elif how == 'divide':
        operator = "/"
    #endif
    
    # Using the first table as basis.
    # Converting the other tables to the units of this table, if they have the same family.
    # Updating the units if it is multipy or divide with data from different families.
    # If add or subtract: it has to be from the same family.
    # If multiply or divide: it does not need to be from the same family.

    table_new = hpf.copy_table(tables[0])
    table_new.__convert_to_baseunit__()
    attributes = pd.DataFrame(index=['cat', 'clss', 'ent', 'family', 'gwp',
        'scen', 'srce', 'tpe', 'unit'])
    for attr in attributes.index:
        if hasattr(table_new, attr):
            attributes.loc[attr, 0] = getattr(table_new, attr)
        #endif
    #endfor
    
    if how in ['add', 'subtract']:
        only_if_all_have_values = (kwargs['only_if_all_have_values'] 
            if 'only_if_all_have_values' in kwargs.values else False)
        for ind in range(1, len(tables)):
            table_act = tables[ind]
            all_indices = set(list(table_new.data.index) + list(table_act.data.index))
            all_columns = set(list(table_new.data.columns) + list(table_act.data.columns))
            table_act.data = table_act.data.reindex(index=all_indices)
            table_act.data = table_act.data.reindex(columns=all_columns)
            if table_new.family == table_act.family:
                if table_new.family == 'emi':
                    table_act.__convert_unit__(table_new.unit, gwp=table_new.gwp)
                else:
                    table_act.__convert_unit__(table_new.unit)
                #endif
                for attr in attributes.index:
                    attributes.loc[attr, ind] = getattr(table_act, attr)
                #endfor
                if how == 'add':
                    if only_if_all_have_values:
                        table_new.data = table_new.data.add(table_act.data)
                    else:
                        table_new.data = table_new.data.add(table_act.data, fill_value=0)
                    #endif
                else:
                    if only_if_all_have_values:
                        table_new.data = table_new.data.add(-1 * table_act.data)
                    else:
                        table_new.data = table_new.data.add(-1 * table_act.data, fill_value=0)
                    #endif
                #endif
            else:
                sys.exit("combine_tables.py: the tables have to belong to the same family.")
            #endif
        #endfor
    #endif
        
    if how in ['multiply', 'divide']:
        for ind in range(1, len(tables)):
            table_act = tables[ind]
            for attr in attributes.index:
                if hasattr(table_act, attr):
                    attributes.loc[attr, ind] = getattr(table_act, attr)
                #endif
            #endfor
            if table_new.family == table_act.family:
                if table_new.family == 'emi':
                    table_act.__convert_unit__(table_new.unit, gwp=gwp)
                else:
                    table_act.__convert_unit__(table_new.unit)
                #endif
                if how == 'multiply':
                    table_new.data = table_new.data.multiply(table_act.data)
                else:
                    table_new.data = table_new.data.div(table_act.data)
                #endif
            else:
                # Convert it to the 'base units'.
                table_act.__convert_to_baseunit__()
                if how == 'multiply':
                    table_new.data = table_new.data.multiply(table_act.data)
                else:
                    table_new.data = table_new.data.div(table_act.data)
                #endif
                table_new.unit = table_new.unit + operator + table_act.unit
                table_new.family = table_new.family + operator + table_act.family
            #endif
            for attr in attributes.index:
                if hasattr(table_act, attr):
                    attributes.loc[attr, ind] = getattr(table_act, attr)
                #endif
            #endfor
        #endfor
    #endif
    
    table_new.data.drop(table_new.data.index[table_new.data.isnull().all(axis=1)], inplace=True)
    
    for attr in attributes.index:
        if len(attributes.loc[attr, :].unique()) == 1:
            setattr(table_new, attr, attributes.loc[attr, 0])
        else:
            setattr(table_new, attr, (operator).join([xx for xx in attributes.loc[attr, :] if type(xx) == str]))
        #endif
    #endfor
    
    for new_attr in new_attrs.keys():
        setattr(table_new, new_attr, new_attrs[new_attr])
    #endif
    
    table_new.__tablename_to_standard__()
    table_new.__name_to_standard__()
    
    return table_new
#enddef

# %%

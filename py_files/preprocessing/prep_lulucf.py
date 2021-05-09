# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def prep_lulucf(database, meta, prios, srce_name, info_per_country, interpolation_method):
    """
    **Prepare LULUCF data (source prioritisation and gap filling)**
    
    Make *one LULUCF table, with the chosen KYOTOGHG_IPCMLULUCF time series*.
    *Prioritisation of data-sources as given in prios.*
    When a source has data, use them, and *fill data gaps* with 'constant filling' 
    (interpolation & forward extrapolation: mean over last values kept constant, 
    backward extrapolation: mean over first available values kept constant).
    If KYOTOGHG is calculated here from CO2 + CH4 + N2O: sum up the already 
    inter- & extrapolated time series.
    
    Problems with LULUCF data: high inter-annual variability, negative / positive emissions, 
    and the data we use are not consistent with the time series used in the pathway extension.
    
    *interpolation_method: 'constant' or 'linear'.*
    """
    
    # %%
    def calc_data():
        
        import numpy as np
        
        # KYOTOGHG/CO2/CH4/N2OAR4_IPCMLULUCF tables.
        available_tables = all_tables.ent[
            (all_tables.ent.isin([xx + meta.gwps.default for xx in meta.gases.lulucf + ['KYOTOGHG']])) &
            (all_tables.cat == 'IPCMLULUCF') & 
            (all_tables.clss == 'TOTAL') &
            (all_tables.tpe == 'NET') &
            (all_tables.scen.isin(['HISTORY', 'HISTCR'])) & 
            (all_tables.srce == srce)]
         
        # If KYOTOGHG is available, use it. Else use the sum over CO2 + CH4 + N2O_IPCMLULUCF.
        gases_to_sum = (['KYOTOGHG' + meta.gwps.default]
            if 'KYOTOGHG' + meta.gwps.default in available_tables.values
            else [xx + meta.gwps.default for xx in meta.gases.lulucf])
        
        # Sum up the data.
        sum_srce = pd.DataFrame(index=meta.isos.EARTH, columns=range(1990, 2051))
        # If there is no value available, it will stay NaN.
        
        nr_available_values_sum = pd.Series(index=meta.isos.EARTH, dtype='float64')
        
        for gas in gases_to_sum:
            
            tablename_orig = available_tables.index[available_tables == gas]
            
            if len(tablename_orig) > 0:
                
                table = hpf.copy_table(getattr(database, tablename_orig[0]))
                
                # Save the number of available values.
                nr_available_values = deepcopy(table.data)
                nr_available_values[table.data.isnull()] = 0
                nr_available_values[~table.data.isnull()] = 1
                nr_available_values = nr_available_values.sum(axis=1)
                nr_available_values_sum = nr_available_values_sum.add(nr_available_values, fill_value=0)
                
                # Fill the missing years (inter / extrapolate).
                table = table.__reindex__(years=range(1990, 2051))
                table.__interpolate__(interpolation_method) # 'constant' or 'linear'
                
                """
                For the future, use the mean over 2010 to whatever the most recent historical value is, 
                or if no values are available starting from 2010, use the last value.
                For the backward extrapolation use the mean over 1990 to 1997, or the first available value.
                """
                for iso3 in meta.isos.EARTH:
                    
                    available_years = [xx for xx in table.data.columns if not np.isnan(table.data.loc[iso3, xx])]
                    
                    if len(available_years) > 0:
                        
                        period_forward = range((2010 if 2010 in available_years else available_years[-1]), 2031) # Upper limit set to something later than last historical year.
                        period_backward = range(1990, (1998 if 1997 in available_years else available_years[0]))
                        table.data.loc[iso3, :] = hpf.timeseries_extrapolate(table.data.loc[iso3, :], 
                            'mean', 'forward', period=period_forward).values
                        table.data.loc[iso3, :] = hpf.timeseries_extrapolate(table.data.loc[iso3, :], 
                            'mean', 'backward', period=period_backward).values
                        
                        i have to fix the proble with IDN!!!
                
                # Add the 'filled-table' to sum_srce.
                sum_srce = sum_srce.add(table.data, fill_value=0)
        
        # Write out the table.
        table_kyotoghg = hpf.copy_table(table)
        table_kyotoghg.data = sum_srce
        table_kyotoghg.ent = 'KYOTOGHG'
        table_kyotoghg.scen = ('INTERCONST' if interpolation_method == 'constant' else 'INTERLIN')
        table_kyotoghg.note = f"Sum over CO2, CH4 and N2O. Interpolation method: {interpolation_method}."
        table_kyotoghg.__tablename_to_standard__()
        table_kyotoghg.__name_to_standard__()
        
        setattr(database, table_kyotoghg.tablename, table_kyotoghg)
        
        # Put the data to emi_lulucf.
        emi_lulucf[srce] = sum_srce
        
        # Uses the data from this source, if the KYOTOGHG values are not all NaN for that country.
        # Can also use it if not all single gases are given.
        nr_available_years_lulucf.loc[:, srce] = nr_available_values_sum.div(len(gases_to_sum))
        
        return nr_available_years_lulucf, emi_lulucf, database
    
    # %%
    def store_data():
        """
        *Only use a source if at least xx values are available for 1990 - 2017.*
        *If no other source has data, then use a source with less than xx values available nevertheless.*
        Store the DataFrames with various sources combined to one datatable in lulucf_table.
        """
        
        lulucf_table = pd.DataFrame(index=meta.isos.EARTH, columns=range(1990, 2051))
        
        for iso3 in nr_available_years_lulucf.index:
            
            nr_available_years_act = nr_available_years_lulucf.loc[iso3, :]
            
            use_srce = (
                [xx for xx in nr_available_years_act.index if nr_available_years_act[xx] > 0]
                if nr_available_years_act.max() < meta.lulucf.nr_available_values
                else [xx for xx in nr_available_years_act.index if nr_available_years_act[xx] >= meta.lulucf.nr_available_values])
            
            if len(use_srce) != 0:
                
                use_srce = use_srce[0]
                lulucf_table.loc[iso3, :] = emi_lulucf[use_srce].loc[iso3, :]
                info_per_country.loc[iso3, 'lulucf_source'] = use_srce
        
        # Store lulucf_table in the database.
        lulucf_table = hpf.create_table(data=lulucf_table, ent='KYOTOGHG', cat='IPCMLULUCF',
            clss='TOTAL', tpe='NET', srce=srce_name, 
            unit=meta.units.default['emi'], gwp=meta.gwps.default, family='emi',
            note="LULUCF data from different sources (one per country) were " + \
                "inter/extrapolated with constant values (interpolation & forward extrapolation: last value kept constant, " + \
                "backward extrapolation: first available value after 1990 used for 1990 to year of first available value). " + \
                '; '.join(sorted([xx + ": " + ', '.join(info_per_country.index[info_per_country.lulucf_source == xx]) 
                 for xx in info_per_country.lulucf_source.unique() if type(xx) == str])))
        lulucf_table.scen = ('INTERCONST' if interpolation_method == 'constant' else 'INTERLIN')
        lulucf_table.__tablename_to_standard__()
        lulucf_table.__name_to_standard__()
        
        setattr(database, lulucf_table.tablename, lulucf_table)
        
        return database, info_per_country
    
    # %%
    import pandas as pd
    import sys
    from copy import deepcopy
    import helpers_functions as hpf
    
    # %%    
    # TODO: somehow scale the LULUCF data we use (after filling the gaps) to the 
    # regional time series used in the pathway extension?
    # Problem: negative emissions (and different data sources).
    
    # Iterate through the prios sources.
    # Get a country vector per datatable for the countries which have data available between 1990 and 2017.
    
    if interpolation_method not in ['constant', 'linear']:
        
        sys.exit("interpolation_method not valid!")
    
    nr_available_years_lulucf = pd.DataFrame(index=meta.isos.EARTH, 
        columns=prios)
    
    all_tables = pd.DataFrame([xx.split('_') for xx in hpf.get_all_attributes_of_class(database)],
        index=hpf.get_all_attributes_of_class(database),
        columns=['ent', 'cat', 'clss', 'tpe', 'scen', 'srce'])
    
    emi_lulucf = {}
    
    for srce in prios:
        
        nr_available_years_lulucf, emi_lulucf, database = calc_data()
    
    """
    Only use a source if at least xx values are available for 1990 - 2017.
    If no other source has data, then use a source with less than xx values available nevertheless.
    Store the DataFrames with various sources combined to one datatable in lulucf_table.
    """
    database, info_per_country = store_data()
    
    return database, info_per_country
    
# %%
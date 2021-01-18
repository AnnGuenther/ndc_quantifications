# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
import pandas as pd
from copy import deepcopy
import helpers_functions as hpf

# %%
def prep_ssps_fill_gaps(database, info_per_country, meta, nrvalues):
    
    """
    **Fill gaps in down-scaled SSP data**
    
    *SSPs: check if there are countries that do have data in some SSPs but not in others and
    use the average over the available SSPs for the non-available SSPs.
    For countries that have PRIMAP-hist data but no SSP data at all (for SSP1 to SSP5), 
    use the PRIMAP-hist data and use the linear regression over the last 6 available years 
    as future estimates.*
    Only happens for countries with very low emissions.
    """
    
    # %%
    def fill_values(database, info_per_country, info_act, 
        primap_extrapol, nrvalues, ent, ssp, ssps_test, ssps_mean):
        
        # Copy the current datatable.
        ssp_to_fill = hpf.copy_table(
            getattr(database, '_'.join([ent, info_act['cat'], info_act['clss'], 
            info_act['tpe'], ssp, info_act['srce']])))
        
        # Fill with mean.
        # Which countries need to be filled?
        isos_to_fill = [xx for xx in ssps_test.index if ssps_test.loc[xx, :].any()]
        # Fill all isos_to_fill with the mean values.
        ssp_to_fill.data.loc[isos_to_fill, :] = ssps_mean.loc[isos_to_fill, :]
        
        # Put the information to info_per_country.
        for iso3 in isos_to_fill:
            if (ssps_test.loc[iso3, ssp]) and \
                not (ssps_mean.loc[:, range(2030, 2051)].isnull().all(axis=0).all()):
                info_per_country.loc[iso3, 'ssps_filled'] += ssp + " for " + ent + \
                    " filled with mean over available SSPs (" + \
                    ', '.join([xx for xx in ssps_test.loc[iso3, :].index
                    if not ssps_test.loc[iso3, xx]]) + ").\n"
        
        # Fill with regression.
        # Which countries need to be filled?
        isos_to_fill = [xx for xx in ssps_test.index if ssps_test.loc[xx, :].all()]
        # Fill all isos_to_fill with the regression.
        ssp_to_fill.data.loc[isos_to_fill, :] = primap_extrapol.reindex(index=isos_to_fill)
        
        # Put the information to info_per_country.
        for iso3 in isos_to_fill:
            info_per_country.loc[iso3, 'ssps_filled'] += ssp + " for " + ent + \
                " filled with PRIMAP data (extrapolated with linear regression over last " + \
                str(nrvalues) + " available values).\n"
        
        # Complete the information in the new table and put it to the database.
        ssp_to_fill.scen = ssp + 'FILLED'
        ssp_to_fill.__tablename_to_standard__()
        ssp_to_fill.__name_to_standard__()
        ssp_to_fill.note += "Check info_per_country.csv for further information."
        
        return ssp_to_fill
    
    # %%
    # ssps_ents: which entities are available from down-scaled SSPs.
    ssps_ents = {
        'emi': ['CO2', 'CH4', 'N2O', 'FGASES', 'KYOTOGHG'],
        'pop': ['POP'],
        'gdp': ['GDPPPP']}
    
    info_per_country.loc[:, 'ssps_filled'] = ''
    
    for family in ssps_ents.keys():
        
        info_act = getattr(meta.ssps, family)
        primap_scen, primap_srce = getattr(meta.primap, family)['scen'], getattr(meta.primap, family)['srce']
        
        for ent in ssps_ents[family]:
            
            # Check if there are countries that do have data in some SSPs but not in others and
            # use the average over the available SSPs for the non-available SSPs.
            ssps_test = pd.DataFrame(index=meta.isos.EARTH, columns=meta.ssps.scens.long)
            for ssp in meta.ssps.scens.long:
                # Checking for future values only (past is PRIMAP-hist).
                ssps_test.loc[:, ssp] = \
                    getattr(database, '_'.join([ent, info_act['cat'], info_act['clss'], 
                    info_act['tpe'], ssp, info_act['srce']])). \
                    data.loc[:, range(2030, 2051)].isnull().all(axis=1)
            
            # Concatenate all the SSPs to one dataframe and groupby index, then calculate the mean.
            # SSP1.
            ssps_mean = deepcopy(getattr(database, '_'.join([ent, info_act['cat'], info_act['clss'], 
                info_act['tpe'], meta.ssps.scens.long[0], info_act['srce']])).data)
            for ssp in meta.ssps.scens.long[1:]: # SSP2 to SSP5.
                ssps_mean = pd.concat((
                    ssps_mean, deepcopy(getattr(database, '_'.join([ent, info_act['cat'], info_act['clss'], 
                    info_act['tpe'], ssp, info_act['srce']])).data)))
            
            ssps_mean = ssps_mean.groupby(ssps_mean.index).mean()
            
            """
            For countries for which there are data available for some SSPs, but not for others, 
            use the average over the available SSPs for the non-available SSPs.
            And for countries that have PRIMAP-hist data, but no SSP data at all, use the PRIMAP-hist 
            data and use the linear regression over the last 6 available years as future estimates.
            """
            
            primap_act = deepcopy(getattr(database, '_'.join([ent, info_act['cat'], info_act['clss'], 
                info_act['tpe'], primap_scen, primap_srce])).data)
            # Reindex to 1990 to 2051 and extrapolate with the mean over the last 6 values.
            primap_act = primap_act.reindex(columns=range(min(primap_act.columns), 2051))
            primap_extrapol = hpf.timeseries_extrapolate(primap_act, 'mean', 'forward', nrvalues=nrvalues)
            
            for ssp in meta.ssps.scens.long:
                
                ssp_to_fill = fill_values(database, info_per_country, info_act, 
                    primap_extrapol, nrvalues, ent, ssp, ssps_test, ssps_mean)
                
                setattr(database, ssp_to_fill.tablename, ssp_to_fill)
        
    return database, info_per_country

# %%
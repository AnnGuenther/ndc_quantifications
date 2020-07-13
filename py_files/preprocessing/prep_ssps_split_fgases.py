# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
from copy import deepcopy
import pandas as pd
import sys
import helpers_functions as hpf

# %%
def prep_ssps_split_fgases(meta, database, nrvalues):
    
    """
    The SSPs only have data for FGASES, not separated into HFCS, PFCS, SF6 and NF3.
    For the calculation of the future pc_cov, a split into the four subgroups is performed.
    The historical share per gas/basket is kept constant and applied to the future FGASES-basket.
    The mean over the last 6 available years is used.
    """
    
    # %%
    def calc_and_store_data(database, meta, fgases_share, nrvalues):
        
        # Apply the calculated mean shares to the future FGASES and add tables to database.
        # Added for IPCM0EL and IPC2.
        set_atts = {'clss': 'TOTAL', 'tpe': 'NET', 'srce': 'SSPSPLIT',
                    'unit': meta.units.default['emi'], 'gwp': meta.gwps.default,
                    'family': 'emi'}
        
        for ssp in meta.ssps.scens.long:
            
            tablename_ssp = 'FGASES_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_' + meta.ssps.emi['srce']
            fgases_ssp = deepcopy(getattr(database, tablename_ssp).data)
            
            for gas in meta.gases.fgases:
                table = hpf.create_table(data=fgases_ssp.multiply(
                    fgases_share[gas].reindex(fgases_ssp.index).values, axis='index'),
                    ent=gas, scen=ssp+'FILLED')
                
                # Set attributes.
                tablename_primap_fgases = 'FGASE_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21'
                table.note = "The future values are calculated by applying the mean historic share for " + \
                    gas + " in the FGASES to the " + tablename_ssp + " (share: mean over last " + str(nrvalues) + \
                    " available values from " + tablename_primap_fgases.replace('FGASES', gas) + "/" + \
                    tablename_primap_fgases + ")."
                
                for attr in set_atts:
                    setattr(table, attr, set_atts[attr])
                
                for cat in ['IPCM0EL', 'IPC2']:
                    table_cat = hpf.copy_table(table)
                    table_cat.cat = cat
                    table_cat.__tablename_to_standard__()
                    table_cat.__name_to_standard__()
                    setattr(database, table_cat.tablename, table_cat)
            
            # Add the FGASES table for IPCM0EL also as IPC2.
            fgases_ssp = hpf.copy_table(getattr(database, tablename_ssp))
            fgases_ssp.category = 'IPC2'
            fgases_ssp.__tablename_to_standard__()
            fgases_ssp.__name_to_standard__()
            
            setattr(database, fgases_ssp.tablename, fgases_ssp)
        
        return database

    # %%
    # Get the primap data for HFCS, PFCS, SF6 and NF3.
    fgases_primap = {}
    for gas in meta.gases.fgases:
        fgases_primap[gas] = deepcopy(getattr(database, gas + '_IPCM0EL_TOTAL_NET_' + 
            meta.primap.emi['scen'] + '_' + meta.primap.emi['srce']).data)
    
    # Calculate the sum over the FGASES, instead of using the database entry for FGASES.
    # Should be the same...
    fgases_primap_total = pd.DataFrame(index=meta.isos.EARTH, columns=fgases_primap['HFCS'].columns)
    for gas in meta.gases.fgases:
        fgases_primap_total = fgases_primap_total.add(fgases_primap[gas], fill_value=0)
    
    # Are there countries for which differences exceed 0.1%?
    test = hpf.ratios_w_zeros(
        100. * fgases_primap_total.add(-
        getattr(database, 'FGASES_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi']).data, fill_value=0), 
        fgases_primap_total, dtype='pd.DataFrame').abs()
    test = test.index[test[test > .1].any(axis=1)]
    if len(test) > 0:
        sys.exit("preprocessing.py: the difference between the calculated sum over F-gases " +
            "and the database entry for FGASES is too high.")
    
    # Calculate the share of HFCS, PFCS, SF6 and NF3 in the total FGASES (historical values).
    fgases_primap['FGASES'] = fgases_primap_total
    fgases_share = {}
    for gas in meta.gases.fgases + ['FGASES']:
        # Some values for FGASES are 0, and one cannot divide by 0.
        # In hpf.ratios_w_zeros, zeros are replaced by nan before the division, and then put back into place.
        ratios = hpf.ratios_w_zeros(fgases_primap[gas], fgases_primap['FGASES'], dtype='pd.DataFrame')
        # Use the mean over the last 6 available years.
        fgases_share[gas] = hpf.timeseries_mean_nrvalues(ratios, nrvalues).loc[:, 'last_values']
    
    # Apply the calculated mean shares to the future FGASES and add tables to database.
    # Added for IPCM0EL and IPC2.
    database = calc_and_store_data(database, meta, fgases_share, nrvalues)
    
    return database
    
# %%
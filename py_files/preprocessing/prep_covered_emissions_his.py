# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
import pandas as pd
import sys
from copy import deepcopy
import helpers_functions as hpf

# %%
def prep_covered_emissions_his(database, coverage, meta, primap):
    
    """
    **Covered emissions (historical values based on per gas/sector emissions)**
    
    The *covered part of emissions (in 'emissions') is calculated here for historical years, 
    for which data per sector and gas combination are available.*
    The assessment is based on the information in coverage.used_per_combi (all entries are 'YES' or 'NO').
    All combinations with 'YES' are summed up to emicov_his, and all combinations with 'NO' are summed up to eminotcov_his.
    
    *For KYOTOGHG_IPCM0EL, excluding LULUCF.*
    """
    
    # %%
    def testing(new_kyoto_ipcm0el, database, meta):
        
        """
        Test if the sum over the covered and not-covered emissions (KYOTOGHG_IPCM0EL) 
        sum up to the original KYOTOGHG_IPCM0EL in 'database'.
        """
            
        # Are there countries for which differences exceed 0.1%?
        test = hpf.ratios_w_zeros(
            100. * new_kyoto_ipcm0el.add(-
            getattr(database, 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_' + \
            meta.primap.current_version['emi']).data, fill_value=0), 
            new_kyoto_ipcm0el, dtype='pd.DataFrame').abs()
        
        test = test.index[test[test > .1].any(axis=1)]
        
        if len(test) > 0:
            
            sys.exit("preprocessing.py: the difference between the calculated sum " +
                "over covered and not-covered KYOTOGHG_IPCM0EL " +
                "and the database entry for KYOTOGHG_IPCM0EL is too high.")
    
    # %%
    coverage.emicov_his = pd.DataFrame(0, index=meta.isos.EARTH, columns=primap['emi'].columns)
    coverage.eminotcov_his = deepcopy(coverage.emicov_his)
    
    calc_combis = {'COV': {'value_str': 'YES', 'note': 'covered', 'attr': 'emicov_his'},
                   'NOTCOV': {'value_str': 'NO', 'note': 'not-covered', 'attr': 'eminotcov_his'}}
    
    # Only for non-LULUCF.
    for combi in [xx for xx in meta.combis_gas_cat if 'LULUCF' not in xx]: # E.g., CO2_IPC1
        for case in calc_combis.keys(): # COV or NOTCOV.
            
            table = hpf.copy_table(getattr(database, combi + '_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi']))
            # All values are 0, and the ones that are covered are then replaced by the PRIMAP-hist emissions for that ent_cat.
            
            cov_act = pd.DataFrame(0., index=table.data.index, columns=table.data.columns)
            # E.g., case == COV --> all countries with YES.
            
            isos_to_add = coverage.used_per_combi.index[coverage.used_per_combi.loc[:, combi] == calc_combis[case]['value_str']]
            cov_act.loc[isos_to_add, :] = table.data.loc[isos_to_add, :]
            
            # Add the emissions from the current combi to the not/covered total.
            setattr(coverage, calc_combis[case]['attr'], 
                getattr(coverage, calc_combis[case]['attr']).add(cov_act, fill_value=0))
            
            # Put cov_act into the database, so that we also have the single tables on coverage per entity_category, 
            # additionally to the table for KYOTOGHG_IPCM0EL that will be added below.
            setattrs = {'data': cov_act, 'clss': case, 'tpe': 'EMI', 'scen': 'HISTORY', 
                        'srce': meta.primap.current_version['emi'], 'family': 'emi'}
            for attr in setattrs.keys():
                setattr(table, attr, setattrs[attr])
            
            table.__tablename_to_standard__()
            table.__name_to_standard__()
            table.note = "Part of emissions " + calc_combis[case]['note'] + " by an (I)NDC, based on per-country, " + \
                "per-main-sector and per-kyoto-GHG information from countries' (I)NDCs and their corresponding " + \
                meta.primap.emi['scen'] + '_' + meta.primap.emi['srce'] + " emissions."
            
            setattr(database, table.tablename, table)
    
    new_kyoto_ipcm0el = coverage.emicov_his.add(coverage.eminotcov_his, fill_value=0)
    
    # Test if the sum over the covered and not-covered emissions (KYOTOGHG_IPCM0EL) 
    # sum up to the original KYOTOGHG_IPCM0EL in 'database'.
    testing(new_kyoto_ipcm0el, database, meta)
        
    # Calculate pccov (values between 0 and 1, not 0% and 100%).
    coverage.pccov_his = hpf.ratios_w_zeros(coverage.emicov_his, new_kyoto_ipcm0el, dtype='pd.DataFrame')
    coverage.pcnotcov_his = hpf.ratios_w_zeros(coverage.eminotcov_his, new_kyoto_ipcm0el, dtype='pd.DataFrame')
    
    # Put the new tables to database (total emi(not)cov and total pc(not)cov).
    set_attrs = {
        'emicov_his': {
            'clss': 'COV', 'tpe': 'EMI', 'note': 'Part of emissions covered', 
            'unit': meta.units.default['emi']},
        'eminotcov_his': {
            'clss': 'NOTCOV', 'tpe': 'EMI', 'note': 'Part of emissions not-covered', 
            'unit': meta.units.default['emi']},
        'pccov_his': {
            'clss': 'COV', 'tpe': 'PC', 'note': 'Share of emissions covered', 
            'unit': meta.units.default['emi'] + "/" + meta.units.default['emi']},
        'pcnotcov_his': {
            'clss': 'NOTCOV', 'tpe': 'PC', 'note': 'Share of emissions not-covered', 
            'unit': meta.units.default['emi'] + "/" + meta.units.default['emi']}}
    
    for attr in set_attrs.keys():
        
        table = hpf.create_table(ent='KYOTOGHG', cat='IPCM0EL', clss=set_attrs[attr]['clss'],
            tpe=set_attrs[attr]['tpe'], scen='HISTORY', srce=meta.primap.current_version['emi'],
            unit=set_attrs[attr]['unit'], gwp=meta.gwps.default)
        table.note = set_attrs[attr]['note'] + " by an (I)NDC, based on per-country, " + \
                "per-main-sector and per-kyoto-GHG information from countries' (I)NDCs and their corresponding " + \
                meta.primap.emi['scen'] + '_' + meta.primap.emi['srce'] + " emissions."
        table.__tablename_to_standard__()
        table.__name_to_standard__()
        table.data = deepcopy(getattr(coverage, attr))
        
        setattr(database, table.tablename, table)
    
    return database, coverage

# %%
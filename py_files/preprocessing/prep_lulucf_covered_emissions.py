# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def prep_lulucf_covered_emissions(database, coverage, interpolation_method):
    """
    Calculate LULUCF emissions covered by an NDC.
    
    Based on KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTEREXTRAPOL_VARIOUS emissions time series (1990 - 2050).
    If LULUCF and CO$_2$ are not "NO", put KYOTOGHG_IPCMLULUCF to covered. Ignoring the information on CH4 and N2O.
    
    interpolation_method = 'constant' or 'linear'
    """
    
    # %%
    import helpers_functions as hpf
    
    # %%
    
    interpolation_method = ('INTERCONST' if interpolation_method == 'constant' else 'INTERLIN')
    tablename_orig = f'KYOTOGHG_IPCMLULUCF_TOTAL_NET_{interpolation_method}_VARIOUS'
    table_orig = getattr(database, tablename_orig).data
    
    # Check which countries don't have 'NO' in the 'coverage' of LULUCF and CO2.
    # The countries for which all data are NaN should stay NaN.
    isos_lu_cov = [xx for xx in table_orig.index 
        if ('NO' not in list(coverage.used_per_gas_per_sec.loc[xx, ['CO2', 'LULUCF']]))
        and not (table_orig.loc[xx, :].isnull().all())]
    isos_lu_notcov = [xx for xx in table_orig.index 
        if not 'NO' not in list(coverage.used_per_gas_per_sec.loc[xx, ['CO2', 'LULUCF']])
        and not (table_orig.loc[xx, :].isnull().all())]
    
    lu_cov = hpf.copy_table(getattr(database, tablename_orig))
    lu_notcov = hpf.copy_table(getattr(database, tablename_orig))
    
    lu_cov.data.loc[isos_lu_notcov, :] = 0.
    lu_notcov.data.loc[isos_lu_cov, :] = 0.
    
    # Put the tables into database.
    attrs_lu = {
        'COV': {
            'table': lu_cov,
            'note': "Emissions covered by a country's (I)NDC, based on " + tablename_orig + ". " + \
                "For countries that do not have 'NO' in the information on the coverage of CO2 and LULUCF, the total LULUCF emissions " + \
                "(CO2, CH4 and N2O) are set to be covered."},
        'NOTCOV': {
            'table': lu_notcov,
            'note': "Emissions not covered by a country's (I)NDC, based on " + tablename_orig + ". " + \
                "For countries that do have 'NO' in the information on the coverage of CO2 and LULUCF, the total LULUCF emissions " + \
                "(CO2, CH4 and N2O) are set to be not covered."}}
    
    for attr in attrs_lu.keys():
        
        table = attrs_lu[attr]['table']
        setattrs = {'clss': attr, 'tpe': 'EMI', 'srce': 'VARIOUS', 'note': attrs_lu[attr]['note']}
        [setattr(table, xx, setattrs[xx]) for xx in setattrs.keys()]
        table.scen = interpolation_method
        table.__tablename_to_standard__()
        table.__name_to_standard__()
        
        setattr(database, table.tablename, table)
    
    return database
# %%
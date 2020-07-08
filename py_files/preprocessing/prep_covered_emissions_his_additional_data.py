# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def prep_covered_emissions_his_additional_data(meta, database, primap):
    """
    Additionally calculate the historical emissions not-/covered for perGas_IPCM0EL and KYOTOGHG_perCategory.
    These values are not needed in further calculations, but nice to have.
    """
    
    # %%
    def covered_emissions_per_Gas_ipcm0el():
        # perGas_IPCM0EL coverage.
        # Sum up all the covered, e.g., CO2_IPC1/IPC2/IPCMAG/IPC4/IPC5.
        
        for gas in meta.gases.kyotoghg:
            for case in calc_combis.keys():
                
                sum_act = pd.DataFrame(0., index=meta.isos.EARTH, columns=primap['emi'].columns)
                
                for cat in meta.categories.main.exclLU:
                    
                    tablename = f"{gas}_{cat}_{case}_EMI_HISTORY_{meta.primap.current_version['emi']}"
                    if tablename in hpf.get_all_attributes_of_class(database):
                        table = deepcopy(getattr(database, tablename).data)
                        sum_act.loc[:, table.columns] = \
                            sum_act.loc[:, table.columns].add(table, fill_value=0)
                
                # Put the tables (not-/cov) to database.
                table = hpf.create_table(ent=gas, cat='IPCM0EL', tpe='EMI', clss=case, scen='HISTORY',
                    srce=meta.primap.current_version['emi'], data=sum_act, unit=meta.units.default['emi'], gwp=meta.gwps.default)
                table.__tablename_to_standard__()
                table.__name_to_standard__()
                table.note = "Part of emissions " + calc_combis[case]['note'] + " by an (I)NDC, based on per-country, " + \
                    "per-main-sector and per-kyoto-GHG information from countries' (I)NDCs and their corresponding " + \
                    meta.primap.emi['scen'] + '_' + meta.primap.emi['srce'] + " emissions."
                
                setattr(database, table.tablename, table)
        
        return database
    
    # %%
    def covered_emissions_per_category_kyotoghg():
        # KYOTOGHG_perCategory.
        # Sum up all the covered, e.g., CO2/CH4/N2O/HFCS/PFCS/SF6/NF3_IPC2.
        for cat in meta.categories.main.exclLU:
            for case in calc_combis.keys():
                
                sum_act = pd.DataFrame(0., index=meta.isos.EARTH, columns=primap['emi'].columns)
                
                for gas in meta.gases.kyotoghg:
                    
                    tablename = f"{gas}_{cat}_{case}_EMI_HISTORY_{meta.primap.current_version['emi']}"
                    if tablename in hpf.get_all_attributes_of_class(database):
                        table = deepcopy(getattr(database, tablename).data)
                        sum_act.loc[:, table.columns] = \
                            sum_act.loc[:, table.columns].add(table, fill_value=0)
                
                # Put the tables (not-/cov) to database.
                table = hpf.create_table(ent='KYOTOGHG', cat=cat, tpe='EMI', clss=case, scen='HISTORY',
                    srce=meta.primap.current_version['emi'], data=sum_act, unit=meta.units.default['emi'], gwp=meta.gwps.default)
                table.__tablename_to_standard__()
                table.__name_to_standard__()
                table.note = "Part of emissions " + calc_combis[case]['note'] + " by an (I)NDC, based on per-country, " + \
                    "per-main-sector and per-kyoto-GHG information from countries' (I)NDCs and their corresponding " + \
                    meta.primap.emi['scen'] + '_' + meta.primap.emi['srce'] + " emissions."
                
                setattr(database, table.tablename, table)
        
        return database
    
    # %%
    import pandas as pd
    from copy import deepcopy
    import helpers_functions as hpf
    
    # %%
    calc_combis = {
        'COV': {'value_str': 'YES', 'note': 'covered'},
        'NOTCOV': {'value_str': 'NO', 'note': 'not-covered'}}
    
    covered_emissions_per_Gas_ipcm0el()
    covered_emissions_per_category_kyotoghg()
    
    return database

# %%
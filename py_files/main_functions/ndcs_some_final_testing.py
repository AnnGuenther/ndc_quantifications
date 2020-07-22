# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in April 2020.
"""

# %%
def ndcs_some_final_testing(database, meta):

    """
    Doing some testing of the constructed global pathways.
    """
    
    import pandas as pd
    from pathlib import Path
    from warnings import warn
    
    # %%
    # EARTH pathways from output.
    ptws_earth = pd.read_csv(Path(meta.path.output_ndcs, 'ndc_targets_pathways_per_group.csv'))
    ptws_earth = ptws_earth.loc[ptws_earth.group == 'EARTH', :]
    
    # Pathways used for group pathways.
    ptws_used = pd.read_csv(Path(meta.path.output_ndcs, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    
    # NDC targets.
    ndc_targets = pd.read_csv(Path(meta.path.output_ndcs, 'ndc_targets.csv'))
    ndc_targets.drop(index=0, inplace=True) # Drop the units row.
    
    years_int = range(1990, 2051)
    years_str = [str(xx) for xx in years_int]
    
    # %%
    def check_one():
        """
        Check if the EARTH pathways for emi_bau, pop, gdp seem ok.
        """
        
        for condi, category, compare in ['emi_bau', 'IPCM0EL', database.emi_bl_exclLU], \
            ['pop', 'DEMOGR', database.pop], ['gdp', 'ECO', database.gdp]:
            
            data_test = ptws_earth.loc[
                (ptws_earth.condi == condi) & 
                (ptws_earth.category == category), years_str].values[0]
            
            # Compare the data to the sum over 'emi_bl_exclLU' in database.
            data_compare = compare.data.loc[meta.isos.EARTH, years_int].sum()
            
            data_diff = data_compare.add(-data_test, fill_value=0)
            if (data_diff.abs() > data_compare*.01).any():
                warn(f"ndcs_some_testing.py check_one: the difference between the input for {condi} and the EARTH pathway is > 1%.")
    
    check_one()
    
    # %%
    def check_two():
        """
        Check if the EARTH pathways for pc_cov, emi_cov seem ok.
        """
        emi_tot = ptws_earth.loc[(ptws_earth.condi == 'emi_bau') & (ptws_earth.category == 'IPCM0EL'), years_str].values[0]
        emi_cov = ptws_earth.loc[(ptws_earth.condi == 'emi_cov') & (ptws_earth.category == 'IPCM0EL'), years_str].values[0]
        pc_cov = ptws_earth.loc[(ptws_earth.condi == 'pc_cov') & (ptws_earth.category == 'IPCM0EL'), years_str].values[0]
        
        emi_cov_compare = emi_tot * pc_cov/100.
        emi_cov_diff = emi_cov - emi_cov_compare
        if (abs(emi_cov_diff) > emi_cov*.01).any():
            warn(f"ndcs_some_testing.py check_two: the difference between the input for emi_cov and the EARTH pathway is > 1%.")
    
    check_two()
    
    # %%
    def check_three():
        """
        Check if the 'used' EARTH pathways seem ok.
        """
        for condi, category, compare in ['emi_bau', 'IPCM0EL', database.emi_bl_exclLU], \
            ['pop', 'DEMOGR', database.pop], ['gdp', 'ECO', database.gdp]:
            
            data_test = ptws_used.loc[
                (ptws_used.condi == condi) & 
                (ptws_used.category == category), years_str].sum().values
            
            # Compare the data to the sum over 'emi_bl_exclLU' in database.
            data_compare = compare.data.loc[meta.isos.EARTH, years_int].sum()
            
            data_diff = data_compare.add(-data_test, fill_value=0)
            if (data_diff.abs() > data_compare*.01).any():
                warn(f"ndcs_some_testing.py check_three: the difference between the input for {condi} and the EARTH pathway is > 1%.")
    
    check_three()
    
    # %%
    def check_four():
        """
        Check if the target pathways for EARTH seem ok.
        """
        category = 'IPCM0EL'
        for condi, rge in ['conditional', 'worst'], ['conditional', 'best'], \
            ['unconditional', 'worst'], ['unconditional', 'best']:
            
            data_test = ptws_used.loc[
                (ptws_used.condi == condi) & (ptws_used.rge == rge) &
                (ptws_used.category == category), years_str].sum().values
            
            # Compare the data to the values in ndc_targets_pathways_per_group.csv.
            data_compare = ptws_earth.loc[
                (ptws_earth.condi == condi) & (ptws_earth.rge == rge) &
                (ptws_earth.category == category), years_str].values[0]
            
            data_diff = data_test - data_compare
        if (abs(data_diff) > data_compare*.01).any():
            warn(f"ndcs_some_testing.py check_four: the difference between the input for {condi}_{rge} and the EARTH pathway is > 1%.")
        
    check_four()    
    
# %%

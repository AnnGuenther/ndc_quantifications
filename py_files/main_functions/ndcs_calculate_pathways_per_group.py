# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def ndcs_calculate_pathways_per_group(
    pathways_per_country, meta):
    """
    Calculate the emissions pathways for a group of countries by summing up all available per-country pathways, 
    per un/conditional_best/worst (chosing one of the target types per country).
    And using baseline emissions where no target is available.

    Chosen per-country pathways stored in ndc_targets_pathways_per_country_used_for_group_pathways.csv.
    Group pathways stored in ndc_targets_pathways_per_group.csv.
    """
    
    # %%
    def get_pathways_per_country_used_for_group_pathways(
        input_pathways, pathways_per_country, meta):
        """
        Get the 'chosen' country-pathways that will be used for the group pathways.
        Depend on the preferred (and available) target types.

        Chosen per-country pathways stored in ndc_targets_pathways_per_country_used_for_group_pathways.csv.
        """
        
        import pandas as pd
        from pathlib import Path
        from warnings import warn
        
        # First get the 'chosen' country-pathways.
        ptws_chosen_per_country = pd.DataFrame(
            columns=['add_info', 'iso3', 'tar_type_used', 
                'condi', 'rge', 'entity', 'category', 'unit', 'gwp'] + list(meta.years.all))
        
        tars_to_use = pd.Series(index=meta.isos.EARTH, dtype='object')
        
        for iso_act in meta.isos.EARTH:
            
            # Use info for EU if country belongs to EU.
            iso_ndc = (meta.EU if iso_act in meta.EU_isos else iso_act)
            
            # Get the time series from pathways_per_country for that country (not pc_cov / pc_ncov).
            ts_iso = pathways_per_country.loc[pathways_per_country.iso3 == iso_act, :]. \
                reindex(columns=ptws_chosen_per_country.columns)
            
            for ent in [xx for xx in input_pathways.keys() if ('pc_cov' not in xx and 'pc_ncov' not in xx)]:
                
                ts_act = ts_iso.loc[
                    (ts_iso.rge == input_pathways[ent]['rge']) &
                    (ts_iso.entity == input_pathways[ent]['ent']) &
                    (ts_iso.category == input_pathways[ent]['cat']), :]
                # Add them to ptws_chosen_per_country.
                ptws_chosen_per_country = ptws_chosen_per_country.append(ts_act, ignore_index=True)
            
            # Get the target types for the calculation of the group pathways (following meta.ndcs_type_prioritisations).
            if iso_act not in meta.calculate_targets_for_ctr:
                
                # If that is true the baseline emissions are to be used.
                tar_used = 'baseline_emissions'
            
            else: # Check which target type to use.
                
                # Use TYPE_RECLASS or baseline_emissions if ndcs_type_prioritisations is not to be used.
                if not meta.ndcs_type_prioritisations['use_it']:
                    
                    if iso_ndc in list(meta.ndcs_info.index):
                        tar_used = meta.ndcs_info.loc[iso_ndc, 'TYPE_RECLASS']
                
                else:
                    # Choose the prioritised target types if available, else use TYPE_RECLASS or baseline_emissions.
                    if iso_act in meta.ndcs_type_prioritisations['countries']:
                        
                        tar_chosen = []
                        for type_prio in meta.ndcs_type_prioritisations['ndcs_type_prioritisations']:
                            
                            if type_prio.upper() in ['TYPE_RECLASS', 'TYPE_MAIN']:
                                tar_chosen = tar_chosen + [meta.ndcs_info.loc[iso_ndc, type_prio.upper()]]
                                
                            else:
                                tars_available_now = [xx 
                                    for xx in pathways_per_country.loc[pathways_per_country.iso3 == iso_act, 'tar_type_used'].unique()
                                    if xx == type_prio]
                                
                                if len(tars_available_now) > 0:
                                    tar_chosen += [type_prio]
                        
                        # Choose the prioritised target types if available, else use TYPE_RECLASS or baseline_emissions.
                        tar_used = (tar_chosen[0] if len(tar_chosen) > 0 else meta.ndcs_info.loc[iso_ndc, 'TYPE_RECLASS'])
                    
                    else: # TYPE_RECLASS or baseline_emissions.
                        tar_used = meta.ndcs_info.loc[iso_ndc, 'TYPE_RECLASS']
                    
                    # If the target type is NGT, try to choose another type.
                    # Preferably ABS, RBY or RBU.
                    # TODO: check that. If the type_main is NGT, we use ABS, RBY, or RBU nevertheless?
                    # Better use type_reclass in that case?
                    if tar_used == 'NGT':
                        tars_available = [xx 
                            for xx in pathways_per_country.loc[pathways_per_country.iso3 == iso_act, 'tar_type_used'].unique()
                            if xx != 'NGT']
                        
                        if len(tars_available) > 0:
                            if 'ABS' in tars_available:
                                tar_used = 'ABS'
                            elif 'RBY' in tars_available:
                                tar_used = 'RBY'
                            elif 'RBB' in tars_available:
                                tar_used = 'RBU'
                            else:
                                tar_used = tars_available[0]
                        else:
                            tar_used = 'baseline_emissions'
            
            if 'tar_used' not in locals() or tar_used == 'NGT' or type(tar_used) != str:
                tar_used = 'baseline_emissions'
            
            tars_available = [xx 
                for xx in pathways_per_country.loc[pathways_per_country.iso3 == iso_act, 'tar_type_used'].unique()
                if type(xx) == str]
            if tar_used not in tars_available:
                warn(f"Something went wrong for {iso_act} and a target type was chosen for the group pathways that does not have values.")
            
            tars_to_use[iso_act] = tar_used
                        
            # Get the pathways for the chosen target type.
            ptws_chosen_per_country = ptws_chosen_per_country.append(
                pathways_per_country.loc[(pathways_per_country.iso3 == iso_act) & (pathways_per_country.tar_type_used == tars_to_use[iso_act]), :]. \
                reindex(columns=ptws_chosen_per_country.columns).reindex(columns=ptws_chosen_per_country.columns), ignore_index=True)
        
        # Write out the chosen time series.
        file_name = 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'
        ptws_chosen_per_country.to_csv(Path(meta.path.output_ndcs, file_name), index=False)
        
        return ptws_chosen_per_country, tars_to_use
    
    # %%
    def calc_pathways_of_group(input_pathways, ptws_groups, ptws_chosen_per_country, 
        meta, group_act, tars_to_use):
        """
        Calculate the group pathways (for un/conditional best/worst; using the chosen country-pathways).
        """
        
        import pandas as pd
        import numpy as np
        from warnings import warn
        import helpers_functions as hpf
        
        # Set up 'ptws' for the current group.
        condi_rges = ['unconditional_worst', 'unconditional_best', 'conditional_worst', 'conditional_best']
        ptws = pd.DataFrame(
            index=list(input_pathways.keys()) + 
            [xx + '_IPCM0EL' for xx in condi_rges], 
            columns=ptws_groups.columns)
        
        # ISO3s for the group. Only use ISO3s that are in meta.isos.EARTH + meta.EU.
        # Replace EU by single countries, if EU is in the list.
        if group_act == meta.EU:
            isos_group = meta.EU_isos
        elif group_act == 'EARTH':
            isos_group = meta.isos.EARTH
        else:
            isos_group = sorted(hpf.get_isos_for_groups(group_act, 'ISO3'))
        
        isos_group = [xx for xx in isos_group if xx in meta.isos.EARTH + [meta.EU]]
        if meta.EU in isos_group:
            isos_group = sorted(set(isos_group + meta.EU_isos))
        
        ptws.loc[:, 'iso3s'] = ', '.join(isos_group)
        
        additional_info = ['condi', 'rge', 'entity', 'category', 'unit', 'gwp']
        
        # Calculate the group pathways (for un/conditional best/worst), if possible.
        if isos_group == [np.nan]:
            warn("ndcs_calculate_pathways_per_group.py: no ISO3s available for group " + group_act + "!")
            
        else:
                        
            # Sum over the time series of the countries in isos_group.
            # Not the pc_cov / pc_ncov values.
            for ent in [xx for xx in input_pathways.keys() if not xx.startswith('pc_')]:
                data_to_sum = ptws_chosen_per_country.loc[
                    (ptws_chosen_per_country.iso3.isin(isos_group)) &
                    (ptws_chosen_per_country.rge == input_pathways[ent]['rge']) &
                    (ptws_chosen_per_country.entity == input_pathways[ent]['ent']) &
                    (ptws_chosen_per_country.category == input_pathways[ent]['cat']), :]
                ptws.loc[ent, meta.years.all] = data_to_sum.loc[:, meta.years.all].sum(axis=0).values
                ptws.loc[ent, additional_info] = data_to_sum.loc[data_to_sum.index[0], additional_info]
            
            # Calculate pc_cov. As sum over 100 * emi_cov / emi_bau.
            cov_case = 'cov'
            bl_case = '_exclLU'
            ptws.loc['pc_' + cov_case + bl_case, meta.years.all] = \
                100. * hpf.ratios_w_zeros(
                    ptws.loc[
                        (ptws.rge == input_pathways['emi_' + cov_case + bl_case]['rge']) &
                        (ptws.entity == input_pathways['emi_' + cov_case + bl_case]['ent']) &
                        (ptws.category == input_pathways['emi_' + cov_case + bl_case]['cat']), 
                        meta.years.all].values[0],
                    ptws.loc[
                        (ptws.rge == input_pathways['emi_bl' + bl_case]['rge']) &
                        (ptws.entity == input_pathways['emi_bl' + bl_case]['ent']) &
                        (ptws.category == input_pathways['emi_bl' + bl_case]['cat']), 
                        meta.years.all].values[0])
            
            ptws.loc['pc_' + cov_case + bl_case, additional_info] = \
                [input_pathways['pc_' + cov_case + bl_case]['rge']]*2 + \
                [input_pathways['pc_' + cov_case + bl_case]['ent'], 
                input_pathways['pc_' + cov_case + bl_case]['cat'], '%', meta.gwps.default]
            
            # Sum over time series of IPCM0EL un/conditional & worst/best.
            cat = 'IPCM0EL'
            for condi in ['unconditional', 'conditional']:
                for rge in ['worst', 'best']:
                    row = condi + '_' + rge + '_' + cat
                    data_to_sum_tars = ptws_chosen_per_country.loc[
                        (ptws_chosen_per_country.iso3.isin(isos_group)) &
                        (ptws_chosen_per_country.condi == condi) &
                        (ptws_chosen_per_country.rge == rge) &
                        (ptws_chosen_per_country.category == cat), :]
                    ptws.loc[row, meta.years.all] = data_to_sum_tars.loc[:, meta.years.all].sum(axis=0).values
                    # Additional information.
                    ptws.loc[row, additional_info] = data_to_sum_tars.loc[data_to_sum_tars.index[0], additional_info]
            
            # Information on the NDC target types used for the group pathways.
            ptws.loc[:, 'ndc_types_used'] = \
                '.\n'.join(zz for zz in 
                [xx + ": " + ', '.join([yy for yy in tars_to_use.index[tars_to_use == xx] if yy in isos_group])
                for xx in ['baseline_emissions'] + list(set(set(meta.target_types) - set(['NGT'])))] if len(zz) > 6) + '.'
            
            ptws.loc[:, 'group'] = group_act
        
        return ptws
    
    # %%
    import pandas as pd
    from pathlib import Path
    
    # %%
    input_pathways = {
        'emi_bl_exclLU': {
            'name': 'IPCM0EL', 'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'rge': 'emi_bau'},
        'pc_cov_exclLU': {
            'name': 'pc_cov_exclLU', 'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'rge': 'pc_cov'},
        'emi_cov_exclLU': {
            'name': 'emi_cov_exclLU', 'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'rge': 'emi_cov'},
        'emi_ncov_exclLU': {
            'name': 'emi_ncov_exclLU', 'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'rge': 'emi_ncov'},
        'pop': {
            'name': 'pop', 'ent': 'POP', 'cat': 'DEMOGR', 'rge': 'pop'},
        'gdp': {
            'name': 'gdp', 'ent': 'GDPPPP', 'cat': 'ECO', 'rge': 'gdp'}}
    
    # First get the 'chosen' country-pathways that will be used for the group pathways.
    # Depends on the preferred (and available) target types.
    ptws_chosen_per_country, tars_to_use = get_pathways_per_country_used_for_group_pathways(
        input_pathways, pathways_per_country, meta)
    
    # Setup 'ptws_groups' to store all the pathways.
    ptws_groups = pd.DataFrame(
        columns=['group', 'iso3s', 'ndc_types_used', 
            'condi', 'rge', 'entity', 'category', 'unit', 'gwp'] + list(meta.years.all))
    
    # Calculate the pathways per group.
    for group_act in sorted(set(meta.groups_for_which_to_calculate_pathways +
        [meta.EU, 'EARTH', 'R5ASIA', 'R5LAM', 'R5MAF', 'R5OECD', 'R5REF'])):
        
        # Calculate the group pathways (for un/conditional best/worst).
        ptws_groups = ptws_groups.append(
            calc_pathways_of_group(input_pathways, ptws_groups, ptws_chosen_per_country, 
                meta, group_act, tars_to_use), ignore_index=True)
    
    # Write out 'ptws_groups'.
    file_name = 'ndc_targets_pathways_per_group.csv'
    ptws_groups.to_csv(Path(meta.path.output_ndcs, file_name), index=False)
    
    print("done calculating the per-group pathways ...")
    
    return ptws_groups, ptws_chosen_per_country

# %%
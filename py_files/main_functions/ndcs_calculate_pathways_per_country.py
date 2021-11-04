# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2021

04/2021:
    Add country pathways (with our methods) for CAT estimates (values for target years).
    Add option meta.use_baseline_if_target_above_bl.
"""

# %% 
def ndcs_calculate_pathways_per_country(database, calculated_targets, meta):
    """
    Calculate the pathway per country and target (per un/conditional best/worst).
    Only for IPCM0EL.

    Stored in 'ndc_targets_pathways_per_country.csv'.
    """
    
    # %%
    def add_timeseries(meta, database, ptws_all):
        """
        Get the cydata for all countries (are stored in ts_act.data) and add some information (gwp, category, ...).
        """
        
        import pandas as pd
        import numpy as np
        from copy import deepcopy
        
        # Get time series for input_pathways.keys() (timeseries for all countries).
        # Values for columns condi & range.
        input_pathways = {
            'emi_bl_exclLU': 'emi_bau', 
            'pc_cov_exclLU': 'pc_cov', 
            'emi_cov_exclLU': 'emi_cov', 
            'emi_ncov_exclLU': 'emi_ncov',
            'pop': 'pop', 
            'gdp': 'gdp'}
        
        for timeseries in input_pathways.keys():
            
            ts_act = getattr(database, timeseries)
            
            ts_add = pd.DataFrame(index=meta.isos.EARTH, columns=ptws_all.columns)
            ts_add.loc[:, 'iso3'] = meta.isos.EARTH
            ts_add.loc[:, ['condi', 'rge', 'entity', 'category', 'unit', 'gwp']] = \
                input_pathways[timeseries], input_pathways[timeseries], ts_act.ent, ts_act.cat, ts_act.unit, \
                (ts_act.gwp if hasattr(ts_act, 'gwp') else np.nan)
            ts_add.loc[:, meta.years.all] = deepcopy(ts_act.data. \
                reindex(index=meta.isos.EARTH). \
                reindex(columns=ptws_all.columns))
        
            ptws_all = ptws_all.append(ts_add, ignore_index=True)
        
        return ptws_all
    
    # %%
    def add_targets_from_other_conditionality_if_needed(meta, targets_act):
        """
        If there is a value in unconditional_best in a year, but not in unconditional_worst, put it there.
        If there is a value in conditional_best in a year, but not in conditional_worst, put it there.
        If there is a value in unconditional in a year, but not in conditional, put it there (the one 
        stored in 'unconditional_worst').
        """
    
        import numpy as np
        
        # If there is a value in unconditional_best in a year, but not in unconditional_worst, put it there.
        yrs_info = []
        
        for yr_act in meta.years.pathways:
            
            if (~np.isnan(targets_act.loc['unconditional_best', yr_act]) \
            and np.isnan(targets_act.loc['unconditional_worst', yr_act])):
                
                targets_act.loc['unconditional_worst', yr_act] = \
                    targets_act.loc['unconditional_best', yr_act]
                yrs_info += [yr_act]
        
        # Put information to add_info.
        if len(yrs_info) > 0:
            
            targets_act.loc['unconditional_worst', 'add_info'] += \
                "The target value from 'unconditional_best' was used for 'unconditional_worst' in " + \
                ', '.join([str(xx) for xx in yrs_info]) + ".\n"
        
        # If there is a value in conditional_best in a year, but not in conditional_worst, put it there.
        yrs_info = []
        
        for yr_act in meta.years.pathways:
            
            if (~np.isnan(targets_act.loc['conditional_best', yr_act]) \
            and np.isnan(targets_act.loc['conditional_worst', yr_act])):
                
                targets_act.loc['conditional_worst', yr_act] = \
                    targets_act.loc['conditional_best', yr_act]
                yrs_info += [yr_act]
        
        # Put information to add_info.
        if len(yrs_info) > 0:
            
            targets_act.loc['conditional_worst', 'add_info'] += \
                "The target value from 'conditional_best' was used for 'conditional_worst' in " + \
                ', '.join([str(xx) for xx in yrs_info]) + ".\n"
        
        # If there is a value in unconditional_best in a year, but not in conditional (testing for best), 
        # put it there.
        yrs_info = []
        
        for yr_act in meta.years.pathways:
            
            if (~np.isnan(targets_act.loc['unconditional_best', yr_act]) \
            and np.isnan(targets_act.loc['conditional_best', yr_act])):
                
                targets_act.loc[['conditional_worst', 'conditional_best'], yr_act] = \
                    targets_act.loc['unconditional_best', yr_act]
                yrs_info += [yr_act]
        
        # Put information to add_info.
        if len(yrs_info) > 0:
            
            for case in ['conditional_worst', 'conditional_best']:
                
                targets_act.loc['conditional_worst', 'add_info'] += \
                    "The target value from 'unconditional_best' was used for '" + case + "' in " + \
                    ', '.join([str(xx) for xx in yrs_info]) + ".\n"
        
        return targets_act
    
    # %%
    def calculate_pathways(ptws_all, emi_bl_act, targets_act, curr_tpe, curr_tar, iso_act, meta):
        """
        Calculate the pathways per un/conditional_best/worst, assuming a linear in/decrease of the 
        % difference to the baseline emissions.
        E.g., if the country has one unconditional_best target that equals a reduction of 20% in 2030 
        (compared to baseline emissions):
        the pathway has a 0% reduction in meta.years.pathways[0], and in 2030 the given
        20% reduction, with a linear increase between meta.years.pathways[0] and 2030.
        
        Use the baseline emissions for 2020.
        Calculate the percentage level (how much percent of the baseline emissions do 
        the single target emissions represent).
        pc_level: interpolate between available values,
        and keep the last available value of pc_level constant (if meta.method_pathways == 'constant_percentages'),
        or keep the absolute difference constant (if meta.method_pathways == 'constant_difference'),
        or keep the last emissions level constant (if meta.method_pathways == 'constant_emissions').
        
        E.g., 2020 is 100%, 2030 is 80%. For 2025 it is 100% + (80%-100%)/(2030-2020) * (2025-2020) = 90%.
        All values of pc_level are 100% (= baseline emissions) if there are no available_years.
        baseline emissions are used in years before the first meta.years.pathways.
        Apply pc_level to baseline emissions to calculate the pathway.
        """
        
        import pandas as pd
        import numpy as np
        from helpers_functions.data_manipulation.ratios_w_zeros import ratios_w_zeros
    
        # Per un/conditional_best/worst.
    
        # Set up 'ptw_calc' to store the pathways for the current 'curr_tar'.
        ptw_calc = pd.DataFrame(
            index=['years', 'targets', 'baseline', 'pathway'],
            columns=ptws_all.columns)
        ptw_calc.add_info = ''
        
        # Add some information.
        ptw_calc.loc[:, ['add_info', 'iso3', 'tar_type_used', 'entity', 'category', 'unit', 'gwp']] = \
            [targets_act.loc[curr_tar, 'add_info'], iso_act, curr_tpe] + \
            [getattr(emi_bl_act, xx) for xx in ['ent', 'cat', 'unit', 'gwp']]
        
        # Un/conditiona best/worst?
        ptw_calc.loc[:, ['condi', 'rge']] = \
            ('unconditional' if 'unconditional' in curr_tar else 'conditional'), \
            ('best' if 'best' in curr_tar else 'worst')
        
        # Years.
        ptw_calc.loc['years', meta.years.pathways] = meta.years.pathways
        
        # For each target year get the target year emissions.
        ptw_calc.loc['targets', :] = targets_act.loc[curr_tar, :].values
        
        # Baseline emissions.
        ptw_calc.loc['baseline', :] = emi_bl_act.data.loc[iso_act, :]. \
            reindex(index=ptw_calc.columns).values
        
        # Use the baseline emissions for 2020 (first year of pathway calculation).
        ptw_calc.loc['targets', meta.years.pathways[0]] = ptw_calc.loc['baseline', meta.years.pathways[0]]
        
        # Calculate the percentage level (how much percent of the baseline emissions do 
        # the single target emissions represent).
        ptw_calc.loc['pc_level', meta.years.pathways] = \
            ratios_w_zeros(ptw_calc.loc['targets', meta.years.pathways].to_list(), 
                           ptw_calc.loc['baseline', meta.years.pathways].to_list())
        
        # pc_level: interpolate between available values, and keep the last available value constant.
        # E.g., 2020 is 100%, 2030 is 80%. For 2025 it is 100% + (80%-100%)/(2030-2020) * (2025-2020) = 90%.
        available_years = ptw_calc.loc['pc_level', meta.years.pathways].index[
            ~ptw_calc.loc['pc_level', meta.years.pathways].isnull()]
        # All values of pc_level are 100% (= baseline emissions) if there are no available_years:
        if len(available_years) == 0:
            
            ptw_calc.loc['pc_level', meta.years.pathways] = 1.
        
        else:
            
            available_vals = [ptw_calc.loc['pc_level', xx] for xx in available_years]
            
            for interp in range(len(available_vals) - 1):
                
                interp_vals = [
                    available_vals[interp] + \
                    (available_vals[interp + 1] - available_vals[interp]) / \
                    (available_years[interp + 1] - available_years[interp]) * \
                    (xx - available_years[interp]) \
                    for xx in range(available_years[interp], available_years[interp + 1])]
                ptw_calc.loc['pc_level', \
                    [xx for xx in np.arange(available_years[interp], available_years[interp + 1])]] = \
                    interp_vals
            
            """
            Keep pc_level constant after last available target for targets that are below the baseline of that year.
            """
            ptw_calc.loc['pc_level', \
                [xx for xx in np.arange(available_years[-1], meta.years.pathways[-1] + 1)]] = \
                ptw_calc.loc['pc_level', available_years[-1]]
        
        # Put baseline emissions to years before the first meta.years.pathways.
        years_baseline = list(set(set(meta.years.all) - set(meta.years.pathways)))
        ptw_calc.loc['pathway', years_baseline] = ptw_calc.loc['baseline', years_baseline]
        
        # Apply pc_level to baseline emissions.
        ptw_calc.loc['pathway', meta.years.pathways] = \
            ptw_calc.loc['pc_level', meta.years.pathways].multiply(
                ptw_calc.loc['baseline', meta.years.pathways])
        
        """
        If the last target is higher than the baseline, use the same growth as in the baseline.
        Else, the mitigated pathway can increase a lot.
        """
        if ptw_calc.loc['targets', available_years[-1]] > ptw_calc.loc['baseline', available_years[-1]]:
            
            years_to_adjust = range(available_years[-1], meta.years.pathways[-1]+1)
            ptw_calc.loc['pathway', years_to_adjust] = \
                ptw_calc.loc['baseline', years_to_adjust].values + \
                    (ptw_calc.loc['targets', available_years[-1]] - \
                     ptw_calc.loc['baseline', available_years[-1]])
        
        """
        Keep the emissions constant after last available target if meta.method_pathways == 'constant_emissions'.
        Else the pc_level or the absolute difference is kept constant.
        """
        yrs_ptw = range(available_years[-1], meta.years.pathways[-1] + 1)
        
        if meta.method_pathways == 'constant_emissions':
            
            ptw_calc.loc['pathway', yrs_ptw] = ptw_calc.loc['pathway', available_years[-1]]
        
        if meta.method_pathways == 'constant_difference':
            
            const_diff = ptw_calc.loc['baseline', available_years[-1]] - ptw_calc.loc['pathway', available_years[-1]]
            ptw_calc.loc['pathway', yrs_ptw] = ptw_calc.loc['baseline', yrs_ptw].add(-const_diff)
        
        """
        If the country has an entry for 'DECLINE_AFTER_YEAR': stop the mitigated emissions from increasing after that year.
        """
        decline_after_year = meta.ndcs_info.loc[iso_act, 'DECLINE_AFTER_YEAR']
        
        if (type(decline_after_year) != str and not np.isnan(decline_after_year)):
            
            # Check if pathway already declines after that year.
            decline_after_year = int(decline_after_year)
            does_it_decline = all([False if ptw_calc.loc['pathway', xx+1] >= ptw_calc.loc['pathway', xx] else True
                for xx in range(decline_after_year, ptw_calc.columns[-1]-1)])
            
            if not does_it_decline:
                
                ptw_calc.loc['pathway', range(decline_after_year+1, ptw_calc.columns[-1]+1)] = ptw_calc.loc['pathway', decline_after_year]
        
        return ptw_calc.loc['pathway', :]
    
    # %%
    def add_baseline_emissions(emi_bl_act, meta, iso_act, columns):
        
        """
        Add the baseline emissions for each iso3 (as un/conditional best/worst pathways).
        """
        import pandas as pd
        
        targets_act = pd.DataFrame(
            index=['unconditional_worst', 'unconditional_best', 'conditional_worst', 'conditional_best'],
            columns=columns)
        targets_act.loc[:, ['condi', 'rge']] = \
            [['unconditional', 'worst'], ['unconditional', 'best'], ['conditional', 'worst'], ['conditional', 'best']]
        targets_act.loc[:, 'add_info'] = \
            "No targets calculated, so the baseline emissions are put in as " + \
            "target pathways for all un/conditional best/worst pathways.\n"
        targets_act.loc[:, ['iso3', 'tar_type_used', 'entity', 'category', 'unit', 'gwp'] + list(meta.years.all)] = \
            [iso_act, 'baseline_emissions'] + [getattr(emi_bl_act, xx) for xx in ['ent', 'cat', 'unit', 'gwp']] + \
            emi_bl_act.data.loc[iso_act, meta.years.all].to_list()
        
        return targets_act
    
    # %%
    import pandas as pd
    from pathlib import Path
    from helpers_functions.classes_tables.copy_table import copy_table
    
    # %%
    # Set up dataframe 'ptws_all'.
    ptws_all = pd.DataFrame(
        columns = ['add_info', 'iso3', 'tar_type_used', 'condi', 'rge', 
        'entity', 'category', 'unit', 'gwp'] + list(meta.years.all))
    ptws_all.add_info = ''
    
    """
    Get the cydata for all countries (are stored in ts_act.data) and add some information (gwp, category, ...).
    """
    ptws_all = add_timeseries(meta, database, ptws_all)
    
    """
    Iterate through EARTH countries, EU28 as single countries.
    Calculate the pathway per country and target type and un/conditional best/worst.
    Use baseline emissions where necessary.
    Use the unconditional target as conditional target as well, if the country does not have a conditional target.
    
    If meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = True
    use the baseline emissions for the unconditional pathways even if the conditional
    pathway (for 2030) is worse than the baseline.
    Else use the conditional pathway as unconditional pathway as well.
    """
    for iso_act in meta.isos.EARTH:
        
        target_name = 'tar_emi_exclLU'
        
        emi_bl_act = copy_table(getattr(database, 'emi_bl_exclLU'))
        
        # Get target data.
        if iso_act in list(calculated_targets.iso3):
            
            calc_tars_iso = calculated_targets.loc[calculated_targets.iso3 == iso_act, :]
            
            """
            If nothing is available, use 'baseline_emissions'.
            """
            curr_tars_all = calc_tars_iso.tar_type_used.unique()
            curr_tars_to_use = [xx for xx in curr_tars_all if xx not in ['NGT', 'ABS_CAT']]
            
            if len(curr_tars_to_use) > 0:
                curr_tars_to_use = curr_tars_to_use
            
            else:
                curr_tars_to_use = ['baseline_emissions']
            
            """
            Calculate pathways per target type.
            """
            for curr_tpe in curr_tars_to_use:
                
                data_curr_tpe = calc_tars_iso.loc[calc_tars_iso.tar_type_used == curr_tpe, :]
                
                """
                If there is CAT data for that country and target type (ABS), additionally calculate the CAT pathways
                following the same methodology as for 'our' pathways.
                """
                data_curr_tpe_ours = data_curr_tpe.loc[data_curr_tpe.scenario != 'CAT']
                data_curr_tpe_cat = data_curr_tpe.loc[data_curr_tpe.scenario == 'CAT']
                
                for data_curr_tpe, which_scen in [data_curr_tpe_ours, ''], [data_curr_tpe_cat, '_CAT']:
                    
                    if len(data_curr_tpe) > 0:
                        
                        # Set up 'targets_act' for the pathways per un/conditional & best/worst.
                        targets_act = pd.DataFrame(
                            index=['unconditional_worst', 'unconditional_best', 'conditional_worst', 'conditional_best'], 
                            columns=ptws_all.columns)
                        targets_act.add_info = '' # Info will be added where needed.
                        
                        # Which target type is used for the pathway calculation.
                        targets_act.loc[:, 'tar_type_used'] = curr_tpe
                        
                        # Per un/conditional_best/worst, put all the target emissions to the correct year in 'targets_act'.
                        for row in data_curr_tpe.index:
                            
                            condi_rge = '_'.join(data_curr_tpe.loc[row, ['condi', 'rge']])
                            targets_act.loc[condi_rge, ['condi', 'rge']] = condi_rge.split('_')
                            targets_act.loc[condi_rge, int(data_curr_tpe.loc[row, 'taryr'])] = \
                                data_curr_tpe.loc[row, target_name]
                                #str(data_curr_tpe.loc[row, target_name])
                        
                        """
                        If there is a value in unconditional_best in a year, but not in unconditional_worst, put it there.
                        If there is a value in conditional_best in a year, but not in conditional_worst, put it there.
                        If there is a value in unconditional in a year, but not in conditional, put it there (the one 
                        stored in 'unconditional_worst').
                        """
                        targets_act = add_targets_from_other_conditionality_if_needed(meta, targets_act)
                        
                        """
                        Calculate the pathways per un/conditional_best/worst, assuming a linear in/decrease of the 
                        % difference to the baseline emissions.
                        E.g., if the country has one unconditional_best target that equals a reduction of 20% in 2030 
                        (compared to baseline emissions):
                        the pathway has a 0% reduction in meta.years.pathways[0], and in 2030 the given
                        20% reduction, with a linear increase between meta.years.pathways[0] and 2030.
                        """
                        # Iterate through un/conditional_best/worst.
                        ptws_tars_act = pd.DataFrame(index=targets_act.index, columns=ptws_all.columns)
                        
                        for curr_tar in targets_act.index:
                            
                            ptws_tars_act.loc[curr_tar, :] = calculate_pathways(
                                ptws_all, emi_bl_act, targets_act, f"{curr_tpe}{which_scen}", curr_tar, iso_act, meta)
                        
                        """
                        Check for meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi.
                        If it is False and the conditional_worst pathway is worse in 2030 than the baseline
                        put the conditional_worst pathway to the unconditional pathways.
                        """
                        bl_2030 = ptws_all.loc[(ptws_all.iso3 == iso_act) & (ptws_all.rge == 'emi_bau') & 
                            (ptws_all.category == 'IPCM0EL'), 2030].values[0]
                        
                        if not meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi:
                            
                            if targets_act.loc[['unconditional_worst', 'unconditional_best'], meta.years.pathways].isnull().all().all():
                                
                                if bl_2030 < ptws_tars_act.loc['conditional_worst', 2030]:
                                    
                                    ptws_tars_act.loc[['unconditional_worst', 'unconditional_best'], meta.years.pathways] = \
                                        ptws_tars_act.loc['conditional_worst', meta.years.pathways].values
                        
                        """
                        Check for meta.use_baseline_if_target_above_bl.
                        If it is True and the mitigated value in 2030 is higher than the baseline, use the baseline.
                        """
                        if meta.use_baseline_if_target_above_bl:
                            
                            for row in ptws_tars_act.index:
                                
                                if bl_2030 < ptws_tars_act.loc[row, 2030]:
                                    
                                    ptws_tars_act.loc[row, meta.years.pathways] = \
                                        ptws_all.loc[(ptws_all.iso3 == iso_act) & (ptws_all.rge == 'emi_bau') & 
                                        (ptws_all.category == 'IPCM0EL'), meta.years.pathways].values[0]
                        
                        ptws_all = ptws_all.append(ptws_tars_act, ignore_index=True)
        
        """
        For each country, even if it does have a different target, also give out 'baseline_emissions'.
        """
        ptws_all = ptws_all.append(
            add_baseline_emissions(emi_bl_act, meta, iso_act, ptws_all.columns), ignore_index=True)
    
    # Sort the rows.
    ptws_all = ptws_all.sort_values(by=['iso3', 'category', 'tar_type_used', 'condi', 'unit'])
    
    # Write out 'ptws_all'.
    file_name = 'ndc_targets_pathways_per_country.csv'
    ptws_all.to_csv(Path(meta.path.output_ndcs, file_name), index=False)
    
    print("done calculating the per-country pathways ...")
    
    return ptws_all

# %%
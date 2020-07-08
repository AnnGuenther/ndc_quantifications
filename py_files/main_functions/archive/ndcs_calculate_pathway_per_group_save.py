# -*- coding: utf-8 -*-
"""
@author: annikag
"""

# %%
import pandas as pd
from pathlib import Path
from get_isos_for_groups.get_isos_for_groups import get_isos_for_groups as get_isos_groups

def ndcs_calculate_pathway_per_group(pathways_all_ncov100, pathways_all_cov100, input_pathways, yrs_all_str, 
                               isos, units, gwp, path_output, file_name, ndc_type_prios, pc_cov_predef, 
                               ndc, ndc_calc_targets_for):
    # Calculate the emissions pathway for a group of countries by summing up all available per-country pathways, 
    # per un/conditional_best/worst (chosing one of the target types per country).
    # And using baseline emissions where no target is available.
    #####
    # First get the 'chosen' country-pathways.
    pathways_groups_ai = pd.DataFrame(columns=['add_info', 'iso3s', 'cov_set_to_100',
                                            'ndc_types_used', 'condi', 'rge', 'entity', 'category', 'unit', 'gwp'] + yrs_all_str)
    


    # Groups for which to get the pathways.
    groups = sorted(['ANNEXI', 'ANNEXI_KAZ', 'AOSIS', 'AR5', 'AG', 'BRICS', 'EIG', 'G7', 'G20', 'G77',
              'GRADUATED_LDCS', 'IMO', 'LDC', 'LLDC', 'NON_ANNEXI', 'OECD', 'OPEC', 'SIDS',
              'UMBRELLA', 'UNFCCC', 'UN_REGIONAL_GROUPS', 'AILAC', 'ALBA', 'APG', 'BASIC', 'CACAM', 'CD', 
              'CfRN', 'CVF', 'EARTH',
              'EEG', 'EIT', 'G77+China', 'GRULAC', 'KYOTO', 'LAS', 'LMDC', 'PA', 'SICA', 'UN', 'WEOG'])
    
    #####
    # Put up 'pathways_groups' to store all the pathways.
    pathways_groups = pd.DataFrame(columns=['add_info', 'group', 'iso3s', 'iso3s_adapted', 'iso3s_missing', 'iso3s_cov_set_to_100',
                                            'ndc_types_used', 'condi', 'rge', 'entity', 'category', 'unit', 'gwp'] + yrs_all_str)
    #####
    # Get emi_bl, pc_cov, pop and gdp.
    emi_bl_name = input_pathways['emi_bl']['name']
    pc_cov_name = input_pathways['pc_cov']['name']
    pop_name = input_pathways['pop']['name']
    gdp_name = input_pathways['gdp']['name']
    
    #####
    # Iterate through the groups and calculate the pathways per group.
    for group_act in groups:
        #####
        # Set up 'pathways_act' for the current group.
        pathways_act = pd.DataFrame(
                index=[emi_bl_name, pc_cov_name, pop_name, gdp_name, 'unconditional_worst', 'unconditional_best', 
                       'conditional_worst', 'conditional_best'],
                columns=pathways_groups.columns)
        #####
        # ISO3s of the current group.
        isos_group_act = sorted(get_isos_groups(group_act, 'ISO3'))
        pathways_act.loc[:, 'iso3s'] = ', '.join(isos_group_act) # Original isos for the group.
        # Remove EU28 single countries, if EU28 is in the list.
        if 'EU28' in isos_group_act:
            isos_group_act = sorted(set(isos_group_act) - set(isos['EU28']))
        # endif
        # If all EU28 single countries are in the list, but EU28 is not, put it in and remove the single countries.
        if ('EU28' not in isos_group_act and len([1 for xx in isos['EU28'] if xx in isos_group_act])) == len(isos['EU28']):
            isos_group_act = sorted(set(isos_group_act + ['EU28']) - set(isos['EU28']))
        # endif
        pathways_act.loc[:, 'iso3s_adapted'] = ', '.join(isos_group_act) # Adapted isos for the group, 
        # regarding the handling of EU28 and its single countries.
        if pc_cov_predef['use_pc_cov_predef']:
            isos_cov100 = sorted(pc_cov_predef['countries'])
            isos_ncov100 = sorted(set(set(isos_group_act) - set(isos_cov100)))
            pathways_act.loc[:, 'iso3s_cov_set_to_100'] = ', '.join(isos_cov100)
        else:
            isos_cov100 = []
            isos_ncov100 = isos_group_act
        # endif
        
        #####
        # Baseline emissions and pc_cov.
        # bl
        emi_bl_act = pathways_all_ncov100.loc[(pathways_all_ncov100.iso3.isin(isos_group_act)) &
            (pathways_all_ncov100.entity == input_pathways['emi_bl']['ent']) & 
            (pathways_all_ncov100.category == input_pathways['emi_bl']['cat']) & 
            (pathways_all_ncov100.unit == units['emi']) &
            ~(pathways_all_ncov100.rge.isin(['best', 'worst'])), :]
        emi_bl_act.index = emi_bl_act.iso3
        # ncov100
        emi_bl_ncov100_act = emi_bl_act.loc[(emi_bl_act.iso3.isin(isos_ncov100)), :]
        # cov100
        emi_bl_cov100_act = emi_bl_act.loc[(emi_bl_act.iso3.isin(isos_cov100)), :]
        # Calculate pc_cov from the per-country covered emissions, divided by the total emissions of these countries.
        # For ncov100:
        pc_ncov100_act = pathways_all_ncov100.loc[(pathways_all_ncov100.iso3.isin(isos_ncov100)) & 
                                      (pathways_all_ncov100.entity == input_pathways['pc_cov']['ent']), :]
        pc_ncov100_act.index = pc_ncov100_act.iso3
        emi_ncov100_act = emi_bl_ncov100_act.loc[:, yrs_all_str].multiply(
                pc_ncov100_act.loc[:, yrs_all_str]/100.).loc[:, yrs_all_str].sum(axis=0)
        emi_cov100_act = emi_bl_cov100_act.loc[:, yrs_all_str].sum(axis=0)
        emi_cov_act = emi_ncov100_act[yrs_all_str].add(emi_cov100_act[yrs_all_str])
        pc_cov_act = emi_cov_act.div(emi_bl_act.loc[:, yrs_all_str].sum(axis=0)) * 100.
        #####
        # Baseline emissions
        pathways_act.loc[emi_bl_name, yrs_all_str] = emi_bl_act.loc[:, yrs_all_str].sum(axis=0).values
        pathways_act.loc[emi_bl_name, 'iso3s_missing'] = ', '.join(sorted(set(set(isos_group_act) - set(emi_bl_act.index))))
        pathways_act.loc[emi_bl_name, ['entity', 'category', 'unit', 'gwp', 'condi', 'rge']] = \
            [input_pathways['emi_bl']['ent'], input_pathways['emi_bl']['cat'], units['emi'], gwp, 'total_emi', 'total_emi']
        #####
        # pc_cov
        pathways_act.loc[pc_cov_name, yrs_all_str] = pc_cov_act[yrs_all_str].values
        pathways_act.loc[pc_cov_name, 'iso3s_missing'] = ', '.join(sorted(set(set(isos_group_act) - set(pc_cov_act.index))))
        pathways_act.loc[pc_cov_name, ['entity', 'category', 'unit', 'gwp']] = \
            [input_pathways['pc_cov']['ent'], input_pathways['pc_cov']['cat'], '%', gwp]
        #####
        # Population
        ptw_act = pathways_all_ncov100.loc[(pathways_all_ncov100.iso3.isin(isos_group_act)) &
            (pathways_all_ncov100.entity == 'pop'), :]
        pathways_act.loc[pop_name, yrs_all_str] = ptw_act.loc[:, yrs_all_str].sum(axis=0).values
        pathways_act.loc[pop_name, 'iso3s_missing'] = ', '.join(sorted(set(set(isos_group_act) - set(ptw_act.index))))
        pathways_act.loc[pop_name, ['entity', 'category', 'unit']] = \
            [input_pathways['pop']['ent'], input_pathways['pop']['cat'], units['pop']]
        #####
        # GDP
        ptw_act = pathways_all_ncov100.loc[(pathways_all_ncov100.iso3.isin(isos_group_act)) &
            (pathways_all_ncov100.entity == 'gdp'), :]
        pathways_act.loc[gdp_name, yrs_all_str] = ptw_act.loc[:, yrs_all_str].sum(axis=0).values
        pathways_act.loc[gdp_name, 'iso3s_missing'] = ', '.join(sorted(set(set(isos_group_act) - set(ptw_act.index))))
        pathways_act.loc[gdp_name, ['entity', 'category', 'unit']] = \
            [input_pathways['gdp']['ent'], input_pathways['gdp']['cat'], units['gdp']]
        #####
        # Get the target types for the calculation of the group pathways (following ndc_type_prios).
        tars_to_use = pd.Series(index=isos_group_act)
        for iso_act in isos_group_act:
            if (ndc_calc_targets_for['use_ndc_calc_targets_for'] and 
                iso_act not in ndc_calc_targets_for['countries']):
                # If that is true the baseline emissions are to be used.
                tars_to_use[iso_act] = 'baseline_emissions'
            else:
                # Check which target type to use.
                if ndc_type_prios['use_ndc_type_prios']:
                    if iso_act in ndc_type_prios['countries']:
                        tar_chosen = []
                        for type_prio in ndc_type_prios:
                            if type_prio.upper() == 'TYPE_CALC':
                                tar_chosen = tar_chosen + [ndc.loc['Type_Calc', iso_act]]
                            elif type_prio.upper() == 'TYPE_ORIG':
                                tar_chosen = tar_chosen + [ndc.loc['Type_Orig', iso_act]]
                            else:
                                tars_available = [xx 
                                    for xx in pathways_all_ncov100.loc[pathways_all_ncov100.iso3 == iso_act, 'tar_type_used'].unique()
                                    if xx == type_prio]
                                if len(tars_available) > 0:
                                    tar_chosen = tar_chosen + [type_prio]
                                # endif
                            # endif
                        # endfor
                        if len(tar_chosen) > 0:
                            tar_used = tar_chosen[0]
                        else:
                            if iso_act in list(ndc.columns):
                                tar_used = ndc.loc['Type_Calc', iso_act]
                            else:
                                tar_used = 'baseline_emissions'
                            # endif
                        # endif
                    else:
                        if iso_act in list(ndc.columns):
                            tar_used = ndc.loc['Type_Calc', iso_act]
                        else:
                            tar_used = 'baseline_emissions'
                        # endif
                    # endif
                    # If the target type is NGT, try to chose another type.
                    # Preferably ABS, BYT or RRB.
                    if tar_used == 'NGT':
                        tars_available = [xx 
                                    for xx in pathways_all_ncov100.loc[pathways_all_ncov100.iso3 == iso_act, 'tar_type_used'].unique()
                                    if xx != 'NGT']
                        if len(tars_available) > 0:
                            if 'ABS' in tars_available:
                                tar_used = 'ABS'
                            elif 'BYT' in tars_available:
                                tar_used = 'BYT'
                            elif 'RBB' in tars_available:
                                tar_used = 'RRB'
                            else:
                                tar_used = tars_available[0]
                            # endif
                        else:
                            tar_used = 'baseline_emissions'
                        # endif
                    # endif
                    tars_to_use[iso_act] = tar_used
                else:
                    if iso_act in list(ndc.columns):
                        tars_to_use[iso_act] = ndc.loc['Type_Calc', iso_act]
                        if tars_to_use[iso_act] == 'NGT':
                            tars_to_use[iso_act] = 'baseline_emissions'
                        # endif
                    else:
                        tars_to_use[iso_act] = 'baseline_emissions'
                    # endif
                # endif
            # endif
        # endfor
        ptws_ncov100_act = pathways_all_ncov100.loc[(pathways_all_ncov100.iso3.isin(isos_ncov100)) &
            (pathways_all_ncov100.entity == input_pathways['emi_bl']['ent']) & 
            (pathways_all_ncov100.category == input_pathways['emi_bl']['cat']) & 
            (pathways_all_ncov100.unit == units['emi']), :]
        ptws_cov100_act = pathways_all_cov100.loc[(pathways_all_cov100.iso3.isin(isos_cov100)) &
            (pathways_all_cov100.entity == input_pathways['emi_bl']['ent']) & 
            (pathways_all_cov100.category == input_pathways['emi_bl']['cat']) & 
            (pathways_all_cov100.unit == units['emi']), :]
        for condi in ['unconditional', 'conditional']:
            for rge in ['worst', 'best']:
                ptw_ncov100_act = ptws_ncov100_act.loc[(ptws_ncov100_act.condi == condi) & (ptws_ncov100_act.rge == rge), :]
                ptw_cov100_act = ptws_cov100_act.loc[(ptws_cov100_act.condi == condi) & (ptws_cov100_act.rge == rge), :]
                ptw_iso = pd.DataFrame(columns=ptw_ncov100_act.columns, index=isos_group_act)
                for iso_act in isos_group_act:
                    if iso_act in isos_ncov100:
                        ptw_iso_act = ptw_ncov100_act.loc[(ptw_ncov100_act.iso3 == iso_act) &
                            (ptw_ncov100_act.tar_type_used == tars_to_use[iso_act]), ptw_iso.columns].values
                    else:
                        ptw_iso_act = ptw_cov100_act.loc[(ptw_cov100_act.iso3 == iso_act) &
                            (ptw_cov100_act.tar_type_used == tars_to_use[iso_act]), ptw_iso.columns].values
                    # endif
                    if 0 not in ptw_iso_act.shape:
                        ptw_iso.loc[iso_act, :] = ptw_iso_act
                # endfor
                condi_rge = condi + '_' + rge
                pathways_act.loc[condi_rge, yrs_all_str] = \
                    ptw_iso.loc[:, yrs_all_str].sum(axis=0).values
                pathways_act.loc[condi_rge, 'iso3s_missing'] = ', '.join(sorted(set(set(isos_group_act) - set(ptw_act.index))))
                pathways_act.loc[condi_rge, ['condi', 'rge', 'entity', 'category', 'unit', 'gwp']] = \
                    [condi, rge, input_pathways['emi_bl']['ent'], 
                     input_pathways['emi_bl']['cat'], units['emi'], gwp]
            # endfor
        # endfor
        pathways_act.loc[:, 'ndc_types_used'] = \
            '.\n'.join([xx + ": " + ', '.join([yy for yy in tars_to_use.index[tars_to_use == xx] 
            if yy in isos_group_act])
            for xx in ['baseline_emissions', 'ABS', 'BYT', 'RRB', 'ARB', 'RIT', 'AIT']]) + '.'
        
        #####
        # General input
        pathways_act.loc[:, 'group'] = group_act
        
        #####
        pathways_groups = pathways_groups.append(pathways_act, ignore_index=True)
    # endfor
    
    #####
    # Write out 'pathways_groups'.
    pathways_groups.to_csv(Path(path_output, file_name), index=False)
    print("done calculating the per-group pathways ...")
    
    #####
    return pathways_groups
# enddef

# %%

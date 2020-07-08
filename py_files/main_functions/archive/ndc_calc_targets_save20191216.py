# -*- coding: utf-8 -*-
"""
@author: annikag
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path

def ndc_calc_targets(time_series, units, ndc, isos, gwp, scenario, yrs_all_str, 
                     path_output, ndc_strengthen, lulucf_fyson):
    #####
    # Set up for pd.DataFrame to store the in / output (for each target one row is added).
    # cols['names'] will be columns, and cols['units'] will be set to first row.
    cols = {'names': {'add_info': ['add_info'],
                      'ndc': ['iso3', 'tar_type_used', 'tar_type_calc', 'tar_type_orig', 'condi', 'rge',
                              'ndc_val', 'ndc_val_corrected_for_lu_and_pc_cov', 
                              'ndc_val_corrected_for_lu_and_pc_cov_cov100', 
                              'ndc_strengthen', 'int_ref', 'refyr', 'taryr'],
                      'tar': ['tar_emi_excl_lu' , 'tar_emi_tot', 
                              'tar_emi_excl_lu_cov100', 'tar_emi_tot_cov100'],
                      'emi': ['gwp', 'scenario', 'emi_bl_excl_lu_refyr', 'emi_bl_excl_lu_taryr', 'emi_bl_lu_refyr',
                              'emi_bl_lu_taryr'],
                      'pc_cov': ['pc_cov_excl_lu_refyr', 'pc_cov_excl_lu_taryr', 'pc_cov_lu_refyr',
                                 'pc_ncov_lu_refyr', 'pc_cov_lu_taryr', 'pc_ncov_lu_taryr'],
                      'int_ref': ['pop_refyr', 'pop_taryr', 'gdp_refyr', 'gdp_taryr'],
                      'cov_gases': ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3'],
                      'cov_sectors': ['energy', 'ippu', 'agriculture', 'waste', 'other', 'lulucf'],
                      'lulucf': ['lulucf_tar_2030_fyson2019']},
            'units': {'add_info': [None],
                      'ndc': [None]*7 + ['%']*2 + [None]*4,
                      'tar': [units['emi']]*4,
                      'emi': [None, None] + [units['emi']]*4,
                      'pc_cov': ['%']*6,
                      'int_ref': [units['pop'], units['pop'], units['gdp'], units['gdp']],
                      'cov_gases': ['nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan'],
                      'cov_sectors': ['nan', 'nan', 'nan', 'nan', 'nan', 'nan'],
                      'lulucf': ['MtCO2eq']}}
    
    #####
    # Dataframe with columns = all the items and sub-items in cols['names']:
    calculated_targets = pd.DataFrame(columns=[item for sublist in [cols['names'][xx] for xx in cols['names'].keys()]
                                                          for item in sublist])
    # Add the units as first row:
    calculated_targets = calculated_targets.append(pd.Series([item for sublist in [cols['units'][xx] for xx in cols['units'].keys()]
                                                               for item in sublist], 
                                         index=calculated_targets.columns), ignore_index=True)
        
    #####
    # Iterate through the iso3s in ndc (also the EU28 single countries, using the EU28 target info for the countries).
    for iso_act in sorted(ndc.columns):        
        add_info = ''
        
        #####
        # For EU28 countries: use the ndc info from EU28.
        if iso_act in isos['EU28']:
            iso_ndc = 'EU28'
        else:
            iso_ndc = iso_act
        # endif
        
        ######
        # Get ndc information.
        ndc_act = ndc.loc[:, iso_ndc]
        ndc_act.index = [xx.upper() for xx in ndc_act.index]
        
        #####
        # Get time series for emi_bl_excl_lu, emi_bl_lu, pc_cov, pop, gdp.
        to_add = {'emi_bl_excl_lu': 'IPCM0EL', 'emi_bl_lu': 'IPCMLULUCF',
                  'pc_cov_excl_lu': 'pc_cov_excl_lu',  'pc_cov_lu': 'pc_cov_lu', 'pc_ncov_lu': 'pc_ncov_lu',
                  'pop': 'pop', 'gdp': 'gdp'}
        # endif
        ts_act = pd.DataFrame(index=to_add.keys(), columns=yrs_all_str)
        for add in to_add.keys():
            ts_to_add = time_series[to_add[add]]
            if iso_act in list(ts_to_add.iso3):
                ts_act.loc[add, :] = ts_to_add.loc[ts_to_add.iso3 == iso_act, ts_act.columns].values
                add_info_act = ts_to_add.loc[ts_to_add.iso3 == iso_act, 'add_info'].values[0]
                if type(add_info_act) == str:
                    add_info = add_info + add + ": " + add_info_act + '\n'
                # endif
                
                #####
                # Add the 'source' info for LULUCF.
                if add == 'emi_bl_lu':
                    add_info2 = ts_to_add.loc[ts_to_add.iso3 == iso_act, 'source'].values[0]
                    if type(add_info2) == str:
                        add_info = add_info + add + ": source " + add_info2 + '.\n'
                    # endif
                # endif
            # endif
        # endfor
        emi_bl_excl_lu = time_series[to_add['emi_bl_excl_lu']]
        emi_bl_excl_lu = emi_bl_excl_lu.loc[emi_bl_excl_lu.iso3 == iso_act, :]
                
        #####
        # Get info that is the same no matter which target year & un/conditional target it is, and put it into 'info'.
        #####
        # For 'info'
        cols_11 = ['iso3', 'tar_type_calc', 'tar_type_orig', 'int_ref', 'refyr']
        cols_12 = ['emi_bl_excl_lu_refyr', 'emi_bl_lu_refyr', 'pc_cov_excl_lu_refyr', 'pc_cov_lu_refyr',
                   'pc_ncov_lu_refyr']
        # As LULUCF can also be negative: pc_cov and pc_ncov needed.
        cols_13 = ['pop_refyr', 'gdp_refyr']
        cols_14 = cols['names']['cov_gases']
        cols_15 = cols['names']['cov_sectors']
        #####
        info = pd.Series(index = cols_11 + cols_12 + cols_13 + cols_14 + cols_15)
        info[cols_11] = [iso_act] + list(ndc_act.loc[['TYPE_CALC', 'TYPE_ORIG', 'INTENSITY_PERCAP_GDP',
            'BASEYEAR']].values)
        #####
        # Reference year (base year).
        refyr_str = 'Y' + info['refyr']
        if refyr_str != 'Ynan':
            info[cols_12] = list(ts_act.loc[['emi_bl_excl_lu', 'emi_bl_lu', 'pc_cov_excl_lu', 'pc_cov_lu',
                'pc_ncov_lu'], refyr_str].values)
            info[cols_13] = list(ts_act.loc[['pop', 'gdp'], refyr_str].values)
        # endif
        info[cols_14] = ndc_act[[xx.upper() for xx in cols_14]]
        info[cols_15] = ndc_act[[xx.upper() for xx in cols_15]]
        #####

        #####
        # Calculate targets for all target types with values available in the input ndc-table.
        for tar_type in ['ABS', 'BYT', 'RRB', 'ARB', 'RIT', 'AIT']:           
            # Get all available target years & un/conditional & best/worst targets.
            # ndc_val depends on the target type, either it is absolute emissions (ABS, ARB), a % (BYT, RRB, RIT), 
            # or an emissions intensity (AIT).
            # ABS: target emissions in MtCO2eq.
            # ARB: absolute  reduction in MtCO2eq (e.g., -3500 stands for 3500 MtCO2eq reduction).
            # BYT, RRB, RIT: percentage reduction (e.g., -20 stands for 20% reduction).
            # AIT: emissions intensity in target year, e.g., 3.2 stands for 3.2 t/cap or 3.2 t/GDP, when int_ref is
            # POP or GDP, respectively.
            ndc_vals_all = ndc_act.loc[[xx for xx in ndc_act.index if xx[:3] == tar_type]]
            ndc_vals_all = ndc_vals_all.drop(index=[xx for xx in ndc_vals_all.index
                                                    if ndc_vals_all[xx].upper() == 'NAN'])
                        
            #####
            # Iterate through the target years + un/conditional + best/worst.
            for tars in ndc_vals_all.index:
                # Set up 'info_act' for the information in this iteration.
                #####
                # For 'info_act'
                cols_21 = ['condi', 'rge', 'ndc_val', 'ndc_val_corrected_for_lu_and_pc_cov', 
                           'ndc_val_corrected_for_lu_and_pc_cov_cov100', 'taryr']
                cols_22 = ['tar_emi_excl_lu', 'tar_emi_tot',
                           'tar_emi_excl_lu_cov100', 'tar_emi_tot_cov100']
                cols_23 = ['gwp', 'scenario', 'emi_bl_excl_lu_taryr', 'emi_bl_lu_taryr', 'pc_cov_excl_lu_taryr',
                           'pc_cov_lu_taryr', 'pc_ncov_lu_taryr']
                cols_24 = ['pop_taryr', 'gdp_taryr']
                info_act = pd.Series(index = cols_21 + cols_22 + cols_23 + cols_24 +
                                     ['tar_type_used', 'ndc_strengthen', 
                                      'lulucf_tar_2030_fyson2019'])
                
                #####
                # Is it un/conditional? Best/worst?
                if 'UNCONDITIONAL' in tars:
                    info_act['condi'] = 'unconditional'
                else:
                    info_act['condi'] = 'conditional'
                # endif
                if 'BEST' in tars:
                    info_act['rge'] = 'best'
                else:
                    info_act['rge'] = 'worst'
                # endif
                
                # Put Fyson2019 LULUCF 2030 emissions in output, not used further.
                if iso_act in lulucf_fyson['data'].index:
                    lu_fy = lulucf_fyson['data'].loc[iso_act, :]
                    lu_fy = lu_fy[['minimum_' + info_act['condi'], 'maximum_' + info_act['condi']]].astype(float)
                    if info_act['rge'] == 'best':
                        lu_fy = min(lu_fy)
                    else:
                        lu_fy = max(lu_fy)
                    # endif    
                    info_act['lulucf_tar_2030_fyson2019'] = lu_fy
                # endif
                
                #####
                info_act['tar_type_used'] = tar_type
                # Get more information from ndc.
                info_act['ndc_val', 'taryr'] = [ndc_vals_all[tars], tars[-4:]]
                taryr_str = 'Y' + info_act['taryr']
                info_act[cols_23] = [gwp, scenario] + list(ts_act.loc[['emi_bl_excl_lu', 'emi_bl_lu',
                        'pc_cov_excl_lu', 'pc_cov_lu', 'pc_ncov_lu'], taryr_str].values)
                info_act[cols_24] = list(ts_act.loc[['pop', 'gdp'], taryr_str].values)
                
                #####
                # Check if ndc_val seems ok.
                ndc_val = info_act['ndc_val']
                if info_act['tar_type_used'] == 'ABS':
                    if 'MTCO2' not in ndc_val.upper():
                        print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                              info_act['tar_type_used'] + ", but 'MtCO2' is not in ndc_val!" +
                              "\n    ndc_val = " + ndc_val)
                    # endif
                # endif
                if info_act['tar_type_used'] in ['BYT', 'RRB', 'RIT']:
                    if ('%' not in ndc_val) or ('-' not in ndc_val):
                        print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                              info_act['tar_type_used'] + ", but '%' or/and '-' is not in ndc_val!" +
                              "\n    ndc_val = " + ndc_val)
                    # endif
                # endif
                if info_act['tar_type_used'] == 'ARB':
                    if ('MTCO2' not in ndc_val.upper()) or ('-' not in ndc_val):
                        print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                              info_act['tar_type_used'] + ", but 'MtCO2' or/and '-' is not in ndc_val!" +
                              "\n    ndc_val = " + ndc_val)
                    # endif
                # endif
                if info_act['tar_type_used'] == 'AIT':
                    if ('TCO2' not in ndc_val.upper()) or ('MTCO2' in ndc_val.upper()):
                        print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                              info_act['tar_type_used'] + ", but 'tCO2' or/and 'MtCO2' is in ndc_val!" +
                              "\n    ndc_val = " + ndc_val)
                    # endif
                # endif
                
                #####
                # Get the numerical value from ndc_val (only looking at the letters up to the first space).
                ndc_val = ndc_val.replace('CO2', '') # If not the '2' will be kept for the numerical value.
                if ' ' in ndc_val:
                    ndc_val = info_act['ndc_val'][:[xx for xx in range(len(info_act['ndc_val']))
                                      if info_act['ndc_val'][xx] == ' '][0]]
                # endif
                ndc_val = float(''.join([xx for xx in ndc_val if xx in '0123456789eE.+-']))
                
                #####
                # If strengthen NDC is chosen.
                if ndc_strengthen['use_ndc_strengthen']:
                    if iso_act in ndc_strengthen['countries']:
                        if info_act['tar_type_used'] in ['BYT', 'RRB', 'RIT']:
                            if ndc_strengthen['how_to'] == 'multiply':
                                ndc_val_new = ndc_val * (1. + ndc_strengthen['pc']/100.)
                                info_act['ndc_strengthen'] = "Multiply ndc_val with " + str(1. +
                                        ndc_strengthen['pc']/100.) + "."
                            # endif
                            if ndc_strengthen['how_to'] == 'add':
                                ndc_val_new = ndc_val - ndc_strengthen['pc'] 
                                # ndc_val usually is negative, e.g., -20%.
                                info_act['ndc_strengthen'] = "Add " + str(ndc_strengthen['pc']) + "% to ndc_val."
                            # endif
                            # If ndc_val_new is bigger than a 100% reduction, set it to 100% reduction.
                            if (ndc_val_new < -100.) and (ndc_val > -100.):
                                ndc_val = -100.
                            else:
                                ndc_val = ndc_val_new
                            # endif
                        # endif
                    # endif
                # endif
                
                #####
                # Get the % reduction (only used in calculations of relative targets).
                red = 1. + ndc_val / 100.
                
                #####
                # Share of national emissions covered.
                pc_cov_excl_lu_refyr = info['pc_cov_excl_lu_refyr']
                pc_cov_excl_lu_taryr = info_act['pc_cov_excl_lu_taryr']
                pc_cov_lu_refyr = info['pc_cov_lu_refyr']
                pc_cov_lu_taryr = info_act['pc_cov_lu_taryr']
                pc_ncov_lu_taryr = info_act['pc_ncov_lu_taryr']
                # 100% coverage as comparison.
                pc_cov_excl_lu_refyr_cov100 = 100.
                pc_cov_excl_lu_taryr_cov100 = 100.
                pc_cov_lu_refyr_cov100 = 100.
                pc_cov_lu_taryr_cov100 = 100.
                pc_ncov_lu_taryr_cov100 = 0.
                                
                #####
                # Calculate the target year emissions depending on the target type.
                if info_act['tar_type_used'] == 'ABS':
                    # Assumption: if LULUCF is covered, the given ABS is incl. LULUCF ...
                    if ndc.loc['LULUCF', iso_act].upper() == 'YES':
                        info_act['tar_emi_tot'] = ndc_val
                        info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot']
                        info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                    else:
                        info_act['tar_emi_excl_lu'] = ndc_val
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                        info_act['tar_emi_tot'] = info_act['tar_emi_excl_lu'] + info_act['emi_bl_lu_taryr']
                        info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot']
                    # endif
                    # Calculate the 'excl. LULUCF' target, by subtracting the target
                    # year LULUCF emissions from the target emissions, and 
                    # referencing these to the non-LULUCF emissions in the reference year / target year.
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        - 100. * (1. - info_act['tar_emi_excl_lu']/info_act['emi_bl_excl_lu_taryr']) # taryr
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        - 100. * (1. - info_act['tar_emi_excl_lu_cov100']/info_act['emi_bl_excl_lu_taryr']) # taryr
                # endif
                if info_act['tar_type_used'] == 'BYT':
                    # Note: when LULUCF is not coverd, the pc_cov is 0.
                    # Therefore we calculate all at once.
                    info_act['tar_emi_tot'] = \
                        ((info['emi_bl_excl_lu_refyr'] * pc_cov_excl_lu_refyr/100.) + \
                         (info['emi_bl_lu_refyr'] * pc_cov_lu_refyr/100.)) * red + \
                         (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr/100.) + \
                          info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr/100.)
                    # cov100
                    info_act['tar_emi_tot_cov100'] = \
                        ((info['emi_bl_excl_lu_refyr'] * pc_cov_excl_lu_refyr_cov100/100.) + \
                         (info['emi_bl_lu_refyr'] * pc_cov_lu_refyr_cov100/100.)) * red + \
                         (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr_cov100/100.) + \
                          info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr_cov100/100.)
                    # Calculate the 'excl. LULUCF' target, by subtracting the target
                    # year LULUCF emissions from the target emissions, and 
                    # referencing these to the non-LULUCF emissions in the reference year.
                    info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        - 100. * (1. - info_act['tar_emi_excl_lu']/info['emi_bl_excl_lu_refyr']) # refyr
                    # cov100
                    info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_tot_cov100'] - info_act['emi_bl_lu_taryr']
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        - 100. * (1. - info_act['tar_emi_excl_lu_cov100']/info['emi_bl_excl_lu_refyr']) # refyr
                # endif
                if info_act['tar_type_used'] == 'RRB':
                    # Note: when LULUCF is not coverd, the pc_cov is 0.
                    # Therefore we calculate all at once.
                    info_act['tar_emi_tot'] = \
                        ((info_act['emi_bl_excl_lu_taryr'] * pc_cov_excl_lu_taryr/100.) + \
                         (info_act['emi_bl_lu_taryr'] * pc_cov_lu_taryr/100.)) * red + \
                         (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr/100.) + \
                          info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr/100.)
                    # cov100
                    info_act['tar_emi_tot_cov100'] = \
                        ((info_act['emi_bl_excl_lu_taryr'] * pc_cov_excl_lu_taryr_cov100/100.) + \
                         (info_act['emi_bl_lu_taryr'] * pc_cov_lu_taryr_cov100/100.)) * red + \
                         (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr_cov100/100.) + \
                          info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr_cov100/100.)
                    # Calculate the 'excl. LULUCF' target, as for BYT.
                    info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        - 100. * (1. -info_act['tar_emi_excl_lu']/info_act['emi_bl_excl_lu_taryr']) # taryr
                    # cov100
                    info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_tot_cov100'] - info_act['emi_bl_lu_taryr']
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        - 100. * (1. -info_act['tar_emi_excl_lu_cov100']/info_act['emi_bl_excl_lu_taryr']) # taryr
                # endif
                if info_act['tar_type_used'] == 'ARB':
                    # Assuming that if LULUCF is covered, the given emissions reduction also includes LULUCF.
                    if ndc.loc['LULUCF', iso_act].upper() == 'YES':
                        info_act['tar_emi_tot'] = (info_act['emi_bl_excl_lu_taryr'] + info_act['emi_bl_lu_taryr']) + ndc_val
                        info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot_cov100']
                        # Calculate the 'excl. LULUCF' target.
                        info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                    else:
                        info_act['tar_emi_excl_lu'] = info_act['emi_bl_excl_lu_taryr'] + ndc_val
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                        # Calculate the 'emi_tot'.
                        info_act['tar_emi_tot'] = info_act['tar_emi_excl_lu'] + info_act['emi_bl_lu_taryr']
                        info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot']
                    # endif
                    # Calculate the corrected ndc_val.
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        - 100. * (1. -info_act['tar_emi_excl_lu']/info_act['emi_bl_excl_lu_taryr']) # taryr
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        info_act['ndc_val_corrected_for_lu_and_pc_cov']
                # endif
                if info_act['tar_type_used'] == 'RIT':
                    # Note: when LULUCF is not coverd, the pc_cov is 0.
                    # Therefore we calculate all at once.
                    if refyr_str == taryr_str:
                        # Like BAU:
                        info_act['tar_emi_tot'] = \
                            ((info_act['emi_bl_excl_lu_taryr'] * pc_cov_excl_lu_taryr/100.) + \
                             (info_act['emi_bl_lu_taryr'] * pc_cov_lu_taryr/100.)) * red + \
                             (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr/100.) + \
                              info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr/100.)
                        # cov100
                        info_act['tar_emi_tot_cov100'] = \
                            ((info_act['emi_bl_excl_lu_taryr'] * pc_cov_excl_lu_taryr_cov100/100.) + \
                             (info_act['emi_bl_lu_taryr'] * pc_cov_lu_taryr_cov100/100.)) * red + \
                             (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr_cov100/100.) + \
                              info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr_cov100/100.)
                        # Calculate the 'excl. LULUCF' target.
                        info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                        info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                            - 100. * (1. -info_act['tar_emi_excl_lu']/info_act['emi_bl_excl_lu_taryr']) # taryr
                        # cov100
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_tot_cov100'] - info_act['emi_bl_lu_taryr']
                        info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                            - 100. * (1. -info_act['tar_emi_excl_lu_cov100']/info_act['emi_bl_excl_lu_taryr']) # taryr
                    else:
                        # Compared to base year:
                        info_act['tar_emi_tot'] = \
                            info_act[info['int_ref'].lower() + '_taryr'] / info[info['int_ref'].lower() + '_refyr'] * \
                            ((info['emi_bl_excl_lu_refyr'] * pc_cov_excl_lu_refyr/100.) + \
                             (info['emi_bl_lu_refyr'] * pc_cov_lu_refyr/100.)) * red + \
                            (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr/100.) + \
                             info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr/100.)
                        # cov100
                        info_act['tar_emi_tot_cov100'] = \
                            info_act[info['int_ref'].lower() + '_taryr'] / info[info['int_ref'].lower() + '_refyr'] * \
                            ((info['emi_bl_excl_lu_refyr'] * pc_cov_excl_lu_refyr_cov100/100.) + \
                             (info['emi_bl_lu_refyr'] * pc_cov_lu_refyr_cov100/100.)) * red + \
                            (info_act['emi_bl_excl_lu_taryr'] * (1. - pc_cov_excl_lu_taryr_cov100/100.) + \
                             info_act['emi_bl_lu_taryr'] * pc_ncov_lu_taryr_cov100/100.)
                        # Calculate the 'excl. LULUCF' target.
                        info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                        info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                            - 100. * (1. -info_act['tar_emi_excl_lu']/info['emi_bl_excl_lu_refyr']) # refyr
                        # cov100
                        info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_tot_cov100'] - info_act['emi_bl_lu_taryr']
                        info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                            - 100. * (1. -info_act['tar_emi_excl_lu_cov100']/info['emi_bl_excl_lu_refyr']) # refyr
                    # endif
                # endif
                if info_act['tar_type_used'] == 'AIT':
                    # Assuming that the given emissions intensities include LULUCF, if LULUCF is covered.
                    if 'CAP' in info_act['ndc_val'].upper():
                        if ndc.loc['LULUCF', iso_act].upper() == 'YES':
                            info_act['tar_emi_tot'] = ndc_val * 1e-6 * info_act['pop_taryr']
                            info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot']
                            # Calculate the 'excl. LULUCF' target.
                            info_act['tar_emi_excl_lu'] = info_act['tar_emi_tot'] - info_act['emi_bl_lu_taryr']
                            info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_tot_cov100'] - info_act['emi_bl_lu_taryr']
                        else:
                            info_act['tar_emi_excl_lu'] = ndc_val * 1e-6 * info_act['pop_taryr']
                            info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                            # Calculate the 'tot' target.
                            info_act['tar_emi_tot'] = info_act['tar_emi_excl_lu'] + info_act['emi_bl_lu_taryr']
                            # cov100
                            info_act['tar_emi_tot_cov100'] = info_act['tar_emi_excl_lu_cov100'] + info_act['emi_bl_lu_taryr']
                        # endif
                    elif 'GDP' in info_act['ndc_val'].upper():
                        if ndc.loc['LULUCF', iso_act].upper() == 'YES':
                            info_act['tar_emi_tot'] = ndc_val * 1e-6 * info_act['gdp_taryr']
                            info_act['tar_emi_tot_cov100'] = info_act['tar_emi_tot']
                        else:
                            info_act['tar_emi_excl_lu'] = ndc_val * 1e-6 * info_act['gdp_taryr']
                            info_act['tar_emi_excl_lu_cov100'] = info_act['tar_emi_excl_lu']
                        # endif
                    else:
                        print("Warning in main_ndc_quantifications.ipynb: for " + iso_act +
                              " AIT, it is not clear which reference to use. " +
                              "The target is " + info_act['ndc_val'] + ". Nothing has been calculated.")
                    # endif
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        - 100. * (1. -info_act['tar_emi_excl_lu']/info_act['emi_bl_excl_lu_taryr']) # taryr
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        - 100. * (1. -info_act['tar_emi_excl_lu_cov100']/info_act['emi_bl_excl_lu_taryr']) # taryr
                # endif
                
                #####
                # If tar_emi_tot or tar_emi_excl_lu are empty but the other value exists, 
                # put the value to both columns.
                val_replace = [info_act['tar_emi_excl_lu'], info_act['tar_emi_tot']]
                val_replace = [xx for xx in val_replace if not np.isnan(xx)]
                if len(val_replace) == 1:
                    info_act['tar_emi_excl_lu'] = val_replace[0]
                    info_act['tar_emi_tot'] = val_replace[0]
                # endif
                val_replace = [info_act['tar_emi_excl_lu_cov100'], info_act['tar_emi_tot_cov100']]
                val_replace = [xx for xx in val_replace if not np.isnan(xx)]
                if len(val_replace) == 1:
                    info_act['tar_emi_excl_lu_cov100'] = val_replace[0]
                    info_act['tar_emi_tot_cov100'] = val_replace[0]
                # endif
                                    
                #####
                # Change format of the values for ndc_val_corrected_for_lu_and_pc_cov 
                # and ndc_val_corrected_for_lu_and_pc_cov_cov100.
                if not np.isnan(info_act['ndc_val_corrected_for_lu_and_pc_cov']):
                    info_act['ndc_val_corrected_for_lu_and_pc_cov'] = \
                        '{:+.2f}'.format(info_act['ndc_val_corrected_for_lu_and_pc_cov']) + '%'
                # endif
                if not np.isnan(info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100']):
                    info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100'] = \
                        '{:+.2f}'.format(info_act['ndc_val_corrected_for_lu_and_pc_cov_cov100']) + '%'
                # endif
                #####
                # Add calculations to 'calculated_targets_act'.
                calculated_targets_act = pd.Series(index=calculated_targets.columns)
                calculated_targets_act[info.index] = info
                calculated_targets_act[info_act.index] = info_act
                calculated_targets_act['add_info'] = add_info
                
                #####
                # Add 'calculated_targets_act' to 'calculated_targets'.
                calculated_targets = calculated_targets.append(calculated_targets_act, ignore_index=True)
            # endfor
        # endif
    # endfor
    
    #####
    # Write out data.
    calculated_targets.to_csv(Path(path_output, 'ndc_targets.csv'), index=False)
    print("done calculating the targets ...")
    
    #####
    return calculated_targets
# enddef

# %%
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def ndcs_calculate_targets(database, meta):
    """
    Calculate the NDC targets for each of the target types available for a country.
    Some NDCs give more than one target type (e.g., they give the absolute value, 
    but say that it is a RBU target and therefore give the % reduction against BAU).
    
    EU28 countries are calculated separately, using the NDC information from the EU28 NDC.
    The per-country target emissions for EU28 countries does not equal the 'real' emissions targets 
    (each of the countries has its own targets to in-sum get to the EU28 total target).
    """
        
    # %%
    def check_ndc_values(ict, iso_act):
        """
        Check if ndc_values seem ok.
        For the different target types there are some criteria to check if the ndc_value seems plausible.
        Does not cover every eventuality.
        """
        
        for ndc_value in [ict['ndc_value_exclLU'], ict['ndc_value_inclLU']]:
            
            if type(ndc_value) == str:
                
                if (ict['tar_type_used'] == 'ABS') \
                    and ('MTCO2' not in ndc_value.replace(' ', '').upper()):
                    print(f"- **{iso_act}**: tar_type_used is {ict['tar_type_used']}, but 'MtCO2' is not in ndc_value!" +
                          f"\n    ndc_value = {ndc_value}")
                
                elif (ict['tar_type_used'] in ['RBY', 'RBU', 'REI']) \
                    and (('%' not in ndc_value) or ('-' not in ndc_value)):
                    print(f"- **{iso_act}**: tar_type_used is {ict['tar_type_used']}, but '%' or/and '-' is not in ndc_value!" +
                          f"\n    ndc_value = {ndc_value}")
                
                elif (ict['tar_type_used'] == 'ABU') \
                    and (('MTCO2' not in ndc_value.replace(' ', '').upper()) or ('-' not in ndc_value)):
                    print(f"- **{iso_act}**: tar_type_used is {ict['tar_type_used']}, but 'MtCO2' or/and '-' is not in ndc_value!" +
                          f"\n    ndc_value = {ndc_value}")
                
                elif (ict['tar_type_used'] == 'AEI') \
                    and (('TCO2' not in ndc_value.replace(' ', '').upper()) or ('MTCO2' in ndc_value.replace(' ', '').upper())):
                    print(f"- **{iso_act}**: tar_type_used is {ict['tar_type_used']}, but 'tCO2' or/and 'MtCO2' is in ndc_value!" +
                          f"\n    ndc_value = {ndc_value}")
    
    # %%
    def strengthen_targets(meta, ict, ndc_value_exclLU, ndc_value_inclLU, iso_act):
        """
        Apply a strengthening to the targets.
        Depends on 'how_to' ('multiply' or 'add').
        
        'add': the reduction is increased by adding the value in 'pc'.
        'multiply': the reduction is increased by multiplying with (100% + the value in 'pc').        
        If this results in a % reduction that exceeds 100%, it is set to 100% (meaning a total 
        reduction ...).
        
        For absolute targets (ABS, ABU, AEI), it is not distinguished between 'add' and 'multiply'.
        """
        
        if ict['tar_type_used'] in ['RBY', 'RBU', 'REI']:
            
            if meta.strengthen_targets['how_to'] == 'multiply':
                # E.g., ndc_value = -20%, strengthen_targets = 10%. new = -.2*1.1 = -.22!
                ndc_value_exclLU_new = ndc_value_exclLU * (1. + meta.strengthen_targets['pc']/100.)
                ndc_value_inclLU_new = ndc_value_inclLU * (1. + meta.strengthen_targets['pc']/100.)
            
            if meta.strengthen_targets['how_to'] == 'add':
                # E.g., ndc_value = -20%, strengthen_targets = 10%. new = -20-10 = -30!
                ndc_value_exclLU_new = ndc_value_exclLU - meta.strengthen_targets['pc'] 
                ndc_value_inclLU_new = ndc_value_inclLU - meta.strengthen_targets['pc'] 
                # ndc_value is negative, e.g., -20%.
            
            # If ndc_value_new is bigger than a 100% reduction (regarding the covered part of emissions ...), 
            # set it to 100% reduction.
            ndc_value_exclLU = (-100. if (ndc_value_exclLU_new < -100.) and (ndc_value_exclLU > -100.)
                else ndc_value_exclLU_new)
            ndc_value_inclLU = (-100. if (ndc_value_inclLU_new < -100.) and (ndc_value_inclLU > -100.)
                else ndc_value_inclLU_new)
            
            # Add information to DataFrame.
            ict['ndc_strengthen_tar'] = (
                "ndc_value is multiplied with " + str(1. + meta.strengthen_targets['pc']/100.) 
                if meta.strengthen_targets['how_to'] == 'multiply'
                else str(meta.strengthen_targets['pc']) + "% is added to ndc_value ") + \
                " (new value exclLU: " + str(ndc_value_exclLU_new) + \
                ", new value inclLU: " + str(ndc_value_inclLU_new) + ")."
        
        elif ict['tar_type_used'] in ['ABS', 'AEI']:
            
            ndc_value_exclLU_new = ndc_value_exclLU * (1. - meta.strengthen_targets['pc']/100.)
            ndc_value_inclLU_new = ndc_value_inclLU * (1. - meta.strengthen_targets['pc']/100.)
            
            # Add information to DataFrame.
            ict['ndc_strengthen_tar'] = \
                "ndc_value is multiplied with " + str(1. - meta.strengthen_targets['pc']/100.) + \
                " (new value exclLU: " + str(ndc_value_exclLU_new) + \
                ", new value inclLU: " + str(ndc_value_inclLU_new) + ")."
        
        elif ict['tar_type_used'] == 'ABU':
            
            ndc_value_exclLU_new = ndc_value_exclLU * (1. + meta.strengthen_targets['pc']/100.)
            ndc_value_inclLU_new = ndc_value_inclLU * (1. + meta.strengthen_targets['pc']/100.)
            
            # Add information to DataFrame.
            ict['ndc_strengthen_tar'] = \
                "ndc_value is multiplied with " + str(1. + meta.strengthen_targets['pc']/100.) + \
                " (new value exclLU: " + str(ndc_value_exclLU_new) + \
                ", new value inclLU: " + str(ndc_value_inclLU_new) + ")."
        
        return meta, ict, ndc_value_exclLU, ndc_value_inclLU
    
    # %%
    def calculate_targets_depending_on_type(
        ict, iso_act, refyr, taryr, ndc_value_exclLU, ndc_value_inclLU, meta):
        
        """
        Calculation of targets: excluding LULUCF and including LULUCF.
        """
        
        #
        import numpy as np
        import sys
        
        """
        Emissions values from NDCs.
        """
        ndcs_emi_inclLU = database.emi_bl_inclLU_ndcs.loc[iso_act, :]
        ndcs_emi_exclLU = database.emi_bl_exclLU_ndcs.loc[iso_act, :]
        ndcs_emi_onlyLU = database.emi_bl_onlyLU_ndcs.loc[iso_act, :]
        
        """
        NDC-level for relative targets. E.g., target is -20%, so the level is 80% (100%-20%).
        """
        if ict['tar_type_used'] in ['RBY', 'RBU', 'REI']:
            ndc_level_exclLU = 1. + ndc_value_exclLU / 100.
            ndc_level_inclLU = 1. + ndc_value_inclLU / 100.
        
        """
        Get the information on whether LULUCF is included in the target or not.
        """
        is_LU_covered_valinfo = (True if not np.isnan(ndc_value_inclLU) else False)
        is_LU_covered_secinfo = (True if ict['lulucf'].upper() == 'YES' else False)
        if is_LU_covered_valinfo:
            if not is_LU_covered_secinfo:
                if (not np.isnan(ndc_value_exclLU) and not np.isnan(ndc_value_inclLU)):
                    pass
                else:
                    print(f"- **{iso_act}** ({ict['tar_type_used']}): something went wrong with the LULUCF coverage. " +
                         f"The ndc-value is {('inclLU' if is_LU_covered_valinfo else 'exclLU')} " +
                         f"but the LULUCF sector is {('covered' if is_LU_covered_secinfo else 'not covered')}!")
        
        """
        Get the reference year (refyr for RBY and REI_RBY, else taryr).
        """
        if ((ict['tar_type_orig'] == 'RBY') or (ict['tar_type_orig'] == 'REI' and ict['refyr'] != ict['taryr'])):
            year_int, refyr_or_taryr = [refyr, 'refyr']
        else:
            year_int, refyr_or_taryr = [taryr, 'taryr']
        
        #
        def calc_targets_inclLU_exclLU(tar_emi_exclLU, tar_emi_inclLU, year_int, refyr_or_taryr):
            
            """
            If no inclLU target is given, calculate it as the sum over tar_emi_exclLU and bl_LU.
            """
            if np.isnan(tar_emi_inclLU):
                bl_onlyLU = ndcs_emi_onlyLU[year_int]
                if np.isnan(bl_onlyLU):
                    bl_onlyLU = ict[f'emi_bl_LU_{refyr_or_taryr}']
                tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU]) # nansum to prevent 'no-result' due to missing bl_onlyLU.
            
            """
            Options to calculate the exclLU target from the given inclLU target:
                
                meta.prio_tar_exclLU_from_tar_inclLU == 'apply_rel_red_to_emi_exclLU':
                    If no exclLU target is given, calculate it assuming the same % reductions in all sectors.
                    Calculate the % reduction of ABS_inclLU compared to the bl_inclLU (use the value given in NDC, if possible)
                    and apply it to our emi_bl_exclLU (assuming 100% coverage).
                
                meta.prio_tar_exclLU_from_tar_inclLU == 'subtract_LU_in_taryr':
                    If no exclLU target is given, subtract the target year onlyLU estimate from the inclLU target (like CAT).
            """
            if np.isnan(tar_emi_exclLU):
                
                if meta.prio_tar_exclLU_from_tar_inclLU == 'apply_rel_red_to_emi_exclLU':
                    bl_inclLU = ndcs_emi_inclLU[year_int]
                    if np.isnan(bl_inclLU):
                        bl_inclLU = np.nansum([ict[f'emi_bl_exclLU_{refyr_or_taryr}'], ict[f'emi_bl_LU_{refyr_or_taryr}']])
                    
                    # ! This is kind of wrong (when the signs differ)...
                    rel_level_vs_inclLU = abs(tar_emi_inclLU / bl_inclLU)
                    if (tar_emi_inclLU < 0 or bl_inclLU < 0):
                        print(f"- **{iso_act}** ({ict['tar_type_used']}): calculating the relative reduction for inclLU: " +
                              f"the baseline emissions (inclLU) are {('negative' if bl_inclLU < 0 else 'positive')} ({bl_inclLU :.2f}) " +
                              f"and the target emissions inclLU are {('negative' if tar_emi_inclLU < 0 else 'positive')} ({tar_emi_inclLU :.2f})!")
                    
                    ndcs_available_data = [ndcs_emi_exclLU[year_int], ndcs_emi_inclLU[year_int], ndcs_emi_onlyLU[year_int]]
                    if len([True for xx in ndcs_available_data if not np.isnan(xx)]) > 1:
                        print(f"- **{iso_act}** ({ict['tar_type_used']}): enough emissions data for the quantification of tar_emi_exclLU are given, why don't we use them?")
                    
                    tar_emi_exclLU = ict[f'emi_bl_exclLU_{refyr_or_taryr}'] * rel_level_vs_inclLU
                    
                    if tar_emi_exclLU < 0:
                        print(f"- **{iso_act}** ({ict['tar_type_used']}): the ABS_exclLU target emissions " +
                              f"based on given ABS_inclLU ({tar_emi_inclLU :.2f}) " +
                              f"and the ratio between tar_emi_inclLU and emi_bl_inclLU_{refyr_or_taryr} " +
                              f"(abs({tar_emi_inclLU :.2f} / {bl_inclLU :.2f}) = {rel_level_vs_inclLU :.2f}) " +
                              f"were negative and set from {tar_emi_exclLU :.2f} to 0!")
                        tar_emi_exclLU = 0.
                
                elif meta.prio_tar_exclLU_from_tar_inclLU == 'subtract_LU_in_taryr':
                    bl_onlyLU = ndcs_emi_onlyLU[year_int]
                    if np.isnan(bl_onlyLU):
                        bl_onlyLU = ict[f'emi_bl_LU_taryr']
                    tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU])
                    
                    if tar_emi_exclLU < 0:
                        print(f"- **{iso_act}** ({ict['tar_type_used']}): the ABS_exclLU target emissions " +
                              f"based on given ABS_inclLU ({tar_emi_inclLU :.2f}), subtracting the " +
                              f"target year LULUCF emissions ({bl_onlyLU :.2f}" +
                              f"{(' from the NDC' if not np.isnan(ndcs_emi_onlyLU[year_int]) else ', value not available in the NDC')}) " +
                              f"were negative and set from {tar_emi_exclLU :.2f} to 0!")
                        tar_emi_exclLU = 0.
                
                else:
                    sys.exit("No valid option to derive exclLU targets from inclLU targets is given.")
                
            
            ict['tar_emi_exclLU'] = tar_emi_exclLU
            ict['tar_emi_inclLU'] = tar_emi_inclLU
            
            if tar_emi_inclLU < 0:
                print(f"- **{iso_act}** ({ict['tar_type_used']}): ABS inclLU is negative ({tar_emi_inclLU :.2f})!")
        
        """ABS target"""
        if ict['tar_type_used'] == 'ABS':
            
            tar_emi_exclLU = ndc_value_exclLU
            tar_emi_inclLU = ndc_value_inclLU
            
            calc_targets_inclLU_exclLU(tar_emi_exclLU, tar_emi_inclLU, year_int, refyr_or_taryr)
        
        """ABU target"""
        if ict['tar_type_used'] == 'ABU':
            
            tar_emi_exclLU = np.nan
            if not np.isnan(ndc_value_exclLU):
                bl_exclLU_taryr = ndcs_emi_exclLU[taryr]
                if np.isnan(bl_exclLU_taryr):
                    bl_exclLU_taryr = ict['emi_bl_exclLU_taryr']
                tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU # ndc_value is negative for a reduction ...
            
            tar_emi_inclLU = np.nan
            if not np.isnan(ndc_value_inclLU):
                bl_inclLU_taryr = ndcs_emi_inclLU[taryr]
                if np.isnan(bl_inclLU_taryr):
                    bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], ict['emi_bl_LU_taryr']])
                tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU
                    
            calc_targets_inclLU_exclLU(tar_emi_exclLU, tar_emi_inclLU, year_int, refyr_or_taryr)
            
            if ict['tar_emi_exclLU'] < 0:
                if np.isnan(ndc_value_exclLU):
                    print(f"- **{iso_act}**: the exclLU target emissions for ABU (based on given ABU_inclLU) " +
                          f"were negative and set from {ict['tar_emi_exclLU'] :.2f} to 0!")
                else:
                    print(f"- **{iso_act}**: the exclLU target emissions for ABU (based on given ABU_exclLU: {ndc_value_exclLU :.2f}, " +
                          f"and the baseline emissions from {('the NDC' if not np.isnan(ndcs_emi_exclLU[taryr]) else 'the SSP')}: " +
                          f"{bl_exclLU_taryr :.2f}) " +
                          f"were negative and set from {ict['tar_emi_exclLU'] :.2f} to 0!")
                ict['tar_emi_exclLU'] = 0.
        
        """AEI target"""
        if ict['tar_type_used'] == 'AEI':
            
            # Get the intensity reference (POP or GDP)
            if ('CAP' in str(ict['ndc_value_exclLU']).upper() or 
                'CAP' in str(ict['ndc_value_inclLU']).upper()):
                ref_act = ict['pop_taryr']
            elif ('GDP' in str(ict['ndc_value_exclLU']).upper() or
                  'GDP' in str(ict['ndc_value_inclLU']).upper()):
                ref_act = ict['gdp_taryr']
            else:
                ref_act = np.nan
                print(f"- **{iso_act}** AEI:, it is not clear which reference to use. " +
                      f"The target is {ict['ndc_value']}. Nothing has been calculated.")
            
            if not np.isnan(ref_act):
                
                tar_emi_exclLU = np.nan
                if not np.isnan(ndc_value_exclLU):
                    tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act
                
                tar_emi_inclLU = np.nan
                if not np.isnan(ndc_value_inclLU):
                    tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act
                
                calc_targets_inclLU_exclLU(tar_emi_exclLU, tar_emi_inclLU, year_int, refyr_or_taryr)
            
        """RBY, RBU or REI target"""
        if ict['tar_type_used'] in ['RBY', 'RBU', 'REI']:
            
            """
            For these targets, the NDC data are not used, as when possible they were already used to
            derive ABS inclLU or exclLU.
            
            For REI targets, the GDP or population growth rate is not taken into account
            in the LULUCF part of the target.
            Else, the effects of the LULUCF part can be unrealisticly large,
            especially when LULUCF was a sink in the reference year, when the strength of 
            a sink would increase a lot due to the intensity growth.
            """
            
            emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr']
            emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr'])
            
            # REI compared to BAU is same as RBU.
            # For REI_RBY, the emissions intensities must be used.
            if ict['tar_type_used'] == 'REI' and refyr != taryr:
                intensity_growth = ict[ict['int_ref'].lower() + '_taryr'] / ict[ict['int_ref'].lower() + '_refyr']
            else:
                intensity_growth = 1.
            
            # exclLU (gives nan if ndc_level_exclLU is nan).
            tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr
            if meta.prio_tar_exclLU_from_tar_inclLU == 'apply_rel_red_to_emi_exclLU':
                if np.isnan(tar_emi_exclLU):
                    """
                    If meta.prio_tar_exclLU_from_tar_inclLU == 'apply_rel_red_to_emi_exclLU' and the 
                    ndc_level_exclLU == nan, we use the ndc_level_inclLU for exclLU as well 
                    (assuming equal relative reductions per sector).
                    Else the exclU target will be calculated by subtracting the target year onlyLU emissions.
                    """
                    tar_emi_exclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr
            
            # inclLU
            # Using the ndc_level_inclLU for exclLU as well (assuming equal relative reductions per sector).
            tar_emi_inclLU = np.nan
            if not np.isnan(ndc_level_inclLU):
                
                # exclLU part:
                tar_part_exclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr
                
                # LULUCF part:
                is_LU_sink_in_refyr = (True if ict['emi_bl_LU_refyr'] < 0 else False)                
                if is_LU_sink_in_refyr:
                    ndc_level_LU = 1. - ndc_value_inclLU / 100. # Strengthen sink.
                else:
                    ndc_level_LU = ndc_level_inclLU # Weaken source.
                tar_part_onlyLU = ndc_level_LU * ict['emi_bl_LU_refyr']
                
                # Sum over exclLU and onlyLU parts.
                tar_emi_inclLU = np.nansum([tar_part_exclLU, tar_part_onlyLU]) # nansum to prevent 'no-result' for missing emi_bl_LU_refyr.
            
            calc_targets_inclLU_exclLU(tar_emi_exclLU, tar_emi_inclLU, year_int, refyr_or_taryr)
        
        if ict['tar_emi_exclLU'] < 0:
            print(f"- **{iso_act}**: the tar_emi_exclLU for {ict['tar_type_used']} was negative and is set to 0!")
            ict['tar_emi_exclLU'] = 0.
        
        return ict
    
    # %%
    import pandas as pd
    import numpy as np
    from pathlib import Path
    from copy import deepcopy
    import helpers_functions as hpf
    
    # %%
    # Set up for pd.DataFrame where to store the in / output (for each calculated target one row is added).
    # column_names will be the columns, and column_units will be put to first row.
    column_names = {
        'add_info': ['add_info'],
        'ndc': ['iso3', 'tar_type_used', 'tar_type_calc', 'tar_type_orig', 'condi', 'rge',
                'ndc_value_exclLU', 'ndc_value_inclLU', 
                'ndc_strengthen_tar', 'int_ref', 'refyr', 'taryr'],
        'tar': ['tar_emi_exclLU' , 'tar_emi_inclLU'],
        'emi': ['gwp', 'scenario', 'emi_bl_exclLU_refyr', 'emi_bl_exclLU_taryr', 
                'emi_bl_LU_refyr', 'emi_bl_LU_taryr'],
        'cov': ['pc_cov_set_to_100', 'pc_cov_exclLU_refyr', 'pc_cov_exclLU_taryr'],
        'int_ref': ['pop_refyr', 'pop_taryr', 'gdp_refyr', 'gdp_taryr'],
        'cov_gases': ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3'],
        'cov_sectors': ['energy', 'ippu', 'agriculture', 'waste', 'other', 'lulucf'],
        'lulucf_fyson': ['lulucf_tar_2030_fyson2019']}
    
    column_units = {
        'add_info': [None],
        'ndc': [None]*8 + [None]*4,
        'tar': [meta.units.default['emi']]*2,
        'emi': [None, None] + [meta.units.default['emi'] + " (" + meta.gwps.default + ")"]*4,
        'cov': [None, '%', '%'],
        'int_ref': [meta.units.default['pop'], meta.units.default['pop'], 
                    meta.units.default['gdp'], meta.units.default['gdp']],
        'cov_gases': ['nan'] * len(column_names['cov_gases']),
        'cov_sectors': ['nan'] * len(column_names['cov_sectors']),
        'lulucf_fyson': ['MtCO2eq']} 
    
    # Setup Dataframe (columns are all the sub-items in column_names):
    calculated_targets = pd.DataFrame(columns=[yy for xx in column_names for yy in column_names[xx]])
    # Add the units as first row:
    calculated_targets.loc[0, :] = [yy for xx in column_units for yy in column_units[xx]]
    
    # Get the LULUCF target quantifications by Fyson and Jeffery (2019) for the output.
    meta.lulucf_fyson = pd.read_csv(Path(meta.path.main, 'data', 'input', 'lulucf_fyson_2019', 
        'fyson_2019_LUlucf_paper_suppl_quanti.csv'), index_col='country')
    
    """
    Iterate through the iso3s in meta.ndcs_info (EU28 as single countries, using the EU28 target info).
    Calculate 'all available targets' per country (targets as in meta.ndcs_info, in columns 
    ['ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI']).
    """
    for iso_act in sorted(list(set(set(meta.ndcs_info.index) - set(['EU28'])))):
        
        # For EU28 countries: use the ndc info from EU28.
        iso_ndc = ('EU28' if iso_act in meta.isos.EU28 else iso_act)
        
        # Get ndc information.
        ndc_act = meta.ndcs_info.loc[iso_ndc, :]
        ndc_act.index = [xx.upper() for xx in ndc_act.index]
        
        # Get time series for 'to_add'.
        to_add = ['emi_bl_exclLU', 'emi_bl_LU', 'pc_cov_exclLU', 'pop', 'gdp']
        ts_act = pd.DataFrame(index=to_add, columns=meta.years.all)
        for add in to_add:
            ts_to_add = deepcopy(getattr(database, add).data)
            if iso_act in list(ts_to_add.index):
                ts_act.loc[add, :] = ts_to_add.loc[iso_act, ts_act.columns].values
        
        # Get info that is the same for that country, no matter which target year & un/conditional target it is,
        # and put it into 'info_general'.
        info_general = pd.Series(index=calculated_targets.columns, dtype='object')
        info_general[['iso3', 'tar_type_calc', 'tar_type_orig', 'int_ref']] = \
            [iso_act] + list(ndc_act.loc[['TYPE_CALC', 'TYPE_ORIG', 'INTENSITY_PERCAP_GDP']].values)
        
        # Values from coverage_used (does not need to be the originally given info from the NDCs...).
        coverage_iso3 = meta.coverage.loc[iso_act, :]
        info_general[column_names['cov_gases']] = coverage_iso3[[xx.upper() for xx in column_names['cov_gases']]]
        info_general[column_names['cov_sectors']] = \
            coverage_iso3[[meta.sectors.main.sec_to_cat[xx.upper()] for xx in column_names['cov_sectors']]]
        
        """
        Calculate targets for all target types with values available in the input ndc-table
        (['ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI']).
        """
        for tar_type in set(set(meta.target_types) - set(['NGT'])):
            
            """
            Get all available target years & un/conditional & best/worst targets.
            ndc_value depends on the target type, either it is an absolute emission (ABS, ABU), 
            a percentage for relative reductions (RBY, RBU, REI), or an emissions intensity (AEI).
            ABS: target emissions in MtCO2eq.
            ABU: absolute  reduction in MtCO2eq (e.g., -3500 stands for 3500 MtCO2eq reduction).
            RBY, RBU, REI: percentage reduction (e.g., -20 stands for 20% reduction).
            AEI: emissions intensity in target year, e.g., 3.2 stands for 3.2 t/cap or 3.2 t/GDP, when int_ref is
            POP or GDP, respectively.
            """
            
            # In meta.ndcs_info, the 'available targets' per target type are stored as nested dictionaries 
            # and can be read in using json. Targets are also separated in 'including_LUlucf' and 'excluding_LUlucf'.
            # Only do anything if there are values available for that target type (and country).
            ndc_values_all_json = ndc_act.loc[tar_type]
            
            if (type(ndc_values_all_json) == str and ndc_values_all_json.upper() != 'NAN'):
                """
                For paper: option to put IND target to conditional or unconditional.
                Normally: outcommented.
                """
                #if iso_act == 'IND':
                #    ndc_values_all_json = ndc_values_all_json.replace('unconditional', 'conditional')
                
                ndc_values_all = hpf.get_targets_from_json(ndc_values_all_json, tar_type, iso_act)
                
                """
                Iterate through the combinations of target years & un/conditional & best/worst.
                Do the calculations depending on the ndc values and the target type.
                """
                for curr_tar in ndc_values_all.index:
                    
                    # In 'ict' all information on the current target (in this iteration) is stored.
                    ict = deepcopy(info_general)
                    
                    # Fill ict with information.
                    ict['condi', 'rge'] = ndc_values_all.loc[curr_tar, ['condi', 'rge']].values
                    ict['tar_type_used', 'taryr'] = tar_type, ndc_values_all.loc[curr_tar, 'taryr']
                    taryr = int(ict['taryr'])
                    
                    # Get the reference year (base year) and get emissions, pop, gdp values for refyr.
                    refyr = ndc_act.loc['BASEYEAR']
                    refyr = (int(refyr) 
                             if ((type(refyr) == str and refyr.upper() != 'NAN') or ((type(refyr) != str and not np.isnan(refyr)))) 
                             else taryr)
                    ict['refyr'] = refyr
                    
                    ict[['emi_bl_exclLU_refyr', 'emi_bl_LU_refyr', 'pc_cov_exclLU_refyr']] = \
                        list(ts_act.loc[['emi_bl_exclLU', 'emi_bl_LU', 'pc_cov_exclLU',], refyr].values)
                    ict[['pop_refyr', 'gdp_refyr']] = list(ts_act.loc[['pop', 'gdp'], refyr].values)
                    
                    ict['ndc_value_exclLU', 'ndc_value_inclLU'] = \
                        ndc_values_all.loc[curr_tar, ['exclLU', 'inclLU']].values
                    ict[['gwp', 'scenario', 'emi_bl_exclLU_taryr', 'emi_bl_LU_taryr', 
                        'pc_cov_exclLU_taryr']] = \
                        [meta.gwps.default, meta.ssps.chosen] + \
                        list(ts_act.loc[['emi_bl_exclLU', 'emi_bl_LU', 'pc_cov_exclLU'], taryr].values)
                    ict[['pop_taryr', 'gdp_taryr']] = list(ts_act.loc[['pop', 'gdp'], taryr].values)
                    
                    """
                    Set the coverage to 100% (not changing LULUCF).
                    Only if meta.set_pccov_to_100 is True and the country is in the 'wanted' countries.
                    Only for relative targets / reductions.
                    """
                    if (meta.set_pccov_to_100['use_it'] and iso_act in meta.set_pccov_to_100['countries']):
                        if tar_type in ['RBY', 'RBU', 'REI']:
                            ict['pc_cov_set_to_100'] = 'Yes (not lulucf)'
                            ict['pc_cov_exclLU_refyr', 'pc_cov_exclLU_taryr'] = 1.
                    
                    """
                    Check if ndc_values seem ok.
                    For the different target types there are some criteria to check if the ndc_value seems plausible.
                    Does not cover every eventuality.
                    """
                    check_ndc_values(ict, iso_act)
                    
                    """
                    Get the numerical values from ndc_value_exclLU and ndc_value_inclLU.
                    exclLU or inclLU was assessed based on the NDCs and stored together with the targets 
                    (reductions or absolute values).
                    exclLU was chosen if LULUCF is not covered, or if LULUCF was covered, but it was stated that this value is for exclLU.
                    inclLU was chosen if LULUCF is covered, or if LULUCF was not covered and it was stated that this value is for inclLU.
                    """
                    ndc_value_exclLU = hpf.get_numerical_value_from_ndcval(ict['ndc_value_exclLU'])
                    ndc_value_inclLU = hpf.get_numerical_value_from_ndcval(ict['ndc_value_inclLU'])
                    
                    """
                    Convert the given absolute value to AR4 (no conversion factors for AR5 available).
                    Based on national conversion factors from AR2 to AR4 from PRIMAPHIST21 KYOTOGHG_IPCM0EL.
                    """
                    if tar_type in ['ABS', 'ABU', 'AEI']:
                        ndcval_to_check = f"{ict['ndc_value_exclLU']} {ict['ndc_value_inclLU']}"
                        if (('AR2' in ndcval_to_check) or ('SAR' in ndcval_to_check)):
                            conversion_gwp = hpf.get_conversion_gwp_national([iso_act], 'AR2', 'AR4').values[0]
                            ndc_value_exclLU = ndc_value_exclLU * conversion_gwp
                            ndc_value_inclLU = ndc_value_inclLU * conversion_gwp
                    
                    """
                    If strengthen NDC is chosen apply the strengthening to the reductions.
                    """
                    if ((meta.strengthen_targets['use_it'])
                        and (iso_act in meta.strengthen_targets['countries'])):
                        meta, ict, ndc_value_exclLU, ndc_value_inclLU = \
                            strengthen_targets(meta, ict, ndc_value_exclLU, ndc_value_inclLU, iso_act)
                    
                    """
                    Calculate the mitigated target year emissions depending on the target type.
                    """
                    ict = calculate_targets_depending_on_type(
                        ict, iso_act, refyr, taryr, ndc_value_exclLU, ndc_value_inclLU, meta)
                    
                    # If tar_emi_inclLU or tar_emi_exclLU are empty but the other value exists, 
                    # put the value to both columns.
                    #val_replace = [ict['tar_emi_exclLU'], ict['tar_emi_inclLU']]
                    #val_replace = [xx for xx in val_replace if not np.isnan(xx)]
                    #if len(val_replace) == 1:
                    #    ict['tar_emi_exclLU'] = val_replace[0]
                    #    ict['tar_emi_inclLU'] = val_replace[0]
                    
                    # Change format of the values for ndc_value_corrected_for_LU_and_pc_cov.
                    """
                    if not np.isnan(ict['ndc_value_corrected_for_LU_and_pc_cov']):
                        ict['ndc_value_corrected_for_LU_and_pc_cov'] = \
                            '{:+.2f}'.format(ict['ndc_value_corrected_for_LU_and_pc_cov']) + '%'
                    """
                    
                    # Put Fyson2019 LULUCF 2030 emissions in output, not used further.
                    if iso_act in meta.lulucf_fyson.index:
                        lu_fy = meta.lulucf_fyson.loc[iso_act, :]
                        lu_fy = lu_fy[['minimum_' + ict['condi'], 'maximum_' + ict['condi']]].astype(float)
                        if ict['rge'] == 'best':
                            lu_fy = min(lu_fy)
                        else:
                            lu_fy = max(lu_fy)
                        
                        ict['lulucf_tar_2030_fyson2019'] = lu_fy

                    # Add 'ict' to 'calculated_targets'.
                    calculated_targets = calculated_targets.append(ict, ignore_index=True)
    
    # Write out data.
    calculated_targets.to_csv(Path(meta.path.output_ndcs, 'ndc_targets.csv'), index=False)
    print("done calculating the targets ...")
    
    # %%
    return calculated_targets

# %%
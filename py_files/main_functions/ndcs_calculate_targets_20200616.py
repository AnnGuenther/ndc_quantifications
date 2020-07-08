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
                    print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                          ict['tar_type_used'] + ", but 'MtCO2' is not in ndc_value!" +
                          "\n    ndc_value = " + ndc_value)
                
                elif (ict['tar_type_used'] in ['RBY', 'RBU', 'REI']) \
                    and (('%' not in ndc_value) or ('-' not in ndc_value)):
                    print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                          ict['tar_type_used'] + ", but '%' or/and '-' is not in ndc_value!" +
                          "\n    ndc_value = " + ndc_value)
                
                elif (ict['tar_type_used'] == 'ABU') \
                    and (('MTCO2' not in ndc_value.replace(' ', '').upper()) or ('-' not in ndc_value)):
                    print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                          ict['tar_type_used'] + ", but 'MtCO2' or/and '-' is not in ndc_value!" +
                          "\n    ndc_value = " + ndc_value)            
                
                elif (ict['tar_type_used'] == 'AEI') \
                    and (('TCO2' not in ndc_value.replace(' ', '').upper()) or ('MTCO2' in ndc_value.replace(' ', '').upper())):
                    print("Warning in main_ndc_quantifications for " + iso_act + ": tar_type_used is " +
                          ict['tar_type_used'] + ", but 'tCO2' or/and 'MtCO2' is in ndc_value!" +
                          "\n    ndc_value = " + ndc_value)
    
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
    def calculate_targets_depending_on_type(ict, iso_act, refyr, taryr, ndc_value_exclLU, ndc_value_inclLU, meta):
        """
        Calculation of targets: excluding LULUCF and including LULUCF.
        """
        
        #
        def emi_target_inclLU(exclLUemiTarget, LUemiTarget):
            
            return exclLUemiTarget + LUemiTarget
        
        def emi_target_exclLU(inclLUemiTarget, LUemiTarget):
            
            return inclLUemiTarget - LUemiTarget
        
        def relative_target_exclLU(
            intensity_growth, ndc_level, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr):
            
            return intensity_growth * ndc_level * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr
        
        def relative_target_inclLU(
            intensity_growth, ndc_value, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr,
            emi_bl_LU_refyr, emi_bl_LU_taryr, is_LU_covered):
            
            ndc_level = 1. + ndc_value / 100.
            tar_exclLU = relative_target_exclLU(
                intensity_growth, ndc_level, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr) \
                
            if not is_LU_covered:
                
                tar_inclLU = tar_exclLU + emi_bl_LU_taryr
            
            else:
                
                is_LU_sink_in_refyr = (True if emi_bl_LU_refyr < 0 else False)
                
                if is_LU_sink_in_refyr:
                    
                    ndc_level_LU = 1. - ndc_value / 100.
                
                else:
                    
                    ndc_level_LU = ndc_level
                    
                tar_inclLU = tar_exclLU + ndc_level_LU * emi_bl_LU_refyr
                
            return tar_inclLU
        
        #
        import numpy as np
        from warnings import warn
        
        #
        """
        Get the % reduction (only used in calculations of relative targets).
        Also get the share of national emissions covered.
        """
        
        #    
        if ict['tar_type_used'] == 'ABS':
            
            # No prioritisation of exclLU or inclLU.
            if ((meta.prioritisation_lulucf in ['exclLU_and_inclLU', 'exclLU_for_relative_no_prio_for_absolute']) 
                or (np.isnan(ndc_value_exclLU) or np.isnan(ndc_value_inclLU))):
                
                # exclLU
                ict['tar_emi_exclLU'] = (
                    ndc_value_exclLU if not np.isnan(ndc_value_exclLU)
                    else emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr']))
                
                # inclLU
                ict['tar_emi_inclLU'] = (
                    ndc_value_inclLU if not np.isnan(ndc_value_inclLU)
                    else emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr']))
                
                # Calculate exclLU/inclLU from the 'other case' (inclLU/exclLU) if needed.
                
                # exclLU
                if np.isnan(ict['tar_emi_exclLU']):
                    ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
                
                # inclLU
                if np.isnan(ict['tar_emi_inclLU']):
                    ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of exclLU.
            elif (meta.prioritisation_lulucf == 'exclLU' and not np.isnan(ndc_value_exclLU)):
                
                # exclLU
                ict['tar_emi_exclLU'] = (
                    ndc_value_exclLU if not np.isnan(ndc_value_exclLU)
                    else emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr']))
            
                # Calculate inclLU from exclLU.
                
                # inclLU
                ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of inclLU.
            elif (meta.prioritisation_lulucf == 'inclLU' and not np.isnan(ndc_value_inclLU)):
                
                # inclLU
                ict['tar_emi_inclLU'] = (
                    ndc_value_inclLU if not np.isnan(ndc_value_inclLU)
                    else emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr']))
                
                # Calculate exclLU from inclLU.
                
                # exclLU
                ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
            
            else:
                warn(f"Something went wrong for {iso_act} ({ict['tar_type_used']}).")
            
            # TODO: I do not check if for ABS everything is covered in the NDC. 
            # Should I add the not-covered part of emissions in the target year?!
        
        #
        elif ict['tar_type_used'] == 'ABU':
            
            # No prioritisation of exclLU or inclLU.
            if ((meta.prioritisation_lulucf in ['exclLU_and_inclLU', 'exclLU_for_relative_no_prio_for_absolute']) 
                or (np.isnan(ndc_value_exclLU) or np.isnan(ndc_value_inclLU))):
                
                # exclLU
                if not np.isnan(ndc_value_exclLU):
                    ict['tar_emi_exclLU'] = ict['emi_bl_exclLU_taryr'] + ndc_value_exclLU # ndc_value is negative ...
                
                # inclLU
                if not np.isnan(ndc_value_inclLU):
                    ict['tar_emi_inclLU'] = ict['emi_bl_exclLU_taryr'] + ict['emi_bl_LU_taryr'] + ndc_value_inclLU
                
                # Calculate exclLU/inclLU from the 'other case' (inclLU/exclLU) if needed.
                
                # exclLU
                if np.isnan(ict['tar_emi_exclLU']):
                    ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
                
                # inclLU
                if np.isnan(ict['tar_emi_inclLU']):
                    ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of exclLU.
            elif (meta.prioritisation_lulucf == 'exclLU' and not np.isnan(ndc_value_exclLU)):
                
                # exclLU
                ict['tar_emi_exclLU'] = ict['emi_bl_exclLU_taryr'] + ndc_value_exclLU # ndc_value is negative ...
                
                # Calculate inclLU from exclLU.
                
                # inclLU
                ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of inclLU.
            elif (meta.prioritisation_lulucf == 'inclLU' and not np.isnan(ndc_value_inclLU)):
                
                # inclLU
                ict['tar_emi_inclLU'] = ict['emi_bl_exclLU_taryr'] + ict['emi_bl_LU_taryr'] + ndc_value_inclLU
                
                # Calculate exclLU from inclLU.
                
                # exclLU
                ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
            
            else:
                warn(f"Something went wrong for {iso_act} ({ict['tar_type_used']}).")
        
        #
        elif ict['tar_type_used'] == 'AEI':
            
            # Get the intensity reference (POP or GDP)
            if ('CAP' in str(ict['ndc_value_exclLU']).upper() or 
                'CAP' in str(ict['ndc_value_inclLU'].upper())):
                ref_act = ict['pop_taryr']
            elif ('GDP' in str(ict['ndc_value_exclLU']).upper() or
                  'GDP' in str(ict['ndc_value_inclLU']).upper()):
                ref_act = ict['gdp_taryr']
            else:
                ref_act = np.nan
                print("Warning in main_ndc_quantifications.ipynb: for " + iso_act +
                      " AEI, it is not clear which reference to use. " +
                      "The target is " + ict['ndc_value'] + ". Nothing has been calculated.")
            
            if not np.isnan(ref_act):
                
                # No prioritisation of exclLU or inclLU.
                if ((meta.prioritisation_lulucf in ['exclLU_and_inclLU', 'exclLU_for_relative_no_prio_for_absolute']) 
                    or (np.isnan(ndc_value_exclLU) or np.isnan(ndc_value_inclLU))):
                    
                    # exclLU
                    if not np.isnan(ndc_value_exclLU):
                        ict['tar_emi_exclLU'] = ndc_value_exclLU * 1e-6 * ref_act
                    
                    # inclLU
                    if not np.isnan(ndc_value_inclLU):
                        ict['tar_emi_inclLU'] = ndc_value_inclLU * 1e-6 * ref_act
            
                    # Calculate the targets from the 'other case' (incl/exclLU) if needed.
                    # exclLU
                    if np.isnan(ict['tar_emi_exclLU']):
                        ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
                    
                    # inclLU
                    if np.isnan(ict['tar_emi_inclLU']):
                        ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
                        
                # Prioritisation of exclLU.
                elif (meta.prioritisation_lulucf == 'exclLU' and not np.isnan(ndc_value_exclLU)):
                    
                    # exclLU
                    ict['tar_emi_exclLU'] = ndc_value_exclLU * 1e-6 * ref_act
                
                    # Calculate inclLU from exclLU.
                    
                    # inclLU
                    ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
                # Prioritisation of inclLU.
                elif (meta.prioritisation_lulucf == 'inclLU' and not np.isnan(ndc_value_inclLU)):
                    
                    # inclLU
                    ict['tar_emi_inclLU'] = ndc_value_inclLU * 1e-6 * ref_act
                    
                    # Calculate exclLU from inclLU.
                    
                    # exclLU
                    ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
            
                else:
                    warn(f"Something went wrong for {iso_act} ({ict['tar_type_used']}).")
        
        #
        if ict['tar_type_used'] in ['RBY', 'RBU', 'REI']:
            
            """
            For REI targets, the GDP or population growth rate is not taken into account
            in the LULUCF part of the target.
            Else, the effects of the LULUCF part can unrealisticly large,
            especially when LULUCF was a sink in the reference year, when the strength of 
            a sink can increase a lot due to the intensity growth.
            """
            
            emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr']
            emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr'])
        
            ndc_level_exclLU = 1. + ndc_value_exclLU / 100.
            ndc_level_inclLU = 1. + ndc_value_inclLU / 100.
                        
            # REI compared to BAU is same as RBU.
            # For REI_RBY, the emissions intensities must be used.
            if ict['tar_type_used'] == 'REI' and refyr != taryr:
                intensity_growth = ict[ict['int_ref'].lower() + '_taryr'] / ict[ict['int_ref'].lower() + '_refyr']
            else:
                intensity_growth = 1.
            
            """
            Get the information on whether LULUCF is included in the target or not.
            Get the emi_cov/notcov for LULUCF (refyr and taryr).
            """
            is_LU_covered = (True if not np.isnan(ndc_level_inclLU) else False)
            is_LU_covered_check = (True if ict['lulucf'].upper() == 'YES' else False)
            if is_LU_covered:
                if not is_LU_covered_check:
                    warn(f"Something went wrong with the LULUCF coverage for {iso_act}!")
            
            # No prioritisation of exclLU or inclLU.
            if ((meta.prioritisation_lulucf == 'exclLU_and_inclLU') 
                or (np.isnan(ndc_value_exclLU) or np.isnan(ndc_value_inclLU))):
                
                # exclLU
                if not np.isnan(ndc_level_exclLU):
                    ict['tar_emi_exclLU'] = relative_target_exclLU(
                        intensity_growth, ndc_level_exclLU, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr)
                else:
                    ict['tar_emi_exclLU'] = relative_target_exclLU(
                        intensity_growth, ndc_level_inclLU, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr)
                
                # inclLU
                if not np.isnan(ndc_value_inclLU):
                    ict['tar_emi_inclLU'] = relative_target_inclLU(
                        intensity_growth, ndc_value_inclLU, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr,
                        ict['emi_bl_LU_refyr'], ict['emi_bl_LU_taryr'], is_LU_covered)
                
                # Calculate inclLU from the 'other case' (exclLU) if needed.
                
                # inclLU
                if np.isnan(ict['tar_emi_inclLU']):
                    ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of exclLU.
            elif (meta.prioritisation_lulucf in ['exclLU', 'exclLU_for_relative_no_prio_for_absolute'] and not np.isnan(ndc_value_exclLU)):
                
                # exclLU
                ict['tar_emi_exclLU'] = relative_target_exclLU(
                    intensity_growth, ndc_level_exclLU, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr)
                
                # inclLU
                ict['tar_emi_inclLU'] = emi_target_inclLU(ict['tar_emi_exclLU'], ict['emi_bl_LU_taryr'])
            
            # Prioritisation of inclLU.
            elif (meta.prioritisation_lulucf == 'inclLU' and not np.isnan(ndc_value_inclLU)):
                
                # inclLU
                ict['tar_emi_inclLU'] = relative_target_inclLU(
                    intensity_growth, ndc_value_inclLU, emi_cov_exclLU_refyr, emi_notcov_exclLU_taryr,
                    ict['emi_bl_LU_refyr'], ict['emi_bl_LU_taryr'], is_LU_covered)
                
                # exclLU
                ict['tar_emi_exclLU'] = emi_target_exclLU(ict['tar_emi_inclLU'], ict['emi_bl_LU_taryr'])
            
            else:
                warn(f"Something went wrong for {iso_act} ({ict['tar_type_used']}).")
        
        #
        """
        How large is the percentage reduction compared to the baseline emissions (excl. LULUCF).
        Compared to base year or target year baseline emissions, depending on the target type.
        Base year: RBY and REI_RBY, else target year.
        """
        
        """
        if ict['tar_type_used'] in ['ABS', 'RBU', 'ABU', 'AEI']:
            year_for_ndc_value_corrected_for_LU_and_pc_cov = 'taryr'
        
        elif ict['tar_type_used'] in ['RBY']:
            year_for_ndc_value_corrected_for_LU_and_pc_cov = 'refyr'
        
        elif ict['tar_type_used'] == 'REI':
            year_for_ndc_value_corrected_for_LU_and_pc_cov = ('taryr' if refyr == taryr else 'refyr')
        
        ict['ndc_value_corrected_for_LU_and_pc_cov'] = \
            - 100. * (1. - ict['tar_emi_exclLU'] / ict['emi_bl_exclLU_' + year_for_ndc_value_corrected_for_LU_and_pc_cov])
        """
        #
        
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
                    Calculate the target year emissions depending on the target type.
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
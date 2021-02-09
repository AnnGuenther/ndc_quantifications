# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
def prep_coverage(meta, infos_from_ndcs, info_per_country):
    
    # TODO: update the text where there are questionmarks.
    
    """
    Calculate the **part of historical emissions that is covered by an NDC.**
    
    If the country does *not have an (I)NDC: nothing is covered.*
    
    Else:
    
    - Assessment based on *PRIMAP-hist HISTCR emissions time series.*
    - Categories and gases assessed (per country):
      
      - *Main categories* (IPC1, IPC2, IPCMAG, IPC4 and IPC5; namely Energy, IPPU, Agriculture, Waste and Other; excludes LULUCF).
      - *Kyoto GHGs*: CO2, CH4, N2O, HFCS, PFCS, SF6, NF3.
    
    - For each of these categories / gases, the information on whether they are covered by the country's NDC is provided (csv-input, assessed by A. Günther).
    - If *no information is available for all gases: CO2, CH4, and N2O are assumed to be covered* (in the csv-file already).
    - If *any of HFCS, PFCS, SF6 or NF3 is covered, put IPPU to covered* (F-gases only relevant in IPC2).
    - If *all sectors (IPC1, 2, MAG, 4) are covered, the category "Other" (IPC5) is set to "YES"* (in the csv-file already).
    - For *all category + gas combinations, the emissions are counted as covered, if neither the category nor the gas are assumed not to be covered* (neither category nor gas can contain a "NO").
    
    Here, matrices on the coverage (Yes: covered, No: not-covered) are created.
    
    We do not include the information on the EU, but put the information into each of the member-states.
    """
    
    # %%
    def current_coverage(meta, iso3, coverage, info_per_country):
        
        # Use EU info for the single EU countries.
        iso3_ndc = (iso3 if iso3 not in meta.EU_isos else meta.EU)
        
        # Update the 'info_cov' regarding the rules mentioned above.
        info_cov = coverage.used_per_gas_per_sec.loc[iso3_ndc, :]
        
        # If no information is given for the covered gases: put CO2 to covered.
        if (('YES' not in list(info_cov[meta.gases.kyotoghg])) and \
            ('NO' not in list(info_cov[meta.gases.kyotoghg]))):
            info_cov['CO2'] = 'YES'
            info_per_country.loc[iso3, 'coverage'] += \
                "CO2 set to covered (as no information on covered gases is available). "
        
        # If no information is given for the covered sectors: put ENERGY to covered.
        if (('YES' not in list(info_cov[meta.sectors.main.inclLU])) and \
            ('NO' not in list(info_cov[meta.sectors.main.inclLU]))):
            info_cov['ENERGY'] = 'YES'
            info_per_country.loc[iso3, 'coverage'] += \
                "ENERGY set to covered (as no information on covered sectors is available). "
        
        # If any of HFCS, PFCS, SF6 or NF3 is covered, put IPPU to covered (FGASES only in IPC2).
        if 'YES' in list(info_cov[meta.gases.fgases]):
            info_cov['IPPU'] = 'YES'
            info_per_country.loc[iso3, 'coverage'] += \
                "IPPU set to covered (as some F-gas is covered). "
        
        # If all sectors (excluding LULUCF) are covered, set OTHER to covered.
        if all(info_cov[meta.sectors.main.exclLU] == 'YES'):
            info_cov['OTHER'] = 'YES'
            info_per_country.loc[iso3, 'coverage'] += \
                "OTHER set to covered (as all remaining main sectors - excluding LULUCF - are covered). "
        
        # Now set all values with 'NAN' to 'NO'.
        info_cov[info_cov == 'NAN'] = 'NO'
        
        # The coverage.used_per_gas_per_sec is the updated info_cov.
        coverage.used_per_gas_per_sec.loc[iso3, info_cov.index] = info_cov
        
        return coverage, info_cov, info_per_country
    
    # %%
    from copy import deepcopy
    import pandas as pd
    from pathlib import Path
    import helpers_functions as hpf
    
    # %%    
    # Combis of gases + main-categories (for F-gases only IPPU / IPC2 is relevant).
    meta.combis_gas_cat = \
        ['CO2_' + xx for xx in meta.categories.main.inclLU] + \
        ['CH4_' + xx for xx in meta.categories.main.inclLU] + \
        ['N2O_' + xx for xx in meta.categories.main.inclLU] + \
        [xx + '_IPC2'
        for xx in meta.gases.fgases]
    
    # Setup a class for the 'coverage'.
    coverage = hpf.create_class(name='coverage')
    
    # Coverage per gas and per sector from the NDCs.
    coverage.orig_per_gas_per_sec = infos_from_ndcs.reindex(
        columns=[f"{xx}_NDCS" for xx in meta.gases.kyotoghg + meta.sectors.main.inclLU]). \
        astype(str).apply(lambda x: x.str.upper())
    coverage.orig_per_gas_per_sec.columns = [xx.replace('_NDCS', '') for xx in coverage.orig_per_gas_per_sec.columns]
    
    coverage.calc_per_gas_per_sec = infos_from_ndcs.reindex(
        columns=[f"{xx}_CALC" for xx in meta.gases.kyotoghg + meta.sectors.main.inclLU]). \
        astype(str).apply(lambda x: x.str.upper())
    coverage.calc_per_gas_per_sec.columns = [xx.replace('_CALC', '') for xx in coverage.calc_per_gas_per_sec.columns]
    # Coverage per gas and per sector, from the NDCs, but modified following the above mentioned rules.
    coverage.used_per_gas_per_sec = deepcopy(coverage.calc_per_gas_per_sec)
    
    # Combinations of gas + sector 'from the NDCs'.
    coverage.orig_per_combi = pd.DataFrame(index=meta.isos.EARTH, columns=meta.combis_gas_cat)
    coverage.orig_per_combi.index.name = 'ISO3'
    #
    coverage.calc_per_combi = pd.DataFrame(index=meta.isos.EARTH, columns=meta.combis_gas_cat)
    coverage.calc_per_combi.index.name = 'ISO3'
    # Combinations of gas + sector, as a result of the above mentioned rules.
    coverage.used_per_combi = pd.DataFrame(index=meta.isos.EARTH, columns=meta.combis_gas_cat)
    coverage.used_per_combi.index.name = 'ISO3'
    
    # Countries with or without NDC (set all to NO and replace those with (I)NDC by YES).
    info_per_country.loc[:, 'NDC'] = 'NO'
    info_per_country.loc[infos_from_ndcs.reindex(index=info_per_country.index).index[
        infos_from_ndcs.reindex(index=info_per_country.index).NDC_INDC.isin(
            ['NDC', 'INDC', 'See EU', 'See EU27'])], 'NDC'] = 'YES'
    
    info_per_country.loc[:, 'coverage'] = ''
    
    for iso3 in meta.isos.EARTH:
        
        # No (I)NDC:
        if iso3 in list(info_per_country.index[info_per_country.NDC == 'NO']):
            coverage.orig_per_combi.loc[iso3, :] = 'NO'
            coverage.used_per_combi.loc[iso3, :] = 'NO'
            coverage.calc_per_combi.loc[iso3, :] = 'NO'
            coverage.used_per_gas_per_sec.loc[iso3, :] = 'NO'
        
        # (I)NDC:
        else:
            
            coverage, info_cov, info_per_country = current_coverage(meta, iso3, coverage, info_per_country)
            
            # For all the combis between gas and category define whether they are covered or not (YES / NO):
            for check_combi in meta.combis_gas_cat:
                
                check_gas, check_cat = check_combi.split('_')
                
                # combis_orig.
                cov_orig_case = [coverage.orig_per_gas_per_sec.loc[iso3, check_gas], 
                            coverage.orig_per_gas_per_sec.loc[iso3, meta.categories.main.cat_to_sec[check_cat]]]
                if cov_orig_case == ['YES', 'YES']:
                    coverage.orig_per_combi.loc[iso3, check_combi] = 'YES'
                elif cov_orig_case == ['NO', 'NO']:
                    coverage.orig_per_combi.loc[iso3, check_combi] = 'NO'
                elif cov_orig_case == ['NAN', 'NAN']:
                    coverage.orig_per_combi.loc[iso3, check_combi] = 'NAN'
                else:
                    coverage.orig_per_combi.loc[iso3, check_combi] = '/'.join(cov_orig_case)
                
                # combis_calc.
                cov_calc_case = [coverage.calc_per_gas_per_sec.loc[iso3, check_gas], 
                            coverage.calc_per_gas_per_sec.loc[iso3, meta.categories.main.cat_to_sec[check_cat]]]
                if cov_calc_case == ['YES', 'YES']:
                    coverage.calc_per_combi.loc[iso3, check_combi] = 'YES'
                elif cov_calc_case == ['NO', 'NO']:
                    coverage.calc_per_combi.loc[iso3, check_combi] = 'NO'
                elif cov_calc_case == ['NAN', 'NAN']:
                    coverage.calc_per_combi.loc[iso3, check_combi] = 'NAN'
                else:
                    coverage.calc_per_combi.loc[iso3, check_combi] = '/'.join(cov_calc_case)
                
                # combis_used.
                if 'NO' in list(info_cov[[check_gas, meta.categories.main.cat_to_sec[check_cat]]]):
                    coverage.used_per_combi.loc[iso3, check_combi] = 'NO'
                else:
                    coverage.used_per_combi.loc[iso3, check_combi] = 'YES'
    
    # Delete EU info only now.
    coverage.orig_per_gas_per_sec.drop(index=[meta.EU], inplace=True)
    coverage.calc_per_gas_per_sec.drop(index=[meta.EU], inplace=True)
    coverage.used_per_gas_per_sec.drop(index=[meta.EU], inplace=True)
    
    # Write out data.
    # Replace the sectors by categories.
    cov_orig_cols = deepcopy(coverage.orig_per_gas_per_sec)
    cov_orig_cols.columns = [meta.sectors.main.sec_to_cat[xx] 
        if xx in meta.sectors.main.sec_to_cat.keys() else xx for xx in cov_orig_cols.columns]
    pd.concat([cov_orig_cols, coverage.orig_per_combi], axis=1). \
        to_csv(Path(meta.path.preprocess, 'coverage_orig_per_gas_and_per_sector_and_combi.csv'))
    
    cov_calc_cols = deepcopy(coverage.calc_per_gas_per_sec)
    cov_calc_cols.columns = [meta.sectors.main.sec_to_cat[xx] 
        if xx in meta.sectors.main.sec_to_cat.keys() else xx for xx in cov_calc_cols.columns]
    pd.concat([cov_calc_cols, coverage.calc_per_combi], axis=1). \
        to_csv(Path(meta.path.preprocess, 'coverage_calc_per_gas_and_per_sector_and_combi.csv'))
    
    cov_used_cols = deepcopy(coverage.used_per_gas_per_sec)
    cov_used_cols.columns = [meta.sectors.main.sec_to_cat[xx] 
        if xx in meta.sectors.main.sec_to_cat.keys() else xx for xx in cov_used_cols.columns]
    pd.concat([cov_used_cols, coverage.used_per_combi], axis=1). \
        to_csv(Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'))
    
    return coverage, info_per_country

# %%
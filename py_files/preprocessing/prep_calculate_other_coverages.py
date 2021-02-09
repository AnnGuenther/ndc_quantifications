# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
def prep_calculate_other_coverages(database, infos_from_ndcs, meta, primap, info_per_country):
    
    # %%
    def chose_covered_gases_and_sectors_if_wanted(meta, coverage, list_of_covered_gases_and_sectors):
        
        """
        E.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
        """
            
        # %%
        # e.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
        # Set all to 'NO', and then Energy & CO2 to 'YES'.
        coverage.used_per_gas_per_sec.loc[:, :] = 'NO'
        coverage.used_per_gas_per_sec.loc[:, list_of_covered_gases_and_sectors] = 'YES'
        
        # %%
        for iso3 in meta.isos.EARTH:
            
            info_cov = coverage.used_per_gas_per_sec.loc[iso3, :]
            
            # For all the combis between gas and category define whether they are covered or not (YES / NO):
            for check_combi in meta.combis_gas_cat:
                
                check_gas, check_cat = check_combi.split('_')
                
                # combis_used.
                if 'NO' in list(info_cov[[check_gas, meta.categories.main.cat_to_sec[check_cat]]]):
                    coverage.used_per_combi.loc[iso3, check_combi] = 'NO'
                else:
                    coverage.used_per_combi.loc[iso3, check_combi] = 'YES'
                
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
        
        # Write out data.
        # Replace the sectors by categories.
        cov_used_cols = deepcopy(coverage.used_per_gas_per_sec)
        cov_used_cols.columns = [meta.sectors.main.sec_to_cat[xx] 
            if xx in meta.sectors.main.sec_to_cat.keys() else xx for xx in cov_used_cols.columns]
        
        return coverage
    
    # %%
    def calculate_the_rest(database, meta, primap, coverage, info_per_country, current_case):
        
        # %% Covered part of historical emissions (KYOTOGHG_IPCM0EL).
        
        """
        The covered part of emissions (in 'emissions') is calculated here for historical years, 
        for which data per sector and gas combination are available.
        The assessment is based on the information in coverage.used_per_combi (all entries are 'YES' or 'NO').
        All combinations with 'YES' are summed up to emicov_his, and all combinations with 'NO' are summed up to eminotcov_his.
        
        For KYOTOGHG_IPCM0EL, excluding LULUCF.
        """
        
        print("    Historical (IPCM0EL)")
        
        database, coverage = prep.prep_covered_emissions_his(database, coverage, meta, primap)
        
        """
        Additionally calculate the historical emissions not-/covered for perGas_IPCM0EL and KYOTOGHG_perCategory.
        These values are not needed in further calculations, but nice to have.
        """
        
        database = prep.prep_covered_emissions_his_additional_data(meta, database, primap)
        
        # %% Covered part of future emissions (KYOTOGHG_IPCM0EL).
        
        # TODO: check the last option if it is still an issue.
        
        """
        Calculate the part of future emissions covered by an NDC (KYOTOGHG_IPCM0EL)
        
        - For countries that cover everything: set pccov_fut to 1 (100%).
        - For countries that cover nothing: set pccov_fut to 0 (0%).
        - For countries that cover all sectors (excl. LULUCF), but not all gases: 
            the SSP entity_IPCM0EL emissions per gas are used to calculate pc\_cov\_fut.
          - SSP data are available for KYOTOGHG, CO$_2$, CH$_4$, N$_2$O and FGASES:
            - For countries that cover only some FGASES, the \% share between HFCS, PFCS, 
                SF$_6$ and NF$_3$ is kept constant (at mean over last 6 available values).
            - The share per gas is applied to the future KYOTOGHG\_IPCM0EL emissions data.
        - For countries that do not cover all sectors:
          - Calculate the slope of pc\_cov\_his (2010 to most recent year with available data ("mry")).
            - If abs(slope) < lim_slope: use the mean over 2010 to mry.
            - If abs(slope) > lim_slope: calculate pc\_cov\_fut from the correlation between emi\_tot\_his and emi\_cov\_his. For 2010 to mry.
                - If any(pc\_cov\_fut) > 90\%, but not all(pc\_cov\_fut) > 90\% --> set the pc\_cov\_fut > 90\% to 90\%.
                - If any(pc\_cov\_fut) < 10\%, but not all(pc\_cov\_fut) < 10\% --> set the pc\_cov\_fut < 10\% to 10\%.
                - Set min(pc\_cov\_fut) to 0\% and max(pc\_cov\_fut) to 100\%.
        - If no future emissions data are available: use the mean over 2010 to mry?!
        
        The future emicov / pccov values depend on the chosen SSP scenario.
        
        One can give a preference for the calculation method of pccov_fut.
        preference_pccov_fut can be 'mean' or 'corr'.
        
        'mean':
            Check for the countries for which the slope of a regression to the last available 
            years of pccov_his is less than slope_lim.
            Use the mean over the years as pccov_fut.
            For the others check the correlation between emitot and emicov and decide 
            whether to better use this correlation for pccov_fut.
        'corr':
            Take the correlation between emitot and emicov, unless it is too 'bad', then take the mean.
        """
        
        print("    Future (IPCM0EL)")
        
        #preference_pccov_fut = 'mean'
        preference_pccov_fut = 'corr'
        
        first_year_for_slope = 2010
        slope_lim = 1./100. 
        rvalue_lim = .85
        
        database, info_per_country, coverage = \
            prep.prep_covered_emissions_fut(database, meta, coverage, info_per_country, preference_pccov_fut, primap,
            first_year_for_slope, slope_lim, rvalue_lim)
        
        # %%
        # Write out the tables for COV / NOTCOV.
        Path(meta.path.output_act, current_case).mkdir(parents=True, exist_ok=True)
        
        for tablename in hpf.get_all_attributes_of_class(database):
            if 'COV' in tablename:
            
                hpf.write_table_from_class_metadata_country_year_matrix(
                    getattr(database, tablename), Path(meta.path.output_act, current_case))
    
    # %%
    from copy import deepcopy
    from pathlib import Path
    import pandas as pd
    
    import helpers_functions as hpf
    import preprocessing as prep
    
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
    coverage.orig_per_gas_per_sec = infos_from_ndcs.reindex(columns=meta.gases.kyotoghg + meta.sectors.main.inclLU). \
        astype(str).apply(lambda x: x.str.upper())
    # Coverage per gas and per sector, from the NDCs, but modified following the above mentioned rules.
    coverage.used_per_gas_per_sec = deepcopy(coverage.orig_per_gas_per_sec)
    
    # Combinations of gas + sector 'from the NDCs'.
    coverage.orig_per_combi = pd.DataFrame(index=meta.isos.EARTH, columns=meta.combis_gas_cat)
    coverage.orig_per_combi.index.name = 'ISO3'
    # Combinations of gas + sector, as a result of the above mentioned rules.
    coverage.used_per_combi = pd.DataFrame(index=meta.isos.EARTH, columns=meta.combis_gas_cat)
    coverage.used_per_combi.index.name = 'ISO3'
    
    info_per_country = deepcopy(info_per_country)
    
    # Path to output-folder.
    meta.path.output_act = Path(meta.path.preprocess, 'other_coverages')
    Path(meta.path.output_act).mkdir(parents=True, exist_ok=True)
    
    infos_from_ndcs = hpf.get_infos_from_ndcs(meta)
    
    # Simply add needed columns on the go (info_per_country.loc[:, 'newcolumn'] = whatever).
    
    # %% Covered part of emissions - matrix on covered gases / sectors.
    
    # TODO: update the text where there are questionmarks.
    
    """
    Calculate the part of historical emissions that is covered by an NDC.
    
    - If the country does not have an (I)NDC: nothing is covered.
    Else:
    - Assessment based on PRIMAP-hist HISTCR emissions time series.
    - Categories and gases assessed (per country):
      - Main categories (IPC1, IPC2, IPCMAG, IPC4 and IPC5; namely Energy, IPPU, Agriculture, Waste and Other; excludes LULUCF).
      - Kyoto GHGs: CO$_2$, CH$_4$, N$_2$O, HFCS, PFCS, SF$_6$, NF$_3$.
    - For each of these categories / gases, the information on whether they are covered by the country's NDC is provided (csv-input, assessed by A. Günther).
    - If no information is available for all gases: only CO$_2$ assumed to be covered (in the csv-file already?!).
    - If no information is available for all sectors: only energy assumed to be covered. Case never happened.
    - If any of HFCS, PFCS, SF6 or NF3 is covered, put IPPU to covered (F-gases only relevant in IPC2).
    - If all sectors (IPC1, 2, MAG, 4) are covered ('YES'), the category "Other" (IPC5) is set to "YES" (in the csv-file already?!).
    - For all category + gas combinations, the emissions are counted as covered, if neither the category nor the gas are assumed not to be covered (neither category nor gas can contain a "NO").
    
    Here, matrices on the coverage (Yes: covered, No: not-covered) are created.
    
    We do not include the information on the EU, but put the information into each of the member-states.
    """
    
    print("Covered part of emissions.")
    
    # Combis of gases + main-categories (for F-gases only IPPU / IPC2 is relevant).
    meta.combis_gas_cat = \
        ['CO2_' + xx for xx in meta.categories.main.inclLU] + \
        ['CH4_' + xx for xx in meta.categories.main.inclLU] + \
        ['N2O_' + xx for xx in meta.categories.main.inclLU] + \
        [xx + '_IPC2'
        for xx in meta.gases.fgases]
    
    """
    Use 'NO' in all cases where coverage is 'NAN'.
    """
    infos_from_ndcs_new = deepcopy(infos_from_ndcs)
    for sec_gas in meta.sectors.main.inclLU + meta.gases.kyotoghg:
        infos_from_ndcs_new.loc[:, sec_gas] = ['No' if (type(xx) == str and xx.upper() == 'NAN') else xx 
            for xx in infos_from_ndcs_new.loc[:, f"{sec_gas}_CALC"].to_list()]
    
    coverage, info_per_country = prep.prep_coverage(meta, infos_from_ndcs_new, info_per_country)
    calculate_the_rest(database, meta, primap, coverage, info_per_country, 'all_nan_to_no')
    
    # %% Chose different coverage if wanted.
    """
    You can chose to setup your own coverage.used_per_gas_per_sec.
    If you do so, write out a file to say what you have chosen!!!
    
    E.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
    """
    
    to_calculate = {
        'CO2_ENERGY_covered': 
            ['CO2', 'ENERGY'],
        'CO2_CH4_N2O_ENERGY_covered': 
            ['CO2', 'CH4', 'N2O', 'ENERGY'],
        'CO2_CH4_N2O_ENERGY_AGRICULTURE_covered': 
            ['CO2', 'CH4', 'N2O', 'ENERGY', 'AGRICULTURE'],
        'CO2_CH4_N2O_ENERGY_AGRICULTURE_IPPU_covered': 
            ['CO2', 'CH4', 'N2O', 'ENERGY', 'AGRICULTURE', 'IPPU'],
        'CO2_CH4_N2O_HFCS_PFCS_SF6_NF3_ENERGY_AGRICULTURE_IPPU_covered': 
            ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3', 'ENERGY', 'AGRICULTURE', 'IPPU']}
    
    for calc in to_calculate.keys():
        
        print(calc)
        coverage = chose_covered_gases_and_sectors_if_wanted(meta, coverage, to_calculate[calc])
        calculate_the_rest(database, meta, primap, coverage, info_per_country, calc)
    
# %%
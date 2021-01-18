# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
def prep_covered_emissions_fut(database, meta, coverage, info_per_country, preference_pccov_fut, primap, 
    first_year_for_slope, slope_lim, rvalue_lim):
    
    # TODO: check the last option if it is still an issue.
    
    """
    Calculate the *part of future emissions covered by an NDC (KYOTOGHG_IPCM0EL)*
    
    - For countries that *cover everything: set pccov_fut to 1 (100%).*
    - For countries that *cover nothing: set pccov_fut to 0 (0%).*
    - For countries that *cover all sectors (excl. LULUCF), but not all gases:* 
        the *SSP entity_IPCM0EL emissions per gas are used to calculate pc\_cov\_fut.*
      
        - SSP data are available for KYOTOGHG, CO2, CH4, N2O and FGASES:
    
            - For countries that cover only some FGASES, the \% share between HFCS, PFCS, SF6 and NF3 is kept constant (at mean over last 6 available PRIMAP-hist values).
            - The share per gas is applied to the future KYOTOGHG\_IPCM0EL emissions data.
    
    - For countries that do *not cover all sectors:*
        
        - Calculate the *slope of pc\_cov\_his (2010 to most recent year with available data ("mry")).*
            
            - If *abs(slope) < lim_slope: use the mean over 2010 to mry*.
            - If *abs(slope) > lim_slope: calculate pc\_cov\_fut from the correlation between emi\_tot\_his and emi\_cov\_his. For 2010 to mry.*
                
                - If any(pc\_cov\_fut) > 90\%, but not all(pc\_cov\_fut) > 90\% --> set the pc\_cov\_fut > 90\% to 90\%.
                - If any(pc\_cov\_fut) < 10\%, but not all(pc\_cov\_fut) < 10\% --> set the pc\_cov\_fut < 10\% to 10\%.
                - If any(pc\_cov\_fut) > 100\% or < 0\% use the mean instead.
    
    - If no future emissions data are available: use the mean over 2010 to mry.
    
    The future emicov / pccov values depend on the chosen SSP scenario.
    
    One can give a *preference for the calculation method of pccov_fut.
    preference_pccov_fut can be 'mean' or 'corr'.*
    
    'mean':
        Check for the countries for which the slope of a regression to the last available years of pccov_his is less than slope_lim.
        Use the mean over the years as pccov_fut.
        For the others check the correlation between emitot and emicov and decide whether to better use this correlation for pccov_fut.
    'corr':
        Take the correlation between emitot and emicov, unless it is too 'bad', then take the mean.
    
    Default: 'corr'.
    """
    
    # %%
    def all_sectors_covered(database, meta, ssp_pccov, info_per_country, info_for_iso, iso3, ssp, cov_gases, ssp_kyoto_ipcm0el):
        """
        If all sectors are covered, one can calculate the pccov_fut from the given share per gas 
        and the gases that are covered.
        """
        
        info_for_iso = info_for_iso + 'test'
        #info_for_iso += "All the sectors are covered. The information on gas-shares from SSPs " + \
        #    "(and PRIMAP-hist) are used to calculate pccov_fut.\n"
        #info_for_iso += "All the sectors are covered. The information on gas-shares from SSPs " + \
        #    "(and PRIMAP-hist) are used to calculate pccov_fut.\n"
        info_per_country.loc[iso3, 'pccov_fut_method_' + ssp[:4]] = 'GasShare'
        
        # Add up all the shares for the covered gases (based on gas_IPCM0EL data).
        covered_gases = [xx for xx in cov_gases.index if cov_gases[xx] == 'YES']
        shares_covered_gases = pd.DataFrame(0, index=covered_gases, columns=ssp_kyoto_ipcm0el.index)
        for gas in shares_covered_gases.index:
            
            shares_covered_gases.loc[gas, :] = pd.Series(hpf.ratios_w_zeros(
                deepcopy(getattr(database, f"{gas}_IPCM0EL_TOTAL_NET_{ssp}FILLED_" + 
                ('PMSSPBIE' if gas in meta.gases.main else 'SSPSPLIT')). \
                data.loc[iso3, ssp_kyoto_ipcm0el.index]), ssp_kyoto_ipcm0el, 
                dtype='pd.DataFrame').transpose().values[0], 
                name=gas, index=ssp_kyoto_ipcm0el.index)
        
        ssp_pccov.loc[iso3, shares_covered_gases.columns] = hpf.nansum(shares_covered_gases, axis=0)
        
        return ssp_pccov, info_per_country, info_for_iso
    
    # %%
    def not_all_sectors_covered(coverage, pccov_his, preference_pccov_fut, info_for_iso, 
        iso3, ssp_kyoto_ipcm0el, ssp_pccov, ssp, info_per_country, available_years, 
        first_year_for_slope, slope_lim, rvalue_lim):
        """
        If not all sectors are covered check for the slope of the regression line to pccov_his, 
        and if pccov_his does not change too much use the mean (if preference_pccov_fut = 'mean'), 
        else use the correlation between emitot and emicov.
        """
        
        slope_lim_str = '{:.2f}'.format(slope_lim)
        
        use_mean = False # Save if the mean should be used or another method.
        
        emicov_his = coverage.emicov_his.loc[iso3, :]
        eminotcov_his = coverage.eminotcov_his.loc[iso3, :]
        
        if len(available_years) > 0:
            
            years_for_slope = [xx for xx in range(first_year_for_slope, available_years[-1]+1)]
            years_for_slope_str = str(min(years_for_slope)) + " to " + str(max(years_for_slope))
            
            pc_cov_his_mean = pccov_his[years_for_slope].mean()
            
            if (pc_cov_his_mean > .9 or pc_cov_his_mean < .1):
                use_mean = True
            
            if preference_pccov_fut == 'mean':
                
                # Calculate the slope of the historical pccov
                # (first_year_for_slope to most recent year with available data (most_recent_year)).
                data_for_linreg = pccov_his[years_for_slope]
                xx, yy, linreg = hpf.linear_regression(
                        list(data_for_linreg.index), 
                        list(data_for_linreg.values))
                linreg_slope_str = '{:.2f}'.format(linreg.slope)
                
                info_for_iso += "Not all the sectors are covered. The slope of the regression line to pccov_his (" + \
                    years_for_slope_str + ") was calculated.\n"
                
                # If abs(linreg.slope) < slope_lim: use the mean over first_year_for_slope to most_recent_year
                # as future pccov. Else: check the correlation between emitot_his and emicov_his.
                if abs(linreg.slope) < slope_lim:
                    
                    use_mean = True
                    
                    info_for_iso += "The slope (" + linreg_slope_str + ") is less than " + \
                        slope_lim_str + ", therefore the mean over " + years_for_slope_str + \
                        " is used as pccov_fut.\n"
            
            if (preference_pccov_fut == 'corr') or (not use_mean):
                
                # Calculate pccov_fut from the correlation between emitot_his and emicov_his.
                # For first_year_for_slope to most_recent_year.
                # If the mean of pccov over years_for_slope is > 50% use pccov, else pcnotcov.
                if pccov_his[years_for_slope].mean() > .5:
                    corr_ref = emicov_his
                    corr_ref_name = 'emicov'
                else:
                    corr_ref = eminotcov_his
                    corr_ref_name = 'eminotcov'
                
                info_for_iso += "The correlation between emitot_his and " + corr_ref_name + \
                    "_his (for " + years_for_slope_str + " is calculated.\n"
                
                xx, yy, linreg = hpf.linear_regression(
                    list(ssp_kyoto_ipcm0el[years_for_slope]), 
                    list(corr_ref[years_for_slope]))
                linreg_rvalue_str = '{:.2f}'.format(linreg.rvalue)
                
                # Only use the correlation if rvalue > .85.
                rvalue_lim_str = '{:.2f}'.format(rvalue_lim)
                
                if linreg.rvalue > rvalue_lim:
                    info_for_iso += "As the rvalue of the correlation (" + linreg_rvalue_str + \
                        ") is larger than " + rvalue_lim_str + \
                        ", the emicov for future years are calculated from the correlation.\n"
                    
                    # Get the emicov or eminotcov values corresponding to the future values of emitot.
                    yrs_fut = range(max(available_years)+1, 2051)
                    # emi_fut are either the covered (corr_ref_name == 'emicov') 
                    # or not-covered (corr_ref_name == 'eminotcov') emissions.
                    emi_fut = pd.Series([ssp_kyoto_ipcm0el[xx] * linreg.slope + linreg.intercept 
                         for xx in yrs_fut], index=yrs_fut, name=iso3)
                    
                    # Only use the correlation if resulting emi_fut never > emitot and never < 0.
                    if any(emi_fut.loc[yrs_fut] > ssp_kyoto_ipcm0el.loc[yrs_fut]) or \
                        any(emi_fut.loc[yrs_fut] < 0.):
                        
                        use_mean = True
                        
                        info_for_iso += "The resulting covered emissions exceed the total emissions or are negative, " + \
                            "therefore the mean over " + years_for_slope_str + " is used insted of the correlation.\n"
                    
                    else:
                        use_mean = False
                        
                        emicov_fut = (emi_fut if corr_ref_name == 'emicov'
                            else ssp_kyoto_ipcm0el.loc[emi_fut.index].add(-emi_fut, fill_value=0))
                        
                        # corr_ref_name == 'eminotcov', subtract the emi_fut from emitot.
                        pccov_fut = hpf.ratios_w_zeros(emicov_fut.loc[yrs_fut], 
                            ssp_kyoto_ipcm0el.loc[yrs_fut], dtype='pd.Series')
                        pccov_fut = pd.Series(hpf.ratios_w_zeros(emicov_fut.loc[yrs_fut], 
                            ssp_kyoto_ipcm0el.loc[yrs_fut], dtype='pd.Series'))
                        
                        # If any pccov_fut > 1 (100%) -> set it to 1.
                        pccov_fut[pccov_fut.gt(1.)] = 1.
                        isos_gt1 = ', '.join(str(xx) for xx in pccov_fut.index[pccov_fut.gt(1.)])
                        info_for_iso += ('' if len(isos_gt1) == 0
                            else "As there were pccov_fut greater than 100%, those were set to 100% (" + isos_gt1 + ").\n")
                        
                        # If any pccov_fut < 0 -> set it to 0.
                        pccov_fut[pccov_fut.lt(0.)] = 0.
                        isos_lt0 = ', '.join(str(xx) for xx in pccov_fut.index[pccov_fut.lt(0.)])
                        info_for_iso += ('' if len(isos_lt0) == 0
                            else "As there were pccov_fut less than 0%, those were set to 0% (" + isos_lt0 + ").\n")
                        
                        # If pccov_fut has values > .9 (90%), but pccov_his(years_for_slope) does not -> set pccov_fut>.9 to .9.
                        lim_pc = .9
                        if not pccov_his[years_for_slope].gt(lim_pc).any():
                            pccov_fut[pccov_fut.gt(lim_pc)] = lim_pc
                        
                        isos_gt09 = ', '.join(str(xx) for xx in pccov_fut.index[pccov_fut.gt(lim_pc)])
                        info_for_iso += ('' if len(isos_gt09) == 0
                            else "As there were pccov_fut greater than 90%, while in " + years_for_slope_str + \
                            " no values were greater than 90%, they were set to 90% (" + isos_gt09 + ").\n")
                        
                        # If pccov_fut has values < .1, but pccov_his(years_for_slope) does not -> set pccov_fut<.1 to .1.
                        lim_pc = .1
                        if not pccov_his[years_for_slope].lt(lim_pc).any():
                            pccov_fut[pccov_fut.lt(lim_pc)] = lim_pc
                        
                        isos_lt01 = ', '.join(str(xx) for xx in pccov_fut.index[pccov_fut.lt(lim_pc)])
                        info_for_iso += ('' if len(isos_lt01) == 0
                            else "As there were pccov_fut less than 10%, while in " + years_for_slope_str + \
                            " no values were less than 10%, they were set to 10% (" + isos_lt01 + ").\n")
                        
                        ssp_pccov.loc[iso3, pccov_fut.index] = pccov_fut
                
                else:
                    use_mean = True
                    
                    info_for_iso += "As the rvalue of the correlation (" + linreg_rvalue_str + \
                        ") is smaller than " + rvalue_lim_str + \
                        ", the emicov for future years is calculated as mean over " + years_for_slope_str + ".\n"
        
            if use_mean:
                
                method  = 'Mean'
                ssp_pccov.loc[iso3, :] = pccov_his[years_for_slope].mean()
                
            else:
                method = 'Correlation'
            
            info_per_country.loc[iso3, 'pccov_fut_method_' + ssp[:4]] = method
        
        return ssp_pccov, pccov_his, info_per_country, info_for_iso
    
    # %%
    def data_to_database(ssp_pccov, database, meta, ssp, primap):
        """
        Put the data to 'database'.
        pccov, pcnotcov, emicov, and eminotcov.
        """
        
        info_attrs = {
            'PCCOV': {
                'data': ssp_pccov,
                'note': "Share of emissions covered", 
                'clss': 'COV', 'tpe': 'PC', 'unit': meta.units.default['emi'] + '/' + meta.units.default['emi']},
            'PCNOTCOV': {
                'data': 1.-ssp_pccov, 
                'note': "Share of emissions not covered",
                'clss': 'NOTCOV', 'tpe': 'PC', 'unit': meta.units.default['emi'] + '/' + meta.units.default['emi']},
            'EMICOV': {
                'data': ssp_pccov.multiply(deepcopy(getattr(database, 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIE').data)), 
                'note': "Emissions covered",
                'clss': 'COV', 'tpe': 'EMI', 'unit': meta.units.default['emi']},
            'EMINOTCOV': {
                'data': (1.-ssp_pccov).multiply(deepcopy(getattr(database, 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIE').data)), 
                'note': "Emissions not covered",
                'clss': 'NOTCOV', 'tpe': 'EMI', 'unit': meta.units.default['emi']}}
        
        for attr in info_attrs.keys():
            
            attrs = info_attrs[attr]
            table = hpf.create_table(data=attrs['data'], ent='KYOTOGHG', cat='IPCM0EL', clss=attrs['clss'],
                tpe=attrs['tpe'], scen=ssp+'FILLED', gwp=meta.gwps.default, unit=attrs['unit'])
            table.srce = preference_pccov_fut.upper()
            table.note = attrs['note'] + " by an (I)NDC, based on per-country, " + \
                "per-main-sector and per-kyoto-GHG information from countries' (I)NDCs and their corresponding " + \
                meta.primap.emi['scen'] + '_' + meta.primap.emi['srce'] + " emissions " + \
                "(" + str(primap['emi'].columns.min()) + " to " + str(primap['emi'].columns.max()) + "). " + \
                "Future values were calculated using methods stated in info_per_country."
            table.__tablename_to_standard__()
            table.__name_to_standard__()
            
            setattr(database, table.tablename, table)
        
        return database
    
    # %%
    import pandas as pd
    import numpy as np
    from copy import deepcopy
    import sys
    import helpers_functions as hpf
    
    # %%
    if preference_pccov_fut not in ['mean', 'corr']:
        sys.exit("prep_covered_emissions_fut.py: the string given for preference_pccov_fut is not valid.")
    
    # Which countries cover 'all sectors', 'all gases', 'everything', or 'nothing'.
    coverage.isos = hpf.create_class(name='isos')
    
    coverage.isos.all_sectors_covered = coverage.used_per_gas_per_sec.index[
        (coverage.used_per_gas_per_sec.loc[:, meta.sectors.main.exclLU] == 'YES').all(axis=1)].to_list()
    coverage.isos.all_gases_covered = coverage.used_per_gas_per_sec.index[
        (coverage.used_per_gas_per_sec.loc[:, meta.gases.kyotoghg] == 'YES').all(axis=1)].to_list()
    coverage.isos.everything_covered = coverage.used_per_gas_per_sec.index[
        (coverage.used_per_gas_per_sec.loc[:, meta.sectors.main.exclLU + meta.gases.kyotoghg] == 'YES').all(axis=1)].to_list()
    coverage.isos.nothing_covered = coverage.used_per_gas_per_sec.index[
        (coverage.used_per_gas_per_sec.loc[:, meta.sectors.main.exclLU + meta.gases.kyotoghg] == 'NO').all(axis=1)].to_list()
    
    # Also put the information on coverage per iso to 'info_per_country'.
    for attr in hpf.get_all_attributes_of_class(coverage.isos):
        
        # First set all to 'NO'.
        # Then replace those for which the isos are in coverage.isos.attr by 'YES'.
        info_per_country.loc[:, attr] = 'NO'
        info_per_country.loc[getattr(coverage.isos, attr), attr] = 'YES'
    
    # Change in pccov up to +/-1% in first_year_for_slope to most recent year with data is allowed
    # (as pccov is from 0 to 1, not from 0% to 100%, the limit is 1.%/100.%).
    pccov_all = {}
    
    for ssp in meta.ssps.scens.long:
        
        # New column for this SSP.
        info_per_country.loc[:, 'pccov_fut_' + ssp[:4]] = ''
        info_per_country.loc[:, 'pccov_fut_method_' + ssp[:4]] = ''
        
        ssp_pccov = pd.DataFrame(index=meta.isos.EARTH, columns=range(1990, 2051))
        
        # Countries with 'everything covered'.
        ssp_pccov.loc[coverage.isos.everything_covered, :] = 1.
        info_per_country.loc[coverage.isos.everything_covered, 'pccov_fut_' + ssp[:4]]= \
            "All sectors and gases are covered and pccov_fut is set to 1 (100%)."
        info_per_country.loc[coverage.isos.everything_covered, 'pccov_fut_method_' + ssp[:4]]= "SetTo100%"
        
        # Countries with 'nothing covered'.
        ssp_pccov.loc[coverage.isos.nothing_covered, :] = 0.
        info_per_country.loc[coverage.isos.nothing_covered, 'pccov_fut_' + ssp[:4]]= \
            "None of the sectors and gases are covered and pccov_fut is set to 0 (0%)."
        info_per_country.loc[coverage.isos.nothing_covered, 'pccov_fut_method_' + ssp[:4]]= "SetTo0%"
        
        # Countries that do not have 'everything covered' or 'nothing covered'.
        for iso3 in sorted(set(set(meta.isos.EARTH) - 
            set(coverage.isos.everything_covered + coverage.isos.nothing_covered))):
            
            info_for_iso = ""
            
            cov_gases = coverage.used_per_gas_per_sec.loc[iso3, meta.gases.kyotoghg]
            
            ssp_kyoto_ipcm0el = deepcopy(getattr(database, 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + 
                ssp + 'FILLED_PMSSPBIE').data.loc[iso3, :])
            
            pccov_his = coverage.pccov_his.loc[iso3, :]
            pccov_notnan = ~pccov_his.isnull()
            available_years = np.array(sorted(pccov_his.index[pccov_notnan]))

            if iso3 in coverage.isos.all_sectors_covered:
                
                """
                If all sectors are covered, one can calculate the pccov_fut from the given share per gas 
                and the gases that are covered.
                """
                ssp_pccov, info_per_country, info_for_iso = \
                    all_sectors_covered(database, meta, ssp_pccov, info_per_country, 
                        info_for_iso, iso3, ssp, cov_gases, ssp_kyoto_ipcm0el)
            
            else:
                
                """
                If not all sectors are covered check for the slope of the regression line to pccov_his, 
                and if pccov_his does not change too much use the mean (if preference_pccov_fut = 'mean'), 
                else use the correlation between emitot and emicov.
                """
                
                ssp_pccov, pccov_his, info_per_country, info_for_iso = \
                    not_all_sectors_covered(coverage, pccov_his, preference_pccov_fut, 
                        info_for_iso, iso3, ssp_kyoto_ipcm0el, ssp_pccov, ssp, info_per_country, available_years,
                        first_year_for_slope, slope_lim, rvalue_lim)
            
            # Replace the historical years by the original pccov.
            ssp_pccov.loc[iso3, available_years] = pccov_his[available_years]
            
            # Replace values > 1 and < 0.
            ssp_pccov[ssp_pccov.gt(1.)] = 1.
            ssp_pccov[ssp_pccov.lt(0.)] = 0.
            
            info_per_country.loc[iso3, 'pccov_fut_' + ssp[:4]]= info_for_iso
        
        pccov_all[ssp] = ssp_pccov
        
        """
        Put the data to 'database'.
        pccov, pcnotcov, emicov, and eminotcov.
        """
        database = data_to_database(ssp_pccov, database, meta, ssp, primap)
    
    return database, info_per_country, coverage

# %%
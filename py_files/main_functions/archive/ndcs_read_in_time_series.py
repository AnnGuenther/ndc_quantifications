# -*- coding: utf-8 -*-
"""
@author: annikag
"""

# %%
import pandas as pd
import copy
import numpy as np

def ndcs_read_in_time_series(time_series, time_series_path, time_series_lu_path, yrs_all_str, isos):
    # %%
    # Read in time series (1990 - 2050) of emi, pc_cov, pop, gdp.
    for val in time_series_path.keys():
        ts_act = pd.read_csv(time_series_path[val])
        for iso_act in ts_act.iso3:
            ####
            # Fill end of time series, if future values are missing 
            # (fill by mean over 2010 to most recent year).
            ts_to_fill = copy.deepcopy(ts_act.loc[ts_act.iso3 == iso_act,
                                                  yrs_all_str])
            if (ts_to_fill.isnull().any().any() \
                and not ts_to_fill.isnull().any().all()):
                # In our setup that should only happen at the end of historic 
                # time series.
                # Fill with constant value at the end (mean over 2010 to 
                # most recent value).
                ts_available = ts_to_fill.loc[:,
                    [xx for xx in ts_to_fill.columns
                     if ts_to_fill.loc[:, xx].notnull().all()]]
                yrs_not_available = [xx for xx in ts_to_fill.columns
                                     if ts_to_fill.loc[:, xx].isnull().all()]
                yrs_for_mean = ['Y' + str(xx) for xx in
                                range(2010, int(ts_available.columns[-1][1:]) + 1)]
                ts_fill = ts_available.loc[:, yrs_for_mean].mean(axis=1).values
                ts_to_fill.loc[:, yrs_not_available] = ts_fill[0]
                ts_act.loc[ts_act.iso3 == iso_act, yrs_all_str] = ts_to_fill
                if type(ts_act.loc[ts_act.iso3 == iso_act, 'add_info']) == str:
                    ts_act.loc[ts_act.iso3 == iso_act, 'add_info'] = \
                        ts_act.loc[ts_act.iso3 == iso_act, 'add_info'].values[0] + \
                        val + \
                        ": The time series was filled by the mean over 2010-" + \
                        yrs_for_mean[-1][1:] + \
                        ", due to missing future values." + '\n'
                else:
                    ts_act.loc[ts_act.iso3 == iso_act, 'add_info'] = val + \
                        ": The time series was filled by the mean over 2010-" + \
                        yrs_for_mean[-1][1:] + \
                        ", due to missing future values." + '\n'
                # endif
            # endif
        # endfor
        
        #####
        # Calculate the EU28 values.
        if val != 'pc_cov_excl_lu': #Summing the percentages results in 28*100.
            if ('EU28' not in list(ts_act.iso3)) \
            or (ts_act.loc[ts_act.iso3 == 'EU28', yrs_all_str].isnull().all(axis=1).values[0]):
                if np.sum([1 for xx in isos['EU28']
                           if xx not in list(ts_act.iso3)]) > 0:
                    print("Warning in main_ndc_quantifications: " +
                          "not all EU28 countries are added to the " +
                          "EU28 time series for " + val + "!")
                # endif
                ts_add = pd.Series(index=ts_act.columns)
                ts_add[ts_add.index] = ts_act.loc[ts_act.iso3 == isos['EU28'][0], :].values[0]
                ts_add['iso3'] = 'EU28'
                ts_add[yrs_all_str] = ts_act.loc[ts_act.iso3.isin(isos['EU28']), yrs_all_str].sum(axis=0).values
                if 'EU28' in list(ts_act.iso3):
                    ts_act.loc[ts_act.iso3 == 'EU28', :] = ts_add.values
                else:
                    ts_act = ts_act.append(ts_add, ignore_index=True)
                # endif
            # endif
        # endif
        
        #####
        # Put in iso3s as index, and reindex to EARTH isos plus 'EU28'.
        ts_act.index = ts_act.iso3
        ts_act = ts_act.reindex(index=sorted(isos['EARTH'] + ['EU28']))
        #####
        # Put ts_act into dictionary 'time_series'.
        time_series[val] = ts_act
    # endfor
    # %%
    # Read in time series 1990-2050 (EU28 should be included already, done in preprocess_pc_cov_lulucf.ipynb).
    # The filling of LULUCF time series was done in MATLAB already (agu_ndc_get_lulucf_data.m).
    for val in time_series_lu_path.keys():
        ts_act = pd.read_csv(time_series_lu_path[val])
        #####
        # Put in iso3s as index, and reindex to EARTH isos plus 'EU28'.
        ts_act.index = ts_act.iso3
        ts_act = ts_act.reindex(index=sorted(isos['EARTH'] + ['EU28']))
        #####
        # Put ts_act into dictionary 'time_series'.
        time_series[val] = ts_act
    # endfor
    
    # %%
    return time_series
# enddef
# %%

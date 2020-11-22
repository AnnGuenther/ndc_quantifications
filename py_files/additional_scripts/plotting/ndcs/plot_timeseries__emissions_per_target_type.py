# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 08/2020.
"""

# %%
"""
Plot time series of emissions per target type, plot SSP2 as line, and give the 
range over the other SSPs.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting_both():
    
    tpes = meta.ndcs.types
    
    colours = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ndc_types.csv'), index_col=0)
    colours.loc['No targets', :] = colours.loc['NAN', :]
    
    years_int = range(1990, 2031)
    
    first_vals_main = pd.Series(dtype='float64')
    last_vals_main = pd.Series(dtype='float64')
    
    first_vals_reclass = pd.Series(dtype='float64')
    last_vals_reclass = pd.Series(dtype='float64')
    
    lnwdth = 2
    
    fig = plt.figure(figsize=(13, 4.5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    
    XL = [years_int[0] - 4, years_int[-1] + 4]
    for axa in [ax1, ax2]:
        axa.set_xlim(XL)
        axa.plot(XL, [0, 0], 'k', linewidth=.1)
    
    markers = {'SSP1': 's', 'SSP2': 'o', 'SSP3': '^', 'SSP4': 'p', 'SSP5': '*'}
    
    for count, tpe in zip(range(len(tpes)), tpes):
        
        isos_reclass = isos_per_type_reclass[tpe]
        
        if tpe in types_ax1:
            axa = ax1
        else:
            axa = ax2
        
        for ssp in emi.keys():
            
            vals_reclass = 1e-3 * emi[ssp].data.loc[isos_reclass, years_int].sum(axis=0)
            vals_nan_reclass = 1e-3 * emi[ssp].data.loc[ctrs_none_reclass, years_int].sum(axis=0)
            vals_all_reclass = 1e-3 * emi[ssp].data.loc[meta.isos.EARTH, years_int].sum(axis=0)
            
            if 'SSP2' in ssp:
                
                #lbl = tpe
                
                axa.plot(years_int, vals_reclass, color=colours.loc[tpe, :].to_list(), linewidth=lnwdth)
                first_vals_reclass.loc[tpe] = vals_reclass[vals_reclass.index[0]]
                last_vals_reclass.loc[tpe] = vals_reclass[vals_reclass.index[-1]]
                
                if count == 0:
                    
                    axa.plot(years_int, vals_nan_reclass, color=colours.loc['No targets', :].to_list(), linewidth=lnwdth)
                    first_vals_reclass.loc['No targets'] = vals_nan_reclass[vals_nan_reclass.index[0]]
                    last_vals_reclass.loc['No targets'] = vals_nan_reclass[vals_nan_reclass.index[-1]]
                    
                    first_vals_reclass.loc['All countries'] = vals_all_reclass[vals_all_reclass.index[0]]
                    last_vals_reclass.loc['All countries'] = vals_all_reclass[vals_all_reclass.index[-1]]
            
            marker = markers[meta.ssps.scens.long_to_short[ssp]]
            axa.plot(years_int[-1] + 3 * count / len(colours.index), vals_reclass[vals_reclass.index[-1]], 
                marker, color=colours.loc[tpe, :].to_list())
            
            if count == 0:
                
                axa.plot(years_int[-1], vals_nan_reclass[vals_nan_reclass.index[-1]],
                    marker, color=colours.loc['No targets', :].to_list())
    
    for count, tpe in zip(range(len(tpes)), tpes):
        
        isos_main = isos_per_type_main[tpe]
        
        if tpe in types_ax1:
            axa = ax1
        else:
            axa = ax2
        
        for ssp in emi.keys():
            
            vals_main = 1e-3 * emi[ssp].data.loc[isos_main, years_int].sum(axis=0)
            vals_nan_main = 1e-3 * emi[ssp].data.loc[ctrs_none_main, years_int].sum(axis=0)
            vals_all_main = 1e-3 * emi[ssp].data.loc[meta.isos.EARTH, years_int].sum(axis=0)
            
            if 'SSP2' in ssp:
                
                #lbl = tpe
                
                axa.plot(years_int, vals_main, '--', color=colours.loc[tpe, :].to_list(), linewidth=lnwdth)
                first_vals_main.loc[tpe] = vals_main[vals_main.index[0]]
                last_vals_main.loc[tpe] = vals_main[vals_main.index[-1]]
                
                if count == 0:
                    
                    axa.plot(years_int, vals_nan_main, '--', color=colours.loc['No targets', :].to_list(), linewidth=lnwdth)
                    first_vals_main.loc['No targets'] = vals_nan_main[vals_nan_main.index[0]]
                    last_vals_main.loc['No targets'] = vals_nan_main[vals_nan_main.index[-1]]
                    
                    first_vals_main.loc['All countries'] = vals_all_main[vals_all_main.index[0]]
                    last_vals_main.loc['All countries'] = vals_all_main[vals_all_main.index[-1]]
        
    axa = ax2
    YL = axa.get_ylim()
    axa.set_ylim()
    
    xadd = .1
    yadd = .05
    count = .2
    axa.text(XL[1] + xadd * (XL[1] - XL[0]), YL[1] - .1 * count * (YL[1] - YL[0]), 
        "type_reclass", 
        color='k', fontweight='bold', va='top')
    count += .5
    axa.text(XL[1] + xadd * (XL[1] - XL[0]), YL[1] - .1 * count * (YL[1] - YL[0]), 
        "Shares (SSP2)", 
        color='k', fontweight='bold', va='top')
    axa.text(XL[1] + xadd * (XL[1] - XL[0]), YL[1] - .1 * count * (YL[1] - YL[0]) - yadd * (YL[1] - YL[0]), 
        f" {years_int[0]} - {years_int[-1]}", 
        color='k', fontsize=8, fontweight='bold', va='top')
    
    count += 1
    for tpe in last_vals_reclass.sort_values(ascending=False).index:
        if tpe != 'All countries':
            axa.text(XL[1] + xadd * (XL[1] - XL[0]), YL[1] - .1 * count * (YL[1] - YL[0]), 
                f"{tpe}", 
                color=colours.loc[tpe, :].to_list(), fontweight='bold', va='top')
            axa.text(XL[1] + xadd * (XL[1] - XL[0]), YL[1] - .1 * count * (YL[1] - YL[0]) - yadd * (YL[1] - YL[0]), 
                f" {100. * first_vals_reclass.loc[tpe] / first_vals_reclass.loc['All countries'] :.1f}% -" +
                f" {100. * last_vals_reclass.loc[tpe] / last_vals_reclass.loc['All countries'] :.1f}%", 
                color=colours.loc[tpe, :].to_list(), fontweight='bold', fontsize=8, va='top')
            
            if tpe in types_ax1:
                axa2 = ax1
            else:
                axa2 = ax2
            
            axa2.plot([XL[0] + .01*(XL[1] - XL[0]), XL[0]], [first_vals_main[tpe], first_vals_main[tpe]], 
                color=colours.loc[tpe, :].to_list(), linewidth=3)
            axa2.plot([XL[1] - .01*(XL[1] - XL[0]), XL[1]], [last_vals_main[tpe], last_vals_main[tpe]], 
                color=colours.loc[tpe, :].to_list(), linewidth=3)
            
            axa2.plot([XL[0] + .01*(XL[1] - XL[0]), XL[0]], [first_vals_reclass[tpe], first_vals_reclass[tpe]], 
                color=colours.loc[tpe, :].to_list(), linewidth=3)
            axa2.plot([XL[1] - .01*(XL[1] - XL[0]), XL[1]], [last_vals_reclass[tpe], last_vals_reclass[tpe]], 
                color=colours.loc[tpe, :].to_list(), linewidth=3)
    
            count += 1
    
    years_rei = [years_int[0], years_int[-1]]
    #emi_all = 1e-3 * emi[next(xx for xx in emi.keys() if 'SSP2' in xx)].data. \
    #    loc[meta.isos.EARTH, years_rei].sum(axis=0)
    emi_REI = 1e-3 * emi[next(xx for xx in emi.keys() if 'SSP2' in xx)].data. \
        loc[isos_per_type_main['REI'], years_rei].sum(axis=0)
    #share_REI = 100. * emi_REI.div(emi_all)
    share_REI_RBY = 100. * 1e-3 * emi[next(xx for xx in emi.keys() if 'SSP2' in xx)].data. \
        loc[isos_per_type_main['REI_RBY'], years_rei].sum(axis=0).div(emi_REI)
    #share_REI_RBU = 100. * 1e-3 * emi[next(xx for xx in emi.keys() if 'SSP2' in xx)].data. \
    #    loc[isos_per_type['REI_RBU'], years_rei].sum(axis=0).div(emi_REI)
    YL = ax1.get_ylim()
    ax1.set_ylim()
#        f"Amongst countries with REI targets, {share_REI_RBY[years_rei[0]]:.1f}% / {share_REI_RBY[years_rei[-1]]:.1f}% " +
#        f" of their emissions in {years_rei[0]} / {years_rei[-1]} originated from countries with REI_RBY targets (for SSP2)." +
    ax1.text(XL[0], YL[0] - 0.16 * np.diff(YL), 
        "type_main as dashed lines, type_reclass as solid lines. "+
        "SSP marker scenarios: SSP1 (squares), SSP2 (circles), SSP3 (triangles), SSP4 (pentagons), SSP5 (stars)." + 
        annotation_add_on,
        fontsize=9, va='top', ha='left')
    
    for axa in [ax1, ax2]:
        YL = axa.get_ylim()
        axa.plot([meta.primap.last_year, meta.primap.last_year], YL, 'k:', linewidth=.2)
        axa.set_ylim(YL)
        axa.yaxis.set_ticks_position('both')
    
    #ax1.set_xlabel('years', fontweight='bold')
    ax1.set_ylabel('emissions / Gt CO$_2$eq (AR4)', fontweight='bold')
    for axa in [ax1, ax2]:
        axa.set_xlabel('year', fontweight='bold')
        axa.set_xticks(np.arange(1990, 2040, 10))
    
    hpf.put_labels_to_subplots(ax1, ax2)
    
    fig.subplots_adjust(right=.8, top=.95, bottom=.23)
    fig.savefig(path_to_file, dpi=300)
    path_to_pdf = str(path_to_file).replace('.png', '.pdf')
    fig.savefig(path_to_pdf, dpi=300)
    hpf.crop_pdf(path_to_pdf)
    fig.clf()
    plt.close(fig)

# %%
meta = setup_metadata()
emi = {}
for ssp in meta.ssps.scens.long:
    emi[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables',
        f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE.csv')).__reindex__(isos=meta.isos.EARTH)

ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)
ndcs.drop(index=['EU28'], inplace=True)
ndcs.loc['USA', :] = np.nan

path_to_folder = Path(meta.path.main, 'plots', 'time_series', 'per_type')

annotation_add_on = \
    "\nABS: absolute emissions, RBY: relative reduction vs. base year emissions, RBU: relative reduction vs. BAU, ABU: absolute reduction vs. BAU, " + \
    "\nREI: relative reduction of emissions intensity, AEI: absolute emissions intensity, NGT: non-GHG target."

isos_per_type_main = hpf.get_isos_per_target_type(ndcs.loc[:, 'TYPE_MAIN'], ndcs.loc[:, 'BASEYEAR'])
ctrs_none_main = isos_per_type_main['NAN']

isos_per_type_reclass = hpf.get_isos_per_target_type(ndcs.loc[:, 'TYPE_RECLASS'], ndcs.loc[:, 'BASEYEAR'])
ctrs_none_reclass = isos_per_type_reclass['NAN']

types_ax1 = ['ABU', 'AEI', 'NGT']
path_to_file = Path(path_to_folder, "time_series_emissions_per_target_type_main_and_reclass_range_of_ssps.png")
plotting_both()

# %%
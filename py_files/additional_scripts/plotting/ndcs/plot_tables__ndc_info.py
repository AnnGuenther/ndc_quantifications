# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
# Create a DataFrame with the available DataAvailable from NDCs,
# for the years and type of DataAvailable that I need for the target quantifications.
##
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()
ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0).reindex(index=meta.isos.EARTH)
ndcs.loc[:, 'ECONOMY_WIDE'] = ['NAN' if type(xx) != str else xx.upper() for xx in ndcs.loc[:, 'ECONOMY_WIDE']]

ndcs.drop(index=[xx for xx in ndcs.index 
    if (type(ndcs.loc[xx, 'NDC_INDC']) != str or not ndcs.loc[xx, 'NDC_INDC'] in ['NDC', 'INDC'])], inplace=True)

colours_case = {'YES': (0, .5, 0), 'NO': (.5, 0, 0), 'NAN': (0, 0, 0)}
markers_case = {'YES': 'x', 'NO': 'x', 'NAN': 'x'}

path_to_folder = Path(meta.path.main, 'plots', 'tables_ndcs')

# %%
# Countries on x-axis.

# Split countries in 3.
country_names = pd.Series(index=ndcs.index, dtype='object')
country_names.loc[:] = [hpf.convert_isos_and_country_names(xx, 'ISO3', 'ShortName')[0] for xx in country_names.index]
# Sort the names alphabetically, not the ISO3s.
country_names = country_names.sort_values()
#country_names['BES'] = 'Bonaire, St Eust. & Saba'
country_names[['ATG', 'BIH', 'CAF', 'PNG', 'STP', 'VCT', 'TTO', 'ARE']] = \
    ['Ant. & Barb.', 'Bosn. & Herz.', 'C. African Rep.', 'P. New Guinea', 'S. Tome & Princ.',
     'St. Vinc. & Grenad.', 'Trini. & Tobago', 'U. Arab Emirates']
ctrs_3 = {}
split_nr = 3
ctrs_div_3 = int(np.ceil(len(country_names)/split_nr))
count = 0
for irange in range(split_nr):
    ctrs_3[irange] = country_names.index[count:count + ctrs_div_3]
    count = count + ctrs_div_3

if ctrs_3[irange][-1] != country_names.index[-1]:
    print("Countries: something went wrong.")

kyotoghg_ipcm0el_2017 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    __reindex__(isos=meta.isos.EARTH, years=[2017])
global_share = 100. * kyotoghg_ipcm0el_2017.__global_share__()

# Plot the covered sectors and gases per country.
case = '_NDCS'
yvals = [xx + case for xx in meta.sectors.main.inclLU + meta.gases.kyotoghg]
yvals_lbls = [meta.sectors.main.sec_to_label[xx] for xx in meta.sectors.main.inclLU] + \
    [meta.gases.gas_to_label[xx] for xx in meta.gases.kyotoghg]
yvals = np.flipud(yvals)
yvals_lbls = np.flipud(yvals_lbls)
yvals_int = list(range(len(yvals)))
xvals_int = list(range(ctrs_div_3))
XL = [xvals_int[0] - 1, xvals_int[-1] + 1]
YL = [yvals_int[0] - .5, yvals_int[-1] + .5]

#fig = plt.figure(figsize=(15, 5))
fig = plt.figure(figsize=(14, 5))
for irange, panel in zip(ctrs_3.keys(), ['(a)', '(b)', '(c)']):
    axa = fig.add_subplot(1, 1, 1)
    
    # Put in a rectangle to separate the sectors and gases:
    axa.add_patch(plt.Rectangle((-.5, -.5), len(xvals_int), len(meta.gases.kyotoghg),
        facecolor=(1, 0, 0), clip_on=False, linewidth=.1, alpha=.1))
    axa.add_patch(plt.Rectangle((-.5, len(meta.gases.kyotoghg) - .5), len(xvals_int), len(yvals_int) - len(meta.gases.kyotoghg),
        facecolor=(0, 0, 1), clip_on=False, linewidth=.1, alpha=.1))
    #axa.text(XL[1] + .01 * np.diff(XL), 0 - .5, 'Sectors', fontweight='bold', ha='left', va='center', rotation=90)
    #axa.text(XL[1] + .01 * np.diff(XL), 0 - .5 + len(meta.gases.kyotoghg), 'Gases', fontweight='bold', ha='left', va='center', rotation=90)
    
    for iso3, row in zip(ctrs_3[irange], range(ctrs_div_3)):
        
        emi_share_2017 = '{:5.2f}'.format(global_share.loc[iso3].values[0])
        if ndcs.loc[iso3, 'ECONOMY_WIDE'] != 'YES':
            axa.text(row + .3, YL[1] + .2 * np.diff(YL), emi_share_2017, rotation=60, 
                     ha='center', va='top', color=colours_case['NAN'])
        else:
            axa.text(row + .3, YL[1] + .2 * np.diff(YL), emi_share_2017, rotation=60, 
                     ha='center', va='top', color=colours_case['YES'], fontweight='bold')
        
        lbl_YES = ('Covered' if row == 0 else '__nolegend__')
        lbl_NO = ('Not covered' if row == 0 else '__nolegend__')
        lbl_NAN = ('No information' if row == 0 else '__nolegend__')
        
        for case, lbl in ['YES', lbl_YES], ['NO', lbl_NO], ['NAN', lbl_NAN]:
            # calc
            axa.scatter([row if (type(xx) == str and xx.upper() == case) 
                else np.nan for xx in ndcs.loc[iso3, [yy.replace('NDCS', 'CALC') for yy in yvals]]], yvals_int, 80, 
                marker='s', color=colours_case[case], label='__nolegend__')
            # white markers
            axa.scatter([row if (type(xx) == str and xx.upper() == case) 
                else np.nan for xx in ndcs.loc[iso3, [yy.replace('NDCS', 'CALC') for yy in yvals]]], yvals_int, 45, 
                marker='s', color=(1, 1, 1), label='__nolegend__')
        
        for case, lbl in ['YES', lbl_YES], ['NO', lbl_NO], ['NAN', lbl_NAN]:
            # orig
            axa.scatter([row if (type(xx) == str and xx.upper() == case) 
                else np.nan for xx in ndcs.loc[iso3, yvals]], yvals_int, 20, 
                marker=markers_case[case], color=colours_case[case], label=lbl)
        
        # Put in a line separating the countries with different first letters.
        if (row > 0 and country_names[ctrs_3[irange][row - 1]][0] != country_names[ctrs_3[irange][row]][0]):
            axa.plot([row - .5, row - .5], axa.get_ylim(), 'k', linewidth=1)
    
    # Grid lines.
    # x-axis.
    for line in np.arange(-.5, ctrs_div_3 + .5, 1):
        axa.plot([line, line], axa.get_ylim(), 'k', linewidth=.2)
    # y-axis.
    for line in np.arange(-.5, len(yvals) + .5, 1):
        axa.plot(axa.get_xlim(), [line, line], 'k', linewidth=.2)
    
    axa.plot(XL, [len(meta.sectors.main.inclLU) + .5, len(meta.sectors.main.inclLU) + .5], 'k', linewidth=1)
    
    # Get rid of the ticks, but put in the names.
    axa.tick_params(axis='both', length=0)
    axa.set_xticks([xx + .5 for xx in xvals_int]) # So that the name positions are better.
    axa.set_yticks([xx + .5 for xx in yvals_int])
    axa.set_xticklabels(country_names.loc[ctrs_3[irange]].to_list(), rotation=60, ha='right', va='top', fontweight='bold')
    axa.set_yticklabels(yvals_lbls, rotation=30, ha='right', va='top', fontweight='bold')
    axa.set_xlim(XL)
    axa.set_ylim(YL)
    axa.text(XL[0] + .01*np.diff(XL), YL[1] + .27*np.diff(YL), panel, fontweight='bold')
    
    #txt = {'Global': .18, 'share': .11, '2017': .04}
    txt = {'Global': .23, 'share': .16, '2017': .09}
    #txt = {'Global': .15, 'share': .08, '2017': .01}
    for txt_act in txt.keys():
        axa.text(XL[0] - 0.005 * np.diff(XL), YL[1] + txt[txt_act] * np.diff(YL), txt_act, 
                 ha='right', va='top', fontweight='bold', rotation=30)
    
    #axa.arrow(XL[0], -.5, - (XL[1] - XL[0]) * .1, 0, facecolor='k', head_width=.3)
    if irange == 0:
        axa.legend(loc='center', bbox_to_anchor=(.5, 1.28), ncol=3)
    
    fig.subplots_adjust(bottom=.37, left=.07, right=.95, top=.83)
    fig.savefig(Path(path_to_folder, f"table_covered_sectors_and_gases_ndcs_orig_vert_{irange}.png"), dpi=300)
    fig.savefig(Path(path_to_folder, f"table_covered_sectors_and_gases_ndcs_orig_vert_{irange}.pdf"), dpi=300)
    hpf.crop_pdf(Path(path_to_folder, f"table_covered_sectors_and_gases_ndcs_orig_vert_{irange}.pdf"))
    fig.clf()

plt.close(fig)

# %%
"""
'Plot' a table with the emissions / population / GDP data needed for the quantification of (I)NDCs on a per-country basis.
For the main NDC types.
"""

# BIH, BRB, CRI, GEO and ISR have been checked, they give various target types and need the base year as well.

colours =  pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ndc_types.csv'), index_col=0)

data_needed = {}

emi_yrs_all = []
pop_yrs_all = []
gdp_yrs_all = []
tpes_all = []

for iso3 in ndcs.index:
    
    ndcs_iso = ndcs.loc[iso3, :]
    ctr =  hpf.convert_isos_and_country_names(iso3, 'ISO3', 'ShortName')[0]
    base_yr = ndcs_iso['BASEYEAR']
    intensity_ref = ndcs_iso['INTENSITY_PERCAP_GDP']
    tpe = ndcs_iso['TYPE_MAIN']
    
    data_needed_iso = {}
    emi_needed = []
    ref_needed = []
    ref = ''
    
    if (type(tpe) == str and tpe.upper() not in ['NAN', 'NGT']):
        
        if type(ndcs_iso[tpe]) != str:
            print(f"{iso3}: even though the type_main is {tpe}, there is no entry in the ndcs_info_table!!!")
        
        else:
            if tpe in ['ABS', 'ABU', 'AEI', 'NAN', 'NGT', 'RBU']:
                if (type(base_yr) != str and not np.isnan(base_yr)):
                    print(f"{iso3}: why does it have a base year?")
                    base_yr = np.nan
            
            ndc_vals = hpf.get_targets_from_json(ndcs_iso[tpe], tpe, iso3)
            tar_yrs = ndc_vals.loc[:, 'taryr'].to_list()
            
            if (type(base_yr) != str and not np.isnan(base_yr)):
                emi_needed.append(int(base_yr))
            for tar_yr in tar_yrs:
                emi_needed.append(int(tar_yr))
            
            emi_needed = sorted(set(emi_needed))
            
            if tpe in ['AEI', 'REI']:
                
                if ((tpe == 'AEI') or (type(base_yr) != str and not np.isnan(base_yr))): # AEI or REI_RBY
                    ref_needed = emi_needed
                else:
                    ref_needed = []
                
                if intensity_ref.upper() == 'POP':
                    ref = 'pop'
                elif intensity_ref.upper() == 'GDP':
                    ref = 'gdp'
                else:
                    print(f"Something went wrong with the intensity reference for {iso3}.")
    
    tpe = (tpe if tpe != 'REI' else ('REI_RBY' if (type(base_yr) != str and not np.isnan(base_yr)) else 'REI_RBU'))
    
    data_needed_iso['emi'] = emi_needed
    data_needed_iso['pop'] = (ref_needed if ref == 'pop' else [])
    data_needed_iso['gdp'] = (ref_needed if ref == 'gdp' else [])
    
    emi_yrs_all += data_needed_iso['emi']
    pop_yrs_all += data_needed_iso['pop']
    gdp_yrs_all += data_needed_iso['gdp']
    
    data_needed_iso['tpe'] = (tpe.upper() if type(tpe) == str else 'NAN')
    tpes_all += [data_needed_iso['tpe']]
    
    data_needed[iso3] = data_needed_iso

emi_yrs_all = sorted(set(emi_yrs_all))
pop_yrs_all = sorted(set(pop_yrs_all))
gdp_yrs_all = sorted(set(gdp_yrs_all))
tpes_all = sorted(set(tpes_all))

# Do not include years > 2050.
yrs_lim = 2051
emi_yrs_all = [xx for xx in emi_yrs_all if xx < yrs_lim]
pop_yrs_all = [xx for xx in pop_yrs_all if xx < yrs_lim]
gdp_yrs_all = [xx for xx in gdp_yrs_all if xx < yrs_lim]

# %%
# Population and GDP indicated by different markers.
# Countries on x-axis.

# Split countries in 3.
country_names = pd.Series(index=ndcs.index, dtype='object')
country_names.loc[:] = [hpf.convert_isos_and_country_names(xx, 'ISO3', 'ShortName')[0] for xx in country_names.index]
# Sort the names alphabetically, not the ISO3s.
country_names = country_names.sort_values()
#country_names['BES'] = 'Bonaire, St Eust. & Saba'
country_names[['ATG', 'BIH', 'CAF', 'PNG', 'STP', 'VCT', 'TTO', 'ARE']] = \
    ['Ant. & Barb.', 'Bosn. & Herz.', 'C. African Rep.', 'P. New Guinea', 'S. Tome & Princ.',
     'St. Vinc. & Grenad.', 'Trini. & Tobago', 'U. Arab Emirates']
ctrs_3 = {}
split_nr = 3
ctrs_div_3 = int(np.ceil(len(country_names)/split_nr))
count = 0
for irange in range(split_nr):
    ctrs_3[irange] = country_names.index[count:count + ctrs_div_3]
    count = count + ctrs_div_3

if ctrs_3[irange][-1] != country_names.index[-1]:
    print("Countries: something went wrong.")

yvals = range(len(emi_yrs_all + sorted(set(pop_yrs_all + gdp_yrs_all))))
yvals_lbls = [str(xx) for xx in emi_yrs_all] + [str(xx) for xx in sorted(set(pop_yrs_all + gdp_yrs_all))]
yvals = np.flipud(yvals)
yvals_lbls = np.flipud(yvals_lbls)
yvals_int = list(range(len(yvals)))
xvals_int = list(range(ctrs_div_3))
XL = [xvals_int[0] - 1, xvals_int[-1] + 1]
YL = [yvals_int[0] - .5, yvals_int[-1] + .5]

fig = plt.figure(figsize=(14, 5))
for irange, panel in zip(ctrs_3.keys(), ['(a)', '(b)', '(c)']):
    axa = fig.add_subplot(1, 1, 1)
    
    # Put in a rectangle to separate the emissions, pop and gdp:
    axa.add_patch(plt.Rectangle((-.5, -.5), len(xvals_int), len(set(gdp_yrs_all + pop_yrs_all)),
        facecolor=(1, 0, 0), clip_on=False, linewidth=.1, alpha=.05))
    axa.add_patch(plt.Rectangle((-.5, len(set(gdp_yrs_all + pop_yrs_all)) - .5), len(xvals_int), len(yvals_int) - len(set(gdp_yrs_all + pop_yrs_all)),
        facecolor=(0, 0, 1), clip_on=False, linewidth=.1, alpha=.05))
    
    # Check for which countries to put in a legend for the type.
    rows_types = {}
    for tpe in tpes_all:
        rows_types[tpe] = []
        for iso3, row in zip(ctrs_3[irange], range(ctrs_div_3)):
            if data_needed[iso3]['tpe'] == tpe:
                rows_types[tpe] += [row]
    
    for iso3, row in zip(ctrs_3[irange], range(ctrs_div_3)):
        
        tpe = data_needed[iso3]['tpe']
        
        if tpe == 'NGT':
            axa.add_patch(plt.Rectangle((row-.5, -.5), 
                1, len(set(gdp_yrs_all + pop_yrs_all)) + len(emi_yrs_all),
                facecolor=colours.loc[tpe].to_list(), clip_on=False, linewidth=.1, alpha=.2))

        if 'RBY' in tpe:
            # The target year emissions might be needed, if not 100% covered.
            axa.scatter(
                [np.nan for xx in np.flipud(sorted(set(gdp_yrs_all + pop_yrs_all)))] +
                [row if (xx in data_needed[iso3]['emi'] and xx > 2020) else np.nan for xx in np.flipud(emi_yrs_all)], 
                yvals_int, 80, marker='s', color=(0, 0, 0), label='__nolegend__')
        
        axa.scatter(
            [row if xx in data_needed[iso3]['gdp'] else np.nan for xx in np.flipud(sorted(set(gdp_yrs_all + pop_yrs_all)))] +
            [np.nan for xx in np.flipud(emi_yrs_all)], 
            yvals_int, 40, marker='^', color=colours.loc[tpe].to_list(), label='__nolegend__')
        axa.scatter(
            [row if xx in data_needed[iso3]['pop'] else np.nan for xx in np.flipud(sorted(set(gdp_yrs_all + pop_yrs_all)))] +
            [np.nan for xx in np.flipud(emi_yrs_all)], 
            yvals_int, 40, marker='o', color=colours.loc[tpe].to_list(), label='__nolegend__')
        
        if tpe in ['AEI', 'ABS']:
            marker_act = 'x'
        else:
            marker_act = 's'
        
        lbl = (tpe if (row == rows_types[tpe][0] and tpe not in ['NGT', 'NAN']) else '__nolegend__')
        axa.scatter(
            [np.nan for xx in np.flipud(sorted(set(gdp_yrs_all + pop_yrs_all)))] +
            [row if xx in data_needed[iso3]['emi'] else np.nan for xx in np.flipud(emi_yrs_all)], 
            yvals_int, 40, marker=marker_act, color=colours.loc[tpe].to_list(), label=lbl)
        
        # Put in a line separating the countries with different first letters.
        if (row > 0 and country_names[ctrs_3[irange][row - 1]][0] != country_names[ctrs_3[irange][row]][0]):
            axa.plot([row - .5, row - .5], axa.get_ylim(), 'k:', linewidth=1.5)
    
    # Grid lines.
    # x-axis.
    for line in np.arange(-.5, ctrs_div_3 + .5, 1):
        axa.plot([line, line], axa.get_ylim(), 'k', linewidth=.2)
    # y-axis.
    for line in np.arange(-.5, len(yvals) + .5, 1):
        axa.plot(axa.get_xlim(), [line, line], 'k', linewidth=.2)
        
    # Line separating historical gdp/pop and projections.
    axa.plot(XL, [len(set(gdp_yrs_all + pop_yrs_all)) - .5 - 3, len(set(gdp_yrs_all + pop_yrs_all)) - .5 - 3],
             'k:', linewidth=1.5)
    # Line separating the emissions and gdp/pop.
    axa.plot(XL, [len(set(gdp_yrs_all + pop_yrs_all)) - .5, len(set(gdp_yrs_all + pop_yrs_all)) - .5], 
             'k', linewidth=1.5)
    # Line separating the historical emissions and projections.
    axa.plot(XL, [4 + len(set(gdp_yrs_all + pop_yrs_all)) - .5, 4 + len(set(gdp_yrs_all + pop_yrs_all)) - .5], 
             'k:', linewidth=1.5)
    
    # Get rid of the ticks, but put in the names.
    axa.tick_params(axis='both', length=0)
    axa.set_xticks([xx + .5 for xx in xvals_int]) # So that the name positions are better.
    axa.set_yticks([xx + .5 for xx in yvals_int])
    axa.set_xticklabels(country_names.loc[ctrs_3[irange]].to_list(), rotation=60, ha='right', va='top', fontweight='bold')
    axa.set_yticklabels(yvals_lbls, ha='right', va='top', fontweight='bold')#, rotation=30)
    axa.set_xlim(XL)
    axa.set_ylim(YL)
    axa.text(XL[0] + .01*np.diff(XL), YL[1] + .05*np.diff(YL), panel, fontweight='bold')
    
    axa.text(XL[1] + .005 * np.diff(XL), YL[1] - .005 * np.diff(YL), 'Emissions', 
        rotation=90, fontweight='bold', ha='left', va='top')
    axa.text(XL[1] + .005 * np.diff(XL), YL[0] + .005 * np.diff(YL), 'GDP or POP', 
        rotation=90, fontweight='bold', ha='left', va='bottom')
    
    #axa.arrow(XL[0], -.5, - (XL[1] - XL[0]) * .1, 0, facecolor='k', head_width=.3)
    axa.legend(loc='center', bbox_to_anchor=(.5, 1.07), ncol=len(tpes_all))
    
    fig.subplots_adjust(bottom=.37, left=.07, right=.95, top=.93)
    fig.savefig(Path(path_to_folder, f"table_data_needed_ndcs_type_main_vert_{irange}.png"), dpi=300)
    fig.savefig(Path(path_to_folder, f"table_data_needed_ndcs_type_main_vert_{irange}.pdf"), dpi=300)
    hpf.crop_pdf(Path(path_to_folder, f"table_data_needed_ndcs_type_main_vert_{irange}.pdf"))
    fig.clf()

plt.close(fig)

# %%
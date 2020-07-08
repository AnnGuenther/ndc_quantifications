# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
"""
Plot the correlation between the emissions of the different sectors / gases and the total emissions.
"""

# %%
def plotting():
    
    ax_cat = fig1.add_subplot(subplots_rows1, subplots_cols1, 1)
    ax_ent = fig1.add_subplot(subplots_rows1, subplots_cols1, 2)
    
    ax2 = fig2.add_subplot(subplots_rows2, subplots_cols2, 1)
    
    emi_tot = tables.KYOTOGHG.data.reindex(index=[iso3]).loc[iso3, :]
    unit_new, multiplier = hpf.get_conversion_to_nice_unit(emi_tot, unit_emi)
    emi_tot = emi_tot * multiplier
    
    yrs_corr = range(2010, meta.primap.last_year + 1)
    
    for cat in cats_to_plot:
        # Cats.
        emi = getattr(tables, cat).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        xx = emi_tot.loc[yrs_corr].to_list()
        yy = emi.loc[yrs_corr].to_list()
        xx, yy, linreg = hpf.linear_regression(xx, yy)
        corrs_rvalues.loc[iso3, 'tot_' + cat] = linreg.rvalue
        
        # Indicate increasing years (colour-coded).
        yrs = np.arange(10, 70, (70-10)/len(emi.index))
        ax_cat.scatter(emi_tot, emi, yrs, color=colours['cats'].loc[cat], 
            label=meta.categories.main.cat_to_label[cat] + "\n" + cat)
        ax_cat.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], color=colours['cats'].loc[cat])
    
    for ent in ents_to_plot:
        # Ents.
        emi = getattr(tables, ent).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        xx = emi_tot.loc[yrs_corr].to_list()
        yy = emi.loc[yrs_corr].to_list()
        xx, yy, linreg = hpf.linear_regression(xx, yy)
        corrs_rvalues.loc[iso3, 'tot_' + ent] = linreg.rvalue
        
        # Indicate increasing years (colour-coded).
        yrs = np.arange(10, 70, (70-10)/len(emi.index))
        ax_ent.scatter(emi_tot, emi, yrs, color=colours['ents'].loc[ent], label=meta.gases.gas_to_label[ent])
        ax_ent.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], color=colours['ents'].loc[ent])
    
    for combi in combis:
        
        emi = getattr(tables, combi).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        
        xx = emi_tot.loc[yrs_corr].to_list()
        yy = emi.loc[yrs_corr].to_list()
        xx, yy, linreg = hpf.linear_regression(xx, yy)
        corrs_rvalues.loc[iso3, 'tot_' + combi] = linreg.rvalue
        
        # Indicate increasing years (colour-coded).
        yrs = np.arange(10, 70, (70-10)/len(emi.index))
        
        ax2.scatter(emi_tot, emi, yrs, color=colours['cats'].loc[combi.split('_')[1]], label=combi)
        ax2.scatter(emi_tot, emi, [xx/4 for xx in yrs], color=colours['ents'].loc[combi.split('_')[0]], label=combi)
        ax2.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], color=colours['cats'].loc[combi.split('_')[1]])
        ax2.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], ':', color=colours['ents'].loc[combi.split('_')[0]])
    
    ax_cat.legend(loc='center', bbox_to_anchor=(1.12, -.25), ncol=len(cats_to_plot))
    ax_ent.legend(loc='center', bbox_to_anchor=(-.15, -.36), ncol=len(ents_to_plot))
    ax2.legend(loc='center', bbox_to_anchor=(1.25, .5))
    
    ax_cat.set_ylabel(unit_new, fontweight='bold')
    ax_cat.set_xlabel(unit_new, fontweight='bold')
    ax_ent.set_xlabel(unit_new, fontweight='bold')
    ax2.set_xlabel(unit_new, fontweight='bold')
    ax2.set_ylabel(unit_new, fontweight='bold')
    
    YL = ax_cat.get_ylim()
    if YL[0] > 0.:
        YL = [0., YL[-1]]
    
    for axa in [ax_cat, ax_ent, ax2]:
        axa.set_ylim(YL)     
    
    ax_cat = hpf.set_ticks_scientific_notation(ax_cat, 'xy', power_limit=4)
    ax_ent = hpf.set_ticks_scientific_notation(ax_ent, 'xy', power_limit=4)
    ax2 = hpf.set_ticks_scientific_notation(ax2, 'xy', power_limit=4)
    ax_cat, ax_ent = hpf.put_labels_to_subplots(ax_cat, ax_ent)
    
    fig1.suptitle(str(emi.index.min()) + " - " + str(emi.index.max()), fontweight='bold')
    fig1.subplots_adjust(wspace=.25, bottom=.3)
    fig1.savefig(Path(plt_path, "corrs_sectors_entities_" + iso3 + ".png"), dpi=300)
    fig1.clf()
    
    ax2.set_title(str(emi.index.min()) + " - " + str(emi.index.max()), fontweight='bold')
    fig2.subplots_adjust(right=.7)
    fig2.savefig(Path(plt_path, f"corrs_combis_{iso3}.png"), dpi=300)
    fig2.clf()

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

plt_path = Path(meta.path.main, 'plots', 'correlations', 'corrs_emis')
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

cats_to_plot = ['IPCM0EL', 'IPC1', 'IPC2', 'IPCMAG', 'IPC4']
ents_to_plot = ['KYOTOGHG', 'CO2', 'CH4', 'N2O', 'FGASES']

unit_emi = 't CO2eq'
gwp = meta.gwps.default

tables = hpf.create_class()
for cat in cats_to_plot:
    
    setattr(tables, cat, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')).
            __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
            __reindex__(index=isos_to_be_plotted))

for ent in ents_to_plot:
    
    setattr(tables, ent, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', ent + '_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')).
            __convert_unit__(unit_emi, entity=ent, gwp=gwp). \
            __reindex__(index=isos_to_be_plotted))
    
combis = [
    'KYOTOGHG_IPCM0EL', 
    'CO2_IPC1', 'CO2_IPC2', 'CO2_IPCMAG', 'CO2_IPC4',
    'CH4_IPC1', 'CH4_IPC2', 'CH4_IPCMAG', 'CH4_IPC4',
    'N2O_IPC1', 'N2O_IPC2', 'N2O_IPCMAG', 'N2O_IPC4',
    'FGASES_IPC2']
for combi in combis:
    
    setattr(tables, combi, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', combi + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __convert_unit__(unit_emi, entity=combi.split('_')[0], gwp=gwp). \
            __reindex__(index=isos_to_be_plotted))

corrs_rvalues = pd.DataFrame(index=isos_to_be_plotted)

colours = {}
colours['cats'] = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
       'plotting', 'colours', 'colours_categories_ipc.csv'), index_col=[0])
colours['ents'] = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
       'plotting', 'colours', 'colours_gases.csv'), index_col=[0])

# %%
subplots_rows1 = 1
subplots_cols1 = 2
fig1 = plt.figure(figsize=(8, 6))

subplots_rows2 = 1
subplots_cols2 = 1
fig2 = plt.figure(figsize=(8, 7))

for iso3 in isos_to_be_plotted:
    
    plotting()

plt.close(fig1)
plt.close(fig2)

# %%

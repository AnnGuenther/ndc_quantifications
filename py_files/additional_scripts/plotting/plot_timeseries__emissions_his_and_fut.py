# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 05/2020.
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    # Plot the time series of the historic emissions, per sector.
    ax_stack_cat = fig1.add_subplot(subplots_rows1, subplots_cols1, 1)
    ax_stack_gas = fig1.add_subplot(subplots_rows1, subplots_cols1, 2)
    
    ax_emi_cat = fig2.add_subplot(subplots_rows2, subplots_cols2, 1)
    ax_pc_cat = fig2.add_subplot(subplots_rows2, subplots_cols2, 2)
    ax_emi_gas = fig2.add_subplot(subplots_rows2, subplots_cols2, 3)
    ax_pc_gas = fig2.add_subplot(subplots_rows2, subplots_cols2, 4)
    
    ax3_stack_cat = fig3.add_subplot(subplots_rows3, subplots_cols3, 1)
    ax3_emi_cat = fig3.add_subplot(subplots_rows3, subplots_cols3, 2)
    ax3_pc_cat = fig3.add_subplot(subplots_rows3, subplots_cols3, 3)
    ax3_stack_gas = fig3.add_subplot(subplots_rows3, subplots_cols3, 4)
    ax3_emi_gas = fig3.add_subplot(subplots_rows3, subplots_cols3, 5)
    ax3_pc_gas = fig3.add_subplot(subplots_rows3, subplots_cols3, 6)
    
    kyoto_ipcm0el_iso = getattr(tables, ssp2).data.reindex(index=[iso3]).loc[iso3, :]
    unit_new, multiplier = hpf.get_conversion_to_nice_unit(kyoto_ipcm0el_iso, unit_emi)
    kyoto_ipcm0el_iso = kyoto_ipcm0el_iso * multiplier
    
    for axa in [ax_pc_cat, ax_pc_gas, ax3_pc_cat, ax3_pc_gas]:
        axa.plot(kyoto_ipcm0el_iso.index, [0.]*len(kyoto_ipcm0el_iso.index), 'k--', linewidth=.5)
        axa.plot(kyoto_ipcm0el_iso.index, [1.]*len(kyoto_ipcm0el_iso.index), color=colours['cats'].loc['IPCM0EL'], linewidth=linewdth)
    
    for axa in [ax_emi_cat, ax_emi_gas, ax3_emi_cat, ax3_emi_gas]:
        data = getattr(tables, ssp2).data
        axa.plot(data.columns, [0.]*len(data.columns), 'k--', linewidth=.5)
    
    for axa in [ax_emi_cat, ax3_emi_cat, ax_stack_cat, ax3_stack_cat]:
        for ssp in meta.ssps.scens.long:
            data = getattr(tables, ssp).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
            axa.plot(data.index, data, ':', color=colours['ssps'].loc[ssp],
                linewidth=linewdth, label=ssp)
    
    for axa in [ax_emi_gas, ax3_emi_gas]:
        axa.plot(kyoto_ipcm0el_iso.index, kyoto_ipcm0el_iso, color=colours['ssps'].loc[ssp2], 
            linewidth=linewdth, label='Total emissions\n(excl. LULUCF; SSP2)')
    
    cat_data = pd.DataFrame(index=meta.categories.main.exclLU, columns=kyoto_ipcm0el_iso.index)
    
    for cat in cat_data.index:
        
        plt_cat = getattr(tables, cat).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        cat_data.loc[cat, plt_cat.index] = plt_cat
        
        for axa in [ax_emi_cat, ax3_emi_cat]:
            axa.plot(plt_cat.index, plt_cat, color=colours['cats'].loc[cat], linewidth=linewdth, 
                            label=meta.categories.main.cat_to_label[cat])
        
        plt_cat = plt_cat.div(kyoto_ipcm0el_iso.loc[plt_cat.index])
        
        for axa in [ax_pc_cat, ax3_pc_cat]:
            axa.plot(plt_cat.index, plt_cat, color=colours['cats'].loc[cat], linewidth=linewdth, 
                           label=meta.categories.main.cat_to_label[cat])
    
    # Plot the time series of the historic emissions, per gas.
    gas_data = pd.DataFrame(index=meta.gases.main + ['FGASES'], columns=kyoto_ipcm0el_iso.index)
    
    for ent in gas_data.index:
        
        plt_gas = getattr(tables, f"{ent}_ssp2").data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        gas_data.loc[ent, plt_gas.index] = plt_gas
        
        for axa in [ax_emi_gas, ax3_emi_gas]:
            axa.plot(plt_gas.index, plt_gas, color=colours['gases'].loc[ent], linewidth=linewdth, 
                            label=meta.gases.gas_to_label[ent])
        
        plt_gas = plt_gas.div(kyoto_ipcm0el_iso.loc[plt_gas.index])
        
        for axa in [ax_pc_gas, ax3_pc_gas]:
            axa.plot(plt_gas.index, plt_gas, color=colours['gases'].loc[ent], linewidth=linewdth, 
                           label=meta.gases.gas_to_label[ent])
    
    # Stacked historical emissions per category / gass.
    # Replace all NaNs with 0s for plotting.
    cat_data[cat_data.isnull()] = 0.
    gas_data[gas_data.isnull()] = 0.
    
    for axa in [ax_stack_cat, ax3_stack_cat]:
        axa.stackplot(cat_data.columns, [list(cat_data.values[xx]) for xx in range(len(cat_data.index))], 
            colors=colours['cats'].values, labels=[meta.categories.main.cat_to_label[xx] for xx in cat_data.index.values])
        
    for axa in [ax_stack_gas, ax3_stack_gas]:
        axa.stackplot(gas_data.columns, [list(gas_data.values[xx]) for xx in range(len(gas_data.index))], 
            colors=colours['gases'].values, labels=[meta.gases.gas_to_label[xx] for xx in gas_data.index.values])
    
    # Set y-lims.
    YL = ax_emi_cat.get_ylim()
    for axa in [ax_emi_cat, ax_emi_gas, ax3_emi_cat, ax3_emi_gas, 
                ax_stack_cat, ax3_stack_cat, ax_stack_gas, ax3_stack_gas]:
        axa.set_ylim(YL)
    
    YL = list(ax_pc_cat.get_ylim()) + list(ax_pc_gas.get_ylim())
    for axa in [ax_pc_cat, ax_pc_gas, ax3_pc_cat, ax3_pc_gas]:
        axa.set_ylim([min(YL), max(YL)])
    
    # Set labels.
    for axa in [ax_stack_cat, ax_stack_gas, ax_emi_gas, ax_pc_gas,
                ax3_stack_gas, ax3_emi_gas, ax3_pc_gas]:
        axa.set_xlabel('year', fontweight='bold')
    
    # Legend.
    ax_stack_cat.legend(loc='center', bbox_to_anchor=(2.7, .6))
    ax_stack_gas.legend(loc='center', bbox_to_anchor=(1.45, .15), ncol=2)
    ax_emi_cat.legend(loc='center left', bbox_to_anchor=(2.3, .5))
    ax_emi_gas.legend(loc='center left', bbox_to_anchor=(2.3, .5))
    handles, labels = ax3_stack_cat.get_legend_handles_labels()
    handles_new, labels_new = [], []
    for count in range(5):
        handles_new.append(handles[count])
        handles_new.append(handles[count + 5])
        labels_new.append(labels[count])
        labels_new.append(labels[count + 5])
    
    ax3_stack_cat.legend(handles_new, labels_new, loc='upper center', bbox_to_anchor=(1.75, -1.5), ncol=len(cat_data))
    ax3_stack_gas.legend(loc='upper center', bbox_to_anchor=(1.8, -.55), ncol=len(gas_data))
    
    ax_emi_cat.set_title('Emissions\n', fontweight='bold')
    ax3_emi_cat.set_title('Emissions\n', fontweight='bold')
    ax3_stack_cat.set_title('Emissions (stacked)\n', fontweight='bold')
    for axa in [ax_emi_cat, ax_emi_gas, ax3_stack_cat, ax3_stack_gas]:
        axa.set_ylabel(unit_new, fontweight='bold')
    
    ax_pc_cat.set_title('Share of emissions\n', fontweight='bold')
    ax3_pc_cat.set_title('Share of emissions\n', fontweight='bold')
    
    for axa in [ax_stack_cat, ax3_stack_cat, ax3_stack_gas, ax3_emi_cat, ax3_emi_gas]:
        axa.set_ylabel(unit_new, fontweight='bold')
    
    for axa in [ax_pc_cat, ax_pc_gas, ax3_pc_cat, ax3_pc_gas]:
        axa.set_ylabel(unit_new + ' / ' + unit_new, fontweight='bold')
    
    # Put in (a), (b), etc. at upper left edges.
    hpf.put_labels_to_subplots(ax_stack_cat, ax_stack_gas)
    hpf.put_labels_to_subplots(ax_emi_cat, ax_pc_cat, ax_emi_gas, ax_pc_gas)
    hpf.put_labels_to_subplots(ax3_stack_cat, ax3_emi_cat, ax3_pc_cat, ax3_stack_gas, ax3_emi_gas, ax3_pc_gas)
    
    fig1.subplots_adjust(wspace=.25, right=.7)
    fig1.savefig(Path(plt_path, f"emi_{iso3}_stacked.png"), dpi=300)
    fig1.clf()
    
    fig2.subplots_adjust(hspace=.2, wspace=.25, right=.8)
    fig2.savefig(Path(plt_path, f"emi_{iso3}_lines.png"), dpi=300)
    fig2.clf()
    
    fig3.subplots_adjust(hspace=.2, wspace=.25, bottom=.3)
    fig3.savefig(Path(plt_path, f"emi_{iso3}_lines_and_stacked.png"), dpi=300)
    fig3.clf()

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

colours = {}
for file, name in ['colours_gases.csv', 'gases'], ['colours_categories_ipc.csv', 'cats'], \
    ['colours_ssps.csv', 'ssps']:
    colours[name] = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
       'plotting', 'colours', file), index_col=[0])

plt_path = Path(meta.path.main, 'plots', 'time_series', 'emi_his_and_fut')
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

unit_emi = 't CO2eq'
gwp = meta.gwps.default

tables = hpf.create_class()

tables.primap = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
    __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
    __reindex__(index=isos_to_be_plotted)

ssp_srce = meta.ssps.emi['srce']
for ssp in meta.ssps.scens.long:
    setattr(tables, ssp, hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f"KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_{ssp_srce}.csv")). \
        __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
        __reindex__(index=isos_to_be_plotted))

for cat in meta.categories.main.exclLU:
    setattr(tables, cat, hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', 'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
        __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
        __reindex__(index=isos_to_be_plotted))

ssp2 = meta.ssps.scens.long[1]
for ent in meta.gases.main + ['FGASES']:
    setattr(tables, ent, hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', ent + '_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        __convert_unit__(unit_emi, entity=ent, gwp=gwp). \
        __reindex__(index=isos_to_be_plotted))
    setattr(tables, f"{ent}_ssp2", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f"{ent}_IPCM0EL_TOTAL_NET_{ssp2}FILLED_{ssp_srce}.csv")). \
        __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
        __reindex__(index=isos_to_be_plotted))

# %%
# fig1: stacked area plots
subplots_rows1 = 1
subplots_cols1 = 2
fig1 = plt.figure(figsize=(10, 4))

# fig2: line plots (not stacked)
subplots_rows2 = 2
subplots_cols2 = 2
fig2 = plt.figure(figsize=(11, 7))

# fig3: all together
subplots_rows3 = 2
subplots_cols3 = 3
fig3 = plt.figure(figsize=(13, 8))

linewdth = 3

for iso3 in isos_to_be_plotted:
    
    plotting()

plt.close(fig1)
plt.close(fig2)
plt.close(fig3)

# %%

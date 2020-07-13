# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.

To be run in py_files.
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    ax_gdp = fig1.add_subplot(subplots_rows1, subplots_cols1, 1)
    ax_pop = fig1.add_subplot(subplots_rows1, subplots_cols1, 2)
    
    # GDP and POP.
    gdp = tables.gdp.data.reindex(index=[iso3]).loc[iso3, :]
    pop = tables.pop.data.reindex(index=[iso3]).loc[iso3, :]
    
    yrs_corr = range(2010, meta.primap.last_year + 1)
    
    for cat in cats_to_plot:
        
        emi = getattr(tables, cat).data.reindex(index=[iso3]).loc[iso3, :]
        
        if not emi.isnull().all():
            
            # GDP.
            xx = gdp.loc[yrs_corr].to_list()
            yy = emi.loc[yrs_corr].to_list()
            xx, yy, linreg = hpf.linear_regression(xx, yy)
            corrs_sectors_rvalues.loc[iso3, 'gdp_' + cat] = linreg.rvalue
            yrs = np.arange(10, 70, (70-10)/len(emi.index))
            ax_gdp.scatter(gdp, emi, yrs, 
                color=colours['cats'].loc[cat], label=meta.categories.main.cat_to_label[cat] + "\n" + cat)
            ax_gdp.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], color=colours['cats'].loc[cat])
            
            # Population.
            xx = pop.loc[yrs_corr].to_list()
            xx, yy, linreg = hpf.linear_regression(xx, yy)
            corrs_sectors_rvalues.loc[iso3, 'pop_' + cat] = linreg.rvalue
            yrs = np.arange(10, 70, (70-10)/len(emi.index))
            ax_pop.scatter(pop, emi, yrs, 
                color=colours['cats'].loc[cat], label=meta.categories.main.cat_to_label[cat] + "\n" + cat)
            ax_pop.plot(xx, [linreg.slope*x + linreg.intercept for x in xx], color=colours['cats'].loc[cat])
    
    ax_gdp.legend(loc='center', bbox_to_anchor=(1.12, -.22), ncol=len(cats_to_plot))
    
    ax_gdp.set_ylabel('Mt CO2eq', fontweight='bold')
    ax_gdp.set_xlabel('2011 US$', fontweight='bold')
    ax_pop.set_xlabel('Pers', fontweight='bold')
    
    ax_gdp.set_title('GDPPPP (' + str(emi.index.min()) + " - " + str(emi.index.max()) + ')', fontweight='bold')
    ax_pop.set_title('Population (' + str(emi.index.min()) + " - " + str(emi.index.max()) + ')', fontweight='bold')
    
    YL = ax_gdp.get_ylim()
    ax_gdp.set_ylim(YL)
    ax_pop.set_ylim(YL)
    
    # Do that after having set the x/ylim (sci_not: only 1e3, 1e6, and not 1e4, 1e8, etc.)
    ax_gdp = hpf.set_ticks_scientific_notation(ax_gdp, 'x')
    ax_pop = hpf.set_ticks_scientific_notation(ax_pop, 'x')
    ax_gdp, ax_pop = hpf.put_labels_to_subplots(ax_gdp, ax_pop)
    
    fig1.subplots_adjust(wspace=.25, bottom=.2)
    
    fig1.savefig(Path(plt_path, f"corrs_sectors_socioeco_{iso3}.png"), dpi=300)
    fig1.clf()

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

cats_to_plot = ['IPCM0EL', 'IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
corrs_sectors_rvalues = pd.DataFrame(index=isos_to_be_plotted, 
    columns=['gdp_' + xx for xx in cats_to_plot] + ['pop_' + xx for xx in cats_to_plot])

colours = {}
colours['cats'] = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
       'plotting', 'colours', 'colours_categories_ipc.csv'), index_col=[0])
colours['cats'].loc['IPCM0EL'] = [.5, .5, .5]
colours['gdp'] = 'b'
colours['pop'] = 'c'

plt_path = Path(meta.path.main, 'plots', 'correlations', 'corrs_sectors_socioeco')
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

tablenames = {
    'gdp': 'GDPPPP_ECO_TOTAL_NET_HISTORY_' + meta.primap.current_version['gdp'],
    'pop': 'POP_DEMOGR_TOTAL_NET_HISTORY_' + meta.primap.current_version['gdp']}
tables = hpf.create_class()
for table in tablenames.keys():
    setattr(tables, table, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', tablenames[table] + '.csv')). \
            __reindex__(index=isos_to_be_plotted))

for cat in cats_to_plot:
    setattr(tables, cat, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_' + 
                 meta.primap.current_version['emi'] + '.csv')). \
            __reindex__(index=isos_to_be_plotted))

# %%
subplots_rows1 = 1
subplots_cols1 = 2
fig1 = plt.figure(figsize=(9, 5))

for iso3 in isos_to_be_plotted:
    
    plotting()

plt.close(fig1)

# %%

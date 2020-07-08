# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
"""
Plot time series of LULUCF emissions from different data-sources.
"""

# %% Import modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    # Plot the time series of the historic lulucf emissions, not per gas.
    # For the different available sources.
    axa = fig1.add_subplot(subplots_rows1, subplots_cols1, 1)
    axa.plot([years[0], years[-1]], [0, 0], 'k--', linewidth=.5)
    
    # Only plot the sources with data.
    plt_data = pd.DataFrame(columns=years)
    
    for srce in lulucf_prios:
        data_act = getattr(tables, srce).data.reindex(index=[iso3]).reindex(columns=years).loc[iso3, years]
        
        if not data_act.isnull().all():
            plt_data.loc[srce, years] = getattr(tables, srce).data.reindex(index=[iso3]).reindex(columns=years).loc[iso3, years]
    
    unit_new, multiplier = hpf.get_conversion_to_nice_unit(plt_data, unit_emi)
    
    for srce in np.flipud(plt_data.index):
        axa.plot(plt_data.columns, plt_data.loc[srce, years].multiply(multiplier), ':', color=colours.loc[srce], 
                 linewidth=linewdth, label='__nolegend__')
        mark = '<'
        if 'CRF' in srce:
            mark = '*'
        elif 'FAO' in srce:
            mark = 's'
        elif 'EDGAR' in srce:
            mark = 'v'
        elif 'BUR' in srce:
            mark = 'p'
        
        axa.plot(plt_data.columns, plt_data.loc[srce, years].multiply(multiplier), mark, color=colours.loc[srce], 
                 label=meta.sources.srce_to_label[srce])
            
    axa.plot(years, tables.chosen.data.reindex(index=[iso3]).loc[iso3, years].multiply(multiplier), 'o', color=[1, 0, 1], markersize=3)
    
    axa.set_xlim([years[0], years[-1]-1])
    
    axa.legend(loc='center', bbox_to_anchor=(1.2, .5))
    
    axa.set_xlabel('year', fontweight='bold')
    axa.set_ylabel(unit_new, fontweight='bold')
    
    fig1.subplots_adjust(right=.7)
    fig1.savefig(Path(plt_path, f"lulucf_{iso3}.png"), dpi=300)
    fig1.clf()

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

# Get data.
plt_path = Path(meta.path.main, 'plots', 'time_series', 'lulucf')
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

cmp = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colourmap_viridis.csv'))
lulucf_prios = meta.lulucf.source_prioritisation
colours = cmp.loc[list(range(0, cmp.index[-1], int(np.ceil(cmp.index[-1]/(len(lulucf_prios)-1))))) + [cmp.index[-1]]]
colours.index = lulucf_prios
unit_emi = 'tCO2eq'
years = range(1990, 2021)

# Datatables.
tables = hpf.create_class()
setattr(tables, 'chosen', hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')). \
        __convert_unit__(unit_emi).__reindex__(index=isos_to_be_plotted, columns=years))

for srce in lulucf_prios:
    
    if 'PRIMAPHIST' in srce:
        scen = 'HISTCR'
    elif 'FAO' in srce:
        scen = 'INTERLIN'
    else:
        scen = 'HISTORY'
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_' + scen + '_' + srce + '.csv')). \
        __convert_unit__(unit_emi).__reindex__(index=isos_to_be_plotted, columns=years)
    
    # The FAO data end in 2016.
    if 'FAO' in srce:
        table.data = table.data.reindex(columns=[xx for xx in table.data.columns if xx <= 2016])
    
    setattr(tables, srce, table)        

# %%
subplots_rows1 = 1
subplots_cols1 = 1
fig1 = plt.figure(figsize=(9, 4))
linewdth = 2

for iso3 in isos_to_be_plotted:
    
    plotting()

plt.close(fig1)

# %%
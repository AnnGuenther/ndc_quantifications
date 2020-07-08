# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
"""
Plot time series of GDP and population.
"""

# %% Import modules.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    ax_gdp = fig1.add_subplot(subplots_rows1, subplots_cols1, 1)
    ax_gdp_emi = fig1.add_subplot(subplots_rows1, subplots_cols1, 2)
    ax_pop = fig1.add_subplot(subplots_rows1, subplots_cols1, 3)
    ax_pop_emi = fig1.add_subplot(subplots_rows1, subplots_cols1, 4)
    
    # Titles.
    ax_gdp.set_title('GDP (PPP)', fontweight='bold')
    ax_gdp_emi.set_title('Emissions per GDP (PPP)', fontweight='bold')
    ax_pop.set_title('Population', fontweight='bold')
    ax_pop_emi.set_title('Emissions per capita', fontweight='bold')
    
    # 0-line.
    for axa in [ax_gdp, ax_gdp_emi, ax_pop, ax_pop_emi]:
        axa.plot([years[0], years[-1]], [0, 0], 'k--', linewidth=.5)
    
    # Get the data for that country.
    ssp_data = pd.DataFrame(columns=['ssp', 'family', 'unit', 'gwp'] + list(years))
    for ssp in ssp_scens:
        
        for what in ['emi_', 'emi_pop_', 'emi_gdp_']:
            ssp_data.loc[what + ssp, :] = \
                [ssp, what[:-1], getattr(tables, what + ssp).unit, getattr(tables, what + ssp).gwp] + \
                list(getattr(tables, what + ssp).data.reindex(index=[iso3]).loc[iso3, :].reindex(index=years).values)
        
        for what in ['pop_', 'gdp_']:
            ssp_data.loc[what + ssp, :] = [ssp, what[:-1], getattr(tables, what + ssp).unit, None] + \
            list(getattr(tables, what + ssp).data.reindex(index=[iso3]).loc[iso3, :].reindex(index=years).values)
    
    for what in ['co2_pop', 'co2_gdp']:
        ssp_data.loc[what, :] = [ssp, what, getattr(tables, what).unit,
            getattr(tables, what).gwp] + \
            list(getattr(tables, what).data.reindex(index=[iso3]).loc[iso3, :].reindex(index=years).values)
    
    # Convert to 'nice looking units'.
    units_new = {}
    for tpe, length in [['emi', 'short'], ['pop', 'long'], ['gdp', 'long'],
                        ['emi_pop', 'long'], ['emi_gdp', 'long']]:
        units_new[tpe] = {}
        data_act = ssp_data.loc[ssp_data.family == tpe, :]
        units_new[tpe]['unit'], units_new[tpe]['multiplier'] = hpf.get_conversion_to_nice_unit(
            data_act.loc[:, years], data_act.unit.unique()[0])
    
    for ssp in ssp_scens:
        
        linewdth = 2
        if 'SSP2' in ssp:
            linewdth = 3
        
        # Plot GDP and emissions/GDP.
        ax_gdp.plot(years, units_new['gdp']['multiplier'] * ssp_data.loc['gdp_' + ssp, years].transpose(), 
                    linewidth=linewdth, color=colours.loc[ssp], label=ssp_scens[ssp])
        ax_gdp_emi.plot(years, units_new['emi_gdp']['multiplier'] * ssp_data.loc['emi_gdp_' + ssp, years].transpose(), 
                        linewidth=linewdth, color=colours.loc[ssp], label=ssp_scens[ssp])
        
        # Plot POP and emissions/capita.
        ax_pop.plot(years, units_new['pop']['multiplier'] * ssp_data.loc['pop_' + ssp, years].transpose(),
                    linewidth=linewdth, color=colours.loc[ssp], label=ssp_scens[ssp])
        ax_pop_emi.plot(years, units_new['emi_pop']['multiplier'] * ssp_data.loc['emi_pop_' + ssp, years].transpose(),
                        linewidth=linewdth, color=colours.loc[ssp], label=ssp_scens[ssp])
        
        if 'SSP5' in ssp: # So that it is displayed last in the legend.
            ax_gdp_emi.plot(years, units_new['emi_gdp']['multiplier'] * ssp_data.loc['co2_gdp', years].transpose(), 
                            'k-.', linewidth=linewdth, label='Energy CO$_2$')
            ax_pop_emi.plot(years, units_new['emi_pop']['multiplier'] * ssp_data.loc['co2_pop', years].transpose(), 
                            'k-.', linewidth=linewdth, label='Energy CO$_2$')
    
    # TODO: include the global share as shaded area.
    
    # Legend
    ax_pop_emi.legend(loc='center', bbox_to_anchor=(-.17, -.35), ncol=len(ssp_scens) + 1)
    
    # Axis-labels.
    for axa in [ax_pop, ax_pop_emi]:
        axa.set_xlabel('year', fontweight='bold')
    
    ax_gdp.set_ylabel(units_new['gdp']['unit'].replace('GKD', ' US$'), fontweight='bold')
    ax_pop.set_ylabel(units_new['pop']['unit'], fontweight='bold')
    ax_gdp_emi.set_ylabel(units_new['emi_gdp']['unit'].replace('GKD', ' US$'), fontweight='bold')
    ax_pop_emi.set_ylabel(units_new['emi_pop']['unit'], fontweight='bold')
    
    # Add (a), (b), (c).
    hpf.put_labels_to_subplots(ax_gdp, ax_gdp_emi, ax_pop, ax_pop_emi)
    
    fig1.subplots_adjust(hspace=.3, wspace=.3, bottom=.2)
    fig1.savefig(Path(plt_path, f"socioeco_{iso3}.png"), dpi=300)
    fig1.clf()

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

# Get data.
# Path.
plt_path = Path(meta.path.main, 'plots', 'time_series', 'socioeco')
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

colours = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
    'plotting', 'colours', 'colours_ssps.csv'), index_col=[0])
ssp_scens = meta.ssps.scens.long_to_short
units = {'emi': 'tCO2eq', 'gdp': '2011GKD', 'pop': 'Pers',
         'emi_pop': 'tCO2eq / Pers', 'emi_gdp': 'tCO2eq / 2011GKD'}
gwp = meta.gwps.default
years = range(1990, 2051)

# Datatables.
# Set the units to the baseunits.
tables = hpf.create_class()
# Also plot the historical CO2_IPC1 emissions per GDPPPP or POP.
tables.CO2_IPC1 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'CO2_IPC1_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        __convert_unit__(units['emi'], entity = 'CO2', gwp=gwp).__reindex__(index=isos_to_be_plotted, columns=years)

for ssp in ssp_scens:
    setattr(tables, 'emi_' + ssp, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIE.csv')). \
            __convert_unit__(units['emi'], entity='KYOTOGHG', gwp=gwp).__reindex__(index=isos_to_be_plotted, columns=years))
    setattr(tables, 'pop_' + ssp, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'POP_DEMOGR_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIEMISC.csv')). \
            __convert_unit__(units['pop']).__reindex__(index=isos_to_be_plotted, columns=years))
    setattr(tables, 'gdp_' + ssp, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'GDPPPP_ECO_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIEMISC.csv')). \
            __convert_unit__(units['gdp']).__reindex__(index=isos_to_be_plotted, columns=years))
    # Emissions per pop or gdp.
    setattr(tables, 'emi_pop_' + ssp, hpf.combine_tables('divide', [getattr(tables, 'emi_' + ssp), getattr(tables, 'pop_' + ssp)]). \
        __reindex__(index=isos_to_be_plotted, columns=years))
    setattr(tables, 'emi_gdp_' + ssp, hpf.combine_tables('divide', [getattr(tables, 'emi_' + ssp), getattr(tables, 'gdp_' + ssp)]). \
        __reindex__(index=isos_to_be_plotted, columns=years))

setattr(tables, 'co2_pop', hpf.combine_tables('divide', [getattr(tables, 'CO2_IPC1'), getattr(tables, 'pop_' + list(ssp_scens.keys())[0])]). \
        __reindex__(index=isos_to_be_plotted, columns=years))
setattr(tables, 'co2_gdp', hpf.combine_tables('divide', [getattr(tables, 'CO2_IPC1'), getattr(tables, 'gdp_' + list(ssp_scens.keys())[0])]). \
        __reindex__(index=isos_to_be_plotted, columns=years))

# %% Plotting.
subplots_rows1 = 2
subplots_cols1 = 2
fig1 = plt.figure(figsize=(10, 8))

for iso3 in isos_to_be_plotted:
    
    plotting()

plt.close(fig1)

# %%
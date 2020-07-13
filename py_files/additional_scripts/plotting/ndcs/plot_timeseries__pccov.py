# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
"""
Plot time series of covered and total emissions per country, and the share of covered emissions (NDCs).
"""

# %% Import packages.
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from os import path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    # Plot the time series of emicov.
    ax_emi = fig.add_subplot(1, 2, 1)
    ax_emi.set_title("Total and covered emissions", fontweight='bold')
    ax_emi.set_xlabel("year", fontweight='bold')
    
    # Plot the time series of pccov.
    ax_pc = fig.add_subplot(1, 2, 2)
    ax_pc.set_title("Share of emissions covered", fontweight='bold')
    ax_pc.set_xlabel("year", fontweight='bold')
    ax_pc.set_ylabel("share of emissions covered", fontweight='bold')
    
    # Get the data for that country & 'nice looking units' for the emissions.      
    emitot = []
    for ssp in ssp_scens:
        emitot += list(getattr(tables, 'emitot_' + ssp).data.reindex(index=[iso3]).loc[iso3, :].values)
    
    unit_emi_new, multiplier = hpf.get_conversion_to_nice_unit(emitot, unit_emi)
    for ssp in ssp_scens:
        
        pc_plt = getattr(tables, 'pccov_' + ssp).data.reindex(index=[iso3]).loc[iso3, :]
        ax_pc.plot(pc_plt.index, pc_plt, color=colours.loc[ssp])
        
        emitot_plt = getattr(tables, 'emitot_' + ssp).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        ax_emi.plot(emitot_plt.index, emitot_plt, color=colours.loc[ssp], label=ssp_scens[ssp])
        
        emicov_plt = getattr(tables, 'emicov_' + ssp).data.reindex(index=[iso3]).loc[iso3, :] * multiplier
        ax_emi.plot(emicov_plt.index, emicov_plt, ':', color=colours.loc[ssp], linewidth=3, label='__nolegend__')
    
    # Plot PRIMAPHIST emissions.
    emitotp_plt = tables.emitot_primap.data.reindex(index=[iso3]).loc[iso3, :] * multiplier
    ax_emi.plot(emitotp_plt.index, emitotp_plt, 'k', label=meta.sources.srce_to_label[meta.primap.current_version['emi']])
    ax_emi.plot(emitotp_plt.index, emicov_plt.loc[emitotp_plt.index], 'k:', linewidth=3, label='__nolegend__')
    
    ax_emi.legend(loc='center', bbox_to_anchor=(1.13, -.2), ncol=len(ssp_scens)+1)
    
    ax_pc.plot(pc_plt.index, [0]*len(pc_plt.index), 'k--', linewidth=.5)
    ax_pc.plot(pc_plt.index, [1]*len(pc_plt.index), 'k--', linewidth=.5)
    ax_emi.plot(emitot_plt.index, [0]*len(emitot_plt.index), 'k--', linewidth=.5)
    
    ax_emi.set_ylabel("emissions / " + unit_emi_new, fontweight='bold')
    
    #hpf.set_ticks_scientific_notation(ax_emi, 'y')
    hpf.put_labels_to_subplots(ax_emi, ax_pc)
    
    fig.subplots_adjust(wspace=.25, bottom=.2)
    plt.savefig(Path(plt_path, f"pccov_{iso3}_{case}.png"), dpi=300)
    plt.clf()
    # TODO: Which sectors / gases are covered.

# %%
meta = setup_metadata()
isos_to_be_plotted = meta.isos.EARTH_EU28

plt_path = Path(meta.path.main, 'plots', 'time_series', str(meta.path.pc_cov).split('\\')[-1])
if ~path.isdir(plt_path):
    plt_path.mkdir(parents=True, exist_ok=True)

colours = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
       'plotting', 'colours', 'colours_ssps.csv'), index_col=[0])
ssp_scens = meta.ssps.scens.long_to_short
unit_emi = 'tCO2eq'
gwp = 'AR4'
years = range(1990, 2030)

    
for case in ['CORR', 'GROWTH']:
    
    # Datatables
    # Set the units to the baseunits.
    tables = hpf.create_class()    
    
    for ssp in ssp_scens:
    
        setattr(tables, 'pccov_' + ssp, hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.pc_cov, f'KYOTOGHG_IPCM0EL_COV_PC_{ssp}FILLED_{case}.csv')). \
                __reindex__(index=isos_to_be_plotted, columns=years))
        
        setattr(tables, 'emicov_' + ssp, hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.pc_cov, f'KYOTOGHG_IPCM0EL_COV_EMI_{ssp}FILLED_{case}.csv')).
                __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
                __reindex__(index=isos_to_be_plotted, columns=years))
        
        setattr(tables, f'emitot_{ssp}', hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.preprocess, 'tables', f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE.csv')).
                __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
                __reindex__(index=isos_to_be_plotted, columns=years))
    
    setattr(tables, 'emitot_primap', hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', f"KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_{meta.primap.current_version['emi']}.csv")).
            __convert_unit__(unit_emi, entity='KYOTOGHG', gwp=gwp). \
            __reindex__(index=isos_to_be_plotted, columns=years))
    
    fig = plt.figure(figsize=(10, 5))
    
    for iso3 in isos_to_be_plotted:
         
        plotting()
    
    plt.close(fig)
    
# %%
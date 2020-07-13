# -*- coding: utf-8 -*-
"""
Author: Annika Günther
Last update in 03/2020.
"""

# %%
"""
Share of emissions per sector, per gas, and per combination of sector and gas.
Share compared to national emissions (or emissions per group of countries).
For PRIMAP-hist.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
from warnings import warn
import re
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def get_table(path_to_file, unit, gwp, meta):
    # Get table and convert the units.
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        path_to_file)
    
    table.ent = table.entity.replace('AR4', '')
    table.cat = table.category
    table.__convert_unit__(unit, entity=table.ent, gwp=gwp)
    
    table.__reindex__(isos=meta.isos.EARTH)
    
    table.data.loc['EARTH', :] = table.data.reindex(index=meta.isos.EARTH).sum(axis=0)
    table.data.loc['EU28', :] = table.data.reindex(index=meta.isos.EU28).sum(axis=0)
    
    return table
    
# %%
def calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year):
    
    path_to_file = Path(meta.path.matlab, '_'.join([gas, cat, 'TOTAL', 'NET', 'HISTCR',
        meta.primap.current_version['emi']]) + '.csv')
    
    if path_to_file.exists():
        table = get_table(path_to_file, unit, gwp, meta)
        
        share = 100 * table.data.reindex(index=meta.isos.EARTH + ['EARTH', 'EU28']).reindex(columns=[year]).div(table_tot_act)
        
        output.loc[share.index, table.ent + '_' + table.cat] = share.loc[:, year]
    
    return output

# %%
# Get metadata.
meta = setup_metadata()

unit, gwp = 'MtCO2eq', 'AR4'

# Get the total emissions.
path_to_file=Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_' + 
    meta.primap.current_version['emi'] + '.csv')
table_tot = get_table(path_to_file, unit, gwp, meta).data

year = 2017

# Setup output DataFrame.
output = pd.DataFrame(index=meta.isos.EARTH + ['EU28', 'EARTH'], dtype='float64')

table_tot_act = table_tot.reindex(index=output.index).reindex(columns=[year])

# Get the 'national' share for 2017 per gas.
cat = 'IPCM0EL'
for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4', 'KYOTOGHGAR4']:
    output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)
    
test = output.loc['DEU', :].reindex(index=[xx + '_' + cat for xx in meta.gases.main + ['FGASES']]).sum()
if abs(100 - test) > 1e-4:
    warn("national_share_of_emissions_per_gas_and_sector.py: something went wrong (test1).")

# Get the global share for 2017 per category.
gas = 'KYOTOGHGAR4'
for cat in meta.categories.main.exclLU:
    output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)

test = output.loc['DEU', :].reindex(index=[gas.replace('AR4', '') + '_' + xx for xx in meta.categories.main.exclLU]).sum()
if abs(100 - test) > 1e-4:
    warn("national_share_of_emissions_per_gas_and_sector.py: something went wrong (test2).")

# Get the global share for 2017 per gas + category combination.
for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4']:
    for cat in meta.categories.main.exclLU:
        output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)

test = output.loc['DEU', :].reindex(index=[gas + '_' + cat 
    for gas in meta.gases.main + ['FGASES'] for cat in meta.categories.main.exclLU]).sum()
if abs(100 - test) > 1e-4:
    warn("national_share_of_emissions_per_gas_and_sector.py: something went wrong (test3).")

output.index.name = f"{year}_MtCO2eq_AR4"

# Write out the data.
output.to_csv(Path(meta.path.main, 'data', 'other', 'national_share_per_gas_and_sector_' + 
    meta.primap.current_version['emi'] + '_HISTCR_' + str(year) + '.csv'))

# %%
"""
Create a "latex" table with the numbers for EARTH and the maximal share on a per-country basis.
"""

out_earth = output.loc['EARTH', :]
value = "{:.3f}".format(1e-3 * table_tot.loc[:, year].reindex(index=meta.isos.EARTH).sum())
value = '~'.join(re.findall('...?',value[:value.find('.')][::-1]))[::-1]+value[value.find('.'):]

txt = str(year) + ": " + value + "~" + 'Gg CO$_2$eq' + " & \multicolumn{2}" + \
    "} & \multicolumn{2}".join(["{|c}{\\bfseries " + xx if xx != 'All Kyoto GHGs' 
    else "{||c}{\\bfseries " + xx for xx in 
    ['CO$_2$', 'CH$_4$', 'N$_2$O', 'F-gases', 'All Kyoto GHGs']])
txt += "} \\tabularnewline \hline \hline"
    
for cat, cat_label in ['IPC1', 'Energy'], ['IPC2', 'IPPU'], \
    ['IPCMAG', 'Agriculture'], ['IPC4', 'Waste'], ['IPC5', 'Other'], ['IPCM0EL', 'All sectors']:
    
    if cat != 'IPCM0EL':
        txt += "\n" + cat_label + " & " + \
            " & ".join([
                ("{:.1f}".format(out_earth.loc[xx + '_' + cat]) 
                 if "{:.1f}".format(out_earth.loc[xx + '_' + cat]) != '0.0'
                 else "{:.2f}".format(out_earth.loc[xx + '_' + cat])) + \
            " & \\itshape " + 
            ("{:.1f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0])
             if "{:.1f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0]) != '0.0'
             else "{:.2f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0]))
            if xx + '_' + cat in list(out_earth.index) else '-- & --' 
            for xx in ['CO2', 'CH4', 'N2O', 'FGASES', 'KYOTOGHG']]) + " \\tabularnewline"
    
    if cat == 'IPCM0EL':
        txt += " \hline \hline \n" + cat_label + " & \\bfseries " + \
            " & \\bfseries ".join([
                ("{:.1f}".format(out_earth.loc[xx + '_' + cat])
                 if "{:.1f}".format(out_earth.loc[xx + '_' + cat]) != '0.0'
                 else "{:.2f}".format(out_earth.loc[xx + '_' + cat])) + \
            " & \\bfseries \\itshape " + 
            ("{:.1f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0])
             if "{:.1f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0]) != '0.0'
             else "{:.2f}".format(output.loc[meta.isos.EARTH, xx + '_' + cat].sort_values(ascending=False)[0]))
            if xx + '_' + cat in list(out_earth.index) else '-- & --' 
            for xx in ['CO2', 'CH4', 'N2O', 'FGASES', 'KYOTOGHG']]) + \
            " \\tabularnewline"

# Remove the last "\\tabularnewline"
txt = txt[:-len('\\tabularnewline')]

# Write the table to a csv-file.
hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'earth_share_per_gas_and_sector_' +
    meta.primap.current_version['emi'] + '_HISTCR_' + str(year) + '_latex_Max.csv'))

# %%
"""
Create a "latex" table with the numbers for EARTH and the 95th percentile of share on a per-country basis.
"""

out_earth = output.loc['EARTH', :]
value = "{:.3f}".format(1e-3 * table_tot.loc[:, year].reindex(index=meta.isos.EARTH).sum())
value = '~'.join(re.findall('...?',value[:value.find('.')][::-1]))[::-1]+value[value.find('.'):]

txt = str(year) + ": " + value + "~" + 'Gg CO$_2$eq' + " & " + \
    " & ".join(["\\bfseries " + xx for xx in 
    ['All gases', 'CO$_2$', 'CH$_4$', 'N$_2$O', 'HFCs', 'PFCs', 'SF$_6$', 'NF$_3$']])
txt += " \\tabularnewline \hline \hline"
    
for cat, cat_label in ['IPCM0EL', 'All sectors'], ['IPC1', 'Energy'], ['IPC2', 'IPPU'], \
    ['IPCMAG', 'Agriculture'], ['IPC4', 'Waste'], ['IPC5', 'Other']:
    
    if cat != 'IPCM0EL':
        txt += "\n" + cat_label + " & " + \
            " & ".join([
                "{:.1f}".format(out_earth.loc[xx + '_' + cat])+ \
            " (" + 
            "{:.1f}".format(np.nanpercentile(output.loc[meta.isos.EARTH, xx + '_' + cat].to_list(), 95)) + ")"
            if xx + '_' + cat in list(out_earth.index) else '--' 
            for xx in ['KYOTOGHG', 'CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3']]) + " \\tabularnewline"
    
    if cat == 'IPCM0EL':
        txt += "\n" + cat_label + " & " + \
            " & ".join([
                "{:.1f}".format(out_earth.loc[xx + '_' + cat])+ \
            " (" + 
            "{:.1f}".format(np.nanpercentile(output.loc[meta.isos.EARTH, xx + '_' + cat].to_list(), 95)) + ")"
            if xx + '_' + cat in list(out_earth.index) else '--' 
            for xx in ['KYOTOGHG', 'CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3']]) + \
            " \\tabularnewline \hline "

# Remove the last "\\tabularnewline"
txt = txt[:-len('\\tabularnewline')]

# Write the table to a csv-file.
hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'earth_share_per_gas_and_sector_' +
    meta.primap.current_version['emi'] + '_HISTCR_' + str(year) + '_latex_95thPercentile.csv'))

# %%
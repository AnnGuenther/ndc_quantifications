# -*- coding: utf-8 -*-
"""
Author: Annika GÜnther, annika.guenther@pik-potsdam.de
Last update: 01/2020
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
"""
Get the temperatures from MAGICC (single runs per NDCmitiQ run, and 600 individual MAGICC temperature pathways per run).
Store them in one file (BAU, NDCCB, NDCCW, NDCUCB, NDCUCW separately).
"""
meta = setup_metadata()

path_to_dir = Path('C:/Users/annikag/primap/output/ndcs')
dirs = hpf.get_all_files_and_or_folders_in_dir(
    path_to_dir, what='folders', how='short', contains='ndcs_')

temp_offset = .61
# warming between the periods 1850-1900 and 1986-2005, according to AR5 WG1 page 193).
# Has to be added to the MAGICC output!

def get_data():
    
    columns = [f"{xx}_{yy}" for xx in dirs for yy in range(600)]
    df = pd.DataFrame(index=range(1950, 2101), columns=columns)
    
    for folder in dirs:
        
        path_to_magicc = Path(path_to_dir, folder, 'MAGICC')
        folders = hpf.get_all_files_and_or_folders_in_dir(
            path_to_magicc, what='folders', how='short', contains='MAGICCresults_')
        
        data = pd.read_csv(Path(path_to_magicc, [xx for xx in folders if what in xx][0],
            'CSSENS_DAT_SURFACE_TEMP_BOXGLOBAL_MAGICC_INDIVIDUAL.OUT'), delim_whitespace=True, skiprows=range(24), header=None)
        
        # test:
        if data.loc[:, 0].astype('int').to_list() != list(range(1950, 2101)) or data.shape != (151, 601):
            print(f"something went wrong for {what} {path_to_magicc}")
        
        data.index = data.loc[:, 0].astype('int')
        data.drop(columns=[0], inplace=True)
        data.columns = [f"{folder}_{xx}" for xx in range(600)]
        # add temp_offset!!
        data = data.add(temp_offset)
        
        df.loc[data.index, data.columns] = data
    
    df.to_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_all_{what}.csv'))
    
    return df

cases = ['BAU', 'NDCCB', 'NDCCW', 'NDCUCB', 'NDCUCW']

all_temps = {}
for what in cases:
    all_temps[what] = get_data()

# %%
"""
Choose a subset: excl SSP5.
"""
pcs_all = pd.DataFrame(index=range(1950, 2101))
for what in cases:
    #data = all_temps[what]
    data = pd.read_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_all_{what}.csv'))
    cols = [xx for xx in data.columns if 'SSP5' not in xx]
    data = data.loc[:, cols]
    pcs_all.loc[:, f'{what}_pc_2_5'] = np.percentile(data, 2.5, axis=1)
    pcs_all.loc[:, f'{what}_pc_16'] = np.percentile(data, 16, axis=1)
    pcs_all.loc[:, f'{what}_pc_50'] = np.percentile(data, 50, axis=1)
    pcs_all.loc[:, f'{what}_pc_84'] = np.percentile(data, 84, axis=1)
    pcs_all.loc[:, f'{what}_pc_97_5'] = np.percentile(data, 97.5, axis=1)

pcs_all.to_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_percentiles_exclSSP5.csv'))

# %%
"""
Choose a subset: per SSP.
"""
for ssp in ['SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5']:
    pcs_all = pd.DataFrame(index=range(1950, 2101))
    for what in cases:
        #data = all_temps[what]
        data = pd.read_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_all_{what}.csv'))
        cols = [xx for xx in data.columns if ssp in xx]
        data = data.loc[:, cols]
        pcs_all.loc[:, f'{what}_pc_2_5'] = np.percentile(data, 2.5, axis=1)
        pcs_all.loc[:, f'{what}_pc_16'] = np.percentile(data, 16, axis=1)
        pcs_all.loc[:, f'{what}_pc_50'] = np.percentile(data, 50, axis=1)
        pcs_all.loc[:, f'{what}_pc_84'] = np.percentile(data, 84, axis=1)
        pcs_all.loc[:, f'{what}_pc_97_5'] = np.percentile(data, 97.5, axis=1)
    
    pcs_all.to_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_percentiles_only{ssp}.csv'))

# %%
"""
Choose a subset: only Main/Reclass pccov100/est (so basically default settings), exclSSP5.
"""
pcs_all = pd.DataFrame(index=range(1950, 2101))
for what in cases:
    #data = all_temps[what]
    data = pd.read_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_all_{what}.csv'))
    cols = [xx for xx in data.columns if not any(yy in xx for yy in ['SSP5', 'FAO', 'BLForUCAboveBL', 'constEmiAfterLastTar'])]
    data = data.loc[:, cols]
    pcs_all.loc[:, f'{what}_pc_2_5'] = np.percentile(data, 2.5, axis=1)
    pcs_all.loc[:, f'{what}_pc_16'] = np.percentile(data, 16, axis=1)
    pcs_all.loc[:, f'{what}_pc_50'] = np.percentile(data, 50, axis=1)
    pcs_all.loc[:, f'{what}_pc_84'] = np.percentile(data, 84, axis=1)
    pcs_all.loc[:, f'{what}_pc_97_5'] = np.percentile(data, 97.5, axis=1)

pcs_all.to_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_percentiles_exclSSP5_onlyDefault.csv'))

# %%
pcs_all = pd.read_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_percentiles_exclSSP5_onlyDefault.csv'), index_col=0)

fig = plt.figure(figsize=(6, 6))

axa = fig.add_subplot(1, 1, 1)

axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'BAU_pc_16'].values, pcs_all.loc[:, 'BAU_pc_84'].values, color='k', alpha=.1)
axa.plot(pcs_all.loc[:, 'BAU_pc_50'], 'k', label='BAU')
axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'NDCUCW_pc_16'].values, pcs_all.loc[:, 'NDCUCW_pc_84'].values, color='r', alpha=.1)
axa.plot(pcs_all.loc[:, 'NDCUCW_pc_50'], 'r', label='NDC uncond. worst')
axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'NDCCB_pc_16'].values, pcs_all.loc[:, 'NDCCB_pc_84'].values, color='g', alpha=.1)
axa.plot(pcs_all.loc[:, 'NDCCB_pc_50'], 'g', label='NDC cond. best')

axa.yaxis.set_ticks_position('both')
axa.set_xlabel('years')
axa.set_ylabel('temperature increase / °C')
axa.legend(loc='upper left')

fig.subplots_adjust(left=.1, bottom=.1, right=.95, top=.95)
path_to_png = Path(meta.path.main, 'plots', 'temperatures', 'temperatures_onlyDefault_exclSSP5.png')
plt.savefig(path_to_png, dpi=300)
plt.clf()
plt.close(fig)

# TODO: try to figure out why my BAU is lower than the CAT.
# https://climateactiontracker.org/global/temperatures/
# Their baseline is higher, but their pledges are lower?!

# %%
pcs_all = pd.read_csv(Path(meta.path.main, 'data', 'magicc_temperatures', f'magicc_temperatures_percentiles_onlySSP2.csv'), index_col=0)

fig = plt.figure(figsize=(6, 6))

axa = fig.add_subplot(1, 1, 1)

axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'BAU_pc_16'].values, pcs_all.loc[:, 'BAU_pc_84'].values, color='k', alpha=.1)
axa.plot(pcs_all.loc[:, 'BAU_pc_50'], 'k', label='BAU')
axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'NDCUCW_pc_16'].values, pcs_all.loc[:, 'NDCUCW_pc_84'].values, color='r', alpha=.1)
axa.plot(pcs_all.loc[:, 'NDCUCW_pc_50'], 'r', label='NDC uncond. worst')
axa.fill_between(range(1950, 2101), pcs_all.loc[:, 'NDCCB_pc_16'].values, pcs_all.loc[:, 'NDCCB_pc_84'].values, color='g', alpha=.1)
axa.plot(pcs_all.loc[:, 'NDCCB_pc_50'], 'g', label='NDC cond. best')

axa.yaxis.set_ticks_position('both')
axa.set_xlabel('years')
axa.set_ylabel('temperature increase / °C')
axa.legend(loc='upper left')

fig.subplots_adjust(left=.1, bottom=.1, right=.95, top=.95)
path_to_png = Path(meta.path.main, 'plots', 'temperatures', 'temperatures_onylSSP2.png')
plt.savefig(path_to_png, dpi=300)
plt.clf()
plt.close(fig)

# %%

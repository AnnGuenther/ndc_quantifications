# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

path_to_folder_reclass = 'ndcs_20200628_2120_SSP2_typeReclass'
tars_reclass = pd.read_csv(Path(meta.path.output, 'output_for_paper', path_to_folder_reclass, 'ndc_targets.csv'))

ndcs_onylLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_onlyLU.csv'), index_col=0)
ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')).data
ssp2_exclLU = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGBFILLED_PMSSPBIE.csv')).data

# %%
fig = plt.figure(figsize=(10, 5))

for iso3 in meta.isos.EARTH:
    
    tars_iso3 = tars_reclass.loc[tars_reclass.iso3 == iso3, :]
    if len(tars_iso3) > 0:
        tar_type_reclass = tars_iso3.tar_type_reclass.unique()[0]
        
        if any(tars_iso3.tar_emi_inclLU.astype(float) < 0.):
            
            ax1 = fig.add_subplot(1, 1, 1)
            
            ax1.plot([1990, 2050], [0, 0], 'k:')
            try:
                ax1.plot(ipcmlulucf.columns, ipcmlulucf.loc[iso3, :], 'g', label='LU external')
            except:
                pass
            
            ax1.plot(ssp2_exclLU.columns, ssp2_exclLU.loc[iso3, :], 'k', label='ssp2 baseline exclLU')
            ax1.scatter(
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'taryr'].astype(float).values,
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'tar_emi_inclLU'].astype(float).values, marker='s', color='b', label='tar_emi_inclLU')
            ax1.scatter(
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'taryr'].astype(float).values,
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'tar_emi_exclLU'].astype(float).values, marker='*', color='b', label='tar_emi_exclLU')
            ax1.scatter(
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'refyr'].astype(float).values,
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'emi_bl_onlyLU_refyr'].astype(float).values, marker='^', color='g', label='LU used refyr')
            ax1.scatter(
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'taryr'].astype(float).values,
                tars_iso3.loc[tars_iso3.tar_type_used == tar_type_reclass, 'emi_bl_onlyLU_taryr'].astype(float).values, marker='o', color='g', label='LU used taryr')
            
            ax1.legend(loc='center', bbox_to_anchor=(1.3, .5))
            ax1.set_ylabel('emissions / Mt CO2eq', fontweight='bold')
            ax1.set_title(f"{iso3}: negative IPC0 target")
            fig.subplots_adjust(left=.2, right=.7)
            path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_negative_tar_ipc0', f'{iso3}_negative_tar_inclLU.png')
            plt.savefig(path_to_png, dpi=300)
            plt.clf()

plt.close(fig)

# %%
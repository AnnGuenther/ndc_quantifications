# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

meta = setup_metadata()

# %%
"""
BWA
"""

# Given 2010 emissions: 8307 Gg CO2eq.
# Given reduction: 15%.
emi_2010 = 8.307
print(f"Target emissions: {emi_2010 * (1-.15) :.3f} MtCO2eq")

# Not sure which part of emissions this stands for.
primap_kyoto_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['BWA', 2010]
print(f"PRIMAP-hist vs. given 2010 emissions: {primap_kyoto_ipcm0el} (KYOTOGHG_IPCM0EL) vs. {emi_2010} MtCO2eq")

primap_kyoto_ipc1 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPC1_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['BWA', 2010]
print(f"PRIMAP-hist vs. given 2010 emissions: {primap_kyoto_ipc1} (KYOTOGHG_IPC1) vs. {emi_2010} MtCO2eq")

sum_cov = 0
for combi_cov in ['CO2_IPC1', 'CO2_IPCMAG', 'CO2_IPC4',
                  'CH4_IPC1', 'CH4_IPCMAG', 'CH4_IPC4',
                  'N2O_IPC1', 'N2O_IPCMAG', 'N2O_IPC4']:
    try:
        sum_cov += hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'{combi_cov}_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        data.loc['BWA', 2010]
    except:
        sum_cov += 0

print(f"Sum over covered gas+sector-combis in 2010: {sum_cov :.3f} MtCO2eq")

# %%

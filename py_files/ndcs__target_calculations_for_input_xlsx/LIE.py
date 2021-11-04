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
LIE
"""

# ABS.
# From RBY and 1990 emissions.
emi_1990 = 0.2287
print(f"ABS 2030 IPC0: {emi_1990 * (1-.4) :.6f} MtCO2eq")

# Is the given value IPC0 or IPCM0EL?
primap_kyoto_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['LIE', 1990]
print(f"PRIMAP-hist vs. given 1990 emissions: {primap_kyoto_ipcm0el :.3f} (KYOTOGHG_IPCM0EL) vs. {emi_1990} MtCO2eq")

primap_kyoto_ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')). \
    data.loc['LIE', 1990]
print(f"PRIMAP-hist KYOTOGHG_IPCM0EL + KYOTOGHG_IPCMLULUCF = {primap_kyoto_ipcm0el + primap_kyoto_ipcmlulucf :.3f} MtCO2eq")

# %%

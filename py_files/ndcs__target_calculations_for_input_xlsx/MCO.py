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
MCO
"""

emi_1990 = .11 # MtCO2eq
red = -.5
print(f"ABS: {emi_1990*(1+red)} MtCO2eq")

# Which share did the F-gases represent in 1990 / 1995?
fgases = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'FGASES_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['MCO', [1990, 1995]]
kyotoghg = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['MCO', [1990, 1995]]
print(f"Share of F-gases (FGASES_IPCM0EL vs. KYOTOGHG_IPCM0EL):\n{100. * fgases / kyotoghg}")

# %%

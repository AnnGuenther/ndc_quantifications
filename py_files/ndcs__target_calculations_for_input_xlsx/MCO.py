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
# NDC2020

emi_onlyLU = {1990: 0, 2018: -0.00002}
emi_exclLU = {1990: 0.10274, 2018: 0.08693}
for year in [1990, 2018]:
    print(f"{year} onlyLU: {hpf.rnd(emi_onlyLU[year]+emi_exclLU[year], 5)} MtCO2eq")

tar_rby = -.55
tar_abs_inclLU = (emi_exclLU[1990] + emi_onlyLU[1990]) * (1+tar_rby)
tar_abs_exclLU = (emi_exclLU[1990]) * (1+tar_rby)
print(f"ABS inclLU: {hpf.rnd(tar_abs_inclLU, 5)} MtCO2eq")
print(f"ABS exclLU: {hpf.rnd(tar_abs_exclLU, 5)} MtCO2eq")

# %%
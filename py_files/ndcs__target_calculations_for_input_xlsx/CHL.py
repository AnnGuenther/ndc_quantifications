# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
from pathlib import Path
import pandas as pd
from copy import deepcopy
import helpers_functions as hpf
from setup_metadata import setup_metadata

meta = setup_metadata()

# %%
"""
CHL
"""

emi_ipcm0el = pd.Series(index=range(2017, 2031), dtype='float64')
emi_ipcm0el[2017] = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['CHL', 2017]
emi_ipcm0el[2030] = 95 # 2030: absolute target
emi_cumulative_2020_2030 = 1100 # MtCO2eq, p. 17.

print(f"Emissions in 2017: {emi_ipcm0el[2017]} MtCO2eq")
for emi_2025 in [95, 99, 100, 105, 110]:
    emi_ts = deepcopy(emi_ipcm0el)
    emi_ts[2025] = emi_2025
    emi_ts = emi_ts.interpolate()
    emi_tot = emi_ts[list(range(2020, 2031))].sum()
    print(f"Assumed emissions in 2025: {emi_2025}, resulting / allowed cumulative emissions: {emi_tot :.0f} / {emi_cumulative_2020_2030}")

# %%

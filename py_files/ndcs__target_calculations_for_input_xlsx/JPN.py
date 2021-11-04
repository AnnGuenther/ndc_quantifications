# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
JPN
"""

# For 2030 these are mitigated values.
emi_tot = {
    'energy_co2': {2013: 1235, 2005: 1219},
    'non_energy_co2': {2013: 75.9, 2005: 85.4},
    'methane': {2013: 36.0, 2005: 39.0},
    'n2o': {2013: 22.5, 2005: 25.5},
    'fgases': {2013: 38.6, 2005: 27.7}}

for yr in [2005, 2013]:
    emi_yr = sum([emi_tot[xx][yr] for xx in emi_tot.keys()])
    print(f"Total emissions (exclLU) {yr}: {emi_yr :.1f} MtCO2eq")

# p. 8-9:
emi_tar_2030 = {'energy_co2': 927, 'non_energy_co2': 70.8, 'methane': 31.6, 'n2o': 21.1, 'fgases': 28.9}
RBU_per_gas = {'energy_co2': -.25, 'non_energy_co2': -.067, 'methane': -.123, 'n2o': -.061, 'fgases': -.251}
yr = 2030
ABS_2030 = sum([emi_tar_2030[xx] for xx in emi_tar_2030.keys()])
print(f"Mitigated emissions (exclLU) {yr}: {ABS_2030 :.1f} MtCO2eq")

emi_inclLU = ABS_2030 - 36.9 # P. 10.
# 36.9 MtCO2eq is target for removals.
print(f"Target inclLU: {emi_inclLU :.1f} MtCO2eq")

# %%
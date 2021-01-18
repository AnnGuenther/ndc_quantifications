# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MNG
"""

# %%
# NDC2016

# ABS
emi_bau = 51.2 # MtCO2eq
ABU = -7.3
print(f"ABS: {emi_bau + ABU :.1f} MtCO2eq")

# %%
# NDC2020

# Figure 1, p. 1
# exclLU (p. 2)
bau_exclLU = {2010: 25.8, 2015: 37.6, 2020: 49.1, 2025: 62.5, 2030: 74.3} # MtCO2eq
miti_exclLU = {2020: 44.9, 2025: 52.3, 2030: 57.4}
tars_exclLU_abu = {}
tars_exclLU_rbu = {}
for year in miti_exclLU.keys():
    tars_exclLU_abu[year] = miti_exclLU[year] - bau_exclLU[year]
    tars_exclLU_rbu[year] = 100 * tars_exclLU_abu[year] / bau_exclLU[year]
    print(f"ABU exclLU {year}: {hpf.rnd(tars_exclLU_abu[year], 1)} MtCO2eq")
    print(f"RBU exclLU {year}: {hpf.rnd(tars_exclLU_rbu[year], 1)}%")

# p. 4: forestry removals: -2.6 MtCO2eq
# not clear which year. assuming it to be constant ...
onlyLU = -2.6
for year in [2010, 2030]:
    print(f"BAU inclLU {year}: {hpf.rnd(bau_exclLU[year] + onlyLU, 1)} MtCO2eq")

abu_condi_exclLU = -20.2 # 16.9 + 3.3
abs_condi_exclLU = bau_exclLU[2030] + abu_condi_exclLU
print(f"ABS condi exclLU 2030: {hpf.rnd(abs_condi_exclLU, 1)} MtCO2eq")

abu_condi_inclLU = -39.7 # 16.9 + 3.3 + 19.5 (not sure)
abs_condi_inclLU = bau_exclLU[2030] + onlyLU + abu_condi_inclLU
print(f"ABS condi inclLU 2030: {hpf.rnd(abs_condi_inclLU, 1)} MtCO2eq")

# %%
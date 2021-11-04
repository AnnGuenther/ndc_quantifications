# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
print('AFG')

# All in MtCO2eq_SAR.

# Table 1.
emi_exclLU = {2025: 41.67295, 2030: 48.93954}
emi_inclLU = {2025: 53.18064, 2030: 61.03425}
lulucf = {2025: 11.50770, 2030: 12.09471}

# ABS.

# From Figure 1.
tar_abs_exclLU = {2025: 40.3, 2030: 42.7}

# LU is not covered.
tar_abs_inclLU = {}
for year in [2025, 2030]:
    tar_abs_inclLU[year] = tar_abs_exclLU[year] + lulucf[year]
    print(f"ABS {year}: {tar_abs_inclLU[year] :.6f} MtCO2eq")

# ABU and RBU.

print("\nexclLU")
for year in [2025, 2030]:
    tar_abu_exclLU = tar_abs_exclLU[year] - emi_exclLU[year]
    print(f"ABU {year}: {tar_abu_exclLU :.6f} MtCO2eq")
    print(f"RBU: {tar_abu_exclLU/emi_exclLU[year]*100. :.1f}%")

print("\ninclLU")
for year in [2025, 2030]:
    tar_abu_inclLU = tar_abs_inclLU[year] - emi_inclLU[year]
    print(f"ABU {year}: {tar_abu_inclLU :.6f} MtCO2eq")
    print(f"RBU: {tar_abu_inclLU/emi_inclLU[year]*100. :.1f}%")

# %%
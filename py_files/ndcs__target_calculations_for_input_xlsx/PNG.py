# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last update: 2/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
PNG
"""

# %%
# NDC2020

onlyLU = {2000: -21.654, 2015: 1.716} # p. 22
inclLU = {2000: -14.179, 2015: 15.193} # p. 18
for year in [2000, 2015]:
    print(f"exclLU {year}: {hpf.rnd(inclLU[year] - onlyLU[year], 3)} MtCO2eq")

# LULUCF target: reduction of 10.000 MtCO2eq by 2030 compared to 2015 levels.
# We do not have ABY targets implemented currently (absolute reduction compared to base year).
# Recalculate the values:
aby = -10.000
onlyLU_2015 = 1.716
onlyLU_2030 = -8.284
rby = aby*100/onlyLU_2015
print(f"RBY onlyLU: {hpf.rnd(rby, 1)}%")
print(f"Test: given onlyLU_2030 is {onlyLU_2030}. "
    f"Equals value calculated based on 2015 emissions and RBY ({onlyLU_2015*(1+rby/100)} MtCO2eq)?")

# %%
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
ARM
"""

# %%
# INDC2015

# 633 MtCO2eq for 2015 to 2050.
# Annual average.
print(f"Annual average {633/len(range(2015, 2051)) :.3f} MtCO2eq")
print(f"Total for 2015 to 2050: {5.4*3.35e6*len(range(2015, 2051))}") 
# They give 633e6, that is close enough. I think that 2015 to 2050 is one year too much.

# %%
# NDC2021

emi_1990_inclLU = 25.118 # MtCO2eq, p. 3
emi_1990_exclLU = 25.885 # p. 3
emi_1990_onlyLU = emi_1990_inclLU - emi_1990_exclLU
print(f"EMI 1990 onlyLU: {hpf.rnd(emi_1990_onlyLU, 3)} MtCO2eq")

emi_2017_inclLU = 10.180 # MtCO2eq, p. 7
emi_2017_exclLU = 10.624 # p. 7
emi_2017_onlyLU = emi_2017_inclLU - emi_2017_exclLU
print(f"EMI 2017 onlyLU: {hpf.rnd(emi_2017_onlyLU, 3)} MtCO2eq")

rby = -.4
abs_inclLU = emi_1990_exclLU * (1+rby) + emi_1990_onlyLU
# TODO: check the target calculation regarding LULUCF!
print(f"ABS inclLU: {hpf.rnd(abs_inclLU, 3)} MtCO2eq")

# %%
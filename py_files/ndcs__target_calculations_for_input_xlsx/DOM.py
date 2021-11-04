# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
DOM
"""

# %%
# NDC2015

emi_2010 = 3.6 # tCO2eq per capita, p. 2
REI = -.25

print(f"AEI: {emi_2010 * (1+REI) :.1f} tCO2eq/capita")

# %%
# NDC2020

bau = 51 # MtCO2eq, p. 7

rbu_uncondi = -.07
rbu_condi = -.2716

abs_uncondi = bau * (1 + rbu_uncondi)
abs_condi = bau * (1 + rbu_condi)

abu_uncondi = abs_uncondi - bau
abu_condi = abs_condi - bau

print(f"\nABS uncondi: {hpf.rnd(abs_uncondi, 3)} MtCO2eq")
print(f"ABS condi: {hpf.rnd(abs_condi, 3)} MtCO2eq")

print(f"\nABU uncondi: {hpf.rnd(abu_uncondi, 3)} MtCO2eq")
print(f"ABU condi: {hpf.rnd(abu_condi, 3)} MtCO2eq")

# Given on p. 5: ABU = -13,853.71 Gg CO2eq 

# %%
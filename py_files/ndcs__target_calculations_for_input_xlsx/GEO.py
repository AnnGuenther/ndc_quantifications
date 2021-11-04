# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
GEO
"""

# %%
# NDC2017

bau_2030 = 38.42 # MtCO2eq
ABS = {'uncondi': 32.66, 'condi': 28.31} # MtCO2eq

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - bau_2030 :.2f} MtCO2eq")

# %%
# NDC2021

# 2015 emissions are 39% of 1990 emissions.
emi_2015 = 18.214 # MtCO2eq
emi_1990 = 100/39*emi_2015
print(f"EMI 1990: {hpf.rnd(emi_1990, 3)} MtCO2eq")

rby_uncondi = -.35
rby_condi_worst = -.5
rby_condi_best = -.57

abs_uncondi = emi_1990 * (1+rby_uncondi)
abs_condi_worst = emi_1990 * (1+rby_condi_worst)
abs_condi_best = emi_1990 * (1+rby_condi_best)

print(f"ABS uncondi: {hpf.rnd(abs_uncondi, 3)} MtCO2eq")
print(f"ABS condi worst: {hpf.rnd(abs_condi_worst, 3)} MtCO2eq")
print(f"ABS condi best: {hpf.rnd(abs_condi_best, 3)} MtCO2eq")

# %%

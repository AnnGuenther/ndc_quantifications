# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MDA
"""

# %%
# NDC2017

# p. 5., emi 1990 (base year).
ipcmlulucf = -5.8866 # MtCO2eq
ipc0 = 37.5322
ipcm0el = 43.4188

RBY = {'uncondi_worst': -.64, 'uncondi_best': -.67, 'condi': -.78}
# LULUCF is sink in base year.
for condi in RBY.keys():
    ABS_exclLU = ipcm0el * (1+RBY[condi])
    ABS_onlyLU = ipcmlulucf
    print(f"{condi} ABS_inclLU: {ABS_exclLU + ABS_onlyLU :.4f} MtCO2eq")

# %%
# NDC2020

# [p. 3] "Total Emissions in the Base Year (NDC2): 44.9 Mt (without LULUCF) 
# and 43.4 Mt (with LULUCF)."
# [p. 3] AR4
emi_inclLU = 43.391 # In Table on p. 10
rby_uncondi = -.7 # p. 3
rby_condi = -.88 # p. 3

abs_uncondi = emi_inclLU * (1 + rby_uncondi)
abs_condi = emi_inclLU * (1 + rby_condi)
print(f"ABS uncondi: {hpf.rnd(abs_uncondi, 1)} MtCO2eq_AR4")
print(f"ABS condi: {hpf.rnd(abs_condi, 1)} MtCO2eq_AR4")

# %%
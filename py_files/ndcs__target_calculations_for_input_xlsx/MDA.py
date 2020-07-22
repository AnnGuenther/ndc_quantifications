# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MDA
"""

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

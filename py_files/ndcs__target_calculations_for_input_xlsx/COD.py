# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
COD
"""

emi_bau_inclLU = 430 # MtCO2eq
red_inclLU = -70 # MtCO2eq
tar_inclLU = emi_bau_inclLU+red_inclLU
print(f"ABS IPC0: {tar_inclLU} MtCO2eq")

emi_bau_onlyLU = 400
tar_onlyLU = 290 # Read from figure 2
red_onlyLU = tar_onlyLU - emi_bau_onlyLU
red_exclLU = red_inclLU - red_onlyLU
print(f"The reduction ABU of onlyLU is {red_onlyLU} MtCO2eq, while the reduction inclLU is {red_inclLU} MtCO2eq")
print(f"So the ABU exclLU 'reduction' is {red_exclLU} MtCO2eq")

emi_bau_exclLU = emi_bau_inclLU - emi_bau_onlyLU
tar_exclLU = emi_bau_exclLU + red_exclLU
print(f"ABS IPCM0EL: {tar_exclLU} MtCO2eq")
print(f"RBU IPCM0EL: {red_exclLU / emi_bau_exclLU * 100. - 100. :.0f}%")

# %%

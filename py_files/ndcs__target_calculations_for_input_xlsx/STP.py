# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
STP
"""

# ABS.
# From given BAU and absolute reduction [p. 7].
emi_ipcm0el = 0.240 # MtCO2eq
emi_red = -0.057
print(f"ABS 2030 IPCM0EL: {emi_ipcm0el + emi_red} MtCO2eq")

emi_lulucf = -0.630
emi_ipc0 = emi_ipcm0el + emi_lulucf
print(f"EMI IPC0: {emi_ipc0} MtCO2eq")

print(f"ABS 2030 IPC0: {emi_ipc0 + emi_red} MtCO2eq")

# %%

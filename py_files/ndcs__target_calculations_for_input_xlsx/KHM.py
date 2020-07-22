# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
KHM
"""

# EMI IPCM0EL from data given on p. 5.
ipcm0el = 11.600
ipcmlulucf = -7.897
ipc0 = ipcm0el + ipcmlulucf

emi_exclLU = ipc0 - ipcmlulucf
print(f"EMI IPCM0EL 2030: {emi_exclLU :.6f} MtCO2eq")

ABU_ipcm0el = -3.100 # MtCO2eq, this is compared to BAU.
ABU_lulucf = 7.897 - 18.492 # This is compared to 2010, not to BAU! We ignore that...
ABU_ipc0 = ABU_ipcm0el + ABU_lulucf
print(f"ABU IPC0: {ABU_ipc0} MtCO2eq")

# %%

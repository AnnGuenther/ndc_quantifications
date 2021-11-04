# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
GAB
"""

# p. 3, first figure
emi_ipcm0el = 1.431 + 3.870 + 0.090 + 0.408 + 0.363
emi_ipcmlulucf = 10.613 - 74.767
emi_ipc0 = emi_ipcm0el + emi_ipcmlulucf
print(f"ipcm0el: {emi_ipcm0el :.3f} MtCO2eq")
print(f"ipc0: {emi_ipc0 :.3f} MtCO2eq")
print(f"ipcmlulucf: {emi_ipcmlulucf :.3f} MtCO2eq")

# %%

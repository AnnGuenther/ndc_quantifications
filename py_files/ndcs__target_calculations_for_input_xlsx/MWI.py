# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import numpy as np

# %%
"""
MWI
"""

emi_bau = {2015: 28.000, 2040: 42.000} # MtCO2eq, p. 3.
yr_interp = 2030
emi_bau[yr_interp] = np.interp(yr_interp, list(emi_bau.keys()), list(emi_bau.values()))
print(f"emi BAU {yr_interp}: {emi_bau[yr_interp] :.3f} MtCO2eq (linear interpolation)")

emi_LULUCF_2015 = 9.9 # MtCO2eq, p. 3.
emi_ipcm0el_2015 = emi_bau[2015] - emi_LULUCF_2015
print(f"emi IPCM0EL 2015: {emi_ipcm0el_2015 :.3f} MtCO2eq")

ABU = {'worst': -14.000, 'best': -16.000}
for rge in ABU.keys():
    print(f"ABS IPC0 {rge} (calculated from linear interpolation of BAU): {emi_bau[2030]+ABU[rge]} MtCO2eq")
    print(f"RBU IPC0 {rge}: {100*ABU[rge]/emi_bau[2030] :.1f}%")

# %%

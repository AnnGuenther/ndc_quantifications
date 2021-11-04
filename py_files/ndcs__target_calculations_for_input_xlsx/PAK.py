# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
PAK
"""

# p. 21 + p. 26, emissions per sector
ipc0 = {1994: 181.7, 2008: 329.51, 2012: 374.10, 2015: 405.07, 2030: 1603}
ipcmlulucf = {1994: 6.52, 2008: 9.29, 2012: 9.67, 2015: 10.39, 2030: 29}
ipcm0el = {}
for yr in ipc0.keys():
    ipcm0el[yr] = ipc0[yr] - ipcmlulucf[yr]
    print(f"{yr}: {ipcm0el[yr] :.2f} MtCO2eq")

# Target. LULUCF is source.
RBU = -.2
yr = 2030
tar_exclLU = ipcm0el[yr]*(1+RBU)
tar_onlyLU = ipcmlulucf[yr]*(1+RBU)
tar_inclLU = tar_exclLU + tar_onlyLU
print(f"Target inclLU: {tar_inclLU} MtCO2eq")
print(f"ABU inclLU: {tar_inclLU - ipc0[yr] :.2f} MtCO2eq")

# %%

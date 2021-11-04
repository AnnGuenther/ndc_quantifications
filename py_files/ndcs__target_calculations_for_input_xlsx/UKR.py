# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
UKR
"""

# IPCMLULUCF from given IPC0 and IPCM0EL [p. 1].
ipc0 = {1990: 874.6, 2012: 375.4}
ipcm0el = {1990: 944.4, 2012: 402.7}

for year in ipcm0el.keys():
    print(f"IPCMLULUCF {year}: {ipc0[year] - ipcm0el[year] :.3f} MtCO2eq")

# ABS.
# Calculated based on given baseyear emissions and % reduction.
ipcm0el = 944.4
ipc0 = 874.6
ipcmlulucf = -69.8
pc_red = -.4
pc_lev = 1 + pc_red
# Do not strengthen the sink.

# LULUCF is a sink in the base year. Everything is covered.
print(f"ABS IPC0: {ipcm0el*pc_lev + ipcmlulucf} MtCO2eq_AR4")

# %%

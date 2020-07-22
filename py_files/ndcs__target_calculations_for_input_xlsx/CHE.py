# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
CHE
"""

ipcm0el_1990 = 53.3
red = {'best': {2025: -.35, 2030: -.5, 2050: -.85}, 'worst': {2050: -.7}}

for rge in red.keys():
    data = red[rge]
    for year in data.keys():
        print(f"{rge} {year}: {ipcm0el_1990 * (1 + data[year]) :.3f}")

# %%

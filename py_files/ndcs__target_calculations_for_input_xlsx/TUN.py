# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TUN
"""

# ABU from given baseline and ABS.
ABS = {
    'unconditional': {2025: 47.4, 2030: 62.2}, 
    'conditional': {2025: 35.0, 2030: 42.4}}
BL = {2025: 51.6, 2030: 68.2}

for condi in ABS.keys():
    data = ABS[condi]
    for year in data.keys():
        ABU = data[year] - BL[year]
        print(f"ABU {condi} {year}: {ABU :.3f} MtCO2eq_AR4")
        print(f"RBU {condi} {year}: {ABU/BL[year]*100 :.1f}%")

# %%

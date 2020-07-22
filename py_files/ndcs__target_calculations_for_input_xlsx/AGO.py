# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
AGO
"""
bau = {2025: 155.819, 2030: 193.250}
ABS = {2025: {'uncondi': 124.656, 'condi': 113.748},
       2030: {'uncondi': 125.612, 'condi': 96.625}}
for year in bau.keys():
    for condi in ABS[year].keys():
        print(f"{year} {condi}: {ABS[year][condi] - bau[year] :.3f} MtCO2eq")

# %%
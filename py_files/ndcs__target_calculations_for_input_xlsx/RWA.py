# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
RWA
"""

# Sum over given reductions.
red = {'transport': 1.260, 'industry': 0.146, 'waste': 0.586, 'forestry': 5.770} # MtCO2eq

red_sum = sum([red[xx] for xx in red.keys()])    
print(f"Total reduction: {red_sum} MtCO2eq")
# Not clear if it is per year or over a period of time.
# We assume it to be over the period 2021-2030.
print(f"per year: {red_sum/10} MtCO2eq")

# %%

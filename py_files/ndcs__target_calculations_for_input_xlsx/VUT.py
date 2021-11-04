# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Updated 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
# NDC2021

# p. 6
energy = 122.44 # Gg CO2eq
IPPU = 0 
AFOLU = 587.48
waste = 10.75

print(hpf.rnd(sum([energy, IPPU, AFOLU, waste]), 2), 'GgCO2eq')
# Not the same as "net GHG emissions (excluding removals)" given on p. 5: 728.359 GgCO2eq
# What are net GHG emissions (excluding removals)?

abu = 78.786 + 30.977 + 29.335 # p. 3-5
print(hpf.rnd(-abu, 3), 'GgCO2eq')

# %%


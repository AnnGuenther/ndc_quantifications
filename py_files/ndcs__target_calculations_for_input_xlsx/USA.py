# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
USA
"""

# %%
# NDC2016

RBY = {'worst': -.26, 'best': -.28}
emi2005_inclLU = 6200 # MtCO2eq, read from figure, p. 1.
for rge in RBY.keys():
   print(f"ABS inclLU {rge}: {emi2005_inclLU * (1+RBY[rge]) :.0f} MtCO2eq.") 

# %%
# NDC2021

emi2005_inclLU = 6635 # MtCO2eq, p. 8, AR5?
RBY = {'worst': -.5, 'best': -.52}
for rge in RBY.keys():
    print(f"ABS inclLU {rge}: {hpf.rnd(emi2005_inclLU * (1+RBY[rge]), 0)} MtCO2eq AR5")

# %%
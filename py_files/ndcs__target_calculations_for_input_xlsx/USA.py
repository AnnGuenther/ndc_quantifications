# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
USA
"""

RBY = {'worst': -.26, 'best': -.28}
emi2005_inclLU = 6200 # MtCO2eq, read from figure, p. 1.
for rge in RBY.keys():
   print(f"ABS inclLU {rge}: {emi2005_inclLU * (1+RBY[rge]) :.0f} MtCO2eq.") 


# %%

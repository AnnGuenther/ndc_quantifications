# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
NOR
"""

# ABS.
# From base year emissions and % reductions.
base = 52 # MtCO2eq
red_best = -.55
red_worst = -.50

ABS_best = base * (1+red_best)
ABS_worst = base * (1+red_worst)
print(f"ABS best: {ABS_best} MtCO2eq")
print(f"ABS worst: {ABS_worst} MtCO2eq")

print(f"ABY best: {ABS_best - base} MtCO2eq")
print(f"ABY worst: {ABS_worst - base} MtCO2eq")

# %%
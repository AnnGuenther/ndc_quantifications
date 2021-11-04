# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
LBN
"""

# %%
# NDC2015

# ABS.
emi_bau = 43.5 # MtCO2eq
red = {'uncondi': -.15, 'condi': -.3}

for condi in red.keys():
    ABS = emi_bau * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_bau :.3f} MtCO2eq")

# %%
# NDC2021

emi_bau = 38.950 # MtCO2eq_AR5, p. 18
abu = {'uncondi': -7.790, 'condi': -12.075} # p. 10

for condi in abu.keys():
    
    abs_2030 = hpf.rnd(emi_bau + abu[condi], 3)
    print(f"ABS {condi}: {abs_2030} MtCO2eq_AR5")

# %%
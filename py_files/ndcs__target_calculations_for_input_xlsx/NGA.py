# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
NGA
"""

RBU = {'uncondi': -.2, 'condi': -.45}
bau = 900 # MtCO2eq

for condi in RBU.keys():
    print(f"ABU {condi}: {bau * RBU[condi] :.1f} MtCO2eq")
    print(f"ABS {condi}: {bau * (1+RBU[condi]) :.1f} MtCO2eq")

# %%

# NDC2021

RBU = {'uncondi': -.2, 'condi': -.45}
bau = 453 # MtCO2eq

for condi in RBU.keys():
    print(f"ABU {condi}: {bau * RBU[condi] :.1f} MtCO2eq")
    print(f"ABS {condi}: {bau * (1+RBU[condi]) :.1f} MtCO2eq")

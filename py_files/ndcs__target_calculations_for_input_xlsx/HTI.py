# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
HTI
"""

bau = 20.7 # MtCO2eq
RBU = {'uncondi': -.05, 'condi': -.31}

for condi in RBU.keys():
    print(f"ABS {condi}: {bau*(1+RBU[condi]) :.1f} MtCO2eq")
    print(f"ABU {condi}: {bau*RBU[condi] :.1f} MtCO2eq")

# %%

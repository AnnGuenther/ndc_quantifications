# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
NER
"""

bau = 96.468 # MtCO2eq
RBU = {'uncondi': -.035, 'condi': -.346}

for condi in RBU.keys():
    print(f"ABU {condi}: {bau*RBU[condi] :.3f} MtCO2eq")
    print(f"ABS {condi}: {bau*(1+RBU[condi]) :.3f} MtCO2eq")

# %%

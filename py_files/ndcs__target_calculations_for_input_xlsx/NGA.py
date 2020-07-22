# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

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

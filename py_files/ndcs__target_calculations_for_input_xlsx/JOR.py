# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
JOR
"""

bau = 51.028 # MtCO2eq
RBU = {'uncondi': -.015, 'condi': -.14}

for condi in RBU.keys():
    print(f"\nABS {condi}: {bau * (1+RBU[condi]) :.3f} MtCO2eq")
    print(f"ABU {condi}: {bau * RBU[condi] :.3f} MtCO2eq")

# %%

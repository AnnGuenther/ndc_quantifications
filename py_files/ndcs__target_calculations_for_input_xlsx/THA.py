# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
THA
"""

emi_bau = 555 # MtCO2eq, p. 2.
RBU = {'uncondi': -.2, 'condi': -.25}

for condi in RBU.keys():
    print(f"{condi} ABS: {emi_bau * (1+RBU[condi]) :.0f} MtCO2eq")
    print(f"{condi} ABU: {emi_bau * RBU[condi] :.0f} MtCO2eq")

# %%
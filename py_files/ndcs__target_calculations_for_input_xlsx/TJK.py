# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TJK
"""

# ABS.
emi_1990 = 25.5 # MtCO2eq
red = {'uncondi_worst': -.1, 'uncondi_best': -.2, 'condi_worst': -.25, 'condi_best': -.35}
for tar in red.keys():
    print(f"{tar}: {emi_1990 * (1 + red[tar]) :.3f} MtCO2eq")

# %%

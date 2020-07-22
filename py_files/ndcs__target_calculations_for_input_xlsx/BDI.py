# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BDI
"""

# p. 8
year = 2025
print(f"{year}")
RBU = {'uncondi': -.02, 'condi': -.17}
ABU = {'uncondi': -1.305, 'condi': -9.897}

for condi in RBU.keys():
    print(f"BAU {condi} {year}: {1/RBU[condi]*ABU[condi] :.3f} MtCO2eq")

bau_chosen = 58.218 # from condi
ABU['uncondi'] = bau_chosen * RBU['uncondi']
print(f"ABU uncondi new {year}: {ABU['uncondi'] :.3f} MtCO2eq")

for condi in RBU.keys():
    print(f"ABS {condi} {year}: {bau_chosen * (1+RBU[condi]) :.3f} MtCO2eq")

year = 2030
print(f"\n{year}")
RBU = {'uncondi': -.03, 'condi': -.20} # p. 8
ABU = {'uncondi': -1.958, 'condi': -14.897} # MtCO2eq, p. 8

for condi in RBU.keys():
    print(f"BAU {condi} {year}: {1/RBU[condi]*ABU[condi] :.3f} MtCO2eq")

bau_chosen = 74.485 # MtCO2eq (from condi)
ABU['uncondi'] = bau_chosen * RBU['uncondi']
print(f"ABU uncondi new {year}: {ABU['uncondi'] :.3f} MtCO2eq")

for condi in RBU.keys():
    print(f"ABS {condi} {year}: {bau_chosen * (1+RBU[condi]) :.3f} MtCO2eq")

# %%

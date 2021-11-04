# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
VNM
"""

# %%
# NDC2016

emi_bau = 787.4 # MtCO2eq
red = {'uncondi': -.08, 'condi': -.25}

for condi in red.keys():
    ABU = emi_bau * red[condi]
    print(f"ABU {condi}: {ABU} MtCO2eq")
    print(f"ABS {condi}: {emi_bau + ABU} MtCO2eq")

# %%
# NDC2020

# p. 12, Table 1

years = [2014, 2020, 2025, 2030]
emi_inclLU = [284.0, 528.4, 726.2, 927.9]
emi_onlyLU = [-37.5, -35.4, -37.9, -49.2]
txt = '{"EMI": {"inclLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{hpf.rnd(emi_inclLU[count], 1)} MtCO2eq_AR4"' + \
        (', ' if count < len(years)-1 else '}}')
txt += ', "onlyLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{hpf.rnd(emi_onlyLU[count], 1)} MtCO2eq_AR4"' + \
        (', ' if count < len(years)-1 else '}}')
txt += ', "exclLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{hpf.rnd(emi_inclLU[count] - emi_onlyLU[count], 1)} MtCO2eq_AR4"' + \
        (', ' if count < len(years)-1 else '}}')
txt += '}'
print(txt)

# 2030 targets exclLU, from Table 3 on p. 15
onlyLU_2030 = -49.2 # from above
inclLU_2030 = 927.9 # from above
exclLU_2030 = inclLU_2030 - onlyLU_2030
abu_exclLU = {'uncondi': -(51.5 + 6.8 + 9.1 + 7.2), 'condi': -(155.8 + 32.6 + 33.1 + 8.0)} # increase in GHGs sequestration, MtCO2eq
abu_inclLU = {'uncondi': -83.9, 'condi': -250.8}

for condi in abu_exclLU.keys():
    print(f"\n{condi}")
    
    abs_inclLU = inclLU_2030 + abu_inclLU[condi]
    print(f"\nABS inclLU: {hpf.rnd(abs_inclLU, 1)} MtCO2eq")
    abs_exclLU = exclLU_2030 + abu_exclLU[condi]
    print(f"ABS exclLU: {hpf.rnd(abs_exclLU, 1)} MtCO2eq")
    
    print(f"\nABU inclLU: {hpf.rnd(abu_inclLU[condi], 1)} MtCO2eq")
    print(f"ABU exclLU: {hpf.rnd(abu_exclLU[condi], 1)} MtCO2eq")
    
    print(f"\nRBU inclLU: {hpf.rnd(100*abu_inclLU[condi]/inclLU_2030, 0)}%")
    print(f"RBU exclLU: {hpf.rnd(100*abu_exclLU[condi]/exclLU_2030, 0)}%")

# %%
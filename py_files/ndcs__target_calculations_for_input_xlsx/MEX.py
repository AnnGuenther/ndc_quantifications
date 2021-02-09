# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MEX
"""

# %%
# NDC2016

# ABS.
emi_2030 = 973 # MtCO2eq
red = {'uncondi': -.22, 'condi': -.36}

for condi in red.keys():
    ABS = emi_2030 * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_2030 :.3f} MtCO2eq")

# %%
# NDC2020
emi_2030 = 991 # MtCO2eq, this includes the LUCF emissions (not absorption)
red = {'uncondi': -.22, 'condi': -.36}

for condi in red.keys():
    ABS = emi_2030 * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_2030 :.3f} MtCO2eq")

# p. 29: table with emissions per sector.
years = [2013, 2020, 2025, 2030]
emi_gross = [709, 804, 902, 991]
emi_lucf_emi = [21, 36, 42, 49]
emi_lucf_abs = [-169, -163, -161, -158]
emi_inclLU = []
emi_exclLU = []
emi_onlyLU = []
for year, count in zip(years, range(len(years))):
    emi_inclLU += [emi_gross[count] + emi_lucf_abs[count]]
    emi_exclLU += [emi_gross[count] - emi_lucf_emi[count]]
    emi_onlyLU += [emi_lucf_emi[count] + emi_lucf_abs[count]]

txt = '{"EMI": {"onlyLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{emi_onlyLU[count]} MtCO2eq"' + \
        (', ' if count < len(years)-1 else '}}')
txt += ', "inclLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{emi_inclLU[count]} MtCO2eq"' + \
        (', ' if count < len(years)-1 else '}}')
txt += ', "exclLU": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{emi_exclLU[count]} MtCO2eq"' + \
        (', ' if count < len(years)-1 else '}}')
txt += ', "gross": {'
for year, count in zip(years, range(len(years))):
    txt += f'"{year}": "{emi_gross[count]} MtCO2eq"' + \
        (', ' if count < len(years)-1 else '}}')
txt += '}'
print('\n' + txt)

# Recalculate the targets.
# p. 5
# "Unconditional contributions: Consist of, alternatively: Reduction of 22% of greenhouse gas emissions (GHG) 
# and 51% of black carbon emissions by 2030 as compared to the baseline business-asusual scenario (BAU). 
# Conditional contributions: A reduction of up to 36% of GHG emissions and 
# 70% of black carbon emissions by 2030 compared to the BAU scenario."
# p. 22
# "The projected BAU scenario to 2030, without any mitigation policy intervention, was quantified at 991 MtCO2e.
# The reduction of unconditional emissions by 2030 translates into a reduction of approximately 210 MtCO2e that year, 
# while compliance with conditional commitments would imply reductions of an additional 137 MtCO2e."
bau_2030_gross = 991 # p. 29
bau_2030_onlyLU = 49 - 158
bau_2030_exclLU = 250 + 186 + 199 + 122 + 101 + 56 + 28
bau_2030_inclLU = bau_2030_onlyLU + bau_2030_exclLU
print(f"\nBAU 2030 inclLU: {hpf.rnd(bau_2030_inclLU, 0)} MtCO2eq")

abu_uncondi_inclLU = -210
abu_condi_inclLU = abu_uncondi_inclLU + -137
print(f"\nABU uncondi inclLU: {hpf.rnd(abu_uncondi_inclLU, 0)} MtCO2eq")
print(f"ABU condi inclLU: {hpf.rnd(abu_condi_inclLU, 0)} MtCO2eq")

# Use the given abu and the bau_2030_inclLU to recalculate ABS and RBU.
# ABU stays the same.
abs_uncondi_inclLU = bau_2030_inclLU + abu_uncondi_inclLU
abs_condi_inclLU = bau_2030_inclLU + abu_condi_inclLU
print(f"\nABS uncondi inclLU: {hpf.rnd(abs_uncondi_inclLU, 0)} MtCO2eq")
print(f"ABS condi inclLU: {hpf.rnd(abs_condi_inclLU, 0)} MtCO2eq")

rbu_uncondi_inclLU = 100 * abu_uncondi_inclLU / bau_2030_inclLU
rbu_condi_inclLU = 100 * abu_condi_inclLU / bau_2030_inclLU
print(f"\nRBU uncondi inclLU: {hpf.rnd(rbu_uncondi_inclLU, 0)}%")
print(f"RBU condi inclLU: {hpf.rnd(rbu_condi_inclLU, 0)}%")

# %%
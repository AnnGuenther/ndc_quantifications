# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

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

# %%
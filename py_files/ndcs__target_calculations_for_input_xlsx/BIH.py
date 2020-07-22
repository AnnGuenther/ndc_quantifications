# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BIH
"""

# Baseline emissions: 20% higher in 2030 than in 2020. And same in 2020 as in 1990.
emi_exclLU_1990 = 34.04349 # [p. 2]
emi_inclLU_1990 = 26.61996 # [p. 2]
emi_LU_1990 = -7.423 # [p. 5] is same as emi_inclLU_1990 - emi_exclLU_1990
# But it might also only be the part that is a sink, the forestry emissions
# might be included in emi_exclLU_1990 ...
emi_exclLU_2030 = 1.2 * emi_exclLU_1990
emi_LU_2015 = -6.470 # [p. 5]: projected intention to keep LULUCF at that level.

emi_exclLU = {
    1990: emi_exclLU_1990,
    2020: emi_exclLU_1990,
    2030: emi_exclLU_2030}
emi_inclLU = {
    1990: emi_inclLU_1990,
    2020: emi_exclLU[2020] + emi_LU_2015,
    2030: emi_exclLU[2030] + emi_LU_2015}

for year in emi_inclLU.keys():
    print(f"IPC0 {year}: {emi_inclLU[year] :.6f}")

print("\nBased on base year emissions and RBY.")
RBY = {'uncondi': +.18, 'condi': -.03}
for condi in RBY.keys():
    ABS_exclLU = emi_exclLU_1990 * (1+RBY[condi])
    ABS_onlyLU = emi_LU_1990 # LU_1990 is a sink.
    ABS_inclLU = ABS_exclLU + ABS_onlyLU
    print(f"{condi} ABS inclLU: {ABS_inclLU :.3f} MtCO2eq")
    print(f"{condi} ABU inclLU: {ABS_inclLU - emi_inclLU[2030] :.3f} MtCO2eq")

# print("\nBased on BAU and RBU.")
# RBU = {'uncondi': -.02, 'condi': -.23}
# emi_LU_2030 = -6.470
# for condi in RBU.keys():
#     ABS_exclLU = emi_exclLU_2030 * (1+RBU[condi])
#     ABU_exclLU = emi_exclLU_2030 * RBU[condi]
#     print(f"{condi} ABS exclLU: {ABS_exclLU :.3f} MtCO2eq")
#     print(f"{condi} ABU exclLU: {ABU_exclLU :.3f} MtCO2eq")
#     ABS_onlyLU = emi_LU_2030 * (1-RBU[condi]) # LU_2030 is a sink
#     ABU_onlyLU = emi_LU_2030 * -RBU[condi]
#     print(f"{condi} ABS inclLU: {ABS_exclLU + ABS_onlyLU :.3f} MtCO2eq")
#     print(f"{condi} ABU inclLU: {ABU_exclLU + ABU_onlyLU :.3f} MtCO2eq")

# %%

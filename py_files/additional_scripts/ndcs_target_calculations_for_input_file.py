# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def f_lulucf(emi_inclLU, emi_exclLU):
    
    lulucf = emi_inclLU - emi_exclLU
    
    print(f"IPCMLULUCF: {lulucf :.6f}")
    
    return lulucf

# %%
def f_emi_inclLU(emi_exclLU, lulucf):
    
    emi_inclLU = emi_exclLU + lulucf
    
    print(f"IPC0: {emi_inclLU :.6f}")
    
    return emi_inclLU

# %%
def f_emi_exclLU(emi_inclLU, lulucf):
    
    emi_exclLU = emi_inclLU - lulucf
    
    print(f"IPCM0EL: {emi_exclLU :.6f}")
    
    return emi_exclLU

# %%
def f_ABS_inclLU(tar_abs_exclLU, lulucf):
    """
    Get ABS IPC0 target from ABS IPCM0EL target and LULUCF.
    """
    
    tar_abs_inclLU = tar_abs_exclLU + lulucf
    
    print(f"ABS IPC0: {tar_abs_inclLU :.6f}")
    
    return tar_abs_inclLU

# %%
def f_ABS_exclLU(tar_abs_inclLU, lulucf):
    """
    Get ABS IPCM0EL target from ABS IPC0 target and LULUCF.
    """
    
    tar_abs_exclLU = tar_abs_inclLU - lulucf
    
    print(f"ABS IPCM0EL: {tar_abs_exclLU :.6f}")
    
    return tar_abs_exclLU
    
# %%
def f_ABU(tar_abs, emi):
    """
    Get ABU IPCM0EL target from ABS IPCM0EL target and BAU IPCM0EL.
    Or all for IPC0.
    """
    
    tar_abu = tar_abs - emi
    
    print(f"ABU: {tar_abu :.6f}")
    
    return tar_abu

# %%
from pathlib import Path
import numpy as np
import pandas as pd
from copy import deepcopy
import helpers_functions as hpf
from setup_metadata import setup_metadata

meta = setup_metadata()

# %%
"""
AFG
"""

# All in MtCO2eq_SAR.

# Table 1.
emi_exclLU = {2025: 41.67295, 2030: 48.93954}
emi_inclLU = {2025: 53.18064, 2030: 61.03425}
lulucf = {2025: 11.50770, 2030: 12.09471}

# ABS.

# From Figure 1.
tar_abs_exclLU = {2025: 40.3, 2030: 42.7}

# LU is not covered.
tar_abs_inclLU = {}
for year in [2025, 2030]:
    print(year)
    tar_abs_inclLU[year] = f_ABS_inclLU(tar_abs_exclLU[year], lulucf[year])

# ABU and RBU.

print("\nexclLU")
for year in [2025, 2030]:
    print(year)
    tar_abu_exclLU = f_ABU(tar_abs_exclLU[year], emi_exclLU[year])
    print(f"RBU: {tar_abu_exclLU/emi_exclLU[year]*100. :.1f}%")

print("\ninclLU")
for year in [2025, 2030]:
    print(year)
    tar_abu_inclLU = f_ABU(tar_abs_inclLU[year], emi_inclLU[year])
    print(f"RBU: {tar_abu_inclLU/emi_inclLU[year]*100. :.1f}%")

# %%
"""
AGO
"""
bau = {2025: 155.819, 2030: 193.250}
ABS = {2025: {'uncondi': 124.656, 'condi': 113.748},
       2030: {'uncondi': 125.612, 'condi': 96.625}}
for year in bau.keys():
    for condi in ABS[year].keys():
        print(f"{year} {condi}: {ABS[year][condi] - bau[year] :.3f} MtCO2eq")

# %%
"""
ARG
"""

# ABU.
bau = 592
ABS_uncondi = 483
ABS_condi = 369

print(f"ABU unconditional: {ABS_uncondi - bau} MtCO2eq")
print(f"ABU conditional: {ABS_condi - bau} MtCO2eq")

# %%
"""
AND
"""

# ABS from BAU and ABU [p. 2].
print(f"{.53055 - .19373 :.6f}")

# %%
"""
ALB
"""

# 0.708 MtCO2eq = 11.5% reduction.
red = 0.708
bau = 100/11.5*red
print(f"BAU: {bau :.3f} MtCO2eq")
print(f"ABS: {bau - red :.3f} MtCO2eq")

# %%
"""
ARM
"""

# 633 MtCO2eq for 2015 to 2050.
# Annual average.
print(f"Annual average {633/len(range(2015, 2051)) :.3f} MtCO2eq")
print(f"Total for 2015 to 2050: {5.4*3.35e6*len(range(2015, 2051))}") 
# They give 633e6, that is close enough. I think that 2015 to 2050 is one year too much.

# %%
"""
AZE
"""
emi_inclLU = 69.641
emi_exclLU = 73.331

lulucf = f_lulucf(emi_inclLU, emi_exclLU)

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
"""
BEN
"""

ABS = {'uncondi': 37, 'condi': 32.5}
bau = 38.5

for condi in ABS.keys():
    ABU = ABS[condi] - bau
    print(f"\nABU {condi}: {ABU} MtCO2eq")
    print(f"RBU {condi}: {ABU/bau*100 :.1f}%")

# %%
"""
BGD
"""

# p. 3
# 69% of BAU in 2030 is 234 MtCO2eq.
bau_2030 = 100/69*234
print(f"BAU in 2030 (IPCM0EL): {bau_2030 :.3f} MtCO2eq")

# ABS from BAU and given ABU. [p. 3].
print(f"ABS unconditional: {bau_2030 - 12 :.3f} MtCO2eq")
print(f"ABS conditional: {bau_2030 - 36 :.3f} MtCO2eq")

# %%# %%
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

"""
print("\nBased on BAU and RBU.")
RBU = {'uncondi': -.02, 'condi': -.23}
emi_LU_2030 = -6.470
for condi in RBU.keys():
    ABS_exclLU = emi_exclLU_2030 * (1+RBU[condi])
    ABU_exclLU = emi_exclLU_2030 * RBU[condi]
    print(f"{condi} ABS exclLU: {ABS_exclLU :.3f} MtCO2eq")
    print(f"{condi} ABU exclLU: {ABU_exclLU :.3f} MtCO2eq")
    ABS_onlyLU = emi_LU_2030 * (1-RBU[condi]) # LU_2030 is a sink
    ABU_onlyLU = emi_LU_2030 * -RBU[condi]
    print(f"{condi} ABS inclLU: {ABS_exclLU + ABS_onlyLU :.3f} MtCO2eq")
    print(f"{condi} ABU inclLU: {ABU_exclLU + ABU_onlyLU :.3f} MtCO2eq")
"""

# %%
"""
BLR
"""

# ABS IPCM0EL.
# From given 1990 emissions [p. 3].
emi_ipcm0el_1990 = 139.15123
print(f"ABS IPCM0EL: {(1-.28) * emi_ipcm0el_1990 :.3f} MtCO2eq_SAR")

# %%
"""
BRB
"""

RBU = {2025: -.37, 2030: -.44}
emi_bau = {2025: 2.2822, 2030: 2.5025}

for yr in RBU.keys():
    print(f"\n{yr} ABS: {emi_bau[yr] * (1+RBU[yr]) :.4f} MtCO2eq")
    print(f"{yr} ABU: {emi_bau[yr] * RBU[yr] :.4f} MtCO2eq")

# %%
"""
BTN
"""

emi = {2000: 1.6, 2013: 2.2} # MtCO2eq
sequestration = {2000: -6.3, 2013: -6.3}

for yr in emi.keys():
    print(f"IPC0 {yr}: {emi[yr] + sequestration[yr] :.1f} MtCO2eq")

# %%
"""
BWA
"""

# Given 2010 emissions: 8307 Gg CO2eq.
# Given reduction: 15%.
emi_2010 = 8.307
print(f"Target emissions: {emi_2010 * (1-.15) :.3f} MtCO2eq")

# Not sure which part of emissions this stands for.
primap_kyoto_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['BWA', 2010]
print(f"PRIMAP-hist vs. given 2010 emissions: {primap_kyoto_ipcm0el} (KYOTOGHG_IPCM0EL) vs. {emi_2010} MtCO2eq")

primap_kyoto_ipc1 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPC1_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['BWA', 2010]
print(f"PRIMAP-hist vs. given 2010 emissions: {primap_kyoto_ipc1} (KYOTOGHG_IPC1) vs. {emi_2010} MtCO2eq")

sum_cov = 0
for combi_cov in ['CO2_IPC1', 'CO2_IPCMAG', 'CO2_IPC4',
                  'CH4_IPC1', 'CH4_IPCMAG', 'CH4_IPC4',
                  'N2O_IPC1', 'N2O_IPCMAG', 'N2O_IPC4']:
    try:
        sum_cov += hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'{combi_cov}_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        data.loc['BWA', 2010]
    except:
        sum_cov += 0

print(f"Sum over covered gas+sector-combis in 2010: {sum_cov :.3f} MtCO2eq")

# %%
"""
CAF
"""

# p. 6, emissions per sector
print('\n', 2010)

emi_2010 = {'lu': 104.02897, 'agri': 6.12000, 'autr_ener': 0.33094, 
            'bois_ener': 5.70454, 'dechets': 0.10055, 'ippu': 0.00013} # MtCO2eq
emi_total_2010 = 116.2855 # excluding sequestration, p. 7
pc_lu_2010 = emi_2010['lu']/emi_total_2010
sequestration_2010 = -330.000

emi_ipcm0el_2010 = 0
for cat in [xx for xx in emi_2010.keys() if xx != 'lu']:
    emi_ipcm0el_2010 += emi_2010[cat]

print(f"IPCM0EL: {emi_ipcm0el_2010 :.4f} MtCO2eq")

emi_lu_2010 = emi_2010['lu'] + sequestration_2010
emi_ipc0_2010 = emi_ipcm0el_2010 + emi_lu_2010

print(f"IPC0: {emi_ipc0_2010 :.4f} MtCO2eq")
print(f"IPCMLULUCF: {emi_lu_2010 :.4f} MtCO2eq")

print('\n', 2050) # p. 7

pc_2050 = {'lu': .684, 'energy': .134, 'agri': .134, 'water': .032, 'ippu': .016}
emi_total_2050 = 189.2718 # excluding sequestration
pc_lu_2050 = pc_2050['lu']
sequestration_2050 = -310.14643
emi_2050 = {}
for cat in pc_2050.keys():
    emi_2050[cat] = pc_2050[cat] * emi_total_2050
    print(f"2050 {cat}: {emi_2050[cat] :.4f} MtCO2eq")

emi_ipcm0el_2050 = 0
for cat in [xx for xx in emi_2050.keys() if xx!= 'lu']:
    emi_ipcm0el_2050 += emi_2050[cat]

print(f"IPCM0EL: {emi_ipcm0el_2050 :.4f} MtCO2eq")

emi_lu_2050 = emi_2050['lu'] + sequestration_2050
emi_ipc0_2050 = emi_ipcm0el_2050 + emi_lu_2050

print(f"IPC0: {emi_ipc0_2050 :.4f} MtCO2eq")
print(f"IPCMLULUCF: {emi_lu_2050 :.4f} MtCO2eq")

sequestration_2030 = np.interp(2030, [2010, 2050], [sequestration_2010, sequestration_2050])
print(f"\nSequestration in 2030: {sequestration_2030} MtCO2eq")
pc_lu_2030 = np.interp(2030, [2010, 2050], [pc_lu_2010, pc_lu_2050])
# Not realistic total emissions:
test_2030 = 100/5*5.500
# Correct total emissions:
test_2050 = 100/25*47.320
# We use the linear interpolation between 2010 and 2050 for the 2030 total emissions.
emi_total_2030 = np.interp(2030, [2010, 2050], [emi_total_2010, emi_total_2050])
emi_ipc0_2030 = emi_total_2030 + sequestration_2030
emi_lu_2030 = sequestration_2030 + pc_lu_2030*emi_total_2030
emi_ipcm0el_2030 = emi_ipc0_2030 - emi_lu_2030
print(f"2030 IPC0: {emi_ipc0_2030 :.4f} MtCO2eq")
print(f"2030 IPCM0EL: {emi_ipcm0el_2030 :.4f} MtCO2eq")
print(f"2030 IPCMLULUCF: {emi_lu_2030 :.4f} MtCO2eq")

ABU_all = {'uncondi': {2030: -4.062, 2050: -10.410},
       'condi': {2030: -5.500, 2050: -47.320}} # MtCO2eq, p. 8
bau_ipc0 = {2030: emi_ipc0_2030, 2050: emi_ipc0_2050}
bau_ipcm0el = {2030: emi_ipcm0el_2030, 2050: emi_ipcm0el_2050}

for condi in ABU_all.keys():
    print(f"\n{condi}")
    for yr in ABU_all[condi].keys():
        bau = bau_ipc0[yr]
        ABU = ABU_all[condi][yr]
        #RBU = ABU/bau # 'Problem': bau and ABU negative.
        ABS = bau + ABU
        print(f"\nIPC0 {yr}")
        print(f"BAU: {bau :.4f} MtCO2eq")
        print(f"ABS: {ABS :.4f} MtCO2eq")
        print(f"ABU: {ABU :.4f} MtCO2eq")
        #print(f"RBU: {RBU*100 :.1f}%")
        
        #print(f"\nIPCM0EL {yr}")
        #print(f"\nBAU: {bau_ipcm0el[yr] :.4f} MtCO2eq")
        #print(f"ABS: {bau_ipcm0el[yr]*(1+RBU) :.4f} MtCO2eq")
        #print(f"ABU: {bau_ipcm0el[yr]*RBU :.4f} MtCO2eq")
        #print(f"RBU: {RBU*100 :.1f}%")

# ABS exclLU.
# Calculated based on given RBU and bau_exclLU.
bau_exclLU = {2030: 32.1905, 2050: 59.8099}
RBU_inclLU = {'uncondi': {2030: -.037, 2050: -.055},
              'condi': {2030: -.05, 2050: -.25}}

for yr in bau_exclLU.keys():
    for condi in RBU_inclLU.keys():
        print(f"\n{yr} {condi} exclLU ABS: {bau_exclLU[yr] * (1+RBU_inclLU[condi][yr]) :.4f} MtCO2eq")
        print(f"{yr} {condi} exclLU ABU: {bau_exclLU[yr] * RBU_inclLU[condi][yr] :.4f} MtCO2eq")

# %%
"""
CHE
"""

ipcm0el_1990 = 53.3
red = {'best': {2025: -.35, 2030: -.5, 2050: -.85}, 'worst': {2050: -.7}}

for rge in red.keys():
    data = red[rge]
    for year in data.keys():
        print(f"{rge} {year}: {ipcm0el_1990 * (1 + data[year]) :.3f}")

# %%
"""
CHL
"""

emi_ipcm0el = pd.Series(index=range(2017, 2031), dtype='float64')
emi_ipcm0el[2017] = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['CHL', 2017]
emi_ipcm0el[2030] = 95 # 2030: absolute target
emi_cumulative_2020_2030 = 1100 # MtCO2eq, p. 17.

print(f"Emissions in 2017: {emi_ipcm0el[2017]} MtCO2eq")
for emi_2025 in [95, 99, 100, 105, 110]:
    emi_ts = deepcopy(emi_ipcm0el)
    emi_ts[2025] = emi_2025
    emi_ts = emi_ts.interpolate()
    emi_tot = emi_ts[list(range(2020, 2031))].sum()
    print(f"Assumed emissions in 2025: {emi_2025}, resulting / allowed cumulative emissions: {emi_tot :.0f} / {emi_cumulative_2020_2030}")

# %%
"""
CIV
"""

# ABU.
# BAU minus 'scenario bas carbone' 2030 [p. 3].
print(f"ABU 2030: {1e-3 * (24576.16 - 34253.25)} MtCO2eq")

# %%
"""
CMR
"""

emi_bau = 104
emi_tar = 71

# ABU.
# Reference 2035 minus INDC 2035 [p. 2]
print(f"ABU 2035: {emi_tar - emi_bau} MtCO2eq")

# %%
"""
COD
"""

emi_bau_inclLU = 430 # MtCO2eq
red_inclLU = -70 # MtCO2eq
tar_inclLU = emi_bau_inclLU+red_inclLU
print(f"ABS IPC0: {tar_inclLU} MtCO2eq")

emi_bau_onlyLU = 400
tar_onlyLU = 290 # Read from figure 2
red_onlyLU = tar_onlyLU - emi_bau_onlyLU
red_exclLU = red_inclLU - red_onlyLU
print(f"The reduction ABU of onlyLU is {red_onlyLU} MtCO2eq, while the reduction inclLU is {red_inclLU} MtCO2eq")
print(f"So the ABU exclLU 'reduction' is {red_exclLU} MtCO2eq")

emi_bau_exclLU = emi_bau_inclLU - emi_bau_onlyLU
tar_exclLU = emi_bau_exclLU + red_exclLU
print(f"ABS IPCM0EL: {tar_exclLU} MtCO2eq")
print(f"RBU IPCM0EL: {red_exclLU / emi_bau_exclLU * 100. - 100. :.0f}%")

# %%
"""
COL
"""

emi_bau = 335
pc_red = {'unconditional': -.2, 'conditional': -.3}

# ABS.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABS 2030 {condi}: {emi_bau * (1 + pc_red[condi]) :.3f} MtCO2eq")

# ABU.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABU 2030 {condi}: {pc_red[condi] * emi_bau :.3f} MtCO2eq")

# %%
"""
COG
"""

# ABU from given ABS and BAU.
ABS = {2025: 8.793, 2035: 15.858}
BAU = {2025: 16.984, 2035: 34.527}

for year in ABS.keys():
    print(f"ABU {year}: {ABS[year] - BAU[year] :.3f} MtCO2eq_SAR")

# %%
"""
CUB
"""

# p. 16
emi_brutto_2010 = 40 # MtCO2eq
emi_brutto_1990 = 100/84*emi_brutto_2010
print(f"emi brutto 1990: {emi_brutto_1990 :.1f} MtCO2eq")
emi_energy_2010 = .76*emi_brutto_2010
emi_agri_2010 = .15*emi_brutto_2010
emi_waste_ippu = .09*emi_brutto_2010

# %%
"""
CRI
"""

ABS = 9.374000 # MtCO2eq
RBU = -.44
bau = 1/(1+RBU)*ABS
ABU = RBU*bau
print(f"2030 BAU: {bau :.3f} MtCO2eq")
print(f"2030 ABU: {ABU :.3f} MtCO2eq")

# %%
"""
COK
"""

emi_tot = 0.069574 # MtCO2eq

pc_electricity = .34
emi_electricity = emi_tot * pc_electricity
print(f"emi electricity: {emi_electricity :.6f} MtCO2eq") # Fits to values in Figure 2, p. 1.

pc_energy = .79
emi_energy = emi_tot * pc_energy
print(f"emi Energy: {emi_energy :.6f} MtCO2eq")

RBY = {2020: -.38, 2030: -.81} # Only electricity

for yr in RBY.keys():
    ABY = emi_electricity * RBY[yr]
    print(f"\nABY {yr}: {ABY :.6f} MtCO2eq")
    print(f"ABS {yr}: {emi_tot + ABY :.6f} MtCO2eq")
    print(f"RBY {yr} compared to emi_energy: {100.*ABY/emi_energy :.1f}%")
    print(f"\nABS {yr} only electricity (comparison with Figure 2): {emi_electricity + ABY :.6f} MtCO2eq")

# %%
"""
COM
"""

# p. 18+22, emissions per sector.
# IPC0 is given in the tables.
ipcm0el = {2000: 0.106600 + 0.053000 + 0.026300,
           2005: 0.025600 + 0.057000 + 0.029900,
           2010: 0.149700 + 0.070600 + 0.034200,
           2015: 0.181300 + 0.081400 + 0.039100,
           2020: 0.219100 + 0.085600 + 0.044700,
           2025: 0.266500 + 0.089800 + 0.050800,
           2030: 0.319200 + 0.094100 + 0.056000}
ipcmlulucf = {2000: 0.061500 - 0.315200 + 0.024600,
              2005: 0.061500 - 0.268800 + 0.027300,
              2010: 0.061500 - 0.209300 + 0.034900,
              2015: 0.061500 - 0.175100 + 0.041200,
              2020: 0.050000 - 0.085200 + 0.043600,
              2025: 0.059600 - 0.078300 + 0.046100,
              2030: 0.069100 - 0.068900 + 0.048500}
for yr in ipcm0el.keys():
    print(f"\nipcm0el {yr}: {ipcm0el[yr] :.6f} MtCO2eq")
    print(f"ipcmlulucf {yr}: {ipcmlulucf[yr] :.6f} MtCO2eq")


ipc0 = {2025: .434500, 2030: .523000} # MtCO2eq, p. 9
ABU_inclLU = {2025: -.301500, 2030: -.441700} # 2020 values ignored.
RBU_inclLU = {2025: -.69, 2030: -.84}
ABS_inclLU = {}
for yr in ipc0.keys():
    ABS_inclLU[yr] = ipc0[yr] + ABU_inclLU[yr]
    print(f"ABS_inclLU {yr}: {ABS_inclLU[yr] :.6f} MtCO2eq")

# Target year onlyLU is positive.
# Calculate the ABS exclLU as ABS inclLU minus the target year LULUCF emissions.
for yr in ipc0.keys():
    ABS_exclLU = ABS_inclLU[yr] - ipcmlulucf[yr]
    ABU_exclLU = ABS_exclLU - ipcm0el[yr]
    RBU_exclLU = ABU_exclLU/ipcm0el[yr]*100
    print(f"\n{yr} ABS exclLU: {ABS_exclLU :.6f} MtCO2eq")
    print(f"{yr} ABU exclLU: {ABU_exclLU :.6f} MtCO2eq")
    print(f"{yr} RBU exclLU: {RBU_exclLU :.1f}%")

# %%
"""
DJI
"""

emi_bau = 4.475 # MtCO2eq
ABS_uncondi = 2.685
ABS_condi = 1.790
print(f"ABU uncondi: {ABS_uncondi - emi_bau :.3f} MtCO2eq")
print(f"ABU condi: {ABS_condi - emi_bau :.3f} MtCO2eq")

# %%
"""
DMA
"""

emi = .1645 # MtCO2eq
red = {2025: -.392, 2030: -.447}

for yr in red.keys():
    print(f"\n{yr}")
    print(f"ABS: {emi*(1+red[yr]) :.3f} MtCO2eq")
    print(f"ABU: {emi*red[yr] :.3f} MtCO2eq")

# %%
"""
DOM
"""

emi_2010 = 3.6 # tCO2eq per capita, p. 2
REI = -.25

print(f"AEI: {emi_2010 * (1+REI) :.1f} tCO2eq/capita")

# %%
"""
ECU
"""

bau_ipcm0el = 76.904
ABS_ipcm0el = {'uncondi': 67.774, 'condi': 60.824}

for condi in ABS_ipcm0el.keys():
    print(f"ABU {condi}: {ABS_ipcm0el[condi] - bau_ipcm0el :.3f} MtCO2eq")

ref_lu = 100/80*35 # p. 17, mitigated by 20% is 35 MtCO2eq/yr.
# Nivel de referencia 2000 - 2008. But here used as BAU ...
print(f"\nBAU LULUCF: {ref_lu} MtCO2eq")

ABS_lu = {'uncondi': ref_lu * (1-.04), 'condi': ref_lu * (1-.2)} # p. 17.

for condi in ABS_lu.keys():
    ABS_ipc0 = ABS_ipcm0el[condi] + ABS_lu[condi]
    print(f"ABS IPC0 {condi}: {ABS_ipc0 :.3f} MtCO2eq")
    # We just assume that the 2000-2008 reference for LULUCF would be the BAU LULUCF emissions.
    print("Assuming the reference LULUCF emissions to be the BAU emissions:")
    ABU_ipc0 = ABS_ipc0 - (bau_ipcm0el + ref_lu)
    print(f"ABU IPC0 {condi}: {ABU_ipc0 :.3f} MtCO2eq")
    RBU_ipc0 = ABU_ipc0/ABS_ipc0*100.
    print(f"RBU IPC0 {condi}: {RBU_ipc0 :.0f}%")    

# %%
"""
ERI
"""

# p. 20
bau = {2025: 9379, 2030: 11466} # ktCO2eq
ABU = {'uncondi': {2025: -376, 2030: -982},
       'condi': {2025: -1518, 2030: -3152}}

for condi in ABU.keys():
    for yr in bau.keys():
        print(f"ABS {condi} {yr}: {0.001*(bau[yr]+ABU[condi][yr])} MtO2eq")

# %%
"""
FJI
"""

emi_bau_energy = 2.500 # MtCO2eq
red = -.3
print(f"ABU: {emi_bau_energy * red} MtCO2eq")

# %%
"""
FSM
"""

ABS = {'uncondi': 0.108, 'condi': 0.094} # MtCO2eq, p. 1
emi_2000 = 0.150 # p. 1

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - emi_2000 :.3f} MtCO2eq")

# %%
"""
GAB
"""

# p. 3, first figure
emi_ipcm0el = 1.431 + 3.870 + 0.090 + 0.408 + 0.363
emi_ipcmlulucf = 10.613 - 74.767
emi_ipc0 = emi_ipcm0el + emi_ipcmlulucf
print(f"ipcm0el: {emi_ipcm0el :.3f} MtCO2eq")
print(f"ipc0: {emi_ipc0 :.3f} MtCO2eq")
print(f"ipcmlulucf: {emi_ipcmlulucf :.3f} MtCO2eq")

# %%
"""
GEO
"""

bau_2030 = 38.42 # MtCO2eq
ABS = {'uncondi': 32.66, 'condi': 28.31} # MtCO2eq

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - bau_2030 :.2f} MtCO2eq")

# %%
"""
GIN
"""

emi_bau = 55 # MtCO2eq
RBU = -.3
ABU = emi_bau * RBU
ABS = emi_bau + ABU
print(f"ABU: {ABU} MtCO2eq")
print(f"ABS: {ABS} MtCO2eq")

# %%
"""
GHA
"""

emi_bau = {2025: 53.5, 2030: 73.95}
RBU = {'uncondi': {2025: -.12, 2030: -.15},
       'condi': {2025: -.27, 2030: -.45}}

for condi in RBU.keys():
    print(f"\n{condi}")
    for yr in emi_bau.keys():
        print(f"{yr}")
        print(f"ABS: {emi_bau[yr]*(1+RBU[condi][yr]) :.2f} MtCO2eq")
        print(f"ABU: {emi_bau[yr]*RBU[condi][yr] :.2f} MtCO2eq")

# %%
"""
GMB
"""

# GgCO2eq
red = {
    'uncondi':
        {'RE': {2025: 78.5, 2030: 104},
         'afforestation': {2025: 275.4, 2030: 330.5}},
    'condi':
        {'nerica': {2025: 397.7, 2030: 397.7},
         'SRI': {2025: 707.0, 2030: 707.0},
         'transmission': {2025: 69.6, 2030: 98.7},
         'lighting': {2025: 42.9, 2030: 41.7},
         'heating': {2025: 19.3, 2030: 36.4},
         'RE_EE': {2025: 121.7, 2030: 174.4},
         'cook_stoves': {2025: 287.6, 2030: 278.4},
         'vehicle': {2025: 114.5, 2030: 193.3},
         'waste': {2025: 239.7, 2030: 413.7}}}

for yr in [2025, 2030]:
    sum_yr = 0.
    for condi in red.keys():
        sum_condi = 0.
        for sec in red[condi].keys():
            sum_yr += red[condi][sec][yr]
            sum_condi += red[condi][sec][yr]
        
        print(f"{yr} {condi}: {sum_condi :.1f} GgCO2eq")
    
    print(f"{yr} total: {sum_yr :.1f} GgCO2eq")

# Values do not fit to Figure 1. The reductions are way too high.

bau = {2025: 3.250, 2030: 3.850} # MtCO2eq, read from Figure 1.
RBU = {2025: -.444, 2030: -.454}
for yr in bau.keys():
    print(f"{yr} ABS: {bau[yr]*(1+RBU[yr]) :.3f} MtCO2eq")
    print(f"{yr} ABU: {bau[yr]*RBU[yr] :.3f} MtCO2eq")

# %%
"""
GTM
"""

bau = 53.85 # MtCO2eq
ABS_uncondi = 47.81
ABS_condi = 41.66
print(f"ABU uncondi: {ABS_uncondi - bau :.2f} MtCO2eq")
print(f"ABU condi: {ABS_condi - bau :.2f} MtCO2eq")

# %%
"""
HND
"""

# ABS.
emi_bau = 28.922
red = -.15
print(f"ABS target: {emi_bau * (1+red) :.3f} MtCO2eq")
print(f"ABU target: {emi_bau * red :.3f} MtCO2eq")

# %%
"""
HTI
"""

bau = 20.7 # MtCO2eq
RBU = {'uncondi': -.05, 'condi': -.31}

for condi in RBU.keys():
    print(f"ABS {condi}: {bau*(1+RBU[condi]) :.1f} MtCO2eq")
    print(f"ABU {condi}: {bau*RBU[condi] :.1f} MtCO2eq")

# %%
"""
IDN
"""

# p. 3.
ipc0_2005 = 1800 # MtCO2eq
ipc0_2000 = ipc0_2005 - 400
print(f"IPC0 2000: {ipc0_2000} MtCO2eq")
ipc0_2012 = 1453

pc_lu_2005 = .63
pc_lu_2012 = .478
lu_2005 = pc_lu_2005*ipc0_2005
lu_2012 = pc_lu_2012*ipc0_2012
print(f"IPCMLULUCF 2005: {lu_2005} MtCO2eq")
print(f"IPCMLULUCF 2012: {lu_2012} MtCO2eq")

ipcm0el_2005 = ipc0_2005 - lu_2005
ipcm0el_2012 = ipc0_2012 - lu_2012
print(f"IPCM0EL 2005: {ipcm0el_2005} MtCO2eq")
print(f"IPCM0EL 2012: {ipcm0el_2012} MtCO2eq")

# Table 1 [p. 10]
emi = {
    2010: {'IPC1': 453.2, 'IPC4': 88, 'IPC2': 36, 'IPCMAG': 110.5, 'IPCMLULUCF': 647},
    2030: {'IPC1': 1669, 'IPC4': 296, 'IPC2': 69.6, 'IPCMAG': 119.66, 'IPCMLULUCF': 714}}

# EMI IPCM0EL.
for year in emi.keys():
    data = sum([emi[year][xx] for xx in emi[year].keys() if xx != 'IPCMLULUCF'])
    print(f"IPCM0EL {year}: {data :.3f} MtCO2eq")

# ABS IPCM0EL.
print(f"ABS unconditional IPCM0EL 2030: {2034 - 217} MtCO2eq") # Table 1.
print(f"ABS conditional IPCM0EL 2030: {1787 - 64} MtCO2eq")

# ABU IPCM0EL.
ABU_ipcm0el = {'uncondi': -834 + 497, 'condi': -1081 + 650}
print(f"ABU unconditional IPCM0EL 2030: {ABU_ipcm0el['uncondi']} MtCO2eq") # Table 1.
print(f"ABU conditional IPCM0EL 2030: {ABU_ipcm0el['condi']} MtCO2eq")

bau_inclLU = 2869
bau_LU = 714
bau_exclLU = bau_inclLU - bau_LU
# RBU IPCM0EL.
for condi in ABU_ipcm0el.keys():
    print(f"RBU {condi} IPCM0EL 2030: {ABU_ipcm0el[condi]/bau_exclLU*100 :.1f}%")

# We calculate the 41% (inclLU) reduction assuming that the additional reductions (compared to the 
# 38% reduction) are in the Energy and Forestry sectors only, and in equal parts.
ABS_inclLU_41 = bau_inclLU * (1-.41)
ABU_inclLU_41 = bau_inclLU * -.41
print(f"\nABS 41% inclLU: {ABS_inclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% inclLU: {ABU_inclLU_41 :.3f} MtCO2eq")
ABS_inclLU_38 = 1787
additional_red_IPCM0EL_41 = - (ABS_inclLU_38 - ABS_inclLU_41)/2
ABS_exclLU_38 = 1723
ABS_exclLU_41 = ABS_exclLU_38 + additional_red_IPCM0EL_41
ABU_exclLU_41 = ABS_exclLU_41 - bau_exclLU
print(f"ABS 41% exclLU: {ABS_exclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% exclLU: {ABU_exclLU_41 :.3f} MtCO2eq")

# Calculate RBU condi_worst exclLU from the given uncondi_best and condi_best (inclLU and exclLU).
# Assuming linear relation.
print(f"RBU condi_worst exclLU: {-np.interp(38.24, [29, 41], [15.60, 20.00]) :.1f}%")
# Or from ABS: print(f"RBU condi_worst exclLU: {-np.interp(1723, [1817, 1675.855], [15.6, 20]) :.1f}%")

# %%
"""
IND
"""

GDP_2014 = 1.69 # USD
GDP_2030 = 6.31
print(f"GDP increase from 2014 to 2030: {GDP_2030/GDP_2014 :.1f}")

# %%
"""
ISR
"""

emi_2030 = 105.5 # MtCO2eq
ABU_2030 = -23.85
print(f"RBU 2030: {100*ABU_2030/emi_2030 :.1f}%")

AEI = {2025: 8.8, 2030: 7.7}
emi_per_cap_2005 = 10.4

for yr in AEI.keys():
    print(f"REI {yr}: {(AEI[yr]/emi_per_cap_2005 - 1) * 100. :.1f}%")

# %%
"""
JAM
"""

emi_bau = {2025: 13.443, 2030: 14.492} # MtCO2eq
emi_tar = {'uncondi': {2025: 12.370, 2030: 13.368}, 'condi': {2025: 12.099, 2030: 13.043}}

for condi in emi_tar.keys():
    for yr in emi_bau.keys():
        ABU = emi_tar[condi][yr] - emi_bau[yr]
        print(f"ABU {condi} {yr}: {ABU :.3f} MtCO2eq")
        print(f"RBU {condi} {yr}: {100*ABU/emi_bau[yr] :.1f}%")

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
"""
JPN
"""

# For 2030 these are mitigated values.
emi_tot = {
    'energy_co2': {2013: 1235, 2005: 1219},
    'non_energy_co2': {2013: 75.9, 2005: 85.4},
    'methane': {2013: 36.0, 2005: 39.0},
    'n2o': {2013: 22.5, 2005: 25.5},
    'fgases': {2013: 38.6, 2005: 27.7}}

for yr in [2005, 2013]:
    emi_yr = sum([emi_tot[xx][yr] for xx in emi_tot.keys()])
    print(f"Total emissions (exclLU) {yr}: {emi_yr :.1f} MtCO2eq")

# p. 8-9:
emi_tar_2030 = {'energy_co2': 927, 'non_energy_co2': 70.8, 'methane': 31.6, 'n2o': 21.1, 'fgases': 28.9}
RBU_per_gas = {'energy_co2': -.25, 'non_energy_co2': -.067, 'methane': -.123, 'n2o': -.061, 'fgases': -.251}
yr = 2030
ABS_2030 = sum([emi_tar_2030[xx] for xx in emi_tar_2030.keys()])
print(f"Mitigated emissions (exclLU) {yr}: {ABS_2030 :.1f} MtCO2eq")

emi_inclLU = ABS_2030 - 36.9 # P. 10.
# 36.9 MtCO2eq is target for removals.
print(f"Target inclLU: {emi_inclLU :.1f} MtCO2eq")

# %%
"""
KEN
"""

# ABS
emi_bau = 143 # MtCO2eq
red = -.3
print(f"ABS: {emi_bau * (1+red)} MtCO2eq")
print(f"ABU: {emi_bau * red} MtCO2eq")

# %%
"""
KHM
"""

# EMI IPCM0EL from data given on p. 5.
ipcm0el = 11.600
ipcmlulucf = -7.897
ipc0 = ipcm0el + ipcmlulucf

print(f"EMI IPCM0EL 2030: {f_emi_exclLU(ipc0, ipcmlulucf)} MtCO2eq")

ABU_ipcm0el = -3.100 # MtCO2eq, this is compared to BAU.
ABU_lulucf = 7.897 - 18.492 # This is compared to 2010, not to BAU! We ignore that...
ABU_ipc0 = ABU_ipcm0el + ABU_lulucf
print(f"ABU IPC0: {ABU_ipc0} MtCO2eq")

# %%
"""
KIR
"""

# p. 9.
ABU_uncondi = -0.010090
ABU = {}
ABU['uncondi'] = {2025: ABU_uncondi, 2030: ABU_uncondi}
ABU['condi'] = {2025: ABU_uncondi -0.035880, 2030: ABU_uncondi -0.038420}

RBU = {'uncondi': {2025: -.137, 2030: -.128},
       'condi': {2025: -.137-.488, 2030: -.128-.490}}

bau = {}
for yr in [2025, 2030]:
    bau_act = []
    for condi in ['uncondi', 'condi']:
        bau_act += [1/RBU[condi][yr]*ABU[condi][yr]]
    
    bau[yr] = np.average(bau_act)
    print(f"BAU {yr}: {bau[yr] :.6f} MtCO2eq (uncondi: {bau_act[0] :.6f}; condi: {bau_act[1] :.6f})")

for condi in ABU.keys():
    print(f"\n{condi}")
    for yr in ABU[condi].keys():
        print(f"\n{yr}")
        print(f"ABS: {bau[yr]*(1+RBU[condi][yr]) :.6f} MtCO2eq")
        print(f"ABU: {ABU[condi][yr] :.6f} MtCO2eq")
        print(f"RBU: {100.*RBU[condi][yr] :.1f}%")

# We use the mean over the calculated BAUs (per year).

# %%
"""
KOR
"""

emi_2030 = 850.6 # MtCO2eq, p. 1.
RBU = -.37

print(f"ABU: {emi_2030 * RBU :.1f} MtCO2eq")
print(f"ABS: {emi_2030 * (1+RBU) :.1f} MtCO2eq")

# %%
"""
LAO
"""

# p. 4+5

ABU = -(0.063 + 0.033 + 0.158 + 16.284)
print(f"ABU: {ABU} MtCO2eq")

# If we include No 1 and 2, the ABU would be by far higher than the given 2000 emissions of 51,000 Gg.
print(f"Probably too high: {ABU - (60.000 + 69.000)/2 - 1468.000} MtCO2eq")

# %%
"""
LBN
"""

# ABS.
emi_bau = 43.5 # MtCO2eq
red = {'uncondi': -.15, 'condi': -.3}

for condi in red.keys():
    ABS = emi_bau * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_bau :.3f} MtCO2eq")

# %%
"""
LCA
"""

# ABS.
# From values given on p. 5.
bl = {2025: 0.758, 2030: 0.816}
abu = {2025: -0.121, 2030: -0.188}

for year in bl.keys():
    print(f"ABS {year}: {bl[year] + abu[year] :.3f} MtCO2eq")

# %%
"""
LIE
"""

# ABS.
# From RBY and 1990 emissions.
emi_1990 = 0.2287
print(f"ABS 2030 IPC0: {emi_1990 * (1-.4) :.6f} MtCO2eq")

# Is the given value IPC0 or IPCM0EL?
primap_kyoto_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['LIE', 1990]
print(f"PRIMAP-hist vs. given 1990 emissions: {primap_kyoto_ipcm0el :.3f} (KYOTOGHG_IPCM0EL) vs. {emi_1990} MtCO2eq")

primap_kyoto_ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')). \
    data.loc['LIE', 1990]
print(f"PRIMAP-hist KYOTOGHG_IPCM0EL + KYOTOGHG_IPCMLULUCF = {primap_kyoto_ipcm0el + primap_kyoto_ipcmlulucf :.3f} MtCO2eq")

# %%
"""
LKA
"""

# LKA gives % reductions against BAU which differ beteween Energy and the other sectors.
# We use the 2017 ratios of the sectors (transport, industry, forests, waste) to calculate the reduction.
# Transport is actually included in IPC1...
cats = ['IPC1', 'IPC2', 'IPCMLULUCF', 'IPC4']
emi_cats = {}
for cat in cats:
    table = f"KYOTOGHG_{cat}_TOTAL_NET_" + ("HISTCR_PRIMAPHIST21.csv" if cat != 'IPCMLULUCF'
        else "INTERLIN_VARIOUS.csv")
    emi_cats[cat] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', table)).data.loc['LKA', 2017]

# IPCMLULUCF is positive.
emi_energy = emi_cats['IPC1']
emi_rest = sum([emi_cats[xx] for xx in cats if xx != 'IPC1'])
RBU = {'energy': {'data': emi_energy, 'uncondi': -.04, 'condi': -.2},
       'rest': {'data': emi_rest, 'uncondi': -.03, 'condi': -.1}}

for condi in ['uncondi', 'condi']:
    ABU = 0.
    for cat in ['energy', 'rest']:
        ABU += RBU[cat]['data'] * RBU[cat][condi]
    
    print(f"RBU {condi}: {100.*ABU/(emi_energy+emi_rest) :.1f}%")

# %%
"""
LSO
"""

# p. 25.
bau = {2025: 4.822, 2030: 5.713} # MtCO2eq
ABS = {'uncondi': {2025: 4.332, 2030: 5.142}, 'condi': {2025: 3.653, 2030: 3.737}}

for condi in ABS.keys():
    print(f"\n{condi}")
    for yr in bau.keys():
        print(f"ABU {yr}: {ABS[condi][yr] - bau[yr] :.3f} MtCO2eq")

# %%
"""
MAR
"""

# Given BAU: does it include AFOLU? p. 7.
bau_2030 = 170.8

tar_condi = {'ipcm0el': {'RBU': -.34, 'ABU': -57.5},
             'ipc0': {'RBU': -.42, 'ABU': -71.9}}
for ipc in tar_condi.keys():
    print(f"ipc BAU: {1/tar_condi[ipc]['RBU']*tar_condi[ipc]['ABU'] :.1f} MtCO2eq")

# That did not help that much, as the results are 169.1 and 171.2 MtCO2eq, and both very close to the given BAU.

# Get the share of IPCMLULUCF vs IPCMAG emissions (historical), as they give the reduction in AFOLU.
ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')).data.loc['MAR', range(2010, 2018)]
ipcmag = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMAG_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')).data.loc['MAR', range(2010, 2018)]

print(f"\nAny ipcmlulucf values for 2010 - 2017 negative? {('Yes' if any(ipcmlulucf < 0) else 'No')}!")
share_ipcmlulucf = 100*ipcmlulucf.div(ipcmlulucf.add(ipcmag)).mean()
print(f"Share of LULUCF in AFOLU emissions (2010-2017): {share_ipcmlulucf :.1f}%")

# p. 13: mitigation share per sector.
miti_agri = 7.9
miti_forest = 12.1
afolu = miti_agri + miti_forest
print(f"\nAFOLU is {afolu}% of the mitigation in 2030.")
print(f"Agriculture is {miti_agri/afolu*100}% of the AFOLU mitigation.")
print(f"Forestry is {miti_forest/afolu*100}% of the AFOLU mitigation.")

# p. 7: reductions with and without AFOLU part.
red_with_afolu = {'uncondi': {2025: -26.0, 2030: -29.4},
                  'condi': {2025: -51.1, 2030: -71.9}}
red_without_afolu = {'uncondi': {2025: -20.3, 2030: -22.1},
                     'condi': {2025: -40.9, 2030: -57.5}}
ABS_without_afolu = {'uncondi': {2025: 122.5, 2030: 148.7},
                     'condi': {2025: 101.8, 2030: 113.2}}
BAU = {2025: 142.7, 2030: 170.8} # p. 7, somehow there is only one BAU (not with/without AFOLU).

for condi in red_with_afolu.keys():
    for yr in red_with_afolu[condi].keys():
        afolu_part = red_with_afolu[condi][yr] - red_without_afolu[condi][yr]
        agri_part = miti_agri/afolu * afolu_part
        print(f"\nThe AFOLU part in {condi} {yr} is {afolu_part :.1f} MtCO2eq.")
        print(f"Out of this {agri_part :.1f} MtCO2eq is from agriculture.")
        ABU_exclLU = red_without_afolu[condi][yr] + agri_part
        RBU_exclLU = ABU_exclLU / BAU[yr] * 100
        ABS_exclLU = ABS_without_afolu[condi][yr] + ABU_exclLU
        print(f"\n{condi} {yr} ABS_exclLU: {ABS_exclLU :.1f} MtCO2eq")
        print(f"{condi} {yr} ABU_exclLU: {ABU_exclLU :.1f} MtCO2eq")
        print(f"{condi} {yr} RBU_exclLU: {RBU_exclLU :.1f}%")

# RBU for inclLU 2025:
for condi in red_with_afolu.keys():
    for yr in red_with_afolu[condi].keys(): 
        print(f"\n{condi} {yr} RBU_inclLU: {red_with_afolu[condi][yr]/BAU[yr] * 100 :.1f}%")

# %%
"""
MCO
"""

emi_1990 = .11 # MtCO2eq
red = -.5
print(f"ABS: {emi_1990*(1+red)} MtCO2eq")

# Which share did the F-gases represent in 1990 / 1995?
fgases = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'FGASES_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['MCO', [1990, 1995]]
kyotoghg = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['MCO', [1990, 1995]]
print(f"Share of F-gases (FGASES_IPCM0EL vs. KYOTOGHG_IPCM0EL):\n{100. * fgases / kyotoghg}")

# %%
"""
MDA
"""

# p. 5., emi 1990 (base year).
ipcmlulucf = -5.8866 # MtCO2eq
ipc0 = 37.5322
ipcm0el = 43.4188

RBY = {'uncondi_worst': -.64, 'uncondi_best': -.67, 'condi': -.78}
# LULUCF is sink in base year.
for condi in RBY.keys():
    ABS_exclLU = ipcm0el * (1+RBY[condi])
    ABS_onlyLU = ipcmlulucf
    print(f"{condi} ABS_inclLU: {ABS_exclLU + ABS_onlyLU :.4f} MtCO2eq")

# %%
"""
MDG
"""

ABS_emissions = 214.206-30
ABS_absorptions = -192.111-61 # MtCO2eq, p. 2

print(f"ABS (incl. LULUCF): {ABS_emissions + ABS_absorptions :.3f} MtCO2eq")
print(f"ABS (emissions, might include some LULUCF emissions): {ABS_emissions :.3f} MtCO2eq")

# %%
"""
MDV
"""

emi_bau_energy_consumption = 3.3 # MtCO2eq, p. 2.
RBU = {'uncondi': -.1, 'condi': -.24}

for condi in RBU.keys():
    print(f"\n{condi} ABS (only energy consumption): {emi_bau_energy_consumption * (1+RBU[condi]) :.1f} MtCO2eq")
    print(f"{condi} ABU: {emi_bau_energy_consumption * RBU[condi] :.1f} MtCO2eq")

# %%
"""
MEX
"""

# ABS.
emi_2030 = 973 # MtCO2eq
red = {'uncondi': -.22, 'condi': -.36}

for condi in red.keys():
    ABS = emi_2030 * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_2030 :.3f} MtCO2eq")

# %%
"""
MHL
"""

emi_2010 = .185 # MtCO2eq, p. 3
RBU = {2025: -.32, 2030: -.45, 2035: -.58}

for yr in RBU.keys():
    print(f"ABS {yr}: {emi_2010 * (1+RBU[yr]) :.3f} MtCO2eq")

# %%
"""
MKD
"""

emi_bau = 17.663 # MtCO2eq
ABS = {'worst': 12.435, 'best': 11.359}

for rge in red.keys():
    print(f"{rge}: {ABS[rge] - emi_bau :.3f} MtCO2eq")

# %%
"""
MLI
"""

ipc0_2010 = -192.003
ipcm0el_2010 = 4.289 + 48.507 # MtCO2eq, p. 5.
ipcmlulucf_2010 = -247.017 # p. 14.
print(f"IPCM0EL 2010: {ipcm0el_2010} MtCO2eq")

base = {'energy': {2015: 3.400, 2020: 4.750, 2025: 6.635, 2030: 9.269},
        'agri': {2020: 68.000, 2025: 76.015, 2030: 86.121},
        'lulucf': {2015: -216.152, 2020: -179.000, 2025: -154.424, 2030: -126.588}}
attenuation = {'energy': {2025: 5.149, 2030: 6.336},
               'agri': {2025: 66.256, 2030: 59.521},
               'lulucf': {2025: -167.826, 2030: -153.079}}

for yr in [2020, 2025, 2030]:
    sum_cats = 0
    for cat in base.keys():
        sum_cats += base[cat][yr]
    
    print(f"Sum over given base pathways (energy, agriculture, LULUCF) {yr}: {sum_cats :.3f} MtCO2eq")

for yr in attenuation['energy'].keys():
    sum_cats = 0
    for cat in attenuation.keys():
        sum_cats += attenuation[cat][yr]
    
    print(f"Sum over given attenuation (energy, agriculture, LULUCF) {yr}: {sum_cats :.3f} MtCO2eq")

# p. 19, overview.
bau = {2015: -155.552814, 2020: -109.788619, 2025: -69.327889, 2030: -29.242410} # MtCO2eq
ABS = {'uncondi': {2025: -79.727072, 2030: -33.628772},
       'condi': {2025: -95.494305, 2030: -84.937087}}

for condi in ABS.keys():
    for yr in ABS[condi].keys():
        ABU = ABS[condi][yr] - bau[yr]
        print(f"\n{yr} {condi} ABU: {ABU :.6f} MtCO2eq")
        print(f"{yr} {condi} RBU: {-ABU/bau[yr]*100 :.1f}%")

# exclLU.
for year in bau.keys():
    ipcm0el = bau[year] - base['lulucf'][year]
    print(f"{year} ipcm0el: {ipcm0el :.3f} MtCO2eq")

# Using the ABS and BAU values on p. 19 and the foresterie values on p. 18 (only given for conditional).
condi = 'condi'
for year in ABS[condi].keys():
    ABS_exclLU = ABS[condi][year] - attenuation['lulucf'][year]
    print(f"{year} {condi} ABS exclLU: {ABS_exclLU :.3f} MtCO2eq")
    print(f"{year} {condi} ABU exclLU: {ABS_exclLU - (base['energy'][year] + base['agri'][year]) :.3f} MtCO2eq")
    

# %%
"""
MNG
"""

# ABS
emi_bau = 51.2 # MtCO2eq
ABU = -7.3
print(f"ABS: {emi_bau + ABU :.1f} MtCO2eq")

# %%
"""
MRT
"""

# 12% of the given 22.3% reduction are unconditional.
uncondi = -22.3 * .12
print(f"RBU uncondi: {uncondi :.1f}%")
emi_bau = 18.84 # MtCO2eq
ABU_uncondi = uncondi/100 * emi_bau
print(f"ABU uncondi: {ABU_uncondi :.3f} MtCO2eq")
print(f"ABS uncondi: {emi_bau + ABU_uncondi :.3f} MtCO2eq")

ABU_condi = -4.2 # MtCO2eq (given)
print(f"ABS condi: {emi_bau + ABU_condi :.3f} MtCO2eq")

# Cumulated emissions per sector given [p. 4]
energy_ippu_dechets = 12711.1 + 30.5 + 386.1
agriculture_lulucf = 20431

# %%
"""
MOZ
"""

# Cumulative reductions over 5 year periods given.
print(f"ABU 2024: {23/5} MtCO2eq")
print(f"ABU 2030: {53.4/6} MtCO2eq")

# %%
"""
MUS
"""

emi_2030 = 7
red = -.3
print(f"Target emissions in 2030: {emi_2030 * (1+red) :.3f} MtCO2eq")
print(f"ABU: {emi_2030 * red :.3f} MtCO2eq")

# %%
"""
MWI
"""

emi_bau = {2015: 28.000, 2040: 42.000} # MtCO2eq, p. 3.
yr_interp = 2030
emi_bau[yr_interp] = np.interp(yr_interp, list(emi_bau.keys()), list(emi_bau.values()))
print(f"emi BAU {yr_interp}: {emi_bau[yr_interp] :.3f} MtCO2eq (linear interpolation)")

emi_LULUCF_2015 = 9.9 # MtCO2eq, p. 3.
emi_ipcm0el_2015 = emi_bau[2015] - emi_LULUCF_2015
print(f"emi IPCM0EL 2015: {emi_ipcm0el_2015 :.3f} MtCO2eq")

ABU = {'worst': -14.000, 'best': -16.000}
for rge in ABU.keys():
    print(f"ABS IPC0 {rge} (calculated from linear interpolation of BAU): {emi_bau[2030]+ABU[rge]} MtCO2eq")
    print(f"RBU IPC0 {rge}: {100*ABU[rge]/emi_bau[2030] :.1f}%")

# %%
"""
MYS
"""

emi_ipc0 = 288.663 # MtCO2eq
emi_lulucf = 25.667 # MtCO2eq
print(f"EMI IPCM0EL: {emi_ipc0 - emi_lulucf :.3f} MtCO2eq")

# %%
"""
NAM
"""

# Conditional
bau = 22.647 # MtCO2eq
RBU = -.1
print(f"ABU: {bau*RBU :.3f} MtCO2eq")
print(f"ABS: {bau*(1+RBU) :.3f} MtCO2eq")

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
"""
NGA
"""

RBU = {'uncondi': -.2, 'condi': -.45}
bau = 900 # MtCO2eq

for condi in RBU.keys():
    print(f"ABU {condi}: {bau * RBU[condi] :.1f} MtCO2eq")
    print(f"ABS {condi}: {bau * (1+RBU[condi]) :.1f} MtCO2eq")

# %%
"""
OMN
"""

# ABU.
# From ABS and BAU.
print(f"ABU 2030: {88.714 - 90.532 :.3f} MtCO2eq")

# %%
"""
PAK
"""

# p. 21 + p. 26, emissions per sector
ipc0 = {1994: 181.7, 2008: 329.51, 2012: 374.10, 2015: 405.07, 2030: 1603}
ipcmlulucf = {1994: 6.52, 2008: 9.29, 2012: 9.67, 2015: 10.39, 2030: 29}
ipcm0el = {}
for yr in ipc0.keys():
    ipcm0el[yr] = f_emi_exclLU(ipc0[yr], ipcmlulucf[yr])
    print(f"{yr}: {ipcm0el[yr] :.2f} MtCO2eq")

# Target. LULUCF is source.
RBU = -.2
yr = 2030
tar_exclLU = ipcm0el[yr]*(1+RBU)
tar_onlyLU = ipcmlulucf[yr]*(1+RBU)
tar_inclLU = tar_exclLU + tar_onlyLU
print(f"Target inclLU: {tar_inclLU} MtCO2eq")
print(f"ABU inclLU: {tar_inclLU - ipc0[yr] :.2f} MtCO2eq")

# %%
"""
PER
"""

# IPCMLULUCF
emi_2010_inclLU = 170.6 # MtCO2eq
emi_2010_exclLU = 78.0
emi_2010_onlyLU = f_lulucf(emi_2010_inclLU, emi_2010_exclLU)
print(f"IPCMLULUCF 2010: {emi_2010_onlyLU} MtCO2eq")
emi_2030_inclLU = 298.3
emi_2030_exclLU = 139.3
emi_2030_onlyLU = f_lulucf(emi_2030_inclLU, emi_2030_exclLU)
print(f"IPCMLULUCF 2030: {emi_2030_onlyLU} MtCO2eq")

# Targets
RBU = {'uncondi': -.2, 'condi': -.3} # inclLU

for condi in RBU.keys():
    ABS_exclLU = emi_2030_exclLU * (1+RBU[condi])
    ABS_onlyLU = emi_2030_onlyLU * (1+RBU[condi])
    ABS_inclLU = ABS_exclLU + ABS_onlyLU
    print(f"\n{condi} ABS IPC0: {ABS_inclLU :.1f} MtCO2eq")
    #print(f"{condi} ABS IPCM0EL: {ABS_exclLU :.1f} MtCO2eq")
    print(f"\n{condi} ABU IPC0: {ABS_inclLU - emi_2030_inclLU :.1f} MtCO2eq")
    #print(f"{condi} ABU IPCM0EL: {ABS_exclLU - emi_2030_exclLU :.1f} MtCO2eq")

# %%
"""
PRY
"""

RBU = {'uncondi': -.1, 'condi': -.2} # p. 5
emi_bau_2030 = 416 # MtCo2eq

for condi in RBU.keys():
    print(f"ABU {condi}: {emi_bau_2030*RBU[condi] :.0f} MtCO2eq")
    print(f"ABS {condi}: {emi_bau_2030 * (1+RBU[condi]) :.0f} MtCO2eq")

# %%
"""
PSE
"""

# Status quo scenario.
bau = 9.1 # MtCO2eq
RBU = -.128
print(f"ABS: {bau*(1+RBU) :.1f} MtCO2eq")
print(f"ABU: {bau*RBU :.1f} MtCO2eq")

# %%
"""
RWA
"""

# Sum over given reductions.
red = {'transport': 1.260, 'industry': 0.146, 'waste': 0.586, 'forestry': 5.770} # MtCO2eq

red_sum = sum([red[xx] for xx in red.keys()])    
print(f"Total reduction: {red_sum} MtCO2eq")
# Not clear if it is per year or over a period of time.
# We assume it to be over the period 2021-2030.
print(f"per year: {red_sum/10} MtCO2eq")

# %%
"""
SEN
"""

bau = {2025: 30.0, 2030: 37.5} # MtCO2eq, read from Figure 1, p. 14.
RBU = {'uncondi': {2025: -.04, 2030: -.05},
       'condi': {2025: -.15, 2030: -.21}}
for yr in bau.keys():
    for condi in RBU.keys():
        print(f"\n{yr} {condi} ABS: {bau[yr] * (1+RBU[condi][yr]) :.1f} MtCO2eq")
        print(f"{yr} {condi} ABU: {bau[yr] * RBU[condi][yr] :.1f} MtCO2eq")

# %%
"""
SLB
"""

ABU = {'uncondi': {2025: -0.008, 2030: -0.008}, 'condi': {2025: -0.018800, 2030: -0.031125}}
RBU = {'uncondi': {2025: -.12, 2030: -.3}, 'condi': {2025: -.27, 2030: -.45}}

for condi in ABU.keys():
    for yr in ABU[condi].keys():
        emi_bau = 1/RBU[condi][yr]*ABU[condi][yr]
        ABS = emi_bau * (1+RBU[condi][yr])
        print(f"\nBAU {condi} {yr}: {emi_bau :.3f} MtCO2eq")
        print(f"ABS {condi} {yr}: {ABS :.3f} MtCO2eq")
        print(f"ABU {condi} {yr}: {ABU[condi][yr] :.3f} MtCO2eq")
        print(f"RBU {condi} {yr}: {100 * RBU[condi][yr] :.0f}%")

# %%
"""
SMR
"""

# ABS.
# From given base year emissions and % reduction. No check if LULUCF is a sink...
print(f"ABS 2030 IPC0: {0.213 * (1-.2)} MtCO2eq_SAR")

# %%
"""
STP
"""

# ABS.
# From given BAU and absolute reduction [p. 7].
emi_ipcm0el = 0.240 # MtCO2eq
emi_red = -0.057
print(f"ABS 2030 IPCM0EL: {emi_ipcm0el + emi_red} MtCO2eq")

emi_lulucf = -0.630
emi_ipc0 = emi_ipcm0el + emi_lulucf
print(f"EMI IPC0: {emi_ipc0} MtCO2eq")

print(f"ABS 2030 IPC0: {emi_ipc0 + emi_red} MtCO2eq")

# %%
"""
SYC
"""

# p. 8
ipc0_2000 = -0.564232
ipcmlulucf_2000 = 0.012540 - 0.837380
ipcm0el_2000 = ipc0_2000 - ipcmlulucf_2000
print(f"IPC0 2000: {ipc0_2000 :.6f} MtCO2eq")
print(f"IPCMLULUCF 2000: {ipcmlulucf_2000 :.6f} MtCO2eq")
print(f"IPCM0EL 2000: {ipcm0el_2000 :.6f} MtCO2eq")

# p. 11
ipc0_2005 = -0.502964
ipcm0el_2005 = 0.0310816
ipcmlulucf_2005 = f_lulucf(ipc0_2005, ipcm0el_2005)
print(f"\nIPC0 2005: {ipc0_2005 :.6f} MtCO2eq")
print(f"IPCMLULUCF 2005: {ipcmlulucf_2005 :.6f} MtCO2eq")
print(f"IPCM0EL 2005: {ipcm0el_2005 :.6f} MtCO2eq")

# p. 11
emi = {2005: .310816, 2030: .911985}
removal  = {2005: -.813780, 2030: -.773896}

ipc0 = {}
for yr in emi.keys():
    ipc0[yr] = emi[yr] + removal[yr]
    print(f"IPC0 {yr}: {ipc0[yr] :.6f} MtCO2eq")

red = -.188
tar_ipc0 = ipc0[2030] + red
print(f"ABS IPC0: {tar_ipc0 :.6f} MtCO2eq")

# %%
"""
TGO
"""

bau = 38.86136 # MtCO2eq
ABS = {'uncondi': 34.53328, 'condi': 27.62662}

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - bau :.5f} MtCO2eq")

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
"""
TLS
"""

emi_2015 = {'CO2': 0.46687, 'CH4': .54856, 'N2O': .46718}
emi_tot = sum([emi_2015[xx] for xx in emi_2015.keys()])
print(f"emi: {emi_tot} MtCO2eq")

# %%
"""
TZA
"""

emi_bau = 145.5 # MtCO2eq
red = {'worst': -.1, 'best': -.2}

for tar in red.keys():
    ABS = emi_bau * (1 + red[tar])
    print(f"ABS {tar}: {ABS :.3f} MtCO2eq")
    print(f"ABU {tar}: {ABS - emi_bau :.3f} MtCO2eq")

#%%
"""
USA
"""

RBY = {'worst': -.26, 'best': -.28}
emi2005_inclLU = 6200 # MtCO2eq, read from figure, p. 1.
for rge in RBY.keys():
   print(f"ABS inclLU {rge}: {emi2005_inclLU * (1+RBY[rge]) :.0f} MtCO2eq.") 


# %%
"""
NOR
"""

# ABS.
# From base year emissions and % reductions.
base = 52 # MtCO2eq
red_best = -.55
red_worst = -.50

ABS_best = base * (1+red_best)
ABS_worst = base * (1+red_worst)
print(f"ABS best: {ABS_best} MtCO2eq")
print(f"ABS worst: {ABS_worst} MtCO2eq")

print(f"ABY best: {ABS_best - base} MtCO2eq")
print(f"ABY worst: {ABS_worst - base} MtCO2eq")

# %%
"""
UGA
"""

ipc0_2000 = 36.5 # MtCO2eq.
ipcmlulucf_2000 = 10.6
ipcm0el_2000 = f_emi_exclLU(ipc0_2000, ipcmlulucf_2000)
print(f"IPCM0EL 2000: {ipcm0el_2000 :.1f} MtCO2eq")

ipc0_2030 = 77.3 # MtCO2eq, p. 17.
ipcmlulucf_2030 = 8 # p. 18.
ipcm0el_2030 = f_emi_exclLU(ipc0_2030, ipcmlulucf_2030)
print(f"IPCM0EL 2030: {ipcm0el_2030 :.1f} MtCO2eq")

ABU_energy = -3.2 # p. 18
ABU_forestry = -(16.9+22.2)/2
ABU_wetlands = -.4

ABU_ipcm0el = ABU_energy
ABU_ipc0 = ABU_energy + ABU_forestry + ABU_wetlands
print(f"ABU IPCM0EL: {ABU_ipcm0el :.1f} MtCO2eq")
print(f"ABU IPC0: {ABU_ipc0 :.1f} MtCO2eq")

ABS_ipcm0el = ipcm0el_2030 + ABU_ipcm0el
ABS_ipc0 = ipc0_2030 + ABU_ipc0
print(f"ABS IPCM0EL: {ABS_ipcm0el :.1f} MtCO2eq")
print(f"ABS IPC0: {ABS_ipc0 :.1f} MtCO2eq")

RBU_ipcm0el = ABU_ipcm0el/ipcm0el_2030*100
RBU_ipc0 = ABU_ipc0/ipc0_2030*100
print(f"RBU IPCM0EL: {RBU_ipcm0el :.1f}%")
print(f"RBU IPC0: {RBU_ipc0 :.1f}%")

# The given RBU is 22%, which is by how much ABS_ipc0 is smaller than ipc0_2030.
# But: the values are more in line with a 30% reduction...

# %%
"""
URY
"""

# ABU.
# Based on counterfactual scenario and un/conditional scenarios [p. 28].
# AR2.

print(f"ABU IPCM0EL unconditional: {41.8 - 81} MtCO2eq_SAR")
print(f"ABU IPCM0EL conditional: {39.0 - 81} MtCO2eq_SAR")
print(f"ABU IPC0 unconditional: {35.8 - 81} MtCO2eq_SAR")
print(f"ABU IPC0 conditional: {33.0 - 81} MtCO2eq_SAR")

print(f"RBU IPCM0EL unconditional: {100*(41.8 - 81)/81 :.1f}%")
print(f"RBU IPCM0EL conditional: {100*(39.0 - 81)/81 :.1f}%")
print(f"RBU IPC0 unconditional: {100*(35.8 - 81)/81 :.1f}%")
print(f"RBU IPC0 conditional: {100*(33.0 - 81)/81 :.1f}%")

# %%
"""
UKR
"""

# IPCMLULUCF from given IPC0 and IPCM0EL [p. 1].
ipc0 = {1990: 874.6, 2012: 375.4}
ipcm0el = {1990: 944.4, 2012: 402.7}

for year in ipcm0el.keys():
    print(f"IPCMLULUCF {year}: {f_lulucf(ipc0[year], ipcm0el[year]) :.3f} MtCO2eq")

# ABS.
# Calculated based on given baseyear emissions and % reduction.
ipcm0el = 944.4
ipc0 = 874.6
ipcmlulucf = -69.8
pc_red = -.4
pc_lev = 1 + pc_red
# Do not strengthen the sink.

# LULUCF is a sink in the base year. Everything is covered.
print(f"ABS IPC0: {ipcm0el*pc_lev + ipcmlulucf} MtCO2eq_AR4")

# %%
"""
TCD
"""

emi = {2010: {'energy': 0.66520, 'agri': 18.44800, 'lu': -10.90877, 'waste': 0.17519},
       2030: {'energy': 2.16500, 'agri': 43.42600, 'lu': -17.38748, 'waste': 0.45585},
       'uncondi': {'energy': 2.16500, 'agri': 38.21570, 'lu': -17.38748, 'waste': 0.45585},
       'condi': {'energy': 1.84025, 'agri': 30.39883, 'lu': -24.34248, 'waste': 0.40285}} # MtCO2eq, p. 12

emi_sum_ipcm0el = {}
for yr_condi in emi.keys():
    emi_tot = 0
    for cat in emi[yr_condi].keys():
        if cat != 'lu':
            emi_tot += emi[yr_condi][cat]
    
    emi_sum_ipcm0el[yr_condi] = emi_tot
    
    print(f"{yr_condi} IPCM0EL: {emi_tot :.5f} MtCO2eq")

emi_2030 = emi[2030]
emi_ipcm0el = sum([emi_2030[xx] for xx in emi_2030.keys() if xx != 'lu'])
emi_ipc0 = sum([emi_2030[xx] for xx in emi_2030.keys()])

print(f"ABU uncondi IPC0: {23.44907 - emi_ipc0 :.4f} MtCO2eq")
print(f"ABU condi IPC0: {8.22945 - emi_ipc0 :.4f} MtCO2eq")

ABU_uncondi = emi_sum_ipcm0el['uncondi'] - emi_ipcm0el
ABU_condi = emi_sum_ipcm0el['condi'] - emi_ipcm0el
print(f"ABU uncondi IPCM0EL: {ABU_uncondi :.4f} MtCO2eq")
print(f"ABU condi IPCM0EL: {ABU_condi :.4f} MtCO2eq")

print(f"RBU uncondi IPCM0EL: {ABU_uncondi / emi_ipcm0el * 100 :.1f}%")
print(f"RBU condi IPCM0EL: {ABU_condi / emi_ipcm0el * 100 :.1f}%")

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
"""
TUN
"""

# ABU from given baseline and ABS.
ABS = {
    'unconditional': {2025: 47.4, 2030: 62.2}, 
    'conditional': {2025: 35.0, 2030: 42.4}}
BL = {2025: 51.6, 2030: 68.2}

for condi in ABS.keys():
    data = ABS[condi]
    for year in data.keys():
        ABU = data[year] - BL[year]
        print(f"ABU {condi} {year}: {ABU :.3f} MtCO2eq_AR4")
        print(f"RBU {condi} {year}: {ABU/BL[year]*100 :.1f}%")
        

# %%
"""
VCT
"""

emi_bau = 0.6 # MtCO2eq
RBU = -.22
print(f"ABS: {emi_bau * (1+RBU) :.3f} MtCO2eq")
print(f"ABU: {emi_bau * RBU :.3f} MtCO2eq")

# %%
"""
VNM
"""

emi_bau = 787.4 # MtCO2eq
red = {'uncondi': -.08, 'condi': -.25}

for condi in red.keys():
    ABU = emi_bau * red[condi]
    print(f"ABU {condi}: {ABU} MtCO2eq")
    print(f"ABS {condi}: {emi_bau + ABU} MtCO2eq")

# %%
"""
WSM
"""

# Electricity subsector in 2014 was 13% of total:
elec = 0.055065 # MtCO2eq
pc = .13

print(f"Total emissions in 2014: {1/pc*elec :.6f} MtCO2eq")

# %%
"""
ZMB
"""

RBU = {'worst': -.25, 'best': -.47}
ABU = {'worst': -20, 'best': -38}

for rge in RBU.keys():
    emi_bau = 1/RBU[rge]*ABU[rge]
    print(f"{rge} BAU: {emi_bau :.1f} MtCO2eq")
    ABS = emi_bau + ABU[rge]
    print(f"{rge} ABS: {ABS :.1f} MtCO2eq")


# %%
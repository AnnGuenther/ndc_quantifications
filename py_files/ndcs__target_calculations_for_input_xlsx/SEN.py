# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
SEN
"""

# %%
# NDC2015

bau = {2025: 30.0, 2030: 37.5} # MtCO2eq, read from Figure 1, p. 14.
RBU = {'uncondi': {2025: -.04, 2030: -.05},
       'condi': {2025: -.15, 2030: -.21}}
for yr in bau.keys():
    for condi in RBU.keys():
        print(f"\n{yr} {condi} ABS: {bau[yr] * (1+RBU[condi][yr]) :.1f} MtCO2eq")
        print(f"{yr} {condi} ABU: {bau[yr] * RBU[condi][yr] :.1f} MtCO2eq")

# %%
# NDC2020

# p. 8
emi_exclLU = {1994: 9.3179, 2000: 13.298, 2005: 13.084}
emi_onlyLU = {1994: -5.997, 2000: -10.555, 2005: -11.434}
# calculate emi_inclLU:
emi_inclLU = {}
for year in emi_exclLU.keys():
    emi_inclLU[year] = emi_exclLU[year] + emi_onlyLU[year]
    print(f"emi inclLU {year}: {hpf.rnd(emi_inclLU[year], 4)} MtCO2eq")

# pp. 14: contributions per sector
bau = {
    'energie': {2025: 19.512, 2030: 23.927},
    'biomasse': {2025: 8.533, 2030: 8.867},
    'agriculture': {2025: 9.903, 2030: 10.600},
    'dechets': {2025: 2.189, 2030: 2.575},
    'ippu': {2025: 3.953, 2030: 3.953},
    'forestrie': {2025: -11.57311, 2030: -11.51066}}
tar_abs_uncondi = {
    'energie': {2025: 18.022, 2030: 21.523},
    'biomasse': {2025: 7.702, 2030: 7.621},
    'agriculture': {2025: 9.732, 2030: 10.350},
    'dechets': {2025: 1.948, 2030: 2.292},
    'ippu': {2025: 3.953, 2030: 3.953},
    'forestrie': {2025: -16.96712, 2030: -16.89432}}
tar_abs_condi = {
    'energie': {2025: 12.615, 2030: 14.048},
    'biomasse': {2025: 7.106, 2030: 6.652},
    'agriculture': {2025: 9.034, 2030: 9.329},
    'dechets': {2025: 0.759, 2030: 0.893},
    'ippu': {2025: 3.792, 2030: 3.631},
    'forestrie': {2025: -29.32821, 2030: -29.32821}}

# p. 14: Les émissions liées à la biomasse (production de charbon et de bois) sont comptabilisées au niveau du secteur de la foresterie.
# We only use 'forestrie' as onlyLU (in line with the historical values).
lu = ['forestrie']
nonlu = ['energie', 'biomasse', 'agriculture', 'dechets', 'ippu']

for year in [2025, 2030]:
    
    bau_onlyLU = sum([bau[xx][year] for xx in lu])
    bau_exclLU = sum([bau[xx][year] for xx in nonlu])
    bau_inclLU = bau_onlyLU + bau_exclLU
    
    print(f"\nBAU onlyLU {year}: {hpf.rnd(bau_onlyLU, 3)} MtCO2eq")
    print(f"BAU exclLU {year}: {hpf.rnd(bau_exclLU, 3)} MtCO2eq")
    print(f"BAU inclLU {year}: {hpf.rnd(bau_inclLU, 3)} MtCO2eq")
    
    abs_uc_exclLU = sum([tar_abs_uncondi[xx][year] for xx in nonlu])
    abs_c_exclLU = sum([tar_abs_condi[xx][year] for xx in nonlu])
    
    print(f"\nABS exclLU {year} unconditional: {hpf.rnd(abs_uc_exclLU, 3)} MtCO2eq")
    print(f"ABS exclLU {year} conditional: {hpf.rnd(abs_c_exclLU, 3)} MtCO2eq")
    
    abs_uc_inclLU = abs_uc_exclLU + sum([tar_abs_uncondi[xx][year] for xx in lu])
    abs_c_inclLU = abs_c_exclLU + sum([tar_abs_condi[xx][year] for xx in lu])
    
    print(f"\nABS inclLU {year} unconditional: {hpf.rnd(abs_uc_inclLU, 3)} MtCO2eq")
    print(f"ABS inclLU {year} conditional: {hpf.rnd(abs_c_inclLU, 3)} MtCO2eq")
    
    abu_uc_exclLU = abs_uc_exclLU - bau_exclLU
    abu_c_exclLU = abs_c_exclLU - bau_exclLU
    
    print(f"\nABU exclLU {year} unconditional: {hpf.rnd(abu_uc_exclLU, 3)} MtCO2eq")
    print(f"ABU exclLU {year} conditional: {hpf.rnd(abu_c_exclLU, 3)} MtCO2eq")
    
    abu_uc_inclLU = abs_uc_inclLU - bau_inclLU
    abu_c_inclLU = abs_c_inclLU - bau_inclLU
    
    print(f"\nABU inclLU {year} unconditional: {hpf.rnd(abu_uc_inclLU, 3)} MtCO2eq")
    print(f"ABU inclLU {year} conditional: {hpf.rnd(abu_c_inclLU, 3)} MtCO2eq")
    
    rbu_uc_exclLU = 100*abu_uc_exclLU/bau_exclLU
    rbu_c_exclLU = 100*abu_c_exclLU/bau_exclLU
    
    print(f"\nRBU exclLU {year} unconditional: {hpf.rnd(rbu_uc_exclLU, 1)}%")
    print(f"RBU exclLU {year} conditional: {hpf.rnd(rbu_c_exclLU, 1)}%")
    
    rbu_uc_inclLU = 100*abu_uc_inclLU/bau_inclLU
    rbu_c_inclLU = 100*abu_c_inclLU/bau_inclLU
    
    print(f"\nRBU inclLU {year} unconditional: {hpf.rnd(rbu_uc_inclLU, 1)}%")
    print(f"RBU inclLU {year} conditional: {hpf.rnd(rbu_c_inclLU, 1)}%")

# The aggregated values on p. 20 do not fit to the non-aggregated values ...
# Test:

bau_2030 = 37.7611405 # p. 20
forestrie = -11.51066
ippu = 3.953
dechets = 2.575
agri = 10.600
biomasse = 8.867
energy = 23.927
print(forestrie + ippu + dechets + agri + biomasse + energy)

# uncondi:
# given as emissions globales on p. 20
abs_2030_uncondi = 35.106
abs_energy = 21.523
abs_biomasse = 7.621
abs_agri = 10.350
abs_dechets = 2.292
abs_ippu = 3.953
abs_forestrie = -16.89432
print(abs_forestrie + abs_ippu + abs_dechets + abs_agri + abs_biomasse + abs_energy)
# test without forestrie
print(abs_ippu + abs_dechets + abs_agri + abs_biomasse + abs_energy)
# the aggregated values and values per sector don't fit ...

# The sum in Tableau 14 does not fit to sectoral values in Tableau 14!

# %%
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

meta = setup_metadata()

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
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

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
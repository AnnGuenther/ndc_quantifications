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

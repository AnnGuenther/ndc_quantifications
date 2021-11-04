# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 05/2021.
"""

# %%
from main_ndc_quantifications import main_ndc_quantifications
import pandas as pd
from pathlib import Path

# %%
"""
Script to run the NDC quantifications (main_ndc_quantifications).
This includes per-country target emissions, pathways, and globally aggregated pathways.

Put in the name(s) of the wanted input-option(s) here. You can run several options in a row.
Options stored in input_all_runs.csv.

e.g.,
main_ndc_quantifications('typeReclass_pccov100_inclUSA')
"""

input_options = pd.read_csv(
    Path(meta.path.py_files, 'MODIFY_INPUT_HERE', 'input_all_runs.csv'), index_col=0)

"""
Give some chosen option(s) here (have to be included or added in input_all_runs.csv).
Else all options will be calculated!

Give some chosen SSP scenario(s) here
(options: ['SSP1', 'SSP2', 'SSP3', 'SSP4', 'SSP5']).
Else all options will be calculated!
"""
chosen_options = ['typeMain_inclUSA']
chosen_ssps = ['SSP1']

for meta.ssps.chosen = \
    ['SSP1BLIMAGE', 'SSP2BLMESGB', 'SSP3BLAIMCGE', 'SSP4BLGCAM4', 'SSP5BLREMMP']:
    
    

# %%
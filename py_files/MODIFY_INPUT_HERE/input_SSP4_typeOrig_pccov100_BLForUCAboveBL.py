# -*- coding: utf-8 -*-

# %%
# Author: Annika Günther, annika.guenther@pik-potsdam.de

# %%
from time import gmtime, strftime
from setup_metadata import setup_metadata

meta = setup_metadata()

# %%
##### ALL THE FOLLOWING CAN BE MODIFIED #####

meta.ssps.chosen = 'SSP4BLGCAM4'

meta.output_folder = ('ndcs_' + 
    strftime("%Y%m%d_%H%M", gmtime()) + '_' + meta.ssps.chosen[:4] +
    '_typeOrig_pccov100_BLForUCAboveBL')

meta.method_pathways = 'constant_percentages'

meta.calculate_targets_for = {
    'use_it': True, 
    'countries': sorted(set(set(meta.isos.EARTH) - set(['USA'])))}

meta.ndcs_type_prioritisations = {
    'use_it': True, 
    'ndcs_type_prioritisations': ['TYPE_ORIG'], 
    'countries': 'all'}

meta.use_ndc_emissions_if_available = False

meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = True

meta.strengthen_targets = {'use_it': False}

meta.set_pccov_to_100 = {'use_it': True, 'countries': 'all'}

meta.groups_for_which_to_calculate_pathways = []

# %%
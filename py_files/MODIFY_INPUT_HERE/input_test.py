# -*- coding: utf-8 -*-

# %%
# Author: Annika Günther, annika.guenther@pik-potsdam.de

# %%
from time import gmtime, strftime
from setup_metadata import setup_metadata

meta = setup_metadata()

# %%
##### ALL THE FOLLOWING CAN BE MODIFIED #####

meta.ssps.chosen = 'SSP2BLMESGB'

meta.output_folder = ('ndcs_' + 
    strftime("%Y%m%d_%H%M", gmtime()) + '_' + meta.ssps.chosen[:4] + '_test')

cat_countries = ['ARG', 'AUS', 'BTN', 'BRA', 'CAN', 'CHL', 'CHN', 'CRI', 'EU28',
    'ETH', 'GMB', 'IND', 'IDN', 'JPN', 'KAZ', 'KEN', 'MEX', 'MAR',
    'NPL', 'NZL','NOR', 'PER', 'PHL', 'RUS', 'SAU', 'SGP', 'ZAF',
    'KOR', 'CHE', 'TUR', 'ARE', 'USA', 'UKR', 'VNM']
meta.calculate_targets_for = {'use_it': True, 'countries': cat_countries}

meta.ndcs_type_prioritisations = {
    'use_it': True, 
    'ndcs_type_prioritisations': ['RBY', 'RBU'], 
    'countries': 'all'}

meta.use_ndc_emissions_if_available = True

meta.set_pccov_to_100 = {'use_it': True, 'countries': 'all'}

meta.method_pathways = 'constant_emissions'

meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False

meta.use_baseline_if_target_above_bl = True

meta.strengthen_targets = {'use_it': True, 'pc': 50, 'how_to': 'multiply', 'countries': cat_countries}

meta.groups_for_which_to_calculate_pathways = ['ANNEXI']

meta.use_CAT_targets = {'use_it': True, 'countries': 'all'}

# %%
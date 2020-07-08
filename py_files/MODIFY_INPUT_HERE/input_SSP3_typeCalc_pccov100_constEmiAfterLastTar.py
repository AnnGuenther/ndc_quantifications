# -*- coding: utf-8 -*-

# %%
# Author: Annika Günther, annika.guenther@pik-potsdam.de

# %%
"""
Provide input for main_ndc_quantifications.py

UNITS:
Units for time series: emissions in Mt CO2eq, population in Pers, GDP in 2011GKD.
Units of NDC input data (infos_from_ndcs_default.xlsx): Mt CO2eq or tCO2eq / cap (all AEI targets are in emissions per capita).

PREPROCESSING:
If you want to do the preprocessing of data, run preprocessing.py, and update the 'folder_preprocess' in setup_metadata.py.
Else, the folder stored in setup_metadata.py will be used.
"""

# %%
from time import gmtime, strftime
from helpers_functions.isos.get_isos_for_groups import get_isos_for_groups
from setup_metadata import setup_metadata

# %%
##### NOTHING TO BE MODIFIED #####
# Set up the class 'meta', where metadata are stored (see setup_metadata.py).
meta = setup_metadata()

# %%
##### ALL THE FOLLOWING CAN BE MODIFIED #####

# %%
# Chose current ssp-scenario:
#meta.ssps.chosen = 'SSP1BLIMAGE'
#meta.ssps.chosen = 'SSP2BLMESGB'
meta.ssps.chosen = 'SSP3BLAIMCGE'
#meta.ssps.chosen = 'SSP4BLGCAM4'
#meta.ssps.chosen = 'SSP5BLREMMP'

# %%
# Output-folder (add something if you want)
meta.output_folder = ('ndc_quantifications_' + 
    strftime("%Y%m%d_%H%M", gmtime()) + '_' + meta.ssps.chosen[:4] +
    '_typeCalc_pccov100_constEmiAfterLastTar')

#%%
"""
Chose the method for the pathway calculations (per country pathways).

'constant_percentages':
    The percentage difference to the baseline emissions of the last available target year
    is kept constant.
'constant_emissions':
    The emissions of the last available target year are kept constant.

Default:
meta.method_pathways = 'constant_percentages'
"""

meta.method_pathways = 'constant_emissions'

# %%
"""
For which countries should targets be used for the calculation of emission pathways for group of countries?
For the others, the baseline emissions will be used.

countries: 'all', or e.g., ['EU28', 'AUS', 'CHN'], or e.g., get_isos_groups(['ANNEXI']).

Default:
meta.calculate_targets_for = {
    'use_it': True, 
    'countries': 'all'}

Example:
cat_countries = ['ARG', 'AUS', 'BTN', 'BRA', 'CAN', 'CHL', 'CHN', 'CRI', 'EU28',
    'ETH', 'GMB', 'IND', 'IDN', 'JPN', 'KAZ', 'KEN', 'MEX', 'MAR',
    'NPL', 'NZL','NOR', 'PER', 'PHL', 'RUS', 'SAU', 'SGP', 'ZAF',
    'KOR', 'CHE', 'TUR', 'ARE', 'USA', 'UKR', 'VNM']
meta.calculate_targets_for = {'use_it': True, 'countries': cat_countries}
"""

meta.calculate_targets_for = {
    'use_it': True, 
    'countries': sorted(set(set(meta.isos.EARTH) - set(['USA'])))}

# %%
"""
Which target-types should be prioritised in the calculation of group-pathways?

ndcs_type_prioritisations can be a certain target tpye (e.g., 'ABS'), or 'TYPE_ORIG' or 'TYPE_CALC'. 
Or several ordered options (only makes sense for != TYPE_ORIG and != TYPE_CALC).

One can chose from ['TYPE_ORIG', 'TYPE_CALC', 'ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI'].

If TYPE_ORIG: use the 'original target type' (what has been stated (+/-) 
in the NDC as target type).
If TYPE_CALC: use the target type that has been assessed to be the 'best 
suitable' (based on the NDC).
Explanation: e.g., when it is an RBU target, but the absolute target emissions are available 
(e.g., given value, or based on their BAU and %-reduction),
TYPE_ORIG can be RBU, and TYPE_CALC can be ABS. It can also have TYPE_ORIG is 
NGT and TYPE_CALC is ABU, as they quantified some reductions.
Iterating through ndc_type_prioritisations, and using TYPE_CALC if none of the iterations 
found target values for the current target type in the NDC input file.
If 'countries' is 'all', apply it to all countries. Else, give ISO3s, and it 
is only applied to those countries.
Else, the pathway is calculated based on TYPE_CALC.

Default:
meta.ndcs_type_prioritisations = {
    'use_it': True, 
    'ndcs_type_prioritisations': ['TYPE_CALC'], 
    'countries': 'all'}
"""

meta.ndcs_type_prioritisations = {
    'use_it': True, 
    'ndcs_type_prioritisations': ['TYPE_CALC'], 
    'countries': 'all'}

# %%
"""
Use NDC emissions data if available.
If TYPE_CALC is used set it to True, for TYPE_ORIG set it to False.
"""

meta.use_ndc_emissions_if_available = True

# %%
"""
For countries without unconditional target: use the baseline emissions for the unconditional 
pathway even if the conditional target is worse than the baseline (in 2030)?

Default:
meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False
"""

meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False

# %%
"""
The targets are strengthened by ndc_strengthen.

Chose between 'how_to': 'add' or 'multiply'.
'add': the reduction is increased by adding the value in 'pc'.
'multiply': the reduction is increased by multiplying with (100% + the value in 'pc').

If this results in a % reduction that exceeds 100%, it is set to 100% (meaning a total 
reduction of the covered part of emissions).

For absolute targets (ABS, ABU, AEI), it is not distinguished between 'add' and 'multiply'.

Default:
meta.strengthen_targets = {'use_it': False}
"""

meta.strengthen_targets = {'use_it': False}

#meta.strengthen_targets = {'use_it': False}
#meta.strengthen_targets = {'use_it': True, 
#   'pc': 5, 
#   'how_to': 'multiply',
#   'countries': 'all'}
#meta.strengthen_targets = {'use_it': True, 
#   'pc': 10,
#   'how_to': 'multiply',
#   'countries': ['EU28', 'CHN', 'IND', 'USA', 'AUS']}

# %%
"""
Predefine that the coverage used for the pathways is 100% for certain countries.
Only possible for relative targets / reductions.

Default:
meta.set_pccov_to_100 = {'use_it': False}
"""

#meta.set_pccov_to_100 = {'use_it': False}
meta.set_pccov_to_100 = {'use_it': True, 'countries': 'all'}
#meta.set_pccov_to_100 = {'use_it': True, 'countries': ['EU28', 'CHN', 'IND', 'USA', 'AUS']}

# %%
"""
Groups for which to get the pathways.
'EU28', 'EARTH', 'R5ASIA', 'R5LAM', 'R5MAF', 'R5OECD', 'R5REF' will be calculated per default.
The R5 regions are needed for the temperature pathways (PRIMAP Emissions Module / Climate Module).

One can chose some of the following groups:
'ANNEXI', 'ANNEXI_KAZ', 'AOSIS', 'AR5', 'AG', 'BRICS', 'EIG', 'G7', 'G20', 'G77',
'GRADUATED_LDCS', 'IMO', 'LDC', 'LLDC', 'NON_ANNEXI', 'OECD', 'OPEC', 'SIDS',
'UMBRELLA', 'UNFCCC', 'UN_REGIONAL_GROUPS', 'AILAC', 'ALBA', 'APG', 'BASIC', 'CACAM', 'CD', 
'CfRN', 'CVF', 'EEG', 'EIT', 'G77+China', 'GRULAC', 'KYOTO', 'LAS', 'LMDC', 'PA', 
'SICA', 'UN', 'WEOG'
And provide a list for
meta.groups_for_which_to_calculate_pathways

Default:
meta.groups_for_which_to_calculate_pathways = []
"""

meta.groups_for_which_to_calculate_pathways = []

# %%
# -*- coding: utf-8 -*-

# %%
# Author: Annika Günther, annika.guenther@pik-potsdam.de

# %%
"""
**Provide input for NDCmitiQ: main_ndc_quantifications.py**

UNITS:
Units for time series: emissions in Mt CO2eq, population in Pers, GDP in 2011GKD.
Units of NDC input data (meta.ndcs.path_to_infos_from_ndcs): Mt CO2eq or tCO2eq / cap (all AEI targets are in emissions per capita).

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
"""
**meta.ssps.chosen**

Chose current ssp-scenario.
"""

#meta.ssps.chosen = 'SSP1BLIMAGE'
meta.ssps.chosen = 'SSP2BLMESGB'
#meta.ssps.chosen = 'SSP3BLAIMCGE'
#meta.ssps.chosen = 'SSP4BLGCAM4'
#meta.ssps.chosen = 'SSP5BLREMMP'

# %%
"""
**meta.output_folder**

Output-folder (add something if you want).
"""
meta.output_folder = ('ndcs_' + 
    strftime("%Y%m%d_%H%M", gmtime()) + '_' + meta.ssps.chosen[:4] + '_default')

# %%
"""
**meta.calculate_targets_for**

For which countries should targets be used for the calculation of emission pathways for group of countries?
For the others, the baseline emissions will be used.

countries: 'all', or e.g., ['EU28', 'AUS', 'CHN'], or e.g., get_isos_groups(['ANNEXI']).

Default:
meta.calculate_targets_for = {'use_it': True, 'countries': 'all'}

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
**meta.ndcs_type_prioritisations**

Which target-types should be prioritised in the calculation of group-pathways?

ndcs_type_prioritisations can be a certain target tpye (e.g., 'ABS'), or 'TYPE_MAIN' or 'TYPE_RECLASS'. 
Or several ordered options (only makes sense for != TYPE_MAIN and != TYPE_RECLASS).

One can chose from ['TYPE_MAIN', 'TYPE_RECLASS', 'ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI'].

If TYPE_MAIN: use the 'main target type' (what has been stated (+/-) 
in the NDC as target type).
If TYPE_RECLASS: use the target type that has been assessed to be the 'best 
suitable' for the quantification (based on the NDC).
Explanation: e.g., when it is an RBU target, but the absolute target emissions are available 
(e.g., given value, or based on their BAU and %-reduction),
TYPE_MAIN can be RBU, and TYPE_RECLASS can be ABS. It can also have TYPE_MAIN is 
NGT and TYPE_RECLASS is ABU, as they quantified some reductions.
Iterating through ndc_type_prioritisations, and using TYPE_RECLASS if none of the iterations 
found target values for the current target type in the NDC input file.
If 'countries' is 'all', apply it to all countries. Else, give ISO3s, and it 
is only applied to those countries.
Else, the pathway is calculated based on TYPE_RECLASS.

Default:
meta.ndcs_type_prioritisations = {'use_it': True, 'ndcs_type_prioritisations': ['TYPE_RECLASS'], 'countries': 'all'}
"""

meta.ndcs_type_prioritisations = {
    'use_it': True, 
    'ndcs_type_prioritisations': ['TYPE_RECLASS'], 
    'countries': 'all'}

# %%
"""
**meta.use_ndc_emissions_if_available**

Use NDC emissions data if available.
If TYPE_RECLASS is used set it to True, for TYPE_MAIN set it to False.
"""

meta.use_ndc_emissions_if_available = True

# %%
"""
**meta.set_pccov_to_100**

Predefine that the coverage used for the pathways is 100% for certain countries.
Only possible for relative targets / reductions.

Default:
meta.set_pccov_to_100 = {'use_it': False}
"""

meta.set_pccov_to_100 = {'use_it': False}
#meta.set_pccov_to_100 = {'use_it': True, 'countries': 'all'}
#meta.set_pccov_to_100 = {'use_it': True, 'countries': ['EU28', 'CHN', 'IND', 'USA', 'AUS']}

#%%
"""
**meta.method_pathways**

Chose the method for the pathway calculations (per country pathways).

'constant_percentages':
    The percentage difference to the baseline emissions of the last available target year
    is kept constant.
'constand_difference':
    The absolute difference to the baseline emissions of the last available target year
    is kept constant.
'constant_emissions':
    The emissions of the last available target year are kept constant.

Default:
meta.method_pathways = 'constant_percentages'
"""

meta.method_pathways = 'constant_percentages'

# %%
"""
**meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi**

For countries without unconditional target but with conditional target: 
use the baseline emissions for the unconditional pathway 
even if the conditional target is worse than the baseline (in 2030)?
Default:
    if the cond ptw is above bl, the uncond ptw = cond ptw & 
    if the cond ptw is below bl, the uncond ptw = bl.

Default:
meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False
"""

meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False

# %%
"""
**meta.use_baseline_if_target_above_bl**

If a country's target emissions (considering pathway in 2030) lies above the 
baseline, use the baseline. By comparing with a run without this swith, one can
check how much 'surplus' countries have (that they might want to sell).
Tests every mitigated pathway individually (so un/conditional best/worst).
Default:
    use target even if it is worse than the baseline emissions

Default:
meta.use_baseline_if_target_above_bl = False
"""

meta.use_baseline_if_target_above_bl = False

# %%
"""
**meta.strengthen_targets**

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
**meta.groups_for_which_to_calculate_pathways**

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
"""
**meta.use_CAT_targets**

Use the https://climateactiontracker.org/ target quantifications instead of our
quantifications for all countries that have values available, or for selected
countries.

Default:
    meta.use_CAT_targets = {'use_it': False}
"""

meta.use_CAT_targets = {'use_it': False}
#meta.use_CAT_targets = {'use_it': True, 'countries': 'all'}
#meta.use_CAT_targets = {'use_it': True, 'countries': ['EU27', 'CHN', 'IND', 'USA', 'AUS']}

# %%
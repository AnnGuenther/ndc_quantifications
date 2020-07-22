# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last update in 06/2020.
"""

# %%
"""
Only works at first import!
"""

# %%
import additional_scripts.for_paper_general_stuff
import additional_scripts.national_share_of_emissions_per_gas_and_sector
import additional_scripts.ndcs_covered_emissions_global

import additional_scripts.plotting.plot_timeseries__ssps
# Takes a lot of time:
#import additional_scripts.plotting.plot_maps__global_and_national_shares

import additional_scripts.plotting.ndcs.plot_timeseries__emissions_per_target_type
import additional_scripts.plotting.ndcs.plot_timeseries__pop_gdp_per_target_type
import additional_scripts.plotting.ndcs.plot_ndcs__IND # Includes output from the module.
import additional_scripts.plotting.ndcs.plot_ndcs__difference_between_baseline_in_ndcs_and_ssps
import additional_scripts.plotting.ndcs.plot_tables__ndc_info
import additional_scripts.plotting.ndcs.plot_maps__ndc_info
import additional_scripts.plotting.ndcs.plot_ndcs__pathways_SSP1to5_inclBL_withRange100pc # Includes output from the module.

# %%
#import preprocessing_general
#import preprocessing_current_pc_cov

#import _to_be_run

# %%

# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2021.
"""

# %%
from main_ndc_quantifications import main_ndc_quantifications

# %%
"""
Script to run the NDC quantifications (main_ndc_quantifications).
This includes per-country target emissions, pathways, and globally aggregated pathways.

Put in the name(s) of the wanted input-file(s) here. You can run several input-files in a row.

Default:
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', '')
"""

"""
Additional runs with the setup of the first paper submission from November 2020.
"""

# SSP1
main_ndc_quantifications('input_SSP1_typeMain_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP1_typeMain_CAT', '')
main_ndc_quantifications('input_SSP1_typeMain_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_CAT', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP1_typeReclass_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP1_typeReclass_CAT', '')
main_ndc_quantifications('input_SSP1_typeReclass_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_CAT', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_constDiffAfterLastTar', '')
# SSP2
main_ndc_quantifications('input_SSP2_typeMain_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP2_typeMain_CAT', '')
main_ndc_quantifications('input_SSP2_typeMain_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_CAT', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP2_typeReclass_CAT', '')
main_ndc_quantifications('input_SSP2_typeReclass_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_CAT', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_constDiffAfterLastTar', '')
# SSP3
main_ndc_quantifications('input_SSP3_typeMain_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP3_typeMain_CAT', '')
main_ndc_quantifications('input_SSP3_typeMain_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_CAT', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeReclass_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP3_typeReclass_CAT', '')
main_ndc_quantifications('input_SSP3_typeReclass_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_CAT', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_constDiffAfterLastTar', '')
# SSP4
main_ndc_quantifications('input_SSP4_typeReclass_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP4_typeReclass_CAT', '')
main_ndc_quantifications('input_SSP4_typeReclass_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_CAT', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeMain_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP4_typeMain_CAT', '')
main_ndc_quantifications('input_SSP4_typeMain_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_CAT', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_constDiffAfterLastTar', '')
# SSP5
main_ndc_quantifications('input_SSP5_typeMain_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP5_typeMain_CAT', '')
main_ndc_quantifications('input_SSP5_typeMain_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_CAT', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeReclass_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP5_typeReclass_CAT', '')
main_ndc_quantifications('input_SSP5_typeReclass_constDiffAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_BLForTarAboveBL', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_CAT', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_constDiffAfterLastTar', '')

# %%

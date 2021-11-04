# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 11/2020.
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

# SSP1
main_ndc_quantifications('input_SSP1_typeMain', '')
main_ndc_quantifications('input_SSP1_typeMain', 'FAO')
main_ndc_quantifications('input_SSP1_typeMain', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeMain_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP1_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP1_typeMain_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeReclass', '')
main_ndc_quantifications('input_SSP1_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP1_typeReclass', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeReclass_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP1_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_constEmiAfterLastTar', '')
# SSP2
main_ndc_quantifications('input_SSP2_typeMain', '')
main_ndc_quantifications('input_SSP2_typeMain', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeMain_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP2_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass', '')
main_ndc_quantifications('input_SSP2_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeReclass_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP2_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_constEmiAfterLastTar', '')
# SSP3
main_ndc_quantifications('input_SSP3_typeMain', '')
main_ndc_quantifications('input_SSP3_typeMain', 'FAO')
main_ndc_quantifications('input_SSP3_typeMain', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeMain_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP3_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP3_typeMain_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeReclass', '')
main_ndc_quantifications('input_SSP3_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP3_typeReclass', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeReclass_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP3_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_constEmiAfterLastTar', '')
# SSP4
main_ndc_quantifications('input_SSP4_typeReclass', '')
main_ndc_quantifications('input_SSP4_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP4_typeReclass', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeReclass_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP4_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeMain', '')
main_ndc_quantifications('input_SSP4_typeMain', 'FAO')
main_ndc_quantifications('input_SSP4_typeMain', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeMain_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP4_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP4_typeMain_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_constEmiAfterLastTar', '')
# SSP5
main_ndc_quantifications('input_SSP5_typeMain', '')
main_ndc_quantifications('input_SSP5_typeMain', 'FAO')
main_ndc_quantifications('input_SSP5_typeMain', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeMain_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP5_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP5_typeMain_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeReclass', '')
main_ndc_quantifications('input_SSP5_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP5_typeReclass', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeReclass_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP5_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_BLForUCAboveBL', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_constEmiAfterLastTar', '')

# %%

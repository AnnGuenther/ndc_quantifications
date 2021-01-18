# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
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
main_ndc_quantifications('input_SSP1_typeMain_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeMain_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP1_typeMain_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeMain_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeMain_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeMain_pccov100_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP1_typeReclass_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeReclass_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP1_typeReclass_pccov100_constEmiAfterLastTar_inclUSA', '')
# SSP2
main_ndc_quantifications('input_SSP2_typeMain_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeMain_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeMain_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeMain_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeReclass_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_constEmiAfterLastTar_inclUSA', '')
# SSP3
main_ndc_quantifications('input_SSP3_typeMain_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeMain_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP3_typeMain_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeMain_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeMain_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeMain_pccov100_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP3_typeReclass_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeReclass_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP3_typeReclass_pccov100_constEmiAfterLastTar_inclUSA', '')
# SSP4
main_ndc_quantifications('input_SSP4_typeReclass_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeReclass_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP4_typeReclass_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeReclass_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeReclass_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeReclass_pccov100_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP4_typeMain_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeMain_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP4_typeMain_pccov100_constEmiAfterLastTar_inclUSA', '')
# SSP5
main_ndc_quantifications('input_SSP5_typeMain_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeMain_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP5_typeMain_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeMain_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeMain_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeMain_pccov100_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP5_typeReclass_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeReclass_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_constEmiAfterLastTar_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_inclUSA', 'FAO')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_inclUSA', 'UNFCCC')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_BLForUCAboveBL_inclUSA', '')
main_ndc_quantifications('input_SSP5_typeReclass_pccov100_constEmiAfterLastTar_inclUSA', '')

# %%

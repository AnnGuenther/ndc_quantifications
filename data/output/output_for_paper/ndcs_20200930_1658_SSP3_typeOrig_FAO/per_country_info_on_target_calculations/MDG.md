

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -31.728041310304093 (-30 MtCO2eq_SAR)
- ndc_value_inclLU: -96.24172530792242 (-91 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [23.36770243 23.36770243]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_refyr = -25.964297574961034
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_taryr = -25.964297574961034
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 49.332
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 49.332 + -31.728041310304093 = 17.603958689695908 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 23.367702425038967
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 23.367702425038967 + -96.24172530792242 = -72.87402288288345
- tar_emi_exclLU = ndc_value_exclLU = 17.603958689695908
- tar_emi_inclLU = ndc_value_inclLU = -72.87402288288345
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 17.603958689695908
- tar_emi_inclLU = -72.87402288288345

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 194.81651925352918 (184.206 MtCO2eq_SAR)
- ndc_value_inclLU: -72.87402288288345 (-68.905 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [23.36770243 23.36770243]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_refyr = -25.964297574961034
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_taryr = -25.964297574961034
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 194.81651925352918
- tar_emi_inclLU = ndc_value_inclLU = -72.87402288288345
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 194.81651925352918
- tar_emi_inclLU = -72.87402288288345

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -14.0 (-14%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [23.36770243 23.36770243]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -14.0 / 100. = 0.86
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_refyr = -25.964297574961034
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 23.367702425038967 - 49.332 = -25.964297574961034
    - bl_onlyLU_taryr = -25.964297574961034
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 49.332 * 0.998068191 = 49.236699998412
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 49.332 * (1 - 0.998068191) = 0.09530000158800032
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.86 * 49.236699998412 + 0.09530000158800032 = 42.43886200022232
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 49.236699998412 + -25.964297574961034 + 0.09530000158800032 = nan
- tar_emi_exclLU = ndc_value_exclLU = 42.43886200022232
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([42.43886200022232, -25.964297574961034]) = 16.47456442526129
- tar_emi_exclLU = 42.43886200022232
- tar_emi_inclLU = 16.47456442526129
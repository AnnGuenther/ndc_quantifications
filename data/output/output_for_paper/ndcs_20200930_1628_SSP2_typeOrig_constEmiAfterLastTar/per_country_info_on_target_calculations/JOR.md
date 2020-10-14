

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -0.765 (-0.765 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 51.028
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 51.028 + -0.765 = 50.263
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 50.263
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([50.263, - -0.9432000000000045]) = 51.2062.
- tar_emi_exclLU = 51.2062
- tar_emi_inclLU = 50.263

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -7.144 (-7.144 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 51.028
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 51.028 + -7.144 = 43.884
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 43.884
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([43.884, - -0.9432000000000045]) = 44.827200000000005.
- tar_emi_exclLU = 44.827200000000005
- tar_emi_inclLU = 43.884

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 50.263 (50.263 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 50.263
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([50.263, - -0.9432000000000045]) = 51.2062.
- tar_emi_exclLU = 51.2062
- tar_emi_inclLU = 50.263

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 43.884 (43.884 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 43.884
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([43.884, - -0.9432000000000045]) = 44.827200000000005.
- tar_emi_exclLU = 44.827200000000005
- tar_emi_inclLU = 43.884

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -1.5 (-1.5%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -1.5 / 100. = 0.985
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 51.9712 * 1.0 = 51.9712
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 51.9712 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 51.9712 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.985 * 51.9712 + -0.9432000000000045 + 0.0 = 50.248432
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 50.248432
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([50.248432, - -0.9432000000000045]) = 51.191632000000006.
- tar_emi_exclLU = 51.191632000000006
- tar_emi_inclLU = 50.248432

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -14.0 (-14%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [51.028 51.028]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -14.0 / 100. = 0.86
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_refyr = -0.9432000000000045
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.028 - 51.9712 = -0.9432000000000045
    - bl_onlyLU_taryr = -0.9432000000000045
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 51.9712 * 1.0 = 51.9712
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 51.9712 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 51.9712 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.86 * 51.9712 + -0.9432000000000045 + 0.0 = 43.752032
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 43.752032
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([43.752032, - -0.9432000000000045]) = 44.695232000000004.
- tar_emi_exclLU = 44.695232000000004
- tar_emi_inclLU = 43.752032
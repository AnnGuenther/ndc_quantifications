

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: -14.55 (-14.550 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 145.5
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 145.5 + -14.55 = 130.95 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 130.95
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([130.95, 222.33137142857143]) = 353.28137142857145
- tar_emi_exclLU = 130.95
- tar_emi_inclLU = 353.28137142857145

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -29.1 (-29.100 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 145.5
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 145.5 + -29.1 = 116.4 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 116.4
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([116.4, 222.33137142857143]) = 338.73137142857144
- tar_emi_exclLU = 116.4
- tar_emi_inclLU = 338.73137142857144

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: 130.95 (130.950 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 130.95
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([130.95, 222.33137142857143]) = 353.28137142857145
- tar_emi_exclLU = 130.95
- tar_emi_inclLU = 353.28137142857145

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 116.4 (116.400 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 116.4
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([116.4, 222.33137142857143]) = 338.73137142857144
- tar_emi_exclLU = 116.4
- tar_emi_inclLU = 338.73137142857144

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: -10.0 (-10%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -10.0 / 100. = 0.9
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 155.4208 * 1.0 = 155.4208
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 155.4208 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.9 * 155.4208 + 0.0 = 139.87872000000002
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (155.4208 + 222.33137142857143) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 139.87872000000002
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([139.87872000000002, 222.33137142857143]) = 362.21009142857145
- tar_emi_exclLU = 139.87872000000002
- tar_emi_inclLU = 362.21009142857145

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -20.0 (-20%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [145.5 145.5]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.0 / 100. = 0.8
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_refyr = 222.33137142857143
    - emi_onlyLU 2030: external_emi_onlyLU used (222.33137142857143).
    - bl_onlyLU_taryr = 222.33137142857143
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 155.4208 * 1.0 = 155.4208
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 155.4208 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8 * 155.4208 + 0.0 = 124.33664000000002
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (155.4208 + 222.33137142857143) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 124.33664000000002
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([124.33664000000002, 222.33137142857143]) = 346.66801142857145
- tar_emi_exclLU = 124.33664000000002
- tar_emi_inclLU = 346.66801142857145
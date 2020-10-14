

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
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 131.0895 * 1.0 = 131.0895
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 131.0895 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.9 * 131.0895 + 0.0 = 117.98055
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (131.0895 + 222.33137142857143) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 117.98055
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([117.98055, 222.33137142857143]) = 340.3119214285714
- tar_emi_exclLU = 117.98055
- tar_emi_inclLU = 340.3119214285714

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
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 131.0895 * 1.0 = 131.0895
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 131.0895 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8 * 131.0895 + 0.0 = 104.8716
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (131.0895 + 222.33137142857143) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 104.8716
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([104.8716, 222.33137142857143]) = 327.20297142857146
- tar_emi_exclLU = 104.8716
- tar_emi_inclLU = 327.20297142857146
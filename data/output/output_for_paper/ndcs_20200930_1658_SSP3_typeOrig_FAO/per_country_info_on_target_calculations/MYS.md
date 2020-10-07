

## tar_type_used: REI, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -35.0 (-35%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [300.26283083          nan]
  - ndcs_emi_exclLU for refyr and taryr: [273.5644106         nan]
  - ndcs_emi_onlyLU for refyr and taryr: [26.69842023         nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.0 / 100. = 0.65
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (26.698420230194024).
    - bl_onlyLU_refyr = 26.698420230194024
    - emi_onlyLU 2030: external_emi_onlyLU used (-112.13901142857144).
    - bl_onlyLU_taryr = -112.13901142857144
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 293.0196 * 0.996686194 = 292.04858989140246
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 443.1277 * (1 - 0.9931484759999999) = 3.036100071614848
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 1291091119056.1208 / 414550406250.0 = 3.114436989063066
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.114436989063066 * nan * 292.04858989140246 + 3.036100071614848 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.114436989063066 * 0.65 * (292.04858989140246 + 26.698420230194024) + 3.036100071614848 = 648.3024610809886
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 648.3024610809886
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([648.3024610809886, - -112.13901142857144]) = 760.44147250956.
- tar_emi_exclLU = 760.44147250956
- tar_emi_inclLU = 648.3024610809886

## tar_type_used: REI, refyr: 2005, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -45.0 (-45%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [300.26283083          nan]
  - ndcs_emi_exclLU for refyr and taryr: [273.5644106         nan]
  - ndcs_emi_onlyLU for refyr and taryr: [26.69842023         nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -45.0 / 100. = 0.55
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (26.698420230194024).
    - bl_onlyLU_refyr = 26.698420230194024
    - emi_onlyLU 2030: external_emi_onlyLU used (-112.13901142857144).
    - bl_onlyLU_taryr = -112.13901142857144
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 293.0196 * 0.996686194 = 292.04858989140246
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 443.1277 * (1 - 0.9931484759999999) = 3.036100071614848
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 1291091119056.1208 / 414550406250.0 = 3.114436989063066
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.114436989063066 * nan * 292.04858989140246 + 3.036100071614848 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.114436989063066 * 0.55 * (292.04858989140246 + 26.698420230194024) + 3.036100071614848 = 549.0307132333927
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 549.0307132333927
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([549.0307132333927, - -112.13901142857144]) = 661.1697246619641.
- tar_emi_exclLU = 661.1697246619641
- tar_emi_inclLU = 549.0307132333927
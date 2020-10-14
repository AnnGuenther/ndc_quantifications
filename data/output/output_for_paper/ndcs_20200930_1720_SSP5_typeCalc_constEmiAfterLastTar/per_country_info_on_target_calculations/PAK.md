

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -320.6 (-320.60 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [1603. 1603.]
  - ndcs_emi_exclLU for refyr and taryr: [1574. 1574.]
  - ndcs_emi_onlyLU for refyr and taryr: [29. 29.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_refyr = 29.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_taryr = 29.0
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 1603.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 1603.0 + -320.6 = 1282.4
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 1282.4
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([1282.4, - 29.0]) = 1253.4.
- tar_emi_exclLU = 1253.4
- tar_emi_inclLU = 1282.4

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 1282.4 (1282.4 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [1603. 1603.]
  - ndcs_emi_exclLU for refyr and taryr: [1574. 1574.]
  - ndcs_emi_onlyLU for refyr and taryr: [29. 29.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_refyr = 29.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_taryr = 29.0
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 1282.4
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([1282.4, - 29.0]) = 1253.4.
- tar_emi_exclLU = 1253.4
- tar_emi_inclLU = 1282.4

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -20.0 (-20%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [1603. 1603.]
  - ndcs_emi_exclLU for refyr and taryr: [1574. 1574.]
  - ndcs_emi_onlyLU for refyr and taryr: [29. 29.]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -20.0 / 100. = 0.8
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_refyr = 29.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (29.0).
    - bl_onlyLU_taryr = 29.0
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1574.0 * 0.993195948 = 1563.290422152
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1574.0 * (1 - 0.993195948) = 10.709577848000007
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 1563.290422152 + 10.709577848000007 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8 * (1563.290422152 + 29.0) + 10.709577848000007 = 1284.5419155696002
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 1284.5419155696002
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([1284.5419155696002, - 29.0]) = 1255.5419155696002.
- tar_emi_exclLU = 1255.5419155696002
- tar_emi_inclLU = 1284.5419155696002
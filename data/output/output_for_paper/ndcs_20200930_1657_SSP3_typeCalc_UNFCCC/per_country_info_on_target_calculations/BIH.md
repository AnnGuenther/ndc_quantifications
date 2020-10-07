

## tar_type_used: RBY, refyr: 1990, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 18.0 (+18%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [26.61996  34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [34.04349  40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-7.42353 -6.47   ]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + 18.0 / 100. = 1.18
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-7.42353).
    - bl_onlyLU_refyr = -7.42353
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 35.7405 * 0.979524335 = 35.0086894950675
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.852188 * (1 - 0.943488555) = 2.308616175291662
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 35.0086894950675 + 2.308616175291662 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 1.18 * 35.0086894950675 + -7.42353 + 2.308616175291662 = 36.19533977947131
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 36.19533977947131
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([36.19533977947131, - -6.47]) = 42.66533977947131.
- tar_emi_exclLU = 42.66533977947131
- tar_emi_inclLU = 36.19533977947131

## tar_type_used: RBY, refyr: 1990, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -3.0 (-3%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [26.61996  34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [34.04349  40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-7.42353 -6.47   ]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -3.0 / 100. = 0.97
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-7.42353).
    - bl_onlyLU_refyr = -7.42353
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 35.7405 * 0.979524335 = 35.0086894950675
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.852188 * (1 - 0.943488555) = 2.308616175291662
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 35.0086894950675 + 2.308616175291662 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.97 * 35.0086894950675 + -7.42353 + 2.308616175291662 = 28.843514985507134
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 28.843514985507134
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([28.843514985507134, - -6.47]) = 35.31351498550713.
- tar_emi_exclLU = 35.31351498550713
- tar_emi_inclLU = 28.843514985507134

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -1.6697333624492292 (-1.634 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 34.382188
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 34.382188 + -1.6697333624492292 = 32.71245463755077
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 32.71245463755077
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([32.71245463755077, - -6.47]) = 39.18245463755077.
- tar_emi_exclLU = 39.18245463755077
- tar_emi_inclLU = 32.71245463755077

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -8.975072290325325 (-8.783 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 34.382188
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 34.382188 + -8.975072290325325 = 25.407115709674674
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 25.407115709674674
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([25.407115709674674, - -6.47]) = 31.877115709674673.
- tar_emi_exclLU = 31.877115709674673
- tar_emi_inclLU = 25.407115709674674

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 33.46415431669973 (32.748 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 33.46415431669973
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([33.46415431669973, - -6.47]) = 39.934154316699725.
- tar_emi_exclLU = 39.934154316699725
- tar_emi_inclLU = 33.46415431669973

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 26.158815388823637 (25.599 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 26.158815388823637
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([26.158815388823637, - -6.47]) = 32.62881538882364.
- tar_emi_exclLU = 32.62881538882364
- tar_emi_inclLU = 26.158815388823637

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -2.0 (-2%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.0 / 100. = 0.98
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.852188 * 0.943488555 = 38.54357182470834
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.852188 * (1 - 0.943488555) = 2.308616175291662
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 38.54357182470834 + 2.308616175291662 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.98 * 38.54357182470834 + -6.47 + 2.308616175291662 = 33.61131656350583
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 33.61131656350583
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([33.61131656350583, - -6.47]) = 40.08131656350583.
- tar_emi_exclLU = 40.08131656350583
- tar_emi_inclLU = 33.61131656350583

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -23.0 (-23%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [34.382188 34.382188]
  - ndcs_emi_exclLU for refyr and taryr: [40.852188 40.852188]
  - ndcs_emi_onlyLU for refyr and taryr: [-6.47 -6.47]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -23.0 / 100. = 0.77
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_refyr = -6.47
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47).
    - bl_onlyLU_taryr = -6.47
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.852188 * 0.943488555 = 38.54357182470834
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.852188 * (1 - 0.943488555) = 2.308616175291662
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 38.54357182470834 + 2.308616175291662 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.77 * 38.54357182470834 + -6.47 + 2.308616175291662 = 25.517166480317083
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 25.517166480317083
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([25.517166480317083, - -6.47]) = 31.987166480317082.
- tar_emi_exclLU = 31.987166480317082
- tar_emi_inclLU = 25.517166480317083
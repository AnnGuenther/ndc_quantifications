

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -9.592228236502176 (-9.130 MtCO2eq_SAR)
- ndc_value_inclLU: -11.430826200782441 (-10.880 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 80.79745019714824
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 80.79745019714824 + -9.592228236502176 = 71.20522196064606 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([80.79745019714824, 45.964949107006596]) = 126.76239930415483
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 126.76239930415483 + -11.430826200782441 = 115.33157310337239
- tar_emi_exclLU = ndc_value_exclLU = 71.20522196064606
- tar_emi_inclLU = ndc_value_inclLU = 115.33157310337239
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 71.20522196064606
- tar_emi_inclLU = 115.33157310337239

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -16.894088723215223 (-16.080 MtCO2eq_SAR)
- ndc_value_inclLU: -26.087078544616542 (-24.830 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 80.79745019714824
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 80.79745019714824 + -16.894088723215223 = 63.90336147393302 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([80.79745019714824, 45.964949107006596]) = 126.76239930415483
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 126.76239930415483 + -26.087078544616542 = 100.67532075953828
- tar_emi_exclLU = ndc_value_exclLU = 63.90336147393302
- tar_emi_inclLU = ndc_value_inclLU = 100.67532075953828
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 63.90336147393302
- tar_emi_inclLU = 100.67532075953828

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 71.20522196064606 (67.774 MtCO2eq_SAR)
- ndc_value_inclLU: 115.33157310337239 (109.774 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 71.20522196064606
- tar_emi_inclLU = ndc_value_inclLU = 115.33157310337239
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 71.20522196064606
- tar_emi_inclLU = 115.33157310337239

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 63.90336147393301 (60.824 MtCO2eq_SAR)
- ndc_value_inclLU: 100.67532075953828 (95.824 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 63.90336147393301
- tar_emi_inclLU = ndc_value_inclLU = 100.67532075953828
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 63.90336147393301
- tar_emi_inclLU = 100.67532075953828

## tar_type_used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -9.0 (-9%)
- ndc_value_inclLU: -10.0 (-10%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -9.0 / 100. = 0.91
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.0 / 100. = 0.9
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 80.79745019714824 * 0.990606703 = 80.03849575060372
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 80.79745019714824 * (1 - 0.990606703) = 0.7589544465445238
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.91 * 80.03849575060372 + 0.7589544465445238 = 73.5939855795939
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.9 * (80.03849575060372 + 45.964949107006596) + 0.7589544465445238 = 114.1620548183938
- tar_emi_exclLU = ndc_value_exclLU = 73.5939855795939
- tar_emi_inclLU = ndc_value_inclLU = 114.1620548183938
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 73.5939855795939
- tar_emi_inclLU = 114.1620548183938

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -20.9 (-20.9%)
- ndc_value_inclLU: -26.0 (-26%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [80.7974502 80.7974502]
  - ndcs_emi_onlyLU for refyr and taryr: [45.96494911 45.96494911]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.9 / 100. = 0.791
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -26.0 / 100. = 0.74
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_refyr = 45.964949107006596
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596).
    - bl_onlyLU_taryr = 45.964949107006596
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 80.79745019714824 * 0.990606703 = 80.03849575060372
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 80.79745019714824 * (1 - 0.990606703) = 0.7589544465445238
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.791 * 80.03849575060372 + 0.7589544465445238 = 64.06940458527207
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.74 * (80.03849575060372 + 45.964949107006596) + 0.7589544465445238 = 94.00150364117614
- tar_emi_exclLU = ndc_value_exclLU = 64.06940458527207
- tar_emi_inclLU = ndc_value_inclLU = 94.00150364117614
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 64.06940458527207
- tar_emi_inclLU = 94.00150364117614
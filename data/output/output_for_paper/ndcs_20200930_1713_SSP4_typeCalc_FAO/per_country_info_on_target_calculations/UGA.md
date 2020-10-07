

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -3.496451917192439 (-3.2 MtCO2eq_SAR)
- ndc_value_inclLU: -25.240012277232918 (-23.1 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [84.46116662 84.46116662]
  - ndcs_emi_exclLU for refyr and taryr: [75.72003683 75.72003683]
  - ndcs_emi_onlyLU for refyr and taryr: [8.74112979 8.74112979]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_refyr = 8.741129792981098
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_taryr = 8.741129792981098
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 75.72003683169875
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 75.72003683169875 + -3.496451917192439 = 72.2235849145063 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 84.46116662467985
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 84.46116662467985 + -25.240012277232918 = 59.22115434744693
- tar_emi_exclLU = ndc_value_exclLU = 72.2235849145063
- tar_emi_inclLU = ndc_value_inclLU = 59.22115434744693
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.2235849145063
- tar_emi_inclLU = 59.22115434744693

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 72.2235849145063 (66.1 MtCO2eq_SAR)
- ndc_value_inclLU: 59.221154347446934 (54.2 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [84.46116662 84.46116662]
  - ndcs_emi_exclLU for refyr and taryr: [75.72003683 75.72003683]
  - ndcs_emi_onlyLU for refyr and taryr: [8.74112979 8.74112979]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_refyr = 8.741129792981098
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_taryr = 8.741129792981098
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 72.2235849145063
- tar_emi_inclLU = ndc_value_inclLU = 59.221154347446934
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.2235849145063
- tar_emi_inclLU = 59.221154347446934

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -4.6 (-4.6%)
- ndc_value_inclLU: -29.9 (-29.9%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [84.46116662 84.46116662]
  - ndcs_emi_exclLU for refyr and taryr: [75.72003683 75.72003683]
  - ndcs_emi_onlyLU for refyr and taryr: [8.74112979 8.74112979]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -4.6 / 100. = 0.954
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -29.9 / 100. = 0.7010000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_refyr = 8.741129792981098
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098).
    - bl_onlyLU_taryr = 8.741129792981098
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 75.72003683169875 * 0.8853787809999999 = 67.04091390732454
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 75.72003683169875 * (1 - 0.8853787809999999) = 8.679122924374216
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.954 * 67.04091390732454 + 8.679122924374216 = 72.63615479196181
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.7010000000000001 * (67.04091390732454 + 8.741129792981098) + 8.679122924374216 = 61.802335558288476
- tar_emi_exclLU = ndc_value_exclLU = 72.63615479196181
- tar_emi_inclLU = ndc_value_inclLU = 61.802335558288476
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.63615479196181
- tar_emi_inclLU = 61.802335558288476
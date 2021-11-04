## ['Ecuador']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -9.592228236502176 (-9.130 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -11.430826200782441 (-10.880 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 80.79745019714824 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 80.79745019714824 + -9.592228236502176 = 71.20522196064606 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([78.7131, 45.964949107006596]) = 124.67804910700659 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 124.67804910700659 + -11.430826200782441 = 113.24722290622415 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 71.20522196064606 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 113.24722290622415 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 71.20522196064606 MtCO2eq
- tar_emi_inclLU = 113.24722290622415 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -16.894088723215223 (-16.080 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -26.087078544616542 (-24.830 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 80.79745019714824 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 80.79745019714824 + -16.894088723215223 = 63.90336147393302 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([78.7131, 45.964949107006596]) = 124.67804910700659 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 124.67804910700659 + -26.087078544616542 = 98.59097056239004 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 63.90336147393302 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 98.59097056239004 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 63.90336147393302 MtCO2eq
- tar_emi_inclLU = 98.59097056239004 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 71.20522196064606 (67.774 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 115.33157310337239 (109.774 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 71.20522196064606 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 115.33157310337239 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 71.20522196064606 MtCO2eq
- tar_emi_inclLU = 115.33157310337239 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 63.90336147393301 (60.824 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 100.67532075953828 (95.824 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 63.90336147393301 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 100.67532075953828 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 63.90336147393301 MtCO2eq
- tar_emi_inclLU = 100.67532075953828 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -9.0 (-9%, from NDC)
- ndc_value_inclLU: -10.0 (-10%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -9.0 / 100. = 0.91
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.0 / 100. = 0.9
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 78.7131 * 1.0 = 78.7131 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 78.7131 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.91 * 78.7131 + 0.0 = 71.628921 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.9 * (78.7131 + 45.964949107006596) + 0.0 = 112.21024419630594 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 71.628921 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 112.21024419630594 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 71.628921 MtCO2eq
- tar_emi_inclLU = 112.21024419630594 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -20.9 (-20.9%, from NDC)
- ndc_value_inclLU: -26.0 (-26%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 80.79745019714824 MtCO2eq, 80.79745019714824 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 45.964949107006596 MtCO2eq, 45.964949107006596 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.9 / 100. = 0.791
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -26.0 / 100. = 0.74
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_refyr = 45.964949107006596 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (45.964949107006596 MtCO2eq).
    - bl_onlyLU_taryr = 45.964949107006596 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 78.7131 * 1.0 = 78.7131 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 78.7131 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.791 * 78.7131 + 0.0 = 62.2620621 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.74 * (78.7131 + 45.964949107006596) + 0.0 = 92.26175633918487 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 62.2620621 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 92.26175633918487 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 62.2620621 MtCO2eq
- tar_emi_inclLU = 92.26175633918487 MtCO2eq
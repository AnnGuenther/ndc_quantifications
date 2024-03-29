## ['Uganda']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | yes |
| Used | yes | yes | yes | yes | yes | yes | yes |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | nan | nan | yes |
| Used | yes | yes | yes | no | no | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -3.496451917192439 (-3.2 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -25.240012277232918 (-23.1 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 84.46116662467985 MtCO2eq, 84.46116662467985 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 75.72003683169875 MtCO2eq, 75.72003683169875 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 8.741129792981098 MtCO2eq, 8.741129792981098 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_refyr = 8.741129792981098 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_taryr = 8.741129792981098 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 75.72003683169875 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 75.72003683169875 + -3.496451917192439 = 72.2235849145063 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 84.46116662467985 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 84.46116662467985 + -25.240012277232918 = 59.22115434744693 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 72.2235849145063 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 59.22115434744693 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.2235849145063 MtCO2eq
- tar_emi_inclLU = 59.22115434744693 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 72.2235849145063 (66.1 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 59.221154347446934 (54.2 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 84.46116662467985 MtCO2eq, 84.46116662467985 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 75.72003683169875 MtCO2eq, 75.72003683169875 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 8.741129792981098 MtCO2eq, 8.741129792981098 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_refyr = 8.741129792981098 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_taryr = 8.741129792981098 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 72.2235849145063 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 59.221154347446934 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.2235849145063 MtCO2eq
- tar_emi_inclLU = 59.221154347446934 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -4.6 (-4.6%, from NDC)
- ndc_value_inclLU: -29.9 (-29.9%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 84.46116662467985 MtCO2eq, 84.46116662467985 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 75.72003683169875 MtCO2eq, 75.72003683169875 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 8.741129792981098 MtCO2eq, 8.741129792981098 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -4.6 / 100. = 0.954
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -29.9 / 100. = 0.7010000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_refyr = 8.741129792981098 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_taryr = 8.741129792981098 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 75.373 * 0.8853787808833863 = 66.73365485152348 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 75.373 * (1 - 0.8853787808833863) = 8.639345148476526 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.954 * 66.73365485152348 + 8.639345148476526 = 72.30325187682992 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.7010000000000001 * (66.73365485152348 + 8.741129792981098) + 8.639345148476526 = 61.54716918427424 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 72.30325187682992 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 61.54716918427424 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.30325187682992 MtCO2eq
- tar_emi_inclLU = 61.54716918427424 MtCO2eq
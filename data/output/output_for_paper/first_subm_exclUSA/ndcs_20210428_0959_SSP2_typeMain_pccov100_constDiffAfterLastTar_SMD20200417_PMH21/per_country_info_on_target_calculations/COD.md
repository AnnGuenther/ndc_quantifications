## ['DR Congo']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | no | yes | no | nan | yes |
| Used | yes | no | yes | no | no | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 40.0 (+40 MtCO2eq, from NDC)
- ndc_value_inclLU: -70.0 (-70 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 430.0 MtCO2eq, 430.0 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 30.0 MtCO2eq, 30.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 400.0 MtCO2eq, 400.0 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_refyr = 400.0 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_taryr = 400.0 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 30.0 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 30.0 + 40.0 = 70.0 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 430.0 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 430.0 + -70.0 = 360.0 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 70.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 360.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 70.0 MtCO2eq
- tar_emi_inclLU = 360.0 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 33.0 (+33%, from NDC)
- ndc_value_inclLU: -17.0 (-17%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 430.0 MtCO2eq, 430.0 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 30.0 MtCO2eq, 30.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 400.0 MtCO2eq, 400.0 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + 33.0 / 100. = 1.33
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -17.0 / 100. = 0.83
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_refyr = 400.0 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_taryr = 400.0 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 108.8342 * 1.0 = 108.8342 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 108.8342 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 1.33 * 108.8342 + 0.0 = 144.749486 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.83 * (108.8342 + 400.0) + 0.0 = 422.332386 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 144.749486 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 422.332386 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 144.749486 MtCO2eq
- tar_emi_inclLU = 422.332386 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 70.0 (70 MtCO2eq, from NDC)
- ndc_value_inclLU: 360.0 (360 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 430.0 MtCO2eq, 430.0 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 30.0 MtCO2eq, 30.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 400.0 MtCO2eq, 400.0 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_refyr = 400.0 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (400.0 MtCO2eq).
    - bl_onlyLU_taryr = 400.0 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 70.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 360.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 70.0 MtCO2eq
- tar_emi_inclLU = 360.0 MtCO2eq
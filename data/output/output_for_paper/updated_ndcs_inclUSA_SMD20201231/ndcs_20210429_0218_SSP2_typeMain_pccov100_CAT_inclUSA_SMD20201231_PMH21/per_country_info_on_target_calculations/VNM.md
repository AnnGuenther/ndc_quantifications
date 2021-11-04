## ['Viet Nam']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | nan | nan |
| Used | yes | yes | yes | yes | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -74.6 (-74.6 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: -83.9 (-83.9 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 977.1 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 977.1 + -74.6 = 902.5 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 927.9 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 927.9 + -83.9 = 844.0 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 902.5 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 844.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 902.5 MtCO2eq
- tar_emi_inclLU = 844.0 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -229.5 (-229.5 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: -250.8 (-250.8 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 977.1 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 977.1 + -229.5 = 747.6 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 927.9 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 927.9 + -250.8 = 677.0999999999999 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 747.6 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 677.0999999999999 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 747.6 MtCO2eq
- tar_emi_inclLU = 677.0999999999999 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 902.5 (902.5 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: 844.0 (844.0 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 902.5 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 844.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 902.5 MtCO2eq
- tar_emi_inclLU = 844.0 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 747.6 (747.6 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: 677.1 (677.1 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 747.6 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 677.1 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 747.6 MtCO2eq
- tar_emi_inclLU = 677.1 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -6.0 (-6%, from NDC)
- ndc_value_inclLU: -9.0 (-9%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -6.0 / 100. = 0.94
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -9.0 / 100. = 0.91
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 429.1816 * 1.0 = 429.1816 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 429.1816 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.94 * 429.1816 + 0.0 = 403.430704 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.91 * 429.1816 + -49.2 + 0.0 = 341.35525600000005 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 403.430704 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 341.35525600000005 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 403.430704 MtCO2eq
- tar_emi_inclLU = 341.35525600000005 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -23.0 (-23%, from NDC)
- ndc_value_inclLU: -27.0 (-27%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 927.9 MtCO2eq, 927.9 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 977.1 MtCO2eq, 977.1 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -49.2 MtCO2eq, -49.2 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -23.0 / 100. = 0.77
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -27.0 / 100. = 0.73
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_refyr = -49.2 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-49.2 MtCO2eq).
    - bl_onlyLU_taryr = -49.2 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 429.1816 * 1.0 = 429.1816 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 429.1816 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.77 * 429.1816 + 0.0 = 330.469832 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.73 * 429.1816 + -49.2 + 0.0 = 264.102568 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 330.469832 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 264.102568 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 330.469832 MtCO2eq
- tar_emi_inclLU = 264.102568 MtCO2eq
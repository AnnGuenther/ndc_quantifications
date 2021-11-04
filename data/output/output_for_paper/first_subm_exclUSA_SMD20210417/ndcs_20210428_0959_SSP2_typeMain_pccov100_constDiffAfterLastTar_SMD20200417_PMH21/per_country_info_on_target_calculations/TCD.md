## ['Chad']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | yes | nan | yes |
| Used | yes | no | yes | yes | no | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -5.2103 (-5.2103 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: -5.2103 (-5.2103 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 46.04685 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 46.04685 + -5.2103 = 40.83655 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 28.659370000000003 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 28.659370000000003 + -5.2103 = 23.449070000000003 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 40.83655 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 23.449070000000003 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 40.83655 MtCO2eq
- tar_emi_inclLU = 23.449070000000003 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -13.4049 (-13.4049 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: -20.42992 (-20.42992 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 46.04685 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 46.04685 + -13.4049 = 32.64195 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 28.659370000000003 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 28.659370000000003 + -20.42992 = 8.229450000000003 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 32.64195 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 8.229450000000003 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 32.64195 MtCO2eq
- tar_emi_inclLU = 8.229450000000003 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -11.3 (-11.3%, from NDC)
- ndc_value_inclLU: -18.2 (-18.2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -11.3 / 100. = 0.887
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -18.2 / 100. = 0.8180000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 71.3566 * 1.0 = 71.3566 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 71.3566 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.887 * 71.3566 + 0.0 = 63.2933042 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8180000000000001 * 71.3566 + -17.38748 + 0.0 = 40.9822188 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 63.2933042 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 40.9822188 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 63.2933042 MtCO2eq
- tar_emi_inclLU = 40.9822188 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -29.1 (-29.1%, from NDC)
- ndc_value_inclLU: -71.0 (-71%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -29.1 / 100. = 0.709
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -71.0 / 100. = 0.29000000000000004
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 71.3566 * 1.0 = 71.3566 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 71.3566 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.709 * 71.3566 + 0.0 = 50.591829399999995 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.29000000000000004 * 71.3566 + -17.38748 + 0.0 = 3.305934000000004 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 50.591829399999995 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 3.305934000000004 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 50.591829399999995 MtCO2eq
- tar_emi_inclLU = 3.305934000000004 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 40.83655 (40.83655 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: 23.44907 (23.44907 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 40.83655 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 23.44907 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 40.83655 MtCO2eq
- tar_emi_inclLU = 23.44907 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 32.64193 (32.64193 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: 8.22945 (8.22945 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.659370000000003 MtCO2eq, 28.659370000000003 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 46.04685 MtCO2eq, 46.04685 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -17.38748 MtCO2eq, -17.38748 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_refyr = -17.38748 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748 MtCO2eq).
    - bl_onlyLU_taryr = -17.38748 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 32.64193 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 8.22945 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 32.64193 MtCO2eq
- tar_emi_inclLU = 8.22945 MtCO2eq
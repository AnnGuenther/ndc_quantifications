## ['Afghanistan']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | nan |
| Used | yes | yes | yes | yes | yes | no |



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -1.4776926549090623 (-1.372950 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -1.4776818920068817 (-1.372940 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 57.23780262308392 MtCO2eq, 57.23780262308392 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 44.85218844341937 MtCO2eq, 44.85218844341937 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 12.38562494256675 MtCO2eq, 12.38562494256675 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_refyr = 12.38562494256675 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_taryr = 12.38562494256675 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 44.85218844341937 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 44.85218844341937 + -1.4776926549090623 = 43.37449578851031 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 57.23780262308392 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 57.23780262308392 + -1.4776818920068817 = 55.76012073107704 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 43.37449578851031 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 55.76012073107704 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 43.37449578851031 MtCO2eq
- tar_emi_inclLU = 55.76012073107704 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -6.71555586730128 (-6.239540 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -6.71555586730128 (-6.239540 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 65.69056624267705 MtCO2eq, 65.69056624267705 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 52.67314817919682 MtCO2eq, 52.67314817919682 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 13.017418063480234 MtCO2eq, 13.017418063480234 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_refyr = 13.017418063480234 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_taryr = 13.017418063480234 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 52.67314817919682 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 52.67314817919682 + -6.71555586730128 = 45.95759231189554 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 65.69056624267705 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 65.69056624267705 + -6.71555586730128 = 58.975010375375774 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 45.95759231189554 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 58.975010375375774 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.95759231189554 MtCO2eq
- tar_emi_inclLU = 58.975010375375774 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 43.3744957885103 (40.3 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 55.76012073107705 (51.807700 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 57.23780262308392 MtCO2eq, 57.23780262308392 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 44.85218844341937 MtCO2eq, 44.85218844341937 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 12.38562494256675 MtCO2eq, 12.38562494256675 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_refyr = 12.38562494256675 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_taryr = 12.38562494256675 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 43.3744957885103 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 55.76012073107705 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 43.3744957885103 MtCO2eq
- tar_emi_inclLU = 55.76012073107705 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 45.95759231189553 (42.7 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 58.97501037537577 (54.794710 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 65.69056624267705 MtCO2eq, 65.69056624267705 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 52.67314817919682 MtCO2eq, 52.67314817919682 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 13.017418063480234 MtCO2eq, 13.017418063480234 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_refyr = 13.017418063480234 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_taryr = 13.017418063480234 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.95759231189553 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 58.97501037537577 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.95759231189553 MtCO2eq
- tar_emi_inclLU = 58.97501037537577 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -3.3 (-3.3%, from NDC)
- ndc_value_inclLU: -2.6 (-2.6%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 57.23780262308392 MtCO2eq, 57.23780262308392 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 44.85218844341937 MtCO2eq, 44.85218844341937 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 12.38562494256675 MtCO2eq, 12.38562494256675 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -3.3 / 100. = 0.967
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.6 / 100. = 0.974
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_refyr = 12.38562494256675 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675 MtCO2eq).
    - bl_onlyLU_taryr = 12.38562494256675 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 36.1235 * 1.0 = 36.1235 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 36.1235 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.967 * 36.1235 + 0.0 = 34.9314245 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.974 * (36.1235 + 12.38562494256675) + 0.0 = 47.24788769406001 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 34.9314245 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 47.24788769406001 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 34.9314245 MtCO2eq
- tar_emi_inclLU = 47.24788769406001 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -13.6 (-13.6%, from NDC)
- ndc_value_inclLU: -10.2 (-10.2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 65.69056624267705 MtCO2eq, 65.69056624267705 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 52.67314817919682 MtCO2eq, 52.67314817919682 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 13.017418063480234 MtCO2eq, 13.017418063480234 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -13.6 / 100. = 0.864
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.2 / 100. = 0.898
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_refyr = 13.017418063480234 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234 MtCO2eq).
    - bl_onlyLU_taryr = 13.017418063480234 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 39.2668 * 0.9999974533193436 = 39.26670000000001 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 39.2668 * (1 - 0.9999974533193436) = 9.999999999703002e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.864 * 39.26670000000001 + 9.999999999703002e-05 = 33.9265288 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.898 * (39.26670000000001 + 13.017418063480234) + 9.999999999703002e-05 = 46.95123802100525 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 33.9265288 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 46.95123802100525 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 33.9265288 MtCO2eq
- tar_emi_inclLU = 46.95123802100525 MtCO2eq
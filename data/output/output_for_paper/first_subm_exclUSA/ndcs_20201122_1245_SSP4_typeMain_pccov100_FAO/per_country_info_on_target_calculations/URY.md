## ['Uruguay']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 45.12066942680393 (41.8 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: 38.64401831290863 (35.8 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.12066942680393 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.64401831290863 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.12066942680393 MtCO2eq
- tar_emi_inclLU = 38.64401831290863 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 42.098232240319454 (39.0 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: 35.621581126424154 (33.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 42.098232240319454 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.621581126424154 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 42.098232240319454 MtCO2eq
- tar_emi_inclLU = 35.621581126424154 MtCO2eq



## Target type used: REI, refyr: 1990, taryr: 2025, unconditional_best
- ndc_value_exclLU: -49.0 (-49% (SAR), from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -49.0 / 100. = 0.51
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (-25.4958182 MtCO2eq).
    - bl_onlyLU_refyr = -25.4958182 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 1.0 = 28.4006 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 94985125609.7469 2011GKD / 27592626953.125 2011GKD = 3.442409661505222
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * 0.51 * 28.4006 + 0.0 = 49.86091491459806 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * nan * 28.4006 + -25.4958182 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 49.86091491459806 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([49.86091491459806, 46.444490037586554]) = 96.30540495218462 MtCO2eq
- tar_emi_exclLU = 49.86091491459806 MtCO2eq
- tar_emi_inclLU = 96.30540495218462 MtCO2eq



## Target type used: REI, refyr: 1990, taryr: 2025, conditional_best
- ndc_value_exclLU: -52.0 (-52% (SAR), from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -52.0 / 100. = 0.48
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (-25.4958182 MtCO2eq).
    - bl_onlyLU_refyr = -25.4958182 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 1.0 = 28.4006 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 94985125609.7469 2011GKD / 27592626953.125 2011GKD = 3.442409661505222
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * 0.48 * 28.4006 + 0.0 = 46.9279199196217 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * nan * 28.4006 + -25.4958182 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 46.9279199196217 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([46.9279199196217, 46.444490037586554]) = 93.37240995720825 MtCO2eq
- tar_emi_exclLU = 46.9279199196217 MtCO2eq
- tar_emi_inclLU = 93.37240995720825 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -42.31412061078264 (-39.2 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: -48.79077172467794 (-45.2 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 40.9903 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.9903 + -42.31412061078264 = -1.32382061078264 MtCO2eq # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-42.314 MtCO2eq) is < 0 (-1.324 MtCO2eq, compared to baseline 40.990 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = -1.32382061078264 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -1.32382061078264 MtCO2eq
- tar_emi_inclLU = 38.644018312908614 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.336557797267105 (-42.0 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: -51.813208911162405 (-48.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 40.9903 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.9903 + -45.336557797267105 = -4.346257797267107 MtCO2eq # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-4.346 MtCO2eq, compared to baseline 40.990 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = -4.346257797267107 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -4.346257797267107 MtCO2eq
- tar_emi_inclLU = 35.62158112642415 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -48.4 (-48.4%, from NDC)
- ndc_value_inclLU: -55.8 (-55.8%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -48.4 / 100. = 0.516
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -55.8 / 100. = 0.44200000000000006
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.9903 * 1.0 = 40.9903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 40.9903 + 0.0 = 21.1509948 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (40.9903 + 46.444490037586554) + 0.0 = 38.64617719661326 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 21.1509948 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.64617719661326 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 21.1509948 MtCO2eq
- tar_emi_inclLU = 38.64617719661326 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -51.9 (-51.9%, from NDC)
- ndc_value_inclLU: -59.3 (-59.3%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -51.9 / 100. = 0.481
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -59.3 / 100. = 0.40700000000000003
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.9903 * 1.0 = 40.9903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 40.9903 + 0.0 = 19.7163343 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (40.9903 + 46.444490037586554) + 0.0 = 35.585959545297726 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 19.7163343 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.585959545297726 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 19.7163343 MtCO2eq
- tar_emi_inclLU = 35.585959545297726 MtCO2eq
- URY LULUCF: second try as some tar_exclLU values < 0 (first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU; 
    second try: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year). 
    Negative tar_exclLU for ['ABU'], with type_main = ['REI'] and type_reclass = ['ABS'].



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 45.12066942680393 (41.8 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: 38.64401831290863 (35.8 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.12066942680393 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.64401831290863 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.12066942680393 MtCO2eq
- tar_emi_inclLU = 38.64401831290863 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 42.098232240319454 (39.0 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: 35.621581126424154 (33.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 42.098232240319454 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.621581126424154 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 42.098232240319454 MtCO2eq
- tar_emi_inclLU = 35.621581126424154 MtCO2eq



## Target type used: REI, refyr: 1990, taryr: 2025, unconditional_best
- ndc_value_exclLU: -49.0 (-49% (SAR), from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -49.0 / 100. = 0.51
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (-25.4958182 MtCO2eq).
    - bl_onlyLU_refyr = -25.4958182 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 1.0 = 28.4006 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 94985125609.7469 2011GKD / 27592626953.125 2011GKD = 3.442409661505222
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * 0.51 * 28.4006 + 0.0 = 49.86091491459806 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * nan * 28.4006 + -25.4958182 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 49.86091491459806 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([49.86091491459806, 46.444490037586554]) = 96.30540495218462 MtCO2eq
- tar_emi_exclLU = 49.86091491459806 MtCO2eq
- tar_emi_inclLU = 96.30540495218462 MtCO2eq



## Target type used: REI, refyr: 1990, taryr: 2025, conditional_best
- ndc_value_exclLU: -52.0 (-52% (SAR), from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -52.0 / 100. = 0.48
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (-25.4958182 MtCO2eq).
    - bl_onlyLU_refyr = -25.4958182 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 1.0 = 28.4006 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 94985125609.7469 2011GKD / 27592626953.125 2011GKD = 3.442409661505222
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * 0.48 * 28.4006 + 0.0 = 46.9279199196217 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.442409661505222 * nan * 28.4006 + -25.4958182 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 46.9279199196217 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([46.9279199196217, 46.444490037586554]) = 93.37240995720825 MtCO2eq
- tar_emi_exclLU = 46.9279199196217 MtCO2eq
- tar_emi_inclLU = 93.37240995720825 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -42.31412061078264 (-39.2 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: -48.79077172467794 (-45.2 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 40.9903 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.9903 + -42.31412061078264 = -1.32382061078264 MtCO2eq # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-42.314 MtCO2eq) is < 0 (-1.324 MtCO2eq, compared to baseline 40.990 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = -1.32382061078264 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -1.32382061078264 MtCO2eq
- tar_emi_inclLU = 38.644018312908614 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.336557797267105 (-42.0 MtCO2eq_AR2, from NDC)
- ndc_value_inclLU: -51.813208911162405 (-48.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 40.9903 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.9903 + -45.336557797267105 = -4.346257797267107 MtCO2eq # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-4.346 MtCO2eq, compared to baseline 40.990 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = -4.346257797267107 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -4.346257797267107 MtCO2eq
- tar_emi_inclLU = 35.62158112642415 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -48.4 (-48.4%, from NDC)
- ndc_value_inclLU: -55.8 (-55.8%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -48.4 / 100. = 0.516
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -55.8 / 100. = 0.44200000000000006
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.9903 * 1.0 = 40.9903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 40.9903 + 0.0 = 21.1509948 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (40.9903 + 46.444490037586554) + 0.0 = 38.64617719661326 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 21.1509948 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 38.64617719661326 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 21.1509948 MtCO2eq
- tar_emi_inclLU = 38.64617719661326 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -51.9 (-51.9%, from NDC)
- ndc_value_inclLU: -59.3 (-59.3%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 87.43479003758655 MtCO2eq, 87.43479003758655 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -51.9 / 100. = 0.481
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -59.3 / 100. = 0.40700000000000003
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_refyr = 46.444490037586554 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 40.9903 = 46.444490037586554 MtCO2eq
    - bl_onlyLU_taryr = 46.444490037586554 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.9903 * 1.0 = 40.9903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.9903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 40.9903 + 0.0 = 19.7163343 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (40.9903 + 46.444490037586554) + 0.0 = 35.585959545297726 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 19.7163343 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.585959545297726 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 19.7163343 MtCO2eq
- tar_emi_inclLU = 35.585959545297726 MtCO2eq    Second method also didn't work for all targets ... so the negative tar_emi_exclLU are set to 0.
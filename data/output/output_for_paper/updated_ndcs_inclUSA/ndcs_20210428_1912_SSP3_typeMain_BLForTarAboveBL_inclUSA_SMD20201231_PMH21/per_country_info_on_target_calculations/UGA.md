## ['Uganda']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | yes |
| Used | yes | yes | yes | yes | yes | yes | yes |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | nan | nan | yes |
| Used | yes | yes | yes | no | no | yes |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 78.8886963816544 (72.2 MtCO2eq_SAR, from NDC)
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
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 78.8886963816544 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([78.8886963816544, - 8.741129792981098]) = 70.1475665886733 MtCO2eq.
- tar_emi_exclLU = 70.1475665886733 MtCO2eq
- tar_emi_inclLU = 78.8886963816544 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 65.886265814595 (60.3 MtCO2eq_SAR, from NDC)
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
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.886265814595 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([65.886265814595, - 8.741129792981098]) = 57.14513602161391 MtCO2eq.
- tar_emi_exclLU = 57.14513602161391 MtCO2eq
- tar_emi_inclLU = 65.886265814595 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -5.572470243025449 (-5.1 MtCO2eq_SAR, from NDC)
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
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 84.46116662467985 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 84.46116662467985 + -5.572470243025449 = 78.8886963816544 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 78.8886963816544 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([78.8886963816544, - 8.741129792981098]) = 70.1475665886733 MtCO2eq.
- tar_emi_exclLU = 70.1475665886733 MtCO2eq
- tar_emi_inclLU = 78.8886963816544 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -18.57490081008483 (-17.0 MtCO2eq_SAR, from NDC)
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
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 84.46116662467985 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 84.46116662467985 + -18.57490081008483 = 65.88626581459502 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.88626581459502 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([65.88626581459502, - 8.741129792981098]) = 57.14513602161392 MtCO2eq.
- tar_emi_exclLU = 57.14513602161392 MtCO2eq
- tar_emi_inclLU = 65.88626581459502 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -6.6 (-6.6%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 84.46116662467985 MtCO2eq, 84.46116662467985 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 75.72003683169875 MtCO2eq, 75.72003683169875 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 8.741129792981098 MtCO2eq, 8.741129792981098 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -6.6 / 100. = 0.9339999999999999
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_refyr = 8.741129792981098 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_taryr = 8.741129792981098 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 84.4316 * 0.8873104678881845 = 74.91704250054804 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 84.4316 * (1 - 0.8873104678881845) = 9.514557499451966 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 74.91704250054804 + 9.514557499451966 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.9339999999999999 * (74.91704250054804 + 8.741129792981098) + 9.514557499451966 = 87.65129042160818 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 87.65129042160818 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([87.65129042160818, - 8.741129792981098]) = 78.91016062862708 MtCO2eq.
- tar_emi_exclLU = 78.91016062862708 MtCO2eq
- tar_emi_inclLU = 87.65129042160818 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -22.0 (-22%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 84.46116662467985 MtCO2eq, 84.46116662467985 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 75.72003683169875 MtCO2eq, 75.72003683169875 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 8.741129792981098 MtCO2eq, 8.741129792981098 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -22.0 / 100. = 0.78
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_refyr = 8.741129792981098 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (8.741129792981098 MtCO2eq).
    - bl_onlyLU_taryr = 8.741129792981098 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 84.4316 * 0.8873104678881845 = 74.91704250054804 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 84.4316 * (1 - 0.8873104678881845) = 9.514557499451966 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 74.91704250054804 + 9.514557499451966 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.78 * (74.91704250054804 + 8.741129792981098) + 9.514557499451966 = 74.76793188840469 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 74.76793188840469 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([74.76793188840469, - 8.741129792981098]) = 66.02680209542359 MtCO2eq.
- tar_emi_exclLU = 66.02680209542359 MtCO2eq
- tar_emi_inclLU = 74.76793188840469 MtCO2eq
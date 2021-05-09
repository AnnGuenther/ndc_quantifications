## ['China']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | nan | nan | nan | nan |
| Used | yes | no | no | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: REI, refyr: 2005, taryr: 2030, unconditional_worst
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -60.0 (-60%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -60.0 / 100. = 0.4
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-420.6954 MtCO2eq).
    - bl_onlyLU_refyr = -420.6954 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-553.3526571428571 MtCO2eq).
    - bl_onlyLU_taryr = -553.3526571428571 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 7808.0066 * 1.0 = 7808.0066 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 18913.6058 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 36362813048294.88 2011GKD / 8456687000000.0 2011GKD = 4.299888720996163
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 4.299888720996163 * nan * 7808.0066 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 4.299888720996163 * 0.4 * 7808.0066 + -420.6954 + 0.0 = 13008.72840512144 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 13008.72840512144 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([13008.72840512144, - -553.3526571428571]) = 13562.081062264297 MtCO2eq.
- tar_emi_exclLU = 13562.081062264297 MtCO2eq
- tar_emi_inclLU = 13008.72840512144 MtCO2eq



## Target type used: REI, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -65.0 (-65%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -65.0 / 100. = 0.35
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-420.6954 MtCO2eq).
    - bl_onlyLU_refyr = -420.6954 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-553.3526571428571 MtCO2eq).
    - bl_onlyLU_taryr = -553.3526571428571 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 7808.0066 * 1.0 = 7808.0066 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 18913.6058 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 36362813048294.88 2011GKD / 8456687000000.0 2011GKD = 4.299888720996163
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 4.299888720996163 * nan * 7808.0066 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 4.299888720996163 * 0.35 * 7808.0066 + -420.6954 + 0.0 = 11330.05042948126 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 11330.05042948126 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([11330.05042948126, - -553.3526571428571]) = 11883.403086624117 MtCO2eq.
- tar_emi_exclLU = 11883.403086624117 MtCO2eq
- tar_emi_inclLU = 11330.05042948126 MtCO2eq
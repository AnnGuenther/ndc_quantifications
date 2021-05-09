## ['Azerbaijan']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | nan | nan |
| Used | yes | yes | yes | yes | yes | yes | yes |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 50.55373356459108 (47.665 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 48.01040296377519 (45.267 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.319759814285714 MtCO2eq).
    - bl_onlyLU_refyr = -8.319759814285714 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.319759814285714 MtCO2eq).
    - bl_onlyLU_taryr = -8.319759814285714 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 50.55373356459108 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 48.01040296377519 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 50.55373356459108 MtCO2eq
- tar_emi_inclLU = 48.01040296377519 MtCO2eq



## Target type used: RBY, refyr: 1990, taryr: 2030, unconditional_best
- ndc_value_exclLU: -35.0 (-35%, from NDC)
- ndc_value_inclLU: -35.0 (-35%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 73.86158731085047 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 77.77521946973731 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -3.913632158886837 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -35.0 / 100. = 0.65
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.0 / 100. = 0.65
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-3.913632158886837 MtCO2eq).
    - bl_onlyLU_refyr = -3.913632158886837 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.319759814285714 MtCO2eq).
    - bl_onlyLU_taryr = -8.319759814285714 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 77.7572 * 1.0 = 77.7572 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 66.8642 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.65 * 77.7572 + 0.0 = 50.54218 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.65 * 77.7572 + -3.913632158886837 + 0.0 = 46.62854784111317 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 50.54218 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 46.62854784111317 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 50.54218 MtCO2eq
- tar_emi_inclLU = 46.62854784111317 MtCO2eq
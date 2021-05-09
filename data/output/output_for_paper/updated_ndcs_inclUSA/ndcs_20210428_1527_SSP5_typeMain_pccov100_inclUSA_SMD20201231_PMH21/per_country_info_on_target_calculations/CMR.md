## ['Cameroon']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | no |



## Target type used: ABU, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: -33.0 (-33 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 104.0 MtCO2eq, 104.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_refyr = 117.79018142857143 MtCO2eq
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_taryr = 117.79018142857143 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 104.0 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 104.0 + -33.0 = 71.0 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 71.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([71.0, 117.79018142857143]) = 188.79018142857143 MtCO2eq
- tar_emi_exclLU = 71.0 MtCO2eq
- tar_emi_inclLU = 188.79018142857143 MtCO2eq



## Target type used: ABS, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: 71.0 (71 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 104.0 MtCO2eq, 104.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_refyr = 117.79018142857143 MtCO2eq
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_taryr = 117.79018142857143 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 71.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([71.0, 117.79018142857143]) = 188.79018142857143 MtCO2eq
- tar_emi_exclLU = 71.0 MtCO2eq
- tar_emi_inclLU = 188.79018142857143 MtCO2eq



## Target type used: RBU, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: -32.0 (-32%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 104.0 MtCO2eq, 104.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -32.0 / 100. = 0.6799999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_refyr = 117.79018142857143 MtCO2eq
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143 MtCO2eq).
    - bl_onlyLU_taryr = 117.79018142857143 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 96.5085 * 1.0 = 96.5085 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 96.5085 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.6799999999999999 * 96.5085 + 0.0 = 65.62577999999999 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (96.5085 + 117.79018142857143) + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 65.62577999999999 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([65.62577999999999, 117.79018142857143]) = 183.41596142857142 MtCO2eq
- tar_emi_exclLU = 65.62577999999999 MtCO2eq
- tar_emi_inclLU = 183.41596142857142 MtCO2eq
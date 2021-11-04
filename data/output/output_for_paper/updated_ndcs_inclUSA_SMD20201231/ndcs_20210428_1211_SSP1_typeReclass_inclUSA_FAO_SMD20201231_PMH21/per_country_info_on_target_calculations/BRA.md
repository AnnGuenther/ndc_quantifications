## ['Brazil']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | nan |
| Used | yes | yes | yes | yes | yes | yes | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 577.245 (577.245 MtCO2eq_AR5, from NDC)
- ndc_value_inclLU: 1787.912 (1787.912 MtCO2eq_AR5, from NDC)
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
    - emi_onlyLU 2025: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_refyr = 348.2120571428572 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_taryr = 348.2120571428572 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 577.245 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 1787.912 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 577.245 MtCO2eq
- tar_emi_inclLU = 1787.912 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 522.269 (522.269 MtCO2eq_AR5, from NDC)
- ndc_value_inclLU: 1617.635 (1617.635 MtCO2eq_AR5, from NDC)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_refyr = 348.2120571428572 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_taryr = 348.2120571428572 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 522.269 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 1617.635 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 522.269 MtCO2eq
- tar_emi_inclLU = 1617.635 MtCO2eq



## Target type used: RBY, refyr: 2005, taryr: 2025, unconditional_best
- ndc_value_exclLU: -37.0 (-37%, from NDC)
- ndc_value_inclLU: -37.0 (-37%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 2837.9559999999997 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 916.262 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 1921.694 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -37.0 / 100. = 0.63
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -37.0 / 100. = 0.63
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (1921.694 MtCO2eq).
    - bl_onlyLU_refyr = 1921.694 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_taryr = 348.2120571428572 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 920.1377 * 1.0 = 920.1377 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1337.7226 * (1 - 0.9999999252460862) = 9.999999997797018e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.63 * 920.1377 + 9.999999997797018e-05 = 579.6868509999999 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.63 * (920.1377 + 1921.694) + 9.999999997797018e-05 = 1790.3540709999997 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 579.6868509999999 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 1790.3540709999997 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 579.6868509999999 MtCO2eq
- tar_emi_inclLU = 1790.3540709999997 MtCO2eq



## Target type used: RBY, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: -43.0 (-43%, from NDC)
- ndc_value_inclLU: -43.0 (-43%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 2837.9559999999997 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 916.262 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 1921.694 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -43.0 / 100. = 0.5700000000000001
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -43.0 / 100. = 0.5700000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (1921.694 MtCO2eq).
    - bl_onlyLU_refyr = 1921.694 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (348.2120571428572 MtCO2eq).
    - bl_onlyLU_taryr = 348.2120571428572 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 920.1377 * 1.0 = 920.1377 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1386.6696 * (1 - 0.999999927884768) = 9.999999992275903e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.5700000000000001 * 920.1377 + 9.999999992275903e-05 = 524.478589 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.5700000000000001 * (920.1377 + 1921.694) + 9.999999992275903e-05 = 1619.844169 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 524.478589 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 1619.844169 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 524.478589 MtCO2eq
- tar_emi_inclLU = 1619.844169 MtCO2eq
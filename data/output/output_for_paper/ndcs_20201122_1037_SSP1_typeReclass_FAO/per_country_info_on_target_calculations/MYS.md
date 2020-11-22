## ['Malaysia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: REI, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -35.0 (-35%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 300.2628308298008 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 273.56441059960684 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 26.698420230194024 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.0 / 100. = 0.65
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (26.698420230194024 MtCO2eq).
    - bl_onlyLU_refyr = 26.698420230194024 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-112.13901142857144 MtCO2eq).
    - bl_onlyLU_taryr = -112.13901142857144 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 293.0196 * 0.9966861939182492 = 292.04858986744784 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 353.8493 * (1 - 0.9803580224688871) = 6.950300000000012 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 1438088122867.419 2011GKD / 414550406250.0 2011GKD = 3.469030788984829
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.469030788984829 * nan * 292.04858986744784 + 6.950300000000012 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.469030788984829 * 0.65 * (292.04858986744784 + 26.698420230194024) + 6.950300000000012 = 725.6833747516256 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 725.6833747516256 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([725.6833747516256, - -112.13901142857144]) = 837.822386180197 MtCO2eq.
- tar_emi_exclLU = 837.822386180197 MtCO2eq
- tar_emi_inclLU = 725.6833747516256 MtCO2eq



## Target type used: REI, refyr: 2005, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -45.0 (-45%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 300.2628308298008 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 273.56441059960684 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 26.698420230194024 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -45.0 / 100. = 0.55
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: ndcs_emi_onlyLU used (26.698420230194024 MtCO2eq).
    - bl_onlyLU_refyr = 26.698420230194024 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-112.13901142857144 MtCO2eq).
    - bl_onlyLU_taryr = -112.13901142857144 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 293.0196 * 0.9966861939182492 = 292.04858986744784 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 353.8493 * (1 - 0.9803580224688871) = 6.950300000000012 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 1438088122867.419 2011GKD / 414550406250.0 2011GKD = 3.469030788984829
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.469030788984829 * nan * 292.04858986744784 + 6.950300000000012 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.469030788984829 * 0.55 * (292.04858986744784 + 26.698420230194024) + 6.950300000000012 = 615.1090555590678 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 615.1090555590678 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([615.1090555590678, - -112.13901142857144]) = 727.2480669876392 MtCO2eq.
- tar_emi_exclLU = 727.2480669876392 MtCO2eq
- tar_emi_inclLU = 615.1090555590678 MtCO2eq
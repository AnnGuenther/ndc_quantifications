## ['India']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | nan | nan | nan | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | nan | yes | nan | yes |
| Used | yes | yes | no | yes | no | yes |



## Target type used: REI, refyr: 2005, taryr: 2030, unconditional_worst
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -33.0 (-33%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -33.0 / 100. = 0.6699999999999999
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-163.6012 MtCO2eq).
    - bl_onlyLU_refyr = -163.6012 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (92.90015714285713 MtCO2eq).
    - bl_onlyLU_taryr = 92.90015714285713 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1807.0605 * 1.0 = 1807.0605 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 3965.4359999999997 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 16684396213126.37 2011GKD / 3131534500000.0 2011GKD = 5.327866007264608
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 5.327866007264608 * nan * 1807.0605 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 5.327866007264608 * 0.6699999999999999 * 1807.0605 + -163.6012 + 0.0 = 6287.0088613837925 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 6287.0088613837925 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([6287.0088613837925, - 92.90015714285713]) = 6194.108704240935 MtCO2eq.
- tar_emi_exclLU = 6194.108704240935 MtCO2eq
- tar_emi_inclLU = 6287.0088613837925 MtCO2eq



## Target type used: REI, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -35.0 (-35%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.0 / 100. = 0.65
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-163.6012 MtCO2eq).
    - bl_onlyLU_refyr = -163.6012 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (92.90015714285713 MtCO2eq).
    - bl_onlyLU_taryr = 92.90015714285713 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1807.0605 * 1.0 = 1807.0605 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 3965.4359999999997 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 16684396213126.37 2011GKD / 3131534500000.0 2011GKD = 5.327866007264608
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 5.327866007264608 * nan * 1807.0605 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 5.327866007264608 * 0.65 * 1807.0605 + -163.6012 + 0.0 = 6094.453337163382 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 6094.453337163382 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([6094.453337163382, - 92.90015714285713]) = 6001.553180020524 MtCO2eq.
- tar_emi_exclLU = 6001.553180020524 MtCO2eq
- tar_emi_inclLU = 6094.453337163382 MtCO2eq
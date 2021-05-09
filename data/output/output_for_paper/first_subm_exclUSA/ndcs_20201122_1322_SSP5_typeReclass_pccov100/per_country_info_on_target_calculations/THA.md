## ['Thailand']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | nan |
| Used | yes | yes | yes | yes | yes | yes | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | no |
| Used | yes | yes | yes | yes | yes | no |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 444.0 (444 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([444.0, 15.342237142857142]) = 459.34223714285713 MtCO2eq
- tar_emi_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = 459.34223714285713 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 416.0 (416 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 416.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([416.0, 15.342237142857142]) = 431.34223714285713 MtCO2eq
- tar_emi_exclLU = 416.0 MtCO2eq
- tar_emi_inclLU = 431.34223714285713 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -111.0 (-111 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 555.0 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 555.0 + -111.0 = 444.0 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([444.0, 15.342237142857142]) = 459.34223714285713 MtCO2eq
- tar_emi_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = 459.34223714285713 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -139.0 (-139 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 555.0 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 555.0 + -139.0 = 416.0 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 416.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([416.0, 15.342237142857142]) = 431.34223714285713 MtCO2eq
- tar_emi_exclLU = 416.0 MtCO2eq
- tar_emi_inclLU = 431.34223714285713 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -20.0 (-20%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.0 / 100. = 0.8
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 555.0 * 1.0 = 555.0 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 555.0 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8 * 555.0 + 0.0 = 444.0 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (555.0 + 15.342237142857142) + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([444.0, 15.342237142857142]) = 459.34223714285713 MtCO2eq
- tar_emi_exclLU = 444.0 MtCO2eq
- tar_emi_inclLU = 459.34223714285713 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -25.0 (-25%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 555.0 MtCO2eq, 555.0 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -25.0 / 100. = 0.75
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_refyr = 15.342237142857142 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142 MtCO2eq).
    - bl_onlyLU_taryr = 15.342237142857142 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 555.0 * 1.0 = 555.0 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 555.0 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.75 * 555.0 + 0.0 = 416.25 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (555.0 + 15.342237142857142) + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 416.25 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([416.25, 15.342237142857142]) = 431.59223714285713 MtCO2eq
- tar_emi_exclLU = 416.25 MtCO2eq
- tar_emi_inclLU = 431.59223714285713 MtCO2eq
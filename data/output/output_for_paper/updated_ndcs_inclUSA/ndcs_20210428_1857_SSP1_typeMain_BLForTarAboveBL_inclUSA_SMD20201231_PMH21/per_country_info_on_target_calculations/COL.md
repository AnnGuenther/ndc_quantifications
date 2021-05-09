## ['Colombia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | nan |
| Used | yes | yes | yes | yes | yes | yes | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 169.44 (169.44 MtCO2eq_AR5, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 345.8 MtCO2eq, 345.8 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 227.86 MtCO2eq, 227.86 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 117.94 MtCO2eq, 117.94 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_refyr = 117.94 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_taryr = 117.94 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 169.44 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([169.44, - 117.94]) = 51.5 MtCO2eq.
- tar_emi_exclLU = 51.5 MtCO2eq
- tar_emi_inclLU = 169.44 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -176.002 (-176.002 MtCO2eq_AR5, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 345.8 MtCO2eq, 345.8 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 227.86 MtCO2eq, 227.86 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 117.94 MtCO2eq, 117.94 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_refyr = 117.94 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_taryr = 117.94 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 345.8 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 345.8 + -176.002 = 169.798 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 169.798 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([169.798, - 117.94]) = 51.858000000000004 MtCO2eq.
- tar_emi_exclLU = 51.858000000000004 MtCO2eq
- tar_emi_inclLU = 169.798 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -51.0 (-51%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 345.8 MtCO2eq, 345.8 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 227.86 MtCO2eq, 227.86 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 117.94 MtCO2eq, 117.94 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -51.0 / 100. = 0.49
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_refyr = 117.94 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (117.94 MtCO2eq).
    - bl_onlyLU_taryr = 117.94 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 203.3702 * 0.9999995082858748 = 203.37010000000004 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 203.3702 * (1 - 0.9999995082858748) = 9.999999998368652e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 203.37010000000004 + 9.999999998368652e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.49 * (203.37010000000004 + 117.94) + 9.999999998368652e-05 = 157.442049 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 157.442049 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([157.442049, - 117.94]) = 39.502049 MtCO2eq.
- tar_emi_exclLU = 39.502049 MtCO2eq
- tar_emi_inclLU = 157.442049 MtCO2eq
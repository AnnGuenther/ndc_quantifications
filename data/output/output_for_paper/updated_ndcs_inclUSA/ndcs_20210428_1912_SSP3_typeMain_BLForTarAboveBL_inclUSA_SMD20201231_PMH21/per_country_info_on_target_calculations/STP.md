## ['Sao Tome & Principe']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 0.183 (0.183 MtCO2eq, from NDC)
- ndc_value_inclLU: -0.447 (-0.447 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -0.39 MtCO2eq, -0.39 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 0.24 MtCO2eq, 0.24 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -0.63 MtCO2eq, -0.63 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_refyr = -0.63 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_taryr = -0.63 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.183 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -0.447 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.183 MtCO2eq
- tar_emi_inclLU = -0.447 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.057 (-0.057 MtCO2eq, from NDC)
- ndc_value_inclLU: -0.057 (-0.057 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -0.39 MtCO2eq, -0.39 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 0.24 MtCO2eq, 0.24 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -0.63 MtCO2eq, -0.63 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_refyr = -0.63 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_taryr = -0.63 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 0.24 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.24 + -0.057 = 0.183 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -0.39 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -0.39 + -0.057 = -0.447 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 0.183 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -0.447 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.183 MtCO2eq
- tar_emi_inclLU = -0.447 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -24.0 (-24%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -0.39 MtCO2eq, -0.39 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 0.24 MtCO2eq, 0.24 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -0.63 MtCO2eq, -0.63 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -24.0 / 100. = 0.76
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_refyr = -0.63 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63 MtCO2eq).
    - bl_onlyLU_taryr = -0.63 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.2085066666666667 * 0.99999520399028 = 0.20850566666666667 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.2085066666666667 * (1 - 0.99999520399028) = 1.0000000000247414e-06 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.76 * 0.20850566666666667 + 1.0000000000247414e-06 = 0.1584653066666667 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.20850566666666667 + -0.63 + 1.0000000000247414e-06 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 0.1584653066666667 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.1584653066666667, -0.63]) = -0.4715346933333333 MtCO2eq
- tar_emi_exclLU = 0.1584653066666667 MtCO2eq
- tar_emi_inclLU = -0.4715346933333333 MtCO2eq
## ['Bhutan']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 6.3 (6.3 MtCO2eq, from NDC)
- ndc_value_inclLU: 0.0 (0 MtCO2eq, from NDC)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (-3.6078142571428566 MtCO2eq).
    - bl_onlyLU_refyr = -3.6078142571428566 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-3.6078142571428566 MtCO2eq).
    - bl_onlyLU_taryr = -3.6078142571428566 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 6.3 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 6.3 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq



## Target type used: ABS, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: 6.3 (6.3 MtCO2eq, from NDC)
- ndc_value_inclLU: 0.0 (0 MtCO2eq, from NDC)
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
    - emi_onlyLU 2050: external_emi_onlyLU used (-3.6078142571428566 MtCO2eq).
    - bl_onlyLU_refyr = -3.6078142571428566 MtCO2eq
    - emi_onlyLU 2050: external_emi_onlyLU used (-3.6078142571428566 MtCO2eq).
    - bl_onlyLU_taryr = -3.6078142571428566 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 6.3 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 6.3 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq
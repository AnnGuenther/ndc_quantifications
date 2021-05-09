## ['Maldives']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | no | nan | nan | no | nan |
| Used | yes | yes | no | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | yes | nan | nan |
| Used | yes | no | no | yes | no | no |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 2.43084 (2.43084 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.43084 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.43084, - 1.6192199999999997]) = 0.8116200000000002 MtCO2eq.
- tar_emi_exclLU = 0.8116200000000002 MtCO2eq
- tar_emi_inclLU = 2.43084 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 0.0 (0 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([0.0, - 1.6192199999999997]) = -1.6192199999999997 MtCO2eq.
- tar_emi_exclLU = -1.6192199999999997 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -0.85408 (-0.85408 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 3.2849199999999996 + -0.85408 = 2.43084 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.43084 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.43084, - 1.6192199999999997]) = 0.8116200000000002 MtCO2eq.
- tar_emi_exclLU = 0.8116200000000002 MtCO2eq
- tar_emi_inclLU = 2.43084 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -3.28492 (-3.28492 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 3.2849199999999996 + -3.28492 = -4.440892098500626e-16 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -4.440892098500626e-16 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-4.440892098500626e-16, - 1.6192199999999997]) = -1.61922 MtCO2eq.
- tar_emi_exclLU = -1.61922 MtCO2eq
- tar_emi_inclLU = -4.440892098500626e-16 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -26.0 (-26%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -26.0 / 100. = 0.74
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.6657 * 1.0 = 1.6657 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.6657 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 1.6657 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.74 * (1.6657 + 1.6192199999999997) + 0.0 = 2.4308407999999995 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.4308407999999995 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.4308407999999995, - 1.6192199999999997]) = 0.8116207999999998 MtCO2eq.
- tar_emi_exclLU = 0.8116207999999998 MtCO2eq
- tar_emi_inclLU = 2.4308407999999995 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -100.0 (-100%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -100.0 / 100. = 0.0
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.6657 * 1.0 = 1.6657 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.6657 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 1.6657 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.0 * (1.6657 + 1.6192199999999997) + 0.0 = 0.0 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([0.0, - 1.6192199999999997]) = -1.6192199999999997 MtCO2eq.
- tar_emi_exclLU = -1.6192199999999997 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq
- MDV LULUCF: second try as some tar_exclLU values < 0 (first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU; 
    second try: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year). 
    Negative tar_exclLU for ['ABS' 'ABU' 'RBU'], with type_main = ['RBU'] and type_reclass = ['ABS'].



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | no | nan | nan | no | nan |
| Used | yes | yes | no | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | yes | nan | nan |
| Used | yes | no | no | yes | no | no |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 2.43084 (2.43084 MtCO2eq, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.43084 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.43084 - 3.2849199999999996 = -0.8540799999999997 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -0.8540799999999997 * 1.6657/3.2849199999999996 = -0.4330824056598029 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -0.4330824056598029 = 1.2326175943401971 MtCO2eq
- tar_emi_exclLU = 1.2326175943401971 MtCO2eq
- tar_emi_inclLU = 2.43084 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 0.0 (0 MtCO2eq, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 0.0 - 3.2849199999999996 = -3.2849199999999996 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -3.2849199999999996 * 1.6657/3.2849199999999996 = -1.6657000000000002 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -1.6657000000000002 = -2.220446049250313e-16 MtCO2eq
- tar_emi_exclLU = -2.220446049250313e-16 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -0.85408 (-0.85408 MtCO2eq, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 3.2849199999999996 + -0.85408 = 2.43084 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.43084 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.43084 - 3.2849199999999996 = -0.8540799999999997 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -0.8540799999999997 * 1.6657/3.2849199999999996 = -0.4330824056598029 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -0.4330824056598029 = 1.2326175943401971 MtCO2eq
- tar_emi_exclLU = 1.2326175943401971 MtCO2eq
- tar_emi_inclLU = 2.43084 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -3.28492 (-3.28492 MtCO2eq, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 3.2849199999999996 + -3.28492 = -4.440892098500626e-16 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -4.440892098500626e-16 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = -4.440892098500626e-16 - 3.2849199999999996 = -3.28492 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -3.28492 * 1.6657/3.2849199999999996 = -1.6657000000000002 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -1.6657000000000002 = -2.220446049250313e-16 MtCO2eq
- tar_emi_exclLU = -2.220446049250313e-16 MtCO2eq
- tar_emi_inclLU = -4.440892098500626e-16 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -26.0 (-26%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -26.0 / 100. = 0.74
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.6657 * 1.0 = 1.6657 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.6657 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 1.6657 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.74 * (1.6657 + 1.6192199999999997) + 0.0 = 2.4308407999999995 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.4308407999999995 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([1.6657, 1.6192199999999997]) = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.4308407999999995 - 3.2849199999999996 = -0.8540792000000001 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -0.8540792000000001 * 1.6657/3.2849199999999996 = -0.4330820000000001 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -0.4330820000000001 = 1.232618 MtCO2eq
- tar_emi_exclLU = 1.232618 MtCO2eq
- tar_emi_inclLU = 2.4308407999999995 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -100.0 (-100%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 3.2849199999999996 MtCO2eq, 3.2849199999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -100.0 / 100. = 0.0
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - *something went wrong with the LULUCF coverage.* The ndc-value is inclLU but the LULUCF sector is not covered!
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_refyr = 1.6192199999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 3.2849199999999996 - 1.6657 = 1.6192199999999997 MtCO2eq
    - bl_onlyLU_taryr = 1.6192199999999997 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.6657 * 1.0 = 1.6657 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.6657 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 1.6657 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.0 * (1.6657 + 1.6192199999999997) + 0.0 = 0.0 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 0.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 3.2849199999999996 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([1.6657, 1.6192199999999997]) = 3.2849199999999996 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 1.6657 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 0.0 - 3.2849199999999996 = -3.2849199999999996 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -3.2849199999999996 * 1.6657/3.2849199999999996 = -1.6657000000000002 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 1.6657 + -1.6657000000000002 = -2.220446049250313e-16 MtCO2eq
- tar_emi_exclLU = -2.220446049250313e-16 MtCO2eq
- tar_emi_inclLU = 0.0 MtCO2eq    Second method also didn't work for all targets ... so the negative tar_emi_exclLU are set to 0.
## ['Namibia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.4424749448561762 (-2.265 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 24.42151438240963 + -2.4424749448561762 = 21.979039437553453 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979039437553453 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([21.979039437553453, - 10.52981438240963]) = 11.449225055143824 MtCO2eq.
- tar_emi_exclLU = 11.449225055143824 MtCO2eq
- tar_emi_inclLU = 21.979039437553453 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -21.625338871587527 (-20.054 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 24.42151438240963 + -21.625338871587527 = 2.7961755108221027 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.7961755108221027 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.7961755108221027, - 10.52981438240963]) = -7.733638871587527 MtCO2eq.
- tar_emi_exclLU = -7.733638871587527 MtCO2eq
- tar_emi_inclLU = 2.7961755108221027 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 21.979039437553457 (20.382 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979039437553457 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([21.979039437553457, - 10.52981438240963]) = 11.449225055143827 MtCO2eq.
- tar_emi_exclLU = 11.449225055143827 MtCO2eq
- tar_emi_inclLU = 21.979039437553457 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 2.686398932726581 (2.4912 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.686398932726581 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.686398932726581, - 10.52981438240963]) = -7.843415449683048 MtCO2eq.
- tar_emi_exclLU = -7.843415449683048 MtCO2eq
- tar_emi_inclLU = 2.686398932726581 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -10.0 (-10%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.0 / 100. = 0.9
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 13.8917 * 0.9999928014569852 = 13.891600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 13.8917 * (1 - 0.9999928014569852) = 9.999999999850047e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 13.891600000000002 + 9.999999999850047e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.9 * (13.891600000000002 + 10.52981438240963) + 9.999999999850047e-05 = 21.979372944168666 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979372944168666 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([21.979372944168666, - 10.52981438240963]) = 11.449558561759037 MtCO2eq.
- tar_emi_exclLU = 11.449558561759037 MtCO2eq
- tar_emi_inclLU = 21.979372944168666 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -88.6 (-88.6%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -88.6 / 100. = 0.1140000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 13.8917 * 0.9999928014569852 = 13.891600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 13.8917 * (1 - 0.9999928014569852) = 9.999999999850047e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 13.891600000000002 + 9.999999999850047e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.1140000000000001 * (13.891600000000002 + 10.52981438240963) + 9.999999999850047e-05 = 2.7841412395946987 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.7841412395946987 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([2.7841412395946987, - 10.52981438240963]) = -7.745673142814931 MtCO2eq.
- tar_emi_exclLU = -7.745673142814931 MtCO2eq
- tar_emi_inclLU = 2.7841412395946987 MtCO2eq
- NAM LULUCF: second try as some tar_exclLU values < 0 (first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU; 
    second try: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year). 
    Negative tar_exclLU for ['ABU' 'ABS' 'RBU'], with type_main = ['RBU'] and type_reclass = ['ABS'].



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.4424749448561762 (-2.265 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 24.42151438240963 + -2.4424749448561762 = 21.979039437553453 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979039437553453 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 21.979039437553453 - 24.42151438240963 = -2.4424749448561762 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.4424749448561762 * 13.8917/24.42151438240963 = -1.3893540204000532 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -1.3893540204000532 = 12.502345979599948 MtCO2eq
- tar_emi_exclLU = 12.502345979599948 MtCO2eq
- tar_emi_inclLU = 21.979039437553453 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -21.625338871587527 (-20.054 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 24.42151438240963 + -21.625338871587527 = 2.7961755108221027 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.7961755108221027 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.7961755108221027 - 24.42151438240963 = -21.625338871587527 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -21.625338871587527 * 13.8917/24.42151438240963 = -12.30115034220868 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -12.30115034220868 = 1.5905496577913194 MtCO2eq
- tar_emi_exclLU = 1.5905496577913194 MtCO2eq
- tar_emi_inclLU = 2.7961755108221027 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 21.979039437553457 (20.382 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979039437553457 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 21.979039437553457 - 24.42151438240963 = -2.4424749448561727 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.4424749448561727 * 13.8917/24.42151438240963 = -1.3893540204000512 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -1.3893540204000512 = 12.50234597959995 MtCO2eq
- tar_emi_exclLU = 12.50234597959995 MtCO2eq
- tar_emi_inclLU = 21.979039437553457 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 2.686398932726581 (2.4912 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.686398932726581 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.686398932726581 - 24.42151438240963 = -21.73511544968305 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -21.73511544968305 * 13.8917/24.42151438240963 = -12.363594597959995 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -12.363594597959995 = 1.528105402040005 MtCO2eq
- tar_emi_exclLU = 1.528105402040005 MtCO2eq
- tar_emi_inclLU = 2.686398932726581 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -10.0 (-10%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.0 / 100. = 0.9
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 13.8917 * 0.9999928014569852 = 13.891600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 13.8917 * (1 - 0.9999928014569852) = 9.999999999850047e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 13.891600000000002 + 9.999999999850047e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.9 * (13.891600000000002 + 10.52981438240963) + 9.999999999850047e-05 = 21.979372944168666 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 21.979372944168666 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([13.8917, 10.52981438240963]) = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 21.979372944168666 - 24.42151438240963 = -2.442141438240963 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.442141438240963 * 13.8917/24.42151438240963 = -1.389164311695916 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -1.389164311695916 = 12.502535688304084 MtCO2eq
- tar_emi_exclLU = 12.502535688304084 MtCO2eq
- tar_emi_inclLU = 21.979372944168666 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -88.6 (-88.6%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 24.42151438240963 MtCO2eq, 24.42151438240963 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -88.6 / 100. = 0.1140000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_refyr = 10.52981438240963 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 24.42151438240963 - 13.8917 = 10.52981438240963 MtCO2eq
    - bl_onlyLU_taryr = 10.52981438240963 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 13.8917 * 0.9999928014569852 = 13.891600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 13.8917 * (1 - 0.9999928014569852) = 9.999999999850047e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 13.891600000000002 + 9.999999999850047e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.1140000000000001 * (13.891600000000002 + 10.52981438240963) + 9.999999999850047e-05 = 2.7841412395946987 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 2.7841412395946987 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 24.42151438240963 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([13.8917, 10.52981438240963]) = 24.42151438240963 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 13.8917 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 2.7841412395946987 - 24.42151438240963 = -21.63737314281493 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -21.63737314281493 * 13.8917/24.42151438240963 = -12.307995801625815 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 13.8917 + -12.307995801625815 = 1.5837041983741855 MtCO2eq
- tar_emi_exclLU = 1.5837041983741855 MtCO2eq
- tar_emi_inclLU = 2.7841412395946987 MtCO2eq
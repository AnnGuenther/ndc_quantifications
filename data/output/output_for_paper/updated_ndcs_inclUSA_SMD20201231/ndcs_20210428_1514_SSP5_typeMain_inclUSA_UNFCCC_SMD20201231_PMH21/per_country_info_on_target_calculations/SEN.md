## ['Senegal']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -1.7701162790827942 (-1.662 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 34.77181484927501 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 34.77181484927501 + -1.7701162790827942 = 33.00169857019222 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 33.00169857019222 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([33.00169857019222, -12.325845786898425]) = 20.67585278329379 MtCO2eq
- tar_emi_exclLU = 33.00169857019222 MtCO2eq
- tar_emi_inclLU = 20.67585278329379 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -2.8277128284986874 (-2.655 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.2174252794497 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.2174252794497 + -2.8277128284986874 = 37.38971245095101 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 37.38971245095101 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([37.38971245095101, -12.259812568304474]) = 25.129899882646534 MtCO2eq
- tar_emi_exclLU = 37.38971245095101 MtCO2eq
- tar_emi_inclLU = 25.129899882646534 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -8.271193154847762 (-7.766 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 34.77181484927501 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 34.77181484927501 + -8.271193154847762 = 26.50062169442725 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 26.50062169442725 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([26.50062169442725, -12.325845786898425]) = 14.174775907528824 MtCO2eq
- tar_emi_exclLU = 26.50062169442725 MtCO2eq
- tar_emi_inclLU = 14.174775907528824 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -11.875328827781683 (-11.150 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.2174252794497 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.2174252794497 + -11.875328827781683 = 28.342096451668016 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 28.342096451668016 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([28.342096451668016, -12.259812568304474]) = 16.082283883363544 MtCO2eq
- tar_emi_exclLU = 28.342096451668016 MtCO2eq
- tar_emi_inclLU = 16.082283883363544 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 33.00276362210502 (30.987 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 33.00276362210502 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([33.00276362210502, -12.325845786898425]) = 20.676917835206595 MtCO2eq
- tar_emi_exclLU = 33.00276362210502 MtCO2eq
- tar_emi_inclLU = 20.676917835206595 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 37.38971245095101 (35.106 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 37.38971245095101 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([37.38971245095101, -12.259812568304474]) = 25.129899882646534 MtCO2eq
- tar_emi_exclLU = 37.38971245095101 MtCO2eq
- tar_emi_inclLU = 25.129899882646534 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 26.501686746340052 (24.883 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 26.501686746340052 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([26.501686746340052, -12.325845786898425]) = 14.175840959441627 MtCO2eq
- tar_emi_exclLU = 26.501686746340052 MtCO2eq
- tar_emi_inclLU = 14.175840959441627 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 28.342096451668013 (26.611 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 28.342096451668013 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([28.342096451668013, -12.259812568304474]) = 16.082283883363537 MtCO2eq
- tar_emi_exclLU = 28.342096451668013 MtCO2eq
- tar_emi_inclLU = 16.082283883363537 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -5.0 (-5%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -5.0 / 100. = 0.95
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 34.9824 * 0.9999971414196852 = 34.982299999999995 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 34.9824 * (1 - 0.9999971414196852) = 0.00010000000000413393 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.95 * 34.982299999999995 + 0.00010000000000413393 = 33.233284999999995 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 34.982299999999995 + -12.325845786898425 + 0.00010000000000413393 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 33.233284999999995 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([33.233284999999995, -12.325845786898425]) = 20.90743921310157 MtCO2eq
- tar_emi_exclLU = 33.233284999999995 MtCO2eq
- tar_emi_inclLU = 20.90743921310157 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -7.0 (-7%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -7.0 / 100. = 0.9299999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 44.7957 * 1.0 = 44.7957 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 44.7957 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.9299999999999999 * 44.7957 + 0.0 = 41.660000999999994 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 44.7957 + -12.259812568304474 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 41.660000999999994 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([41.660000999999994, -12.259812568304474]) = 29.40018843169552 MtCO2eq
- tar_emi_exclLU = 41.660000999999994 MtCO2eq
- tar_emi_inclLU = 29.40018843169552 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -23.7 (-23.7%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.77181484927501 MtCO2eq, 34.77181484927501 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.325845786898425 MtCO2eq, -12.325845786898425 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -23.7 / 100. = 0.763
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_refyr = -12.325845786898425 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-12.325845786898425 MtCO2eq).
    - bl_onlyLU_taryr = -12.325845786898425 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 34.9824 * 0.9999971414196852 = 34.982299999999995 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 34.9824 * (1 - 0.9999971414196852) = 0.00010000000000413393 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.763 * 34.982299999999995 + 0.00010000000000413393 = 26.6915949 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 34.982299999999995 + -12.325845786898425 + 0.00010000000000413393 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 26.6915949 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([26.6915949, -12.325845786898425]) = 14.365749113101574 MtCO2eq
- tar_emi_exclLU = 26.6915949 MtCO2eq
- tar_emi_inclLU = 14.365749113101574 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -29.5 (-29.5%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.2174252794497 MtCO2eq, 40.2174252794497 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -12.259812568304474 MtCO2eq, -12.259812568304474 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -29.5 / 100. = 0.7050000000000001
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_refyr = -12.259812568304474 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-12.259812568304474 MtCO2eq).
    - bl_onlyLU_taryr = -12.259812568304474 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 44.7957 * 1.0 = 44.7957 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 44.7957 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.7050000000000001 * 44.7957 + 0.0 = 31.5809685 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 44.7957 + -12.259812568304474 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 31.5809685 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([31.5809685, -12.259812568304474]) = 19.32115593169553 MtCO2eq
- tar_emi_exclLU = 31.5809685 MtCO2eq
- tar_emi_inclLU = 19.32115593169553 MtCO2eq
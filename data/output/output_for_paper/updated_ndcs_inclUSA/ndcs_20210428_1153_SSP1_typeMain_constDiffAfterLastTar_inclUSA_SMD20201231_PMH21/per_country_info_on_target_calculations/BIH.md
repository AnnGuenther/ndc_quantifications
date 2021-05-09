## ['Bosnia & Herzegovina']



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
- ndc_value_inclLU: -1.6697333624492292 (-1.634 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 34.382188 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 34.382188 + -1.6697333624492292 = 32.71245463755077 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 32.71245463755077 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([32.71245463755077, - -6.47]) = 39.18245463755077 MtCO2eq.
- tar_emi_exclLU = 39.18245463755077 MtCO2eq
- tar_emi_inclLU = 32.71245463755077 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -8.975072290325325 (-8.783 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 34.382188 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 34.382188 + -8.975072290325325 = 25.407115709674674 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 25.407115709674674 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([25.407115709674674, - -6.47]) = 31.877115709674673 MtCO2eq.
- tar_emi_exclLU = 31.877115709674673 MtCO2eq
- tar_emi_inclLU = 25.407115709674674 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 33.46415431669973 (32.748 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 33.46415431669973 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([33.46415431669973, - -6.47]) = 39.934154316699725 MtCO2eq.
- tar_emi_exclLU = 39.934154316699725 MtCO2eq
- tar_emi_inclLU = 33.46415431669973 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 26.158815388823637 (25.599 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 26.158815388823637 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([26.158815388823637, - -6.47]) = 32.62881538882364 MtCO2eq.
- tar_emi_exclLU = 32.62881538882364 MtCO2eq
- tar_emi_inclLU = 26.158815388823637 MtCO2eq



## Target type used: RBY, refyr: 1990, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 18.0 (+18%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 26.61996 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.043490000000006 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -7.42353 MtCO2eq, -6.47 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + 18.0 / 100. = 1.18
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-7.42353 MtCO2eq).
    - bl_onlyLU_refyr = -7.42353 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 35.7405 * 0.9795243352878078 = 35.00868950535389 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 31.9636 * (1 - 0.9300454266728404) = 2.2359999999999984 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 35.00868950535389 + 2.2359999999999984 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 1.18 * 35.00868950535389 + -7.42353 + 2.2359999999999984 = 36.122723616317586 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 36.122723616317586 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([36.122723616317586, - -6.47]) = 42.592723616317585 MtCO2eq.
- tar_emi_exclLU = 42.592723616317585 MtCO2eq
- tar_emi_inclLU = 36.122723616317586 MtCO2eq



## Target type used: RBY, refyr: 1990, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -3.0 (-3%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 26.61996 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 34.043490000000006 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -7.42353 MtCO2eq, -6.47 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -3.0 / 100. = 0.97
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-7.42353 MtCO2eq).
    - bl_onlyLU_refyr = -7.42353 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 35.7405 * 0.9795243352878078 = 35.00868950535389 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 31.9636 * (1 - 0.9300454266728404) = 2.2359999999999984 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 35.00868950535389 + 2.2359999999999984 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.97 * 35.00868950535389 + -7.42353 + 2.2359999999999984 = 28.770898820193274 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 28.770898820193274 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([28.770898820193274, - -6.47]) = 35.24089882019327 MtCO2eq.
- tar_emi_exclLU = 35.24089882019327 MtCO2eq
- tar_emi_inclLU = 28.770898820193274 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.0 (-2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.0 / 100. = 0.98
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 31.9636 * 0.9300454266728404 = 29.727600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 31.9636 * (1 - 0.9300454266728404) = 2.2359999999999984 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 29.727600000000002 + 2.2359999999999984 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.98 * 29.727600000000002 + -6.47 + 2.2359999999999984 = 24.899048 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 24.899048 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([24.899048, - -6.47]) = 31.369048 MtCO2eq.
- tar_emi_exclLU = 31.369048 MtCO2eq
- tar_emi_inclLU = 24.899048 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -23.0 (-23%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 34.382188 MtCO2eq, 34.382188 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 40.852188 MtCO2eq, 40.852188 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -6.47 MtCO2eq, -6.47 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -23.0 / 100. = 0.77
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_refyr = -6.47 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-6.47 MtCO2eq).
    - bl_onlyLU_taryr = -6.47 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 31.9636 * 0.9300454266728404 = 29.727600000000002 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 31.9636 * (1 - 0.9300454266728404) = 2.2359999999999984 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 29.727600000000002 + 2.2359999999999984 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.77 * 29.727600000000002 + -6.47 + 2.2359999999999984 = 18.656252000000002 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 18.656252000000002 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([18.656252000000002, - -6.47]) = 25.126252 MtCO2eq.
- tar_emi_exclLU = 25.126252 MtCO2eq
- tar_emi_inclLU = 18.656252000000002 MtCO2eq
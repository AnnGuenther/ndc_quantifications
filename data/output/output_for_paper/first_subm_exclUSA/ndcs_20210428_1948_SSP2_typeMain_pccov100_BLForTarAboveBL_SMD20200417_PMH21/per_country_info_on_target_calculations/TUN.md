## ['Tunisia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -4.2 (-4.2 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 51.6 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 51.6 + -4.2 = 47.4 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 47.4 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([47.4, - 3.409700000000001]) = 43.9903 MtCO2eq.
- tar_emi_exclLU = 43.9903 MtCO2eq
- tar_emi_inclLU = 47.4 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -6.0 (-6.0 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 68.2 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 68.2 + -6.0 = 62.2 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.2 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([62.2, - 12.458200000000005]) = 49.7418 MtCO2eq.
- tar_emi_exclLU = 49.7418 MtCO2eq
- tar_emi_inclLU = 62.2 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -16.6 (-16.6 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 51.6 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 51.6 + -16.6 = 35.0 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([35.0, - 3.409700000000001]) = 31.5903 MtCO2eq.
- tar_emi_exclLU = 31.5903 MtCO2eq
- tar_emi_inclLU = 35.0 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -25.8 (-25.8 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 68.2 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 68.2 + -25.8 = 42.400000000000006 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 42.400000000000006 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([42.400000000000006, - 12.458200000000005]) = 29.9418 MtCO2eq.
- tar_emi_exclLU = 29.9418 MtCO2eq
- tar_emi_inclLU = 42.400000000000006 MtCO2eq



## Target type used: REI, refyr: 2010, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -13.0 (-13%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.3 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -13.0 / 100. = 0.87
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2010: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 28.3 - 39.7174 = -11.417399999999997 MtCO2eq
    - bl_onlyLU_refyr = -11.417399999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 39.7174 * 1.0 = 39.7174 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 55.7418 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 244849805741.8093 2011GKD / 110864757812.5 2011GKD = 2.20854499277319
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 2.20854499277319 * nan * 39.7174 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 2.20854499277319 * 0.87 * 39.7174 + -11.417399999999997 + 0.0 = 64.8969684594938 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 64.8969684594938 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([64.8969684594938, - 12.458200000000005]) = 52.4387684594938 MtCO2eq.
- tar_emi_exclLU = 52.4387684594938 MtCO2eq
- tar_emi_inclLU = 64.8969684594938 MtCO2eq



## Target type used: REI, refyr: 2010, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -41.0 (-41%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 28.3 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -41.0 / 100. = 0.5900000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2010: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 28.3 - 39.7174 = -11.417399999999997 MtCO2eq
    - bl_onlyLU_refyr = -11.417399999999997 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 39.7174 * 1.0 = 39.7174 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 55.7418 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = ict[ict['int_ref'] + '\_taryr'] / ict[ict['int_ref'] + '\_refyr'] = 244849805741.8093 2011GKD / 110864757812.5 2011GKD = 2.20854499277319
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 2.20854499277319 * nan * 39.7174 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 2.20854499277319 * 0.5900000000000001 * 39.7174 + -11.417399999999997 + 0.0 = 40.336022288622246 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 40.336022288622246 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([40.336022288622246, - 12.458200000000005]) = 27.87782228862224 MtCO2eq.
- tar_emi_exclLU = 27.87782228862224 MtCO2eq
- tar_emi_inclLU = 40.336022288622246 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 47.4 (47.4 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 47.4 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([47.4, - 3.409700000000001]) = 43.9903 MtCO2eq.
- tar_emi_exclLU = 43.9903 MtCO2eq
- tar_emi_inclLU = 47.4 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 62.2 (62.2 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.2 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([62.2, - 12.458200000000005]) = 49.7418 MtCO2eq.
- tar_emi_exclLU = 49.7418 MtCO2eq
- tar_emi_inclLU = 62.2 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 35.0 (35.0 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 35.0 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([35.0, - 3.409700000000001]) = 31.5903 MtCO2eq.
- tar_emi_exclLU = 31.5903 MtCO2eq
- tar_emi_inclLU = 35.0 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 42.4 (42.4 MtCO2eq_AR4, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 42.4 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([42.4, - 12.458200000000005]) = 29.941799999999994 MtCO2eq.
- tar_emi_exclLU = 29.941799999999994 MtCO2eq
- tar_emi_inclLU = 42.4 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -8.1 (-8.1%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -8.1 / 100. = 0.919
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 48.1903 * 1.0 = 48.1903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 48.1903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 48.1903 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.919 * (48.1903 + 3.409700000000001) + 0.0 = 47.4204 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 47.4204 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([47.4204, - 3.409700000000001]) = 44.0107 MtCO2eq.
- tar_emi_exclLU = 44.0107 MtCO2eq
- tar_emi_inclLU = 47.4204 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -8.8 (-8.8%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -8.8 / 100. = 0.912
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 55.7418 * 1.0 = 55.7418 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 55.7418 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 55.7418 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.912 * (55.7418 + 12.458200000000005) + 0.0 = 62.19840000000001 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.19840000000001 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([62.19840000000001, - 12.458200000000005]) = 49.7402 MtCO2eq.
- tar_emi_exclLU = 49.7402 MtCO2eq
- tar_emi_inclLU = 62.19840000000001 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -32.2 (-32.2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 51.6 MtCO2eq, 51.6 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -32.2 / 100. = 0.6779999999999999
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_refyr = 3.409700000000001 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 51.6 - 48.1903 = 3.409700000000001 MtCO2eq
    - bl_onlyLU_taryr = 3.409700000000001 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 48.1903 * 1.0 = 48.1903 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 48.1903 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 48.1903 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.6779999999999999 * (48.1903 + 3.409700000000001) + 0.0 = 34.9848 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 34.9848 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([34.9848, - 3.409700000000001]) = 31.5751 MtCO2eq.
- tar_emi_exclLU = 31.5751 MtCO2eq
- tar_emi_inclLU = 34.9848 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -37.8 (-37.8%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 68.2 MtCO2eq, 68.2 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -37.8 / 100. = 0.6220000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_refyr = 12.458200000000005 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 68.2 - 55.7418 = 12.458200000000005 MtCO2eq
    - bl_onlyLU_taryr = 12.458200000000005 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 55.7418 * 1.0 = 55.7418 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 55.7418 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 55.7418 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.6220000000000001 * (55.7418 + 12.458200000000005) + 0.0 = 42.42040000000001 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 42.42040000000001 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([42.42040000000001, - 12.458200000000005]) = 29.962200000000003 MtCO2eq.
- tar_emi_exclLU = 29.962200000000003 MtCO2eq
- tar_emi_inclLU = 42.42040000000001 MtCO2eq
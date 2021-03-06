## ['Burundi']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | nan | nan | yes |
| Used | yes | no | yes | no | no | yes |



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 62.982222002881095 (57.054 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.982222002881095 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([62.982222002881095, - 55.80476795603694]) = 7.177454046844154 MtCO2eq.
- tar_emi_exclLU = 7.177454046844154 MtCO2eq
- tar_emi_inclLU = 62.982222002881095 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 79.75716934322149 (72.250 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.75716934322149 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([79.75716934322149, - 72.65449804193567]) = 7.102671301285824 MtCO2eq.
- tar_emi_exclLU = 7.102671301285824 MtCO2eq
- tar_emi_inclLU = 79.75716934322149 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 53.34181563783814 (48.321 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.34181563783814 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([53.34181563783814, - 55.80476795603694]) = -2.462952318198802 MtCO2eq.
- tar_emi_exclLU = -2.462952318198802 MtCO2eq
- tar_emi_inclLU = 53.34181563783814 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 65.77951843354855 (59.588 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.77951843354855 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([65.77951843354855, - 72.65449804193567]) = -6.874979608387122 MtCO2eq.
- tar_emi_exclLU = -6.874979608387122 MtCO2eq
- tar_emi_inclLU = 65.77951843354855 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -1.2849459531558451 (-1.164 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 64.26716795603694 + -1.2849459531558451 = 62.982222002881095 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.982222002881095 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([62.982222002881095, - 55.80476795603694]) = 7.177454046844154 MtCO2eq.
- tar_emi_exclLU = 7.177454046844154 MtCO2eq
- tar_emi_inclLU = 62.982222002881095 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.4672286987141874 (-2.235 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 82.22439804193567 + -2.4672286987141874 = 79.75716934322148 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.75716934322148 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([79.75716934322148, - 72.65449804193567]) = 7.10267130128581 MtCO2eq.
- tar_emi_exclLU = 7.10267130128581 MtCO2eq
- tar_emi_inclLU = 79.75716934322148 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -10.925352318198797 (-9.897 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 64.26716795603694 + -10.925352318198797 = 53.341815637838145 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.341815637838145 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([53.341815637838145, - 55.80476795603694]) = -2.462952318198795 MtCO2eq.
- tar_emi_exclLU = -2.462952318198795 MtCO2eq
- tar_emi_inclLU = 53.341815637838145 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -16.444879608387136 (-14.897 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 82.22439804193567 + -16.444879608387136 = 65.77951843354853 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.77951843354853 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([65.77951843354853, - 72.65449804193567]) = -6.874979608387136 MtCO2eq.
- tar_emi_exclLU = -6.874979608387136 MtCO2eq
- tar_emi_inclLU = 65.77951843354853 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.0 (-2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.0 / 100. = 0.98
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 8.4624 * 0.7612244601193747 = 6.441785871314197 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 8.4624 * (1 - 0.7612244601193747) = 2.0206141286858035 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 6.441785871314197 + 2.0206141286858035 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.98 * (6.441785871314197 + 55.80476795603694) + 2.0206141286858035 = 63.02223687948991 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 63.02223687948991 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([63.02223687948991, - 55.80476795603694]) = 7.217468923452969 MtCO2eq.
- tar_emi_exclLU = 7.217468923452969 MtCO2eq
- tar_emi_inclLU = 63.02223687948991 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -3.0 (-3%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -3.0 / 100. = 0.97
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 9.5699 * 0.7675568463623149 = 7.345442264002718 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 9.5699 * (1 - 0.7675568463623149) = 2.224457735997283 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 7.345442264002718 + 2.224457735997283 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.97 * (7.345442264002718 + 72.65449804193567) + 2.224457735997283 = 79.8243998327575 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.8243998327575 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([79.8243998327575, - 72.65449804193567]) = 7.169901790821839 MtCO2eq.
- tar_emi_exclLU = 7.169901790821839 MtCO2eq
- tar_emi_inclLU = 79.8243998327575 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -17.0 (-17%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -17.0 / 100. = 0.83
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 8.4624 * 0.7612244601193747 = 6.441785871314197 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 8.4624 * (1 - 0.7612244601193747) = 2.0206141286858035 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 6.441785871314197 + 2.0206141286858035 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.83 * (6.441785871314197 + 55.80476795603694) + 2.0206141286858035 = 53.68525380538725 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.68525380538725 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([53.68525380538725, - 55.80476795603694]) = -2.1195141506496924 MtCO2eq.
- tar_emi_exclLU = -2.1195141506496924 MtCO2eq
- tar_emi_inclLU = 53.68525380538725 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -20.0 (-20%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -20.0 / 100. = 0.8
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 9.5699 * 0.7675568463623149 = 7.345442264002718 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 9.5699 * (1 - 0.7675568463623149) = 2.224457735997283 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 7.345442264002718 + 2.224457735997283 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8 * (7.345442264002718 + 72.65449804193567) + 2.224457735997283 = 66.22440998074799 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 66.22440998074799 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([66.22440998074799, - 72.65449804193567]) = -6.430088061187675 MtCO2eq.
- tar_emi_exclLU = -6.430088061187675 MtCO2eq
- tar_emi_inclLU = 66.22440998074799 MtCO2eq
- BDI LULUCF: second try as some tar_exclLU values < 0 (first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU; 
    second try: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year). 
    Negative tar_exclLU for ['ABS' 'ABU' 'RBU'], with type_main = ['RBU'] and type_reclass = ['ABS'].



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | nan | nan | yes |
| Used | yes | no | yes | no | no | yes |



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 62.982222002881095 (57.054 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.982222002881095 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 62.982222002881095 - 64.26716795603694 = -1.284945953155848 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -1.284945953155848 * 8.4624/64.26716795603694 = -0.1691956714418225 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -0.1691956714418225 = 8.293204328558177 MtCO2eq
- tar_emi_exclLU = 8.293204328558177 MtCO2eq
- tar_emi_inclLU = 62.982222002881095 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 79.75716934322149 (72.250 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.75716934322149 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 79.75716934322149 - 82.22439804193567 = -2.4672286987141803 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.4672286987141803 * 9.5699/82.22439804193567 = -0.287154816405987 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -0.287154816405987 = 9.282745183594013 MtCO2eq
- tar_emi_exclLU = 9.282745183594013 MtCO2eq
- tar_emi_inclLU = 79.75716934322149 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 53.34181563783814 (48.321 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.34181563783814 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 53.34181563783814 - 64.26716795603694 = -10.925352318198804 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -10.925352318198804 * 8.4624/64.26716795603694 = -1.4385992785736381 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -1.4385992785736381 = 7.023800721426363 MtCO2eq
- tar_emi_exclLU = 7.023800721426363 MtCO2eq
- tar_emi_inclLU = 53.34181563783814 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 65.77951843354855 (59.588 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.77951843354855 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 65.77951843354855 - 82.22439804193567 = -16.444879608387126 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -16.444879608387126 * 9.5699/82.22439804193567 = -1.9139799999999991 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -1.9139799999999991 = 7.655920000000002 MtCO2eq
- tar_emi_exclLU = 7.655920000000002 MtCO2eq
- tar_emi_inclLU = 65.77951843354855 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -1.2849459531558451 (-1.164 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 64.26716795603694 + -1.2849459531558451 = 62.982222002881095 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 62.982222002881095 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 62.982222002881095 - 64.26716795603694 = -1.284945953155848 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -1.284945953155848 * 8.4624/64.26716795603694 = -0.1691956714418225 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -0.1691956714418225 = 8.293204328558177 MtCO2eq
- tar_emi_exclLU = 8.293204328558177 MtCO2eq
- tar_emi_inclLU = 62.982222002881095 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.4672286987141874 (-2.235 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 82.22439804193567 + -2.4672286987141874 = 79.75716934322148 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.75716934322148 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 79.75716934322148 - 82.22439804193567 = -2.4672286987141945 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.4672286987141945 * 9.5699/82.22439804193567 = -0.28715481640598867 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -0.28715481640598867 = 9.282745183594011 MtCO2eq
- tar_emi_exclLU = 9.282745183594011 MtCO2eq
- tar_emi_inclLU = 79.75716934322148 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -10.925352318198797 (-9.897 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 64.26716795603694 + -10.925352318198797 = 53.341815637838145 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.341815637838145 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 53.341815637838145 - 64.26716795603694 = -10.925352318198797 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -10.925352318198797 * 8.4624/64.26716795603694 = -1.438599278573637 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -1.438599278573637 = 7.023800721426364 MtCO2eq
- tar_emi_exclLU = 7.023800721426364 MtCO2eq
- tar_emi_inclLU = 53.341815637838145 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -16.444879608387136 (-14.897 MtCO2eq_SAR, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 82.22439804193567 + -16.444879608387136 = 65.77951843354853 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 65.77951843354853 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 65.77951843354853 - 82.22439804193567 = -16.44487960838714 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -16.44487960838714 * 9.5699/82.22439804193567 = -1.913980000000001 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -1.913980000000001 = 7.65592 MtCO2eq
- tar_emi_exclLU = 7.65592 MtCO2eq
- tar_emi_inclLU = 65.77951843354853 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -2.0 (-2%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.0 / 100. = 0.98
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 8.4624 * 0.7612244601193747 = 6.441785871314197 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 8.4624 * (1 - 0.7612244601193747) = 2.0206141286858035 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 6.441785871314197 + 2.0206141286858035 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.98 * (6.441785871314197 + 55.80476795603694) + 2.0206141286858035 = 63.02223687948991 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 63.02223687948991 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([8.4624, 55.80476795603694]) = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 63.02223687948991 - 64.26716795603694 = -1.244931076547033 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -1.244931076547033 * 8.4624/64.26716795603694 = -0.16392669970113402 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -0.16392669970113402 = 8.298473300298866 MtCO2eq
- tar_emi_exclLU = 8.298473300298866 MtCO2eq
- tar_emi_inclLU = 63.02223687948991 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -3.0 (-3%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -3.0 / 100. = 0.97
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 9.5699 * 0.7675568463623149 = 7.345442264002718 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 9.5699 * (1 - 0.7675568463623149) = 2.224457735997283 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 7.345442264002718 + 2.224457735997283 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.97 * (7.345442264002718 + 72.65449804193567) + 2.224457735997283 = 79.8243998327575 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 79.8243998327575 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([9.5699, 72.65449804193567]) = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 79.8243998327575 - 82.22439804193567 = -2.3999982091781646 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -2.3999982091781646 * 9.5699/82.22439804193567 = -0.2793300213678698 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -0.2793300213678698 = 9.290569978632131 MtCO2eq
- tar_emi_exclLU = 9.290569978632131 MtCO2eq
- tar_emi_inclLU = 79.8243998327575 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -17.0 (-17%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 64.26716795603694 MtCO2eq, 64.26716795603694 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -17.0 / 100. = 0.83
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_refyr = 55.80476795603694 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 64.26716795603694 - 8.4624 = 55.80476795603694 MtCO2eq
    - bl_onlyLU_taryr = 55.80476795603694 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 8.4624 * 0.7612244601193747 = 6.441785871314197 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 8.4624 * (1 - 0.7612244601193747) = 2.0206141286858035 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 6.441785871314197 + 2.0206141286858035 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.83 * (6.441785871314197 + 55.80476795603694) + 2.0206141286858035 = 53.68525380538725 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 53.68525380538725 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 64.26716795603694 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([8.4624, 55.80476795603694]) = 64.26716795603694 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 8.4624 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 53.68525380538725 - 64.26716795603694 = -10.581914150649695 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -10.581914150649695 * 8.4624/64.26716795603694 = -1.393376947459628 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 8.4624 + -1.393376947459628 = 7.0690230525403726 MtCO2eq
- tar_emi_exclLU = 7.0690230525403726 MtCO2eq
- tar_emi_inclLU = 53.68525380538725 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -20.0 (-20%, from NDC)
- lulucf_first_try: False
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 82.22439804193567 MtCO2eq, 82.22439804193567 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -20.0 / 100. = 0.8
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_refyr = 72.65449804193567 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 82.22439804193567 - 9.5699 = 72.65449804193567 MtCO2eq
    - bl_onlyLU_taryr = 72.65449804193567 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 9.5699 * 0.7675568463623149 = 7.345442264002718 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 9.5699 * (1 - 0.7675568463623149) = 2.224457735997283 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 7.345442264002718 + 2.224457735997283 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8 * (7.345442264002718 + 72.65449804193567) + 2.224457735997283 = 66.22440998074799 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 66.22440998074799 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- It is lulucf second try. Get the ABU_inclLU and split it into the onlyLU and exclLU parts (depending on the onlyLU and exclLU contributions in the target year).
  - bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 82.22439804193567 MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_inclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_inclLU_taryr is the sum over external_bl_exclLU_taryr and bl_onlyLU_taryr.
    - bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([9.5699, 72.65449804193567]) = 82.22439804193567 MtCO2eq
  - bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - (tar_type_used in ['RBY', 'RBU', 'REI'] or np.isnan(bl_exclLU_taryr)):
    - calculating tar_exclLU from tar_inclLU: the bl_exclLU_taryr is the external_bl_exclLU_taryr.
    - bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 9.5699 MtCO2eq
  - ABU_inclLU = tar_emi_inclLU - bl_inclLU_taryr = 66.22440998074799 - 82.22439804193567 = -15.999988061187679 MtCO2eq
  - ABU_exclLU = ABU_inclLU * bl_exclLU_taryr/bl_inclLU_taryr = -15.999988061187679 * 9.5699/82.22439804193567 = -1.862200142452455 MtCO2eq
  - tar_emi_exclLU = bl_exclLU_taryr + ABU_exclLU = 9.5699 + -1.862200142452455 = 7.707699857547546 MtCO2eq
- tar_emi_exclLU = 7.707699857547546 MtCO2eq
- tar_emi_inclLU = 66.22440998074799 MtCO2eq
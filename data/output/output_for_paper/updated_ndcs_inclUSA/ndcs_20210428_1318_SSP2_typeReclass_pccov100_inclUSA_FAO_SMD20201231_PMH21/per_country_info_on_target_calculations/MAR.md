## ['Morocco']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | no | no | no | no |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -23.09312509174689 (-22.6 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -26.567312052452177 (-26.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 134.6788 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 134.6788 + -23.09312509174689 = 111.58567490825311 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -26.567312052452177 = 119.24635832773721 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 111.58567490825311 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 119.24635832773721 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 111.58567490825311 MtCO2eq
- tar_emi_inclLU = 119.24635832773721 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -25.545492358127092 (-25.0 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -30.04149901315746 (-29.4 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 151.7949 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 151.7949 + -25.545492358127092 = 126.24940764187292 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -30.04149901315746 = 144.48530477756685 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 126.24940764187292 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 144.48530477756685 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 126.24940764187292 MtCO2eq
- tar_emi_inclLU = 144.48530477756685 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.879704275196254 (-44.9 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -52.21498638001178 (-51.1 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 134.6788 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 134.6788 + -45.879704275196254 = 88.79909572480375 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -52.21498638001178 = 93.59868400017761 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 88.79909572480375 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 93.59868400017761 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 88.79909572480375 MtCO2eq
- tar_emi_inclLU = 93.59868400017761 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -64.5790046813453 (-63.2 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -73.46883602197352 (-71.9 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 151.7949 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 151.7949 + -64.5790046813453 = 87.21589531865472 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -73.46883602197352 = 101.05796776875079 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 87.21589531865472 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 101.05796776875079 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 87.21589531865472 MtCO2eq
- tar_emi_inclLU = 101.05796776875079 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 102.07978746307586 (99.9 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 119.24635832773727 (116.7 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 102.07978746307586 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 119.24635832773727 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 102.07978746307586 MtCO2eq
- tar_emi_inclLU = 119.24635832773727 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 126.39909618801285 (123.7 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 144.48530477756682 (141.4 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 126.39909618801285 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 144.48530477756682 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 126.39909618801285 MtCO2eq
- tar_emi_inclLU = 144.48530477756682 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 58.14154060709726 (56.9 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 93.59868400017766 (91.6 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 58.14154060709726 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 93.59868400017766 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 58.14154060709726 MtCO2eq
- tar_emi_inclLU = 93.59868400017766 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 51.090984716254184 (50.0 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 101.05796776875079 (98.9 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 51.090984716254184 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 101.05796776875079 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 51.090984716254184 MtCO2eq
- tar_emi_inclLU = 101.05796776875079 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -15.8 (-15.8%, from NDC)
- ndc_value_inclLU: -18.2 (-18.2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -15.8 / 100. = 0.842
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -18.2 / 100. = 0.8180000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 134.6788 * 1.0 = 134.6788 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 134.6788 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.842 * 134.6788 + 0.0 = 113.39954959999999 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8180000000000001 * (134.6788 + 11.134870380189398) + 0.0 = 119.27558237099493 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 113.39954959999999 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 119.27558237099493 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 113.39954959999999 MtCO2eq
- tar_emi_inclLU = 119.27558237099493 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -14.6 (-14.6%, from NDC)
- ndc_value_inclLU: -17.2 (-17.2%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -14.6 / 100. = 0.854
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -17.2 / 100. = 0.8280000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 151.7949 * 1.0 = 151.7949 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 151.7949 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.854 * 151.7949 + 0.0 = 129.6328446 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8280000000000001 * (151.7949 + 22.73190379072429) + 0.0 = 144.50819353871972 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 129.6328446 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 144.50819353871972 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 129.6328446 MtCO2eq
- tar_emi_inclLU = 144.50819353871972 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -31.5 (-31.5%, from NDC)
- ndc_value_inclLU: -35.8 (-35.8%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 145.8136703801894 MtCO2eq, 145.8136703801894 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -31.5 / 100. = 0.685
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.8 / 100. = 0.642
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_refyr = 11.134870380189398 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 134.6788 = 11.134870380189398 MtCO2eq
    - bl_onlyLU_taryr = 11.134870380189398 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 134.6788 * 1.0 = 134.6788 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 134.6788 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.685 * 134.6788 + 0.0 = 92.25497800000001 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.642 * (134.6788 + 11.134870380189398) + 0.0 = 93.61237638408159 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 92.25497800000001 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 93.61237638408159 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 92.25497800000001 MtCO2eq
- tar_emi_inclLU = 93.61237638408159 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -37.0 (-37.0%, from NDC)
- ndc_value_inclLU: -42.1 (-42.1%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -37.0 / 100. = 0.63
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -42.1 / 100. = 0.579
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 151.7949 * 1.0 = 151.7949 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 151.7949 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.63 * 151.7949 + 0.0 = 95.63078700000001 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.579 * (151.7949 + 22.73190379072429) + 0.0 = 101.05101939482937 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 95.63078700000001 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 101.05101939482937 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 95.63078700000001 MtCO2eq
- tar_emi_inclLU = 101.05101939482937 MtCO2eq



## Target type used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 3.0654590829752513 (3 tCO2eq_SAR/capita, from NDC)
- ndc_value_inclLU: 2.656731205245218 (2.6 tCO2eq_SAR/capita, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 174.5268037907243 MtCO2eq, 174.5268037907243 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_refyr = 22.73190379072429 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 151.7949 = 22.73190379072429 MtCO2eq
    - bl_onlyLU_taryr = 22.73190379072429 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 38742105.2255 Pers
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 3.0654590829752513 * 1e-6 * 38742105.2255 = 118.76233835709192 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.656731205245218 * 1e-6 * 38742105.2255 = 102.92735990947966 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 118.76233835709192 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 102.92735990947966 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 118.76233835709192 MtCO2eq
- tar_emi_inclLU = 102.92735990947966 MtCO2eq
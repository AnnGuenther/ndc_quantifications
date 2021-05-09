## ['Armenia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | nan | nan |
| Used | yes | yes | yes | yes | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | nan | yes | nan | yes |
| Used | yes | yes | no | yes | no | yes |



## Target type used: AEI, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 5.691860255808942 (5.4 tCO2eq_SAR/capita, from NDC)
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
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_refyr = -0.10647761428571427 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_taryr = -0.10647761428571427 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2810023.7323 Pers
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2810023.7323 = 15.994262399758275 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 15.994262399758275 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([15.994262399758275, - -0.10647761428571427]) = 16.10074001404399 MtCO2eq.
- tar_emi_exclLU = 16.10074001404399 MtCO2eq
- tar_emi_inclLU = 15.994262399758275 MtCO2eq



## Target type used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 5.691860255808942 (5.4 tCO2eq_SAR/capita, from NDC)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_refyr = -0.10647761428571427 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_taryr = -0.10647761428571427 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2730207.7531 Pers
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2730207.7531 = 15.539960999971322 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 15.539960999971322 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([15.539960999971322, - -0.10647761428571427]) = 15.646438614257036 MtCO2eq.
- tar_emi_exclLU = 15.646438614257036 MtCO2eq
- tar_emi_inclLU = 15.539960999971322 MtCO2eq



## Target type used: AEI, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 2.181879764726761 (2.07 tCO2eq_SAR/capita, from NDC)
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
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_refyr = -0.10647761428571427 MtCO2eq
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.10647761428571427 MtCO2eq).
    - bl_onlyLU_taryr = -0.10647761428571427 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2302547.3231 Pers
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.181879764726761 * 1e-6 * 2302547.3231 = 5.023881411597661 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 5.023881411597661 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([5.023881411597661, - -0.10647761428571427]) = 5.130359025883376 MtCO2eq.
- tar_emi_exclLU = 5.130359025883376 MtCO2eq
- tar_emi_inclLU = 5.023881411597661 MtCO2eq
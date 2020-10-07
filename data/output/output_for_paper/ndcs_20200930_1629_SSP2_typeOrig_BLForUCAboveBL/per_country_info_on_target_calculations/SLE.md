

## tar_type_used: ABS, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: 7.58 (7.58 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (7.3231528571428575).
    - bl_onlyLU_refyr = 7.3231528571428575
    - emi_onlyLU 2035: external_emi_onlyLU used (7.3231528571428575).
    - bl_onlyLU_taryr = 7.3231528571428575
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 7.58
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([7.58, 7.3231528571428575]) = 14.903152857142857
- tar_emi_exclLU = 7.58
- tar_emi_inclLU = 14.903152857142857
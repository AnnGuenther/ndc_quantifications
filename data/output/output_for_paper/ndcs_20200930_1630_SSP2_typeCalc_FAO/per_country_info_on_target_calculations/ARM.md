

## tar_type_used: AEI, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 5.691860255808942 (5.4 tCO2eq_SAR/capita)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_refyr = -0.10647761428571427
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_taryr = -0.10647761428571427
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2843105.2404
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2843105.2404 = 16.182557720914886
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 16.182557720914886
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([16.182557720914886, - -0.10647761428571427]) = 16.2890353352006.
- tar_emi_exclLU = 16.2890353352006
- tar_emi_inclLU = 16.182557720914886

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 5.691860255808942 (5.4 tCO2eq_SAR/capita)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_refyr = -0.10647761428571427
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_taryr = -0.10647761428571427
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2788180.7597
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2788180.7597 = 15.869935252147611
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 15.869935252147611
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([15.869935252147611, - -0.10647761428571427]) = 15.976412866433325.
- tar_emi_exclLU = 15.976412866433325
- tar_emi_inclLU = 15.869935252147611

## tar_type_used: AEI, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 2.181879764726761 (2.07 tCO2eq_SAR/capita)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_refyr = -0.10647761428571427
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.10647761428571427).
    - bl_onlyLU_taryr = -0.10647761428571427
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2474753.4555
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.181879764726761 * 1e-6 * 2474753.4555 = 5.3996144872430785
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 5.3996144872430785
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([5.3996144872430785, - -0.10647761428571427]) = 5.506092101528793.
- tar_emi_exclLU = 5.506092101528793
- tar_emi_inclLU = 5.3996144872430785
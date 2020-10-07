

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
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2926355.2785
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2926355.2785 = 16.65640530407086
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 16.65640530407086
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([16.65640530407086, - -0.10647761428571427]) = 16.762882918356574.
- tar_emi_exclLU = 16.762882918356574
- tar_emi_inclLU = 16.65640530407086

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
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2926816.9733
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 5.691860255808942 * 1e-6 * 2926816.9733 = 16.659033206353293
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 16.659033206353293
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([16.659033206353293, - -0.10647761428571427]) = 16.765510820639008.
- tar_emi_exclLU = 16.765510820639008
- tar_emi_inclLU = 16.659033206353293

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
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2862602.3676
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.181879764726761 * 1e-6 * 2862602.3676 = 6.245854180325356
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 6.245854180325356
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([6.245854180325356, - -0.10647761428571427]) = 6.352331794611071.
- tar_emi_exclLU = 6.352331794611071
- tar_emi_inclLU = 6.245854180325356
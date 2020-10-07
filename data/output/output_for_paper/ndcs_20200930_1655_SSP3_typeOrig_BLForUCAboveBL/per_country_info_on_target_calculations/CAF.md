

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 20.0 (20 tCO2eq/cap)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 5752713.3165
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 20.0 * 1e-6 * 5752713.3165 = 115.05426632999999
- tar_emi_exclLU = ndc_value_exclLU = 115.05426632999999
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([115.05426632999999, -199.4851]) = -84.43083367
- tar_emi_exclLU = 115.05426632999999
- tar_emi_inclLU = -84.43083367

## tar_type_used: AEI, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: 12.0 (12 tCO2eq/cap)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 7349553.4809
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 12.0 * 1e-6 * 7349553.4809 = 88.1946417708
- tar_emi_exclLU = ndc_value_exclLU = 88.1946417708
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([88.1946417708, -180.6845]) = -92.48985822920001
- tar_emi_exclLU = 88.1946417708
- tar_emi_inclLU = -92.48985822920001

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -1.191 (-1.1910 MtCO2eq)
- ndc_value_inclLU: -4.062 (-4.062 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 32.1905
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 32.1905 + -1.191 = 30.9995 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -167.2946
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -167.2946 + -4.062 = -171.35660000000001
- tar_emi_exclLU = ndc_value_exclLU = 30.9995
- tar_emi_inclLU = ndc_value_inclLU = -171.35660000000001
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 30.9995
- tar_emi_inclLU = -171.35660000000001

## tar_type_used: ABU, refyr: 2050, taryr: 2050, unconditional_best
- ndc_value_exclLU: -3.2895 (-3.2895 MtCO2eq)
- ndc_value_inclLU: -10.41 (-10.410 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 59.8099
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 59.8099 + -3.2895 = 56.5204 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -120.8746
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -120.8746 + -10.41 = -131.2846
- tar_emi_exclLU = ndc_value_exclLU = 56.5204
- tar_emi_inclLU = ndc_value_inclLU = -131.2846
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 56.5204
- tar_emi_inclLU = -131.2846

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -1.6095 (-1.6095 MtCO2eq)
- ndc_value_inclLU: -5.4983 (-5.4983 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 32.1905
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 32.1905 + -1.6095 = 30.581 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -167.2946
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -167.2946 + -5.4983 = -172.7929
- tar_emi_exclLU = ndc_value_exclLU = 30.581
- tar_emi_inclLU = ndc_value_inclLU = -172.7929
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 30.581
- tar_emi_inclLU = -172.7929

## tar_type_used: ABU, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: -14.9525 (-14.9525 MtCO2eq)
- ndc_value_inclLU: -47.32 (-47.320 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 59.8099
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 59.8099 + -14.9525 = 44.8574 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -120.8746
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -120.8746 + -47.32 = -168.1946
- tar_emi_exclLU = ndc_value_exclLU = 44.8574
- tar_emi_inclLU = ndc_value_inclLU = -168.1946
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 44.8574
- tar_emi_inclLU = -168.1946

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 30.9995 (30.9995 MtCO2eq)
- ndc_value_inclLU: -171.3566 (-171.3566 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 30.9995
- tar_emi_inclLU = ndc_value_inclLU = -171.3566
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 30.9995
- tar_emi_inclLU = -171.3566

## tar_type_used: ABS, refyr: 2050, taryr: 2050, unconditional_best
- ndc_value_exclLU: 56.5204 (56.5204 MtCO2eq)
- ndc_value_inclLU: -131.2846 (-131.2846 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 56.5204
- tar_emi_inclLU = ndc_value_inclLU = -131.2846
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 56.5204
- tar_emi_inclLU = -131.2846

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 30.581 (30.5810 MtCO2eq)
- ndc_value_inclLU: -172.7946 (-172.7946 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 30.581
- tar_emi_inclLU = ndc_value_inclLU = -172.7946
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 30.581
- tar_emi_inclLU = -172.7946

## tar_type_used: ABS, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: 44.8574 (44.8574 MtCO2eq)
- ndc_value_inclLU: -168.1946 (-168.1946 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 44.8574
- tar_emi_inclLU = ndc_value_inclLU = -168.1946
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 44.8574
- tar_emi_inclLU = -168.1946

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -3.7 (-3.7%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -3.7 / 100. = 0.963
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 10.7089 * 1.0 = 10.7089
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 10.7089 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 10.7089 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.963 * 10.7089 + -199.4851 + 0.0 = -189.17242929999998
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = -189.17242929999998
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-189.17242929999998, - -199.4851]) = 10.312670700000012.
- tar_emi_exclLU = 10.312670700000012
- tar_emi_inclLU = -189.17242929999998

## tar_type_used: RBU, refyr: 2050, taryr: 2050, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -5.5 (-5.5%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -5.5 / 100. = 0.945
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 14.9592 * 0.999993315 = 14.959099997748
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 14.9592 * (1 - 0.999993315) = 0.00010000225200009378
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 14.959099997748 + 0.00010000225200009378 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.945 * 14.959099997748 + -180.6845 + 0.00010000225200009378 = -166.54805049987615
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = -166.54805049987615
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-166.54805049987615, - -180.6845]) = 14.13644950012386.
- tar_emi_exclLU = 14.13644950012386
- tar_emi_inclLU = -166.54805049987615

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -5.0 (-5%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-167.2946 -167.2946]
  - ndcs_emi_exclLU for refyr and taryr: [32.1905 32.1905]
  - ndcs_emi_onlyLU for refyr and taryr: [-199.4851 -199.4851]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -5.0 / 100. = 0.95
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_refyr = -199.4851
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-199.4851).
    - bl_onlyLU_taryr = -199.4851
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 10.7089 * 1.0 = 10.7089
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 10.7089 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 10.7089 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.95 * 10.7089 + -199.4851 + 0.0 = -189.311645
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = -189.311645
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-189.311645, - -199.4851]) = 10.17345499999999.
- tar_emi_exclLU = 10.17345499999999
- tar_emi_inclLU = -189.311645

## tar_type_used: RBU, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -25.0 (-25%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-120.8746 -120.8746]
  - ndcs_emi_exclLU for refyr and taryr: [59.8099 59.8099]
  - ndcs_emi_onlyLU for refyr and taryr: [-180.6845 -180.6845]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -25.0 / 100. = 0.75
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_refyr = -180.6845
    - emi_onlyLU 2050: ndcs_emi_onlyLU used (-180.6845).
    - bl_onlyLU_taryr = -180.6845
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 14.9592 * 0.999993315 = 14.959099997748
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 14.9592 * (1 - 0.999993315) = 0.00010000225200009378
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 14.959099997748 + 0.00010000225200009378 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.75 * 14.959099997748 + -180.6845 + 0.00010000225200009378 = -169.465074999437
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = -169.465074999437
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-169.465074999437, - -180.6845]) = 11.219425000563007.
- tar_emi_exclLU = 11.219425000563007
- tar_emi_inclLU = -169.465074999437


## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -6.058565502338564 (-5.76 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.41147336802911
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.41147336802911 + -6.058565502338564 = 34.35290786569054 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 34.35290786569054
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([34.35290786569054, 0.01987334285714286]) = 34.372781208547686
- tar_emi_exclLU = 34.35290786569054
- tar_emi_inclLU = 34.372781208547686

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -10.6340446577505 (-10.11 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.41147336802911
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.41147336802911 + -10.6340446577505 = 29.777428710278606 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 29.777428710278606
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([29.777428710278606, 0.01987334285714286]) = 29.79730205313575
- tar_emi_exclLU = 29.777428710278606
- tar_emi_inclLU = 29.79730205313575

## tar_type_used: REI, refyr: 1990, taryr: 2030, unconditional_best
- ndc_value_exclLU: -34.0 (-34%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [50.46175    40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -34.0 / 100. = 0.6599999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.0188921).
    - bl_onlyLU_refyr = 0.0188921
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 46.5928 * 1.0 = 46.5928
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.41147336802911 * (1 - 1.0) = 0.0
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 81345766175.7403 / 55324222656.25 = 1.4703463016764255
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.4703463016764255 * 0.6599999999999999 * 46.5928 + 0.0 = 45.21498376873457
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.4703463016764255 * nan * (46.5928 + 0.0188921) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 45.21498376873457
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([45.21498376873457, 0.01987334285714286]) = 45.234857111591715
- tar_emi_exclLU = 45.21498376873457
- tar_emi_inclLU = 45.234857111591715

## tar_type_used: REI, refyr: 1990, taryr: 2030, conditional_best
- ndc_value_exclLU: -43.0 (-43%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [50.46175    40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -43.0 / 100. = 0.5700000000000001
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.0188921).
    - bl_onlyLU_refyr = 0.0188921
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 46.5928 * 1.0 = 46.5928
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.41147336802911 * (1 - 1.0) = 0.0
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 81345766175.7403 / 55324222656.25 = 1.4703463016764255
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.4703463016764255 * 0.5700000000000001 * 46.5928 + 0.0 = 39.04930416390714
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.4703463016764255 * nan * (46.5928 + 0.0188921) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 39.04930416390714
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([39.04930416390714, 0.01987334285714286]) = 39.069177506764284
- tar_emi_exclLU = 39.04930416390714
- tar_emi_inclLU = 39.069177506764284

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 34.35290786569054 (32.66 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 34.35290786569054
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([34.35290786569054, 0.01987334285714286]) = 34.372781208547686
- tar_emi_exclLU = 34.35290786569054
- tar_emi_inclLU = 34.372781208547686

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 29.777428710278603 (28.31 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 29.777428710278603
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([29.777428710278603, 0.01987334285714286]) = 29.797302053135745
- tar_emi_exclLU = 29.777428710278603
- tar_emi_inclLU = 29.797302053135745

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -15.0 (-15%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -15.0 / 100. = 0.85
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.41147336802911 * 1.0 = 40.41147336802911
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.41147336802911 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.85 * 40.41147336802911 + 0.0 = 34.34975236282474
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (40.41147336802911 + 0.01987334285714286) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 34.34975236282474
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([34.34975236282474, 0.01987334285714286]) = 34.369625705681884
- tar_emi_exclLU = 34.34975236282474
- tar_emi_inclLU = 34.369625705681884

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -25.0 (-25%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.41147337 40.41147337]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -25.0 / 100. = 0.75
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_refyr = 0.01987334285714286
    - emi_onlyLU 2030: external_emi_onlyLU used (0.01987334285714286).
    - bl_onlyLU_taryr = 0.01987334285714286
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.41147336802911 * 1.0 = 40.41147336802911
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.41147336802911 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.75 * 40.41147336802911 + 0.0 = 30.30860502602183
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (40.41147336802911 + 0.01987334285714286) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 30.30860502602183
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([30.30860502602183, 0.01987334285714286]) = 30.328478368878972
- tar_emi_exclLU = 30.30860502602183
- tar_emi_inclLU = 30.328478368878972
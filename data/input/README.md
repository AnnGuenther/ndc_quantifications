### infos_from_ndcs_default.xlsx

Information retrieved from within NDCs. Most of the table entries are self-explanatory and not mentioned here.

- Light green background: done.
- White background: to do.
- Blue background: (maybe) more information available.

#### type_calc and type_orig

- Possible types: 
  - **ABS**:
        Absolute target emissions.
        E.g., target is to reduce emissions in 2030 to 500 MtCO2eq.
  - **RBY**: 
        Relative reduction compared to base year.
        E.g., 20% emissions reduction compared to 2010 emissions in 2030.
  - **RBU**: 
        Relative reduction compared to BAU. 
        E.g., 20% emissions reduction compared to business-as-usual (BAU) emissions in 2030.
  - **ABU**: 
        Absolute reduction compared to BAU.
        E.g., 350 MtCO2eq reduction compared to BAU emissions in 2030.
  - **REI**:
        Relative emissions intensity reduction.
        Compared to base year. E.g., 20% emissions intensity reduction compared to 2010 emissions intensity in 2030.
        Or compared to BAU. This is basically a simple RRB target, but some NDCs state it as intensity targets.
  - **AEI**: 
        Absolute emissions intensity. 
        E.g., 2.1 tCO2eq/cap in 2030.
  - **NGT**: 
        Non-GHG targets. 
        Nothing is calculated, baseline emissions are assumed.

- type_orig is the 'original' target type of the NDC, e.g., a reduction of 20% compared to BAU is a RBU target.
- type_calc is a reclassification based on the data provided within the NDC. If type_orig is RBU, but in the NDC the quantification is provided, or enough data to do the quantification based on the given emissions, then we reclassify the target to type_calc = ABS.

#### Coverage (sectors)

- coverage_sectors_ndcs: coverage as stated in the NDC (sometimes +/- clearly stated; YES, NO, or NAN).
- coverage_sectors_calc: adapted coverage (only YES or NO)
  - e.g., if they say economy-wide we cover all sectors excl. LULUCF, even if they do not state all sectors in their 'covered sectors' section;
  - if any F-gas is covered, IPPU is generally assumed to be covered, as F-gases are only relevant in that sector;
  - if all sectors (exclLU) are covered, 'Other' is assumed to be covered.
- Format: {"YES": ["Energy", "IPPU"], "NO": ["LULUCF"], "NAN": ["Agriculture", "Waste"]}.

#### Economy-wide

- economy_wide: Yes, No, NaN.
- economy_wide_comment: Where to find the information, what is written in the NDC.

#### land_sector

Information on the Land Use, Land-Use Change and Forestry sector.

#### Coverage (gases)

- coverage_gases_ndcs: coverage as stated in the NDC (sometimes +/- clearly stated; YES, NO, or NAN).
- coverage_gases_calc: adapted coverage (only YES or NO)
  - 

**Row 'BaseYear'**: can only be integer or NaN or empty, do not put in anything else (not, e.g.: 2005 [p. 3])


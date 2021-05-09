# NDCmitiQ: a tool to quantify and analyse GHG mitigation targets

**Recommended citation**

This paper citation will be updated once the manuscript is published.
The discussion paper is available as "Günther, A., Gütschow, J., and Jeffery, M. L.: NDCmitiQ v1.0.0: a tool to quantify and analyse GHG mitigation targets, Geosci. Model Dev. Discuss. [preprint],  https://doi.org/10.5194/gmd-2020-392, in review, 2021."

**Content**

- Use of the software and output data, and support
- Abstract
- Notes
- Target types
- Share of emissions covered by an NDC
- Quantification options, output files, and data format description
- Data sources
- Changelog

**Use of the software and output data, and support**

Before using the software NDCmitiQ, please read this document and the article describing the methodology. The article will be referenced here as soon as it is published.

Please notify us ([annika.guenther@pik-potsdam.de](mailto:annika.guenther@pik-potsdam.de)) if you use the software or output data so that we can keep track of how it is used and take the information into consideration when updating and improving the software.

When using the software or output data (or one of its updates), please cite the DOI of the precise version. Please consider also citing the relevant original data sources when using the output data (see data sources section).

If you encounter possible errors or other things that should be noted or need support in using the software or output data or have any other questions regarding NDCmitiQ, please contact [annika.guenther@pik-potsdam.de](mailto:annika.guenther@pik-potsdam.de), or open an issue in the corresponding [GitHub-repository](https://github.com/AnnGuenther/ndc_quantifications).

**Abstract**

This software can be used to quantify emissions mitigation targets stated in the Nationally Determined Contributions (NDCs). The output includes national targets and emissions pathways and globally aggregated mitigated emissions pathways. Several quantification options are available, including, i.a., the five marker scenarios of the Shared Socioeconomic Pathways (SSPs) as baseline trajectories.

**Notes**

For details on how to run NDCmitiQ, please refer to the `README.md`-file in the main directory. Additional information is provided in the files `requirements.txt`, and `/docs/build/html/index.html`.

Please note that for members of the EU NDC, the single quantifications are based on assumed equal contributions by member states, and can therefore only be used as aggregated EU-wide emissions.

**Target types**

The following target types are distinguished in NDCmitiQ:

- **ABS**: **ABS**olute target emissions
- **RBY**: **R**elative reduction compared to **B**ase **Y**ear
- **ABU**: **A**bsolute reduction compared to **B**usiness-as-**U**sual
- **RBU**: **R**elative reduction compared to **B**usiness-as-**U**sual
- **AEI**: **A**bsolute **E**missions **I**ntensity target
- **REI**: **R**elative reduction in **E**missions **I**ntensity compared to a base year or target year
- **NGT**: **N**on-**G**HG **T**arget (assuming baseline emissions)

**Share of emissions covered by an NDC**

We assessed the covered sectors and gases and derived estimates of the share of national emissions covered by an NDC. The data is stored in csv-files in the folder `/data/preprocess/pc_cov_yyyymmdd_hhmm/` (calculation: `/py_files/preprocessing_current_pc_cov.py`).

**Quantification options, output files, and data format description**

NDCmitiQ contains several quantification options (i.a., regarding the input time series, or the prioritised target type). More details are available in `/py_files/MODIFY_INPUT_HERE/input_DEFAULT_with_EXPLANATIONS.py`. Here, the output is included for runs with different options (see `/data/output/output_for_paper/`, about 1min20s per run), with one folder per run. The folder name structure begins with `ndcs_yyyymmdd_hhss_`, followed by, e.g.:

- **SSP1 to SSP5**: which SSP marker scenario is chosen for the run. This information is also important if the run is based on NDC emissions data (type_reclass), as not for all countries emissions data were provided, and the SSP baselines are used for the pathway construction.
- **typeMain**: runs with type_main (main target type stated in the NDC), based on external emissions data (PRIMAP-hist v2.1 HISTCR and down-scaled SSP marker scenarios).
- **typeReclass**: runs with type_reclass (reclassified target type, e.g., if the country has a base year target, but provides a quantification of the target emissions it can be reclassified as an absolute target), based on emissions data from the NDCs where possible.
- **pccov100**: runs with an assumed coverage of 100%. Without pccov100: coverage based on estimated %cov (calculated from covered sectors and gases stated in the NDC and emissions data per sector and gas).
- **constEmiAfterLastTar**: runs with assumed constant emissions after a Party’s last target year. Without constEmiAfterLastTar: instead of the emissions, the relative difference to the baseline is kept constant after the last target year.
- **constDiffAfterLastTar**: runs with assumed constant absolute difference to baseline emissions after a Party's last target year. Without constDiffAfterLastTar: instead of the emissions, the relative difference to the baseline is kept constant after the last target year.
- **BLForUCAboveBL**: runs using the baseline emissions as the unconditional pathways for Parties without unconditional targets, even if the baseline is better than the conditional targets. Without BLForUCAboveBL: conditional worst pathway is used in this case instead of the baseline.
- **BLForTarAboveBL**: runs using the baseline emissions if the mitigated pathway lies above baseline in 2030. Without BLForTarAboveBL: calculated mitigated pathway is used instead of baseline.
- **UNFCCC / FAO**: runs using LULUCF (Land Use, Land-Use Change and Forestry) data with UNFCCC or FAO chosen as the primary prioritised data source (UNFCCC, CRF, BUR, FAO or FAO, CRF, BUR, UNCFFF). Without UNFCCC / FAO: prioritisation is CRF, BUR, UNFCCC, and FAO.
- **CAT**: runs using CAT quantifications (Copyright © 2020 Climate Action Tracker by Climate Analytics and NewClimate Institute with all rights reserved) for all countries with data available. Without CAT: using NDCmitiQ quantifications.

Per run, the single per-country targets can be found in `ndc_targets.csv`, the country-pathways are available in `ndc_targets_pathways_per_country_used_for_group_pathways.csv`, and the aggregated pathways are stored in `ndc_targets_pathways_per_group.csv`. Additionally, each of the folders contains the file `log_file.md` (information on the setup for the model run), and the sub-folder `/per_country_info_on_target_calculations/` that provides per-country information on how exactly the national targets were quantified. The input that can easily be modified is: time series of emissions (exclLU and onlyLU), %cov (exclLU), population, and GDP, and information from the NDCs (exclLU: emissions excluding contributions from LULUCF, onlyLU: LULUCF emissions, GDP: Gross Domestic Product).

**Data sources**

The following data sources are used in the NDCmitiQ:

- Downscaled RCP scenarios [data](https://zenodo.org/record/3638137#references)
- PRIMAP-hist v2.1 [data](https://dataservices.gfz-potsdam.de/pik/showshort.php?id=escidoc:4736895)
- PRIMAP-hist SocioEco v2.1 [data](https://dataservices.gfz-potsdam.de/pik/showshort.php?id=escidoc:4736895)
- PRIMAP-crf 2019 [data](https://doi.org/10.5281/zenodo.3775575)
- UNFCCC Nationaly Inventory Submissions 2019 [data](https://unfccc.int/process-and-meetings/transparency-and-reporting/reporting-and-review-under-the-convention/greenhouse-gas-inventories-annex-i-parties/national-inventory-submissions-2019)
- BUR submissions [data](https://unfccc.int/process/transparency-and-reporting/reporting-and-review-under-convention/biennial-update-reports-0)
- EDGAR version 4.3.2 [data](https://data.jrc.ec.europa.eu/collection/EDGAR), [paper](https://essd.copernicus.org/preprints/essd-2017-79/)
- FAOSTAT [data](http://www.fao.org/faostat/en//#data)
- CAT [webpage, data](https://climateactiontracker.org/)

**Changelog**

NDCmitiQ v1.0.1

- Contributions submitted up to 31st December 2020 (generally considering 2016 submission by USA).
- New quantification options:
  - constDiffAfterLastTar
  - BLForTarAboveBL
  - CAT

NDCmitiQ v1.0.0

- Current version: contributions submitted up to 17th April 2020 (generally not considering 2016 submission by USA).

Note: please do not consider the folder `/data/other/`.
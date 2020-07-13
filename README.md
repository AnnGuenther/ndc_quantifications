## Quantification of NDC GHG target emissions

NDCs: Nationally Determined Contributions.

------

- Quantification of the NDC GHG mitigation target emissions per country, and the national emissions pathways and aggregated global emissions pathways.

- Per country the un-/conditional best/worst target emissions are calculated.
- Target emissions are calculated using the NDC emissions data when available (type_calc) or one perform comparison runs with other input data (type_orig).
- Emissions are calculated in- or excluding LULUCF, depending on a Party's NDC, and the opposite case is derived from this quantified target.
- The information from the NDCs is stored in ``/data/input/infos_from_ndcs_default.xlsx``.

-------

- In the Matlab PRIMAP Emissions Module run ``ndcs_get_all_data_agu.m`` to write out all the tables needed for the quantifications from the PRIMAPDB to ``/data/preprocess/matlab_tables`` as csv-files. These tables are available in the repository, so one can skip this step.

- Open a python console and go to the folder ``py_files`` (all of the following is run using python3):
  - Run ``preprocessing_general.py`` to create the input needed for the quantifications. It is saved in ``/data/preprocess/preprocess``. The preprocessed data are available in the repo.
  - Run ``preprocessing_current_pc_cov.py``, which will store the tables with the covered part of emissions per country in ``/data/preprocess/pc_cov_yyyymmdd_hhmm``. The preprocessed data are available in the repo.
  - Put the new folder-name ``preprocess_yyyymmdd_hhmm`` into ``setup_metadata.py`` (``folder_preprocess = 'preprocess_yyyymmdd_hhmm'``).
  - Go to ``/MODIFY_INPUT_HERE`` and copy the file ``input_default.py`` and adjust it as you wish.
  - Go to ``_to_be_run.py`` and put in the input-file(s) that you wish to work with (``main_ndc_quantifications('input_default', '')``) and run ``_to_be_run.py``.
  - The output (emissions targets per country, per-country pathways, global pathways) is stored in ``/data/output/``.
- After the calculations are finished, one can estimate end of the century temperatures using the Matlab PRIMAP Emissions Module and Climate Module (``calculate_NDC_impacts_agu.m``).

----

The python code is stored in a Spyder project.
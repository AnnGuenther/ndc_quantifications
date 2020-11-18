## Quantification of NDC GHG target emissions (NDCmitiQ)

NDC: Nationally Determined Contribution.
GHG: Greenhouse Gas.

------

- Quantification of the NDC GHG mitigation target emissions per country, and the national emissions pathways and aggregated global emissions pathways.
- Per country the un-/conditional best/worst target emissions are calculated.
- Target emissions are calculated using the NDC emissions data when available (type_calc = type_reclass) or one can perform comparison runs with other input data (type_orig = type_main).
- Emissions are calculated in- or excluding LULUCF, depending on a Party's NDC, and the opposite case is derived from this quantified target.
- The information that we retrieved from within the NDCs is stored in ``/data/input/infos_from_ndcs_default.xlsx``.
- The preprocessing is based on output from the MATLAB-based PRIMAP Emissions Module. The output and preprocessed data are available in the repository. If one has access to the MATLAB PRIMAP Emissions and Climate Modules, after running NDCmitiQ, one can estimate the end-of-century warming from the constructed emissions pathways.
- We hope that in the future it will be possible for a broader community to use the entire suite of tools, not only NDCmitiQ. This needs a porting and open-sourcing of the functionalities from MATLAB to Python.

-------

If you have access to the MATLAB-based PRIMAP Emissions Module you can do the following:

- In the PRIMAP Emissions Module run ``ndcs_get_all_data_agu.m`` to write out all the tables needed for the quantifications from the PRIMAPDB to ``/data/preprocess/matlab_tables`` as csv-files. These tables are available in the repository, so one can skip this step.
- Open a python console and go to the folder ``py_files`` (all of the following is run using python3):
  - Run ``preprocessing_general.py`` to create the input needed for the quantifications. It is saved in ``/data/preprocess/preprocess``. The preprocessed data are available in the repository.
  - Run ``preprocessing_current_pc_cov.py``, which will store the tables with the covered part of emissions per country in ``/data/preprocess/pc_cov_yyyymmdd_hhmm``. The preprocessed data are available in the repository.
  - Put the new folder-name ``preprocess_yyyymmdd_hhmm`` into ``setup_metadata.py`` (```folder_preprocess = 'preprocess_yyyymmdd_hhmm'```).

--------------------

If you do not have access to the MATLAB tools, you can do the following (**running NDCmitiQ**).

- Open a python console and go to the folder ``py_files`` (all of the following is run using python3):
  - Go to ``/MODIFY_INPUT_HERE`` and copy the file ``input_default.py`` and adjust it as you wish.
  - Go to ``_to_be_run.py`` and put in the input-file(s) that you wish to work with (``main_ndc_quantifications('input_default', '')``) and run ``_to_be_run.py``.
  - The output (emissions targets per country, per-country pathways, global pathways) is stored in ``/data/output/``.

---------------

If you have access to the MATLAB-based PRIMAP Emissions and Climate Module you can do the following:

- After the calculations are finished, one can estimate end of the century temperatures using the Matlab PRIMAP Emissions Module and Climate Module (``calculate_NDC_impacts_agu.m``).

----

Further information can be found in ``/docs/build/html/index.html`` or ``/docs/build/latex/ndcmitiq.pdf`` (produced with ``/py_files/additional_scripts/make_documentation.py``).

---------

The python code is stored in a Spyder project (``/py_files/*``).

----

Information on the national emissions and targets based on emissions data provided in the NDCs is stored in ``/py_files/ndcs__target_calculations_for_input_xlsx/``, containing single .py-files per country. Here, e.g., (i) the target emissions are calculated if a country provides baseline emissions in the NDC, or (ii) the LULUCF emissions for a year are calculated if an NDC gives the emissions inclLU and exclLU, or (iii) the baseline emissions are calculated from single sectoral emissions, if the sum is not provided, and (iv) further similar calculations are performed.

-------

When modifying and adding folders and files in the repository, please consider the following:

- When adding a new folder in ``/py_files`` or its sub-folders, and if the new folder contain .py-files that should be available to the module, please add a ``__init__.py`` file (empty, or containing code such as ``from .file_name import function_name``, with the ``file_name`` being the .py-file name in which a function is stored, and ``function_name`` being the function name, defined by ``def function_name(variables)``).
- When adding a new file or folder that should only be available locally on your machine and not in the online repository, add a ``.gitingore`` file including the files / folders that should be ignored. If you add a new folder with .py-files, please add a ``.gitingore`` file containing ``/__pycache__/*`` to ignore the folder ``__pycache__`` that will be produced when running your code.
- In .py-files stored in ``/py_files/``, and the sub-folders ``/preprocessing/``, ``/main_functions/``, and ``/MODIFY_INPUT_HERE/``, please use the following code for comments that should be included in the documentation: ``"""\ncomment\n"""`` (\n denotes a new line). To check which functions are considered in the documentation go to ``/py_files/additional_scripts/make_documentation.py`` (``files = [...]``).


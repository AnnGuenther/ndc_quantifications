### Running 'old' version

First paper submission from November 2020

Run setup_metadata.py with:

```python
"""
This part can be modified.
"""

submission_until = 20200417 # For the first paper submission: 20200417, yyyymmdd

# Which version of the file infos_from_ndcs.xlsx to be used.
infos_from_ndcs_xlsx = 'infos_from_ndcs__paper_first_submission_202011.xlsx'

# Current PRIMAP-hist
current_primap = 'PMH21'
current_primap_srcs = {
'emi': 'PRIMAPHIST21', 'pop': 'PMHSOCIOECO21', 'gdp': 'PMHSOCIOECO21'}
current_primap_last_year = 2017

# pc_cov made on yyyymmdd_hhss, smd submissions up to date yyyymmdd, pmh21 PRIMAP-hist v2.1
############################################################################
# !!!!! TO BE MODIFIED AFTER RUNNING preprocessing_current_pc_cov.py !!!!! #
############################################################################
path_preprocess = 'pc_cov_20210428_0819_SMD20200417_PMH21'

# How many years should be used when calculating the mean over the last available years.
meta.average_nrvalues = 6
```

Then run preprocessing_general.py and preprocessing_current_pc_cov.py.

Update the path_preprocess in setup_metadata.py (as indicated in the console after running preprocessing_current_pc_cov.py). Preprocessed data for paper_first_submission_202011 can be found in pc_cov_20210428_0834_SMD20200417_PMH21.

Then make all the runs you want with this setup (\_to_be_run__paper_first_submission_202011.py)

### New runs

Run setup_metadata.py with:

Then run preprocessing_current_pc_cov.py (no changes in the output of preprocessing_general.py, so it does not have to be rerun).
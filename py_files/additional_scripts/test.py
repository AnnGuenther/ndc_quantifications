# %%
import pandas as pd
import numpy as np
from pathlib import Path
import os
from copy import deepcopy
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata
meta = setup_metadata()

# %%
ctrs = sorted([
    'CHL', 'NZL', 'AND', 'RWA', 'JAM', 'VNM', 'MNG', 'THA', 'AGO', 'RUS', 'GRD', 'NPL', 'CHE',
    'BRA', 'TON', 'CUB', 'CRI', 'GBR', 'PNG', 'EU27', 'PER', 'NIC', 'MCO', 'PAN', 'KEN',
    'MDV', 'SEN', 'ARE', 'DOM', 'KOR', 'MEX', 'ARG', 'COL', 'ZMB', 'FJI', 'ETH', 'BRN', 'KHM',
    'MHL', 'AUS', 'BGD'])

eu27 = [
    'HUN', 'GRC', 'DEU', 'FRA', 'IRL', 'FIN', 'ITA',
    'EST', 'LVA', 'LTU', 'DNK', 'CZE', 'LUX', 'CYP', 'MLT', 'HRV', 'NLD', 'POL', 'BGR', 'PRT',
    'BEL', 'ROU', 'SVK', 'SVN', 'AUT', 'ESP', 'SWE']

# %%
data = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.main, 'data', 'preprocess', 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv'))
data_ctrs = data.data.reindex(index=ctrs, columns=[2017])
data_ctrs.loc['EU27', 2017] = data.data.reindex(index=eu27, columns=[2017]).sum().values
data_ctrs.sort_values(2017, ascending=False)

# %%
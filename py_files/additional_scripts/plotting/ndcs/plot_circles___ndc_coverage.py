# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
# Plot the number of (I)NDCs that cover a sector / gas.

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()
info = pd.read_csv(Path(meta.path.preprocess, 'coverage_of_combis_orig.csv'),
                   index_col=0)
info.drop(columns=[xx for xx in info.columns if 'LULUCF' in xx], inplace=True)
cmp = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 
    'plotting', 'colours', 'colourmap_inferno.csv'))

# %%
for case in info.columns:
    gas, cat = case.split('_')
    number = len(info.loc[info.loc[:, case] == 'YES', case])
    plt.scatter(gas, cat, number, color=cmp.loc[cmp.shape[0] - np.floor(number/info.shape[0]*cmp.shape[0])])
    plt.text(gas, cat, str(number))

# %%
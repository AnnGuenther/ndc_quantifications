# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
# Get path to model-folder:

# %%
from pathlib import Path

# %%
def get_path_to_main_folder():
    path_cwd = Path.cwd()
    path_cwd_split = str(path_cwd).split('\\')
    path_main = '\\'.join(path_cwd_split[:[xx for xx in range(len(path_cwd_split)) \
        if path_cwd_split[xx] == 'ndc_quantifications'][0]+1])
    return Path(path_main)
#enddef

# %%

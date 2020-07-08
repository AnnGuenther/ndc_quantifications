# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
#####
# Import ISO3s or ISO2s for a group
#####

# %%
def get_isos_for_groups(Groups, ISO):
    """
    Give list of Groups for which you need the ISO3s.
    Return dict of Groups, with list of ISO3s.
    If len(Groups) == 1 --> return list instead of dict.
    """
    
    # %%
    import pandas as pd
    import numpy as np
    import os
    from pathlib import Path
    
    # %%
    if type(Groups) == str:
        Groups = [Groups]
    #
    Out = dict.fromkeys(Groups)
    Path_File = Path(os.path.dirname(os.path.realpath(__file__)), 'iso3_iso2_groups.csv')
    Data = pd.read_csv(Path_File).astype(str)
    for Group_Act in Out:
        ID = np.where(Data.Group == Group_Act)[0]
        if len(ID) == 0:
            print('WARNING in func_ISOs_For_Groups: no information available for ' + Group_Act + '.')
            if len(Groups) == 1:
                Out = [np.nan]
            else:
                Out[Group_Act] = [np.nan]
        else:
            Countries = sorted(list(Data.loc[ID, ISO]))
            if len(Groups) == 1:
                Out = Countries
            else:
                Out[Group_Act] = Countries
    
    return sorted(Out)
# %%

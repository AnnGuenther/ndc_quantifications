# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

#####
# Get LongNames For Groups
#####

import pandas as pd
import numpy as np
import os
from pathlib import Path

# Give list of Groups for which you need the LongNames.
# Return dict of Groups, with list of LongNames.
# If len(Groups) == 1 --> return list instead of dict.

def get_long_name_for_group_or_country(Groups):
    if type(Groups) == str:
        Groups = [Groups]
    #
    Out = dict.fromkeys(Groups)
    Path_File = Path(os.path.dirname(os.path.realpath(__file__)), 'groups_longnames_and_sources.csv')
    Data = pd.read_csv(Path_File).astype(str)
    for Group_Act in Out:
        ID = np.where(Data.Group == Group_Act)[0]
        if len(ID) == 0:
            print('WARNING in func_Group_To_LongNames: no information available for ' + Group_Act + '.')
            if len(Groups) == 1:
                Out = [np.nan]
            else:
                Out[Group_Act] = [np.nan]
        else:
            GroupNames = sorted(list(Data.loc[ID, 'LongName']))
            if len(Groups) == 1:
                Out = GroupNames
            else:
                Out[Group_Act] = GroupNames
    return Out

# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last modified in 04/2020.
"""

# %%
def create_colormap(df_colours):
    """
    Create a colormap from given colours and values for which colours are given.
    Give, e.g., pd.DataFrame([[rgb list for colour 1], [rgb list for colour 2], [rgb list for colour 3]], 
        index=[-1, 1, 5])
    colour 1 will be at -1, colour 2 at 1, colour 3 at 5, and the values in between are 
    interpolated with equal spacing.
    """
    
    # %%
    import numpy as np
    #import pandas as pd
        
    # %%
    #df_colours = pd.DataFrame([[1, 0, 0], [0, 0, 1], [0, 1, 0]], index=[-1, .1, 2], columns=['r', 'g', 'b'])
    ids = df_colours.index
    
    if len(ids) == 2:
        ids_new = list(np.arange(min(ids), max(ids), abs(max(ids) - min(ids))/254)) + [ids[-1]]
    
    # Problem if a given 'middle value' is not in the index anymore after the interpolation, therefore use the second approach for len(ids) > 2:
    else:
        ids_new = []
        for ct in range(len(ids)-1):
            ids_act = [ids[ct], ids[ct+1]]
            ids_new += list(np.arange(ids_act[0], ids_act[-1], abs(ids_act[-1] - ids_act[0])/(abs(ids_act[-1] - ids_act[0])/(ids[-1] - ids[0])*254)))
        ids_new += [ids_act[-1]]
    
    df_colours = df_colours.reindex(index=ids_new)
    df_colours = df_colours.interpolate()
    
    return(df_colours)

# %%
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
def put_labels_to_subplots(*args, **kwargs):
    
    """
    Put labels, e.g., (a), (b), etc. to plots. Upper left corner.
    
    args are the axis, in the correct labelling order.
    
    kwargs:
        labels (e.g., ['i', 'ii', 'iii'])
    """
    
    # %%
    from warnings import warn
    
    # %%
    
    labels_default = 'abcdefghijklmnopqrstuvwxyz'
    if 'labels' in kwargs.keys():
        labels = kwargs['labels']
        if len(labels) != len(args):
            warn("Wrong number of labels. Default is used.")
            labels = labels_default
    else:
        labels = labels_default
    
    for idn in range(len(args)):
        axa = args[idn]
        XL = axa.get_xlim()
        YL = axa.get_ylim()
        axa.text(XL[0] + .01*(XL[1] - XL[0]), YL[1] - .01*(YL[1] - YL[0]), 
                 "(" + labels[idn] + ")", fontweight='bold', ha='left', va='top')
    
    return args

# %%

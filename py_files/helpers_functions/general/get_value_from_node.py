# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
import inspect

# %%
# Get value from class or dict from given strings.
def get_value_from_node(class_or_dict, list_of_path_through_nodes):
    subthing = class_or_dict
    for sub in list_of_path_through_nodes:
        if inspect.isclass(class_or_dict):
            subthing = getattr(subthing, sub)
        else: # Not testing whether it is really a dict... 
            # If it is not it will give an error.
            subthing = subthing[sub]
        #endif
    return subthing
#enddef

# %%  
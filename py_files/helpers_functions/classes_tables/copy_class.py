# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
# When simply deepcopying the class, changes will affect both classes.
# Does not handle sub-classes.

# %%
from copy import deepcopy
from helpers_functions.classes_tables.get_all_attributes_of_class import \
    get_all_attributes_of_class
from helpers_functions.classes_tables.create_class import create_class

# %%
def copy_class(class_in):
    class_out = create_class()
    all_attributes = get_all_attributes_of_class(class_in)
    for attr in all_attributes:
        setattr(class_out, attr, deepcopy(getattr(class_in, attr)))
    #endfor
    return class_out
#enddef

# %%

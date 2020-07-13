# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Adapted from answer on https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class by Matt Luongo / adiro.

Last updated in 02/2020
"""

# %%
# Get all attributes of a class.

# %%
import inspect

# %%
def get_all_attributes_of_class(class_in):
    attrs = inspect.getmembers(class_in, lambda xx: not(inspect.isroutine(xx)))
    attrs = [xx for xx in attrs if not(xx[0].startswith('__') and xx[0].endswith('__'))]
    attrs_list = []
    for attr in attrs:
        attrs_list.append(attr[0])
    #endfor
    return attrs_list
#enddef

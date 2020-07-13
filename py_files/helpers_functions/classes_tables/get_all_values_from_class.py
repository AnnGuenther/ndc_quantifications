# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
# Get all the values in a class (with subclasses of all levels) as list of text.
# Includes the 'path' of attribute names.

# %%
import inspect
import pandas as pd
from helpers_functions.classes_tables.get_all_attributes_of_class import \
    get_all_attributes_of_class

# %%
# Which attributes of class are classes and which are not.
def check_attrs(clss):
    is_class = []
    is_not_class = []
    for attr in get_all_attributes_of_class(clss):
        if (inspect.isclass(getattr(clss, attr)) or
            'class' in str(type(getattr(clss, attr))).replace("<class", "")):
            is_class.append(attr)
        else:
            is_not_class.append(attr)
        #endif
    #endfor
    return is_class, is_not_class
#enddef

# %%
# Get all values (with 'path' of attribute names). As strings.
def get_all_values_from_class(clss):
    list_of_values = []
    continue_checking = []
    txt = []
    is_class, is_not_class = check_attrs(clss)
    for xx in is_not_class:
        txt_act = []
        val = getattr(clss, xx)
        # Put out pd.Series and pd.DataFrame as strings of the values (separating rows by ;).
        if isinstance(val, pd.Series):
            val = val.to_frame().transpose()
        #endif
        if isinstance(val, pd.DataFrame):
            txt_act += [xx, str(type(val))]
            index_name = ('ind,' if val.index.name == None else val.index.name)
            txt_act += [index_name] + [str(xx) for xx in val.columns]
            for idn in val.index:
                txt_act += [str(xx) for xx in val.loc[idn, :]]
            #endfor
        else:
            txt_act += [xx, str(type(val)), str(val)]
        #endif
        txt += [txt_act]
    #endfor
    continue_checking += [clss.__name__ + '.' + xx for xx in is_class]
    list_of_values += txt
    while len(continue_checking) > 0:
        for attr in continue_checking:
            subclasses = attr.split('.')
            subclss = clss
            for sub in subclasses[1:]:
                subclss = getattr(subclss, sub)
            #endfor
            txt = []
            is_class, is_not_class = check_attrs(subclss)
            for xx in is_not_class:
                txt_act = []
                val = getattr(subclss, xx)
                txt_act += ['.'.join(subclasses[1:]) + '.' + xx]
                if isinstance(val, pd.Series):
                    val = val.to_frame().transpose()
                #endif
                if isinstance(val, pd.DataFrame):
                    txt_act += [str(type(val))]
                    index_name = ('ind,' if val.index.name == None else val.index.name)
                    txt_act += [index_name] + [str(xx) for xx in val.columns]
                    for idn in val.index:
                        txt_act += [str(xx) for xx in val.loc[idn, :]]
                    #endfor
                else:
                    txt_act += [str(type(val)), str(val)]
                #endif
                txt += [txt_act]
            #endfor
            continue_checking += [attr + '.' + xx for xx in is_class]
            continue_checking.remove(attr)
            list_of_values += txt
        #endfor
    #endwhile
    return sorted(list_of_values)
#enddef

# %%
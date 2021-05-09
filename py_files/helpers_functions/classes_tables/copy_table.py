# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def copy_table(class_in, **kwargs):
    """
    When simply deepcopying the class, changes will affect both classes (the original and the copy).
    copy_tables does not handle sub-classes.
    
    One can specify
        isos=list_of_iso3s_to_copy and 
        years=list_of_years_to_copy_as_integers (or range of integers).
    """
    
    # %%
    from copy import deepcopy
    import helpers_functions as hpf
    
    # %%
    class_out = hpf.create_table()
    all_attributes = hpf.get_all_attributes_of_class(class_in)
    
    for attr in all_attributes:
        
        if attr == 'data':
            
            data = deepcopy(getattr(class_in, 'data'))
            data = (data.reindex(index=kwargs['isos']) if 'isos' in kwargs.keys() else data)
            data = (data.reindex(columns=kwargs['years']) if 'years' in kwargs.keys() else data)
            setattr(class_out, 'data', data)
            
        else:
            
            setattr(class_out, attr, deepcopy(getattr(class_in, attr)))
    
    class_out.__tablename_to_standard__()
    class_out.__name_to_standard__()
    
    return class_out

# %%

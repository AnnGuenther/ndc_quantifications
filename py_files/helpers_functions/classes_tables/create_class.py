# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
"""
Create a class with the attributes 'data' and the ones given in 'kwargs'.
"""

# %%
class create_class():
    def __init__(self, **kwargs):
        for ind in kwargs.keys():
            if ind != 'name':
                setattr(self, ind, kwargs[ind])
            else:
                self.__name__ = kwargs[ind]
# %%
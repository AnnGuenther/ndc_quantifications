# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def read_text_from_file(path_to_file):
    fid = open(path_to_file, 'r')
    text = fid.read()
    fid.close()
    
    return text
#enddef

# %%
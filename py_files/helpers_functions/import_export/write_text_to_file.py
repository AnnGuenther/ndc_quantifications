# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def write_text_to_file(text, path_to_file):
    fid = open(path_to_file, 'w')
    fid.write(text)
    fid.close()
#enddef

# %%
# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020.
"""

# %%
# Include figure in md-text.

# %%
def include_figure_md(path_to_file, caption, **kwargs):
    txt = ""
    if 'width' in kwargs.keys():
        width = str(kwargs['width'])
    else:
        width = '100'
    #endif
    txt += "\n\n![" + caption + "]" + \
        "(" + str(path_to_file) + "){width=" + width + "%}"
    return txt
#enddef

# %%
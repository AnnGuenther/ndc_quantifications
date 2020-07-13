# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
"""
Include a figure in html-code.
Produces something like:
<p align="center">
<img src="file:///C:/.../...png" alt="test" width="400"/><br>
<caption><i>Fig. 1: caption</i></caption>
</p>"""

# %%
def include_figure_html(txt, path_to_figure, caption, **kwargs):
    txt += "\n\n<p align="
    if 'align' in kwargs.keys():
        txt += "'" + kwargs['align'] + "'"
    else:
        txt +="'center'"
    #endif
    txt += ">\n<img src='file:///" + str(path_to_figure) + "'"
    if 'alt' in kwargs.keys():
        txt += " alt='" + kwargs['alt'] + "'"
    #endif
    txt += " width='"
    if 'width' in kwargs.keys():
        txt += str(kwargs['width'])
    else:
        txt += "800"
    #endif
    txt += "'/><br>\n<caption><i>"
    if 'number' in kwargs.keys():
        number = kwargs['number']
        txt += "Fig. " + str(number) + ": " + caption
        number += 1
    else:
        txt += caption
        number = None
    #endif
    txt += "</i></caption>\n</p>"
    return txt, number
# enddef

# %%
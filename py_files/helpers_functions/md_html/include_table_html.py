# -*- coding: utf-8 -*-
"""
Author: Annika Günther
Last updated in 02/2020.
"""

# %%
# 
"""
Include a table in html-code.
Produces something like:
<table style="width:30%" align="center">
  <caption><i>Tab. 1: caption</i></caption>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  <tr>
    <td>Annika</td>
    <td>Günther</td>
  </tr>
</table>
"""

# %%
import numpy as np
import pandas as pd

# %%
def include_table_html(txt, heads, content, caption, **kwargs):
    # first_col_style: e.g., "", "em", ["i", "b"].
    if 'first_col_style' in kwargs.keys():
        first_col_style = kwargs['first_col_style']
        if type(first_col_style) == str:
            first_col_style = [first_col_style]
        #endif
        style_start = ""
        style_end = ""
        for style in first_col_style:
            style_start += "<" + style + ">"
            style_end += "</" + style + ">"
        #endfor
    else:
        style_start = "<em>"
        style_end = "</em>"
    #endif
    txt += "\n<table style='width:"
    if 'width' in kwargs.keys():
        width = kwargs['width']
    else:
        width = 80
    #endif
    txt += str(width) + "%' align="
    if 'align' in kwargs.keys():
        txt += "'" + kwargs['align'] + "'"
    else:
        txt += "'center'"
    #endif
    if 'width_cols_equal' in kwargs.keys():
        txt += " class='fixed'"
        width_cols_equal = kwargs['width_cols_equal']
    else:
        width_cols_equal = False
    #endif
    txt += ">\n  <caption><br><i>"
    if 'number' in kwargs.keys():
        number = kwargs['number']
        txt += "Tab. " + str(number) + ": " + caption
        number += 1
    else:
        txt += caption
        number = None
    #endif
    txt += "\n</i></caption>\n"
    if width_cols_equal:
        for cols in range(len(heads)):
            txt += "<col width='" + str(np.floor(width/len(heads))) + "' \>"
        #endfor
        txt += "\n"
    #endif
    txt += "  <tr>"
    heads = pd.Series(heads, index=range(len(heads))).astype(str)
    if isinstance(content, pd.Series):
        content_df = pd.DataFrame(columns=range(len(heads)))
        content_df.loc[0, :] = content.values
    else:
        content_df = pd.DataFrame(content, columns=range(len(heads))).astype(str)
    #endif
    for cols in range(len(heads)):
        txt += "\n    <th>" + heads[cols] + "</th>"
    #endfor
    txt += "\n  </tr>\n  <tr>"
    for rows in range(len(content_df.index)):
        for cols in range(len(heads)):
            # First columns with different style.
            if cols == 0:
                txt += "\n    <td>" + style_start + content_df.loc[rows, cols] + style_end + "</td>"
            else:
                txt += "\n    <td>" + content_df.loc[rows, cols] + "</td>"
            #endif
        #endfor
        txt += "\n  </tr>"
    #endfor
    txt += "\n  </tr>\n</table>"
    return txt, number
# enddef

# %%
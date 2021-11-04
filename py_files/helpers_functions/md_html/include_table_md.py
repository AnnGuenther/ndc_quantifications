# -*- coding: utf-8 -*-
"""
Author: Annika Günther
Last updated in 02/2020.
"""

# %%
def include_table_md(heads, content, caption, **kwargs):
    """
    Include a table in md-code.
    Produces something like:
    caption
    | head1  | head2  |
    |--------|--------|
    | row1_1 | row1_2 |
    | row2_1 | row2_2 |
    
    OPTIONAL:
        align = 'clr'
            One alignment per column (c: center, l: left, r: right).
    """
    
    # %%
    import pandas as pd
    
    # %%
    if 'align' in kwargs.keys():
        align = kwargs['align']
    #endif

    heads = pd.Series(heads, index=range(len(heads))).astype(str)
    if isinstance(content, pd.Series):
        content_df = pd.DataFrame(columns=range(len(heads)))
        content_df.loc[0, :] = content.values
    else:
        content_df = pd.DataFrame(content, columns=range(len(heads))).astype(str)
    #endif
    
    txt = "\n\n"
    for cols in range(len(heads)):
        txt += " | " + heads[cols]
    #endfor
    
    txt += " |\n"
    for cols in range(len(heads)):
        if not 'align' in kwargs.keys():
            txt += "|---"
        else:
            if align[cols] == 'c':
                txt += "|:---:"
            elif align[cols] == 'l':
                txt += "|:---"
            elif align[cols] == 'r':
                txt += "|---:"
            #endif
        #endif
    #endfor
    
    txt += "\n"    
    for rows in content_df.index:
        for cols in content_df.columns:
            txt += " | " + content_df.loc[rows, cols]
        #endfor
        txt += " |\n"
    #endfor
    txt += "Table: " + caption
    return txt
# enddef

# %%
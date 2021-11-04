# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
"""
Calculate ratios_w_signs for given valuesIn (can be positive, 0 or negative).
If you use the ratios_w_signs, apply them to absolute values!!!

Replace the 0s by NaNs and remember where the 0s were (put the ratios_w_signs to 0 in the end), unless all values are 0.
Save the valuesIn_signs of the valuesIn.
Calculate the abs() valuesIn_abs.
Calculate the sum over valuesIn_abs: valuesIn_abs_sum.
Calculate the ratio between the valuesIn_abs/valuesIn_abs_sum = ratios_wo_signs (all ratios_wo_signs are positive and sum up to 1).
Apply the valuesIn_signs to the ratios_wo_signs (valuesIn_signs * ratios_wo_signs = ratios_w_signs).
Sum over all those ratios_w_signs is not 1, unless all values were positive).

Calculate the original valuesIn:
valuesIn = ratios_w_signs * valuesIn_abs_sum
If you use the ratios_w_signs, apply them to absolute values!!!

If you multiply the ratios or ratios_mod with 100%, you get the percentage values.
"""

"""
Examples:
ALL POSITIVE
                                  valueIn_1 valueIn_2 valueIn_3 valueIn_4    sums
valuesIn                           2.00      3.00      3.00      1.00        valuesIn_sum            9.00
valuesIn_abs                       2.00      3.00      3.00      1.00        valuesIn_abs_sum        9.00
valuesIn_signs                     1.00      1.00      1.00      1.00
ratios_wo_signs                    0.22      0.33      0.33      0.11        ratios_wo_signs_sum     1.00
ratios_w_signs                     0.22      0.33      0.33      0.11        ratios_w_signs_sum      1.00
ratios_w_signs * valuesIn_abs_sum  2.00      3.00      3.00      1.00

SOME POSITIVE SOME NEGATIVE
                                  valueIn_1 valueIn_2 valueIn_3 valueIn_4    sums
valuesIn                          -2.00     -3.00      3.00      1.00        valuesIn_sum           -1.00
valuesIn_abs                       2.00      3.00      3.00      1.00        valuesIn_abs_sum        9.00
valuesIn_signs                    -1.00     -1.00      1.00      1.00
ratios_wo_signs                    0.22      0.33      0.33      0.11        ratios_wo_signs_sum     1.00
ratios_w_signs                    -0.22     -0.33      0.33      0.11        ratios_w_signs_sum     -0.11
ratios_w_signs * valuesIn_abs_sum -2.00     -3.00      3.00      1.00

SOME POSITIVE SOME NEGATIVE SOME ZERO
                                  valueIn_1 valueIn_2 valueIn_3 valueIn_4    sums
valuesIn                          -2.00      0.00      3.00      1.00        valuesIn_sum            2.00
valuesIn_abs                       2.00      0.00      3.00      1.00        valuesIn_abs_sum        6.00
valuesIn_signs                    -1.00      0.00      1.00      1.00
ratios_wo_signs                    0.22      0.00      0.33      0.11        ratios_wo_signs_sum     1.00
ratios_w_signs                    -0.22      0.00      0.33      0.11        ratios_w_signs_sum      0.33
ratios_w_signs * valuesIn_abs_sum -2.00      0.00      3.00      1.00

ALL ZEROS:
Everything is zero, also the ratios_wo_signs_sum ...
"""

# %%
"""
np.sign(-5) --> -1
np.sign(+5) --> +1
np.sing(0) --> 0
"""

# %%
import numpy as np
import pandas as pd
from warnings import warn

# %%
def ratios_w_signs(valuesIn):
    if isinstance(valuesIn, pd.Series):
        tpe = 'series'
    elif isinstance(valuesIn, pd.DataFrame):
        tpe = 'df'
    elif isinstance(valuesIn, list):
        tpe = 'list'
    elif isinstance(valuesIn, tuple):
        tpe = 'tuple'
    elif isinstance(valuesIn, np.ndarray):
        tpe = 'np'
    else:
        tpe = None
        warn("ratios_w_signs.py: wrong input, nothing calculated.")
    #endif
    if tpe in ['series', 'df', 'list', 'tuple', 'np']:
        if tpe == 'series':
            if matrix.isnull().all():
                nansum = np.nan
        elif tpe != 'df':
            matrix = pd.DataFrame(matrix)

#enddef

# %%

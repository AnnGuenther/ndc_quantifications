# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated: 11/2020
"""

# %%
def rnd(num, digits):
    """
    Round a number to given digits.
    Input:
        num: number or string
        digits: digits as number
    Returns string
    """
    
    import math
    import numpy as np
    
    if np.isnan(float(num)):
        return np.nan
    
    else:
        num = str(float(num))
        main, decimals = num.split('.')
        
        if digits > 0:
            if len(decimals) < digits:
                decimals_new = decimals + '0'*(digits - len(decimals))
            elif len(decimals) == digits:
                decimals_new = decimals
            elif len(decimals) > digits:
                decimals_new = decimals[:digits+1]
                decimals_new = decimals_new[:digits] + '.' + decimals_new[-1]
                if decimals_new[-1] in '01234':
                    decimals_new = math.floor(float(decimals_new))
                else:
                    if decimals_new[-3] == '9':
                        main = str(int(main) + 1)
                        decimals_new = '0'*digits
                    else:
                        decimals_new = math.ceil(float(decimals_new))
            return main + '.' + str(decimals_new)
        
        elif digits == 0:
            decimals_new = decimals[0]
            if decimals_new in '01234':
                main = main
            elif decimals_new in '56789':
                main = main = str(int(main) + 1)
            else:
                print("Something went wrong!")
            return main
        
        else:
            print("Negative input for 'digits' not allowed!")    

# %%
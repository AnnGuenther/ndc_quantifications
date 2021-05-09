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
        return num
    
    else:
        
        num = str(float(num))
        main, decimals = num.split('.')
        main_f = float(main)
        
        if digits > 0:
            
            if len(decimals) < digits:
                # Add 0s after last value.
                decimals_new = decimals + '0'*(digits - len(decimals))
            
            elif len(decimals) == digits:
                # Use same as given.
                decimals_new = decimals
            
            elif len(decimals) > digits:
                
                # Round.
                # do not use decimals_new = str(int(decimals[:digits+1])/10)
                decimals_new = decimals[:digits+1]
                decimals_new = decimals_new[:digits] + '.' + decimals_new[-1]
                
                if decimals_new[-1] in '01234':
                    decimals_new = math.floor(float(decimals_new))
                
                else:
                    
                    if decimals_new[-3] == '9': # number before point
                        
                        #main = str(int(main) + 1) # TODO! try main = vorzeichen(main) + str(int(abs(main) + 1))
                        main = ('-' if np.sign(main_f) == -1 else '') + str(int(abs(main_f) + 1))
                        decimals_new = '0'*digits
                    
                    else:
                        decimals_new = math.ceil(float(decimals_new))
            
            missing_zeros = '0' * (digits - len(str(decimals_new)))
            return main + '.' + missing_zeros + str(decimals_new)
        
        elif digits == 0:
            
            decimals_new = decimals[0]
            
            if decimals_new in '01234':
                main = main
            
            elif decimals_new in '56789':
                main = ('-' if np.sign(main_f) == -1 else '') + str(int(abs(main_f) + 1))
            
            else:
                print("Something went wrong!")
            
            return main
        
        else:
            print("Negative input for 'digits' not allowed!")

# %%
'''
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
'''

# %%
def linear_regression(xx, yy):
    """
    Linear regression to xx and yy data.
    
    INPUT:
    xx and yy: list or np.array of numericals.
    
    OUTPUT:
    Gives out the xx and yy data (as np.arrays), and the linregress values 
    LinregressResult(slope=2.0, intercept=0.0, rvalue=1.0, pvalue=9.003163161571059e-11, stderr=0.0)
    """
    
    # %%
    import numpy as np
    from scipy.stats import linregress
    from warnings import warn
    import sys
    
    # %%
    xx = np.array(xx)
    yy = np.array(yy)
    xx_allnan = [np.nan] * xx.shape[0]
    yy_allnan = [np.nan] * yy.shape[0]
    
    if len(xx) != len(yy):
        sys.exit("linear_regression.py: xx and yy have different lengths. Nothing was calculated.", UserWarning)
            
    elif len(xx) == 1:
        warn("linear_regression.py: regression from one values not possible. The output are all NaNs.", UserWarning)
        linreg = linregress(xx_allnan, yy_allnan)
        
        return xx_allnan, yy_allnan, linreg
    
    elif (len(xx) == 0 or len(yy) == 0):
        sys.exit("linear_regression.py: empty input for xx or yy.")
    
    elif (np.isnan(xx).all() or np.isnan(yy).all()):
        warn("linear_regression.py: empty xx and / or yy as input, or all NaN. The output are all NaNs.", UserWarning)
        class linreg:
            slope = np.nan
            intercept = np.nan
            rvalue = np.nan
            pvalue = np.nan
            stderr = np.nan
        
        return xx_allnan, yy_allnan, linreg
    
    else:
        # Remove the values that are nan in xx or in yy (remove them from both).
        xxreg = [xx[x] for x in range(len(xx)) if (not np.isnan(yy[x])) and (not np.isnan(xx[x]))]
        yyreg = [yy[y] for y in range(len(yy)) if (not np.isnan(xx[y])) and (not np.isnan(yy[y]))]
        
        if len(xxreg) > 1:
            linreg = linregress(xxreg, yyreg)
            xxout = [xx[x] if not np.isnan(yy[x]) else np.nan for x in range(len(xx))]
            yyout = [yy[y] if not np.isnan(xx[y]) else np.nan for y in range(len(yy))]
            
            return xxout, yyout, linreg
        
        else:
            warn("linear_regression.py: regression only for > 1 values. The output are all NaNs.", UserWarning)
            linreg = linregress(xx_allnan, yy_allnan)
            
            return xx_allnan, yy_allnan, linreg

# %%
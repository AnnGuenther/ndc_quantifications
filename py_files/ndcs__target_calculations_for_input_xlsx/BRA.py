# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 01/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
BRA
"""

"""
"NDC2020: "The reference indicator will be quantified on the basis of the total 
net emissions of greenhouse gases (GHG) in the reference year of 2005 reported in 
the “National Inventory of Anthropogenic Emissions by Sources and Removals by 
Sinks of Greenhouse Gases not controlled by the Montreal Protocol”. For reference 
purposes, the level of emissions of greenhouse gases for the base year is 
registered in the current inventory as per the “Third National Communication 
from Brazil to the United Nations Framework Convention on Climate Change”, 
submitted on 20 April 2016.

https://unfccc.int/resource/docs/natc/branc3es.pdf
"""

# %%
def get_data(inclLU, onlyLU, gwp):
    years = [1990, 1995, 2000, 2005, 2010]
    txt = '{"EMI": {"onlyLU": {'
    for year, count in zip(years, range(len(years))):
        txt += f'"{year}": "{hpf.rnd(onlyLU[count], 3)} MtCO2eq_{gwp}"' + \
            (', ' if count < len(years)-1 else '}}')
    txt += ', "inclLU": {'
    for year, count in zip(years, range(len(years))):
        txt += f'"{year}": "{hpf.rnd(inclLU[count], 3)} MtCO2eq_{gwp}"' + \
            (', ' if count < len(years)-1 else '}}')
    txt += ', "exclLU": {'
    for year, count in zip(years, range(len(years))):
        txt += f'"{year}": "{hpf.rnd(inclLU[count] - onlyLU[count], 3)} MtCO2eq_{gwp}"' + \
            (', ' if count < len(years)-1 else '}}')
    txt += '}'
    return txt

    # %%
# GWP SAR
# Data given as Gg -> convert it to Mt
emi_gwpsar_inclLU = [1342.909, 2568.872, 1992.520, 2735.898, 1271.399]
emi_gwpsar_onlyLU = [792.038, 1931.478, 1265.606, 1904.666, 349.173]
txt_sar = get_data(emi_gwpsar_inclLU, emi_gwpsar_onlyLU, 'SAR')

# GWP AR5
emi_gwpar5_inclLU = [1410.434, 2651.780, 2074.399, 2837.956, 1364.197]
emi_gwpar5_onlyLU = [797.413, 1946.934, 1276.260, 1921.694, 355.002]
txt_ar5 = get_data(emi_gwpar5_inclLU, emi_gwpar5_onlyLU, 'AR5')

# %%

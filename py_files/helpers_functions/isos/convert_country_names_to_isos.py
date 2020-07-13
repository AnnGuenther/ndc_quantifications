# Author: Annika Guenther, annika.guenther@pik-potsdam.de
# %%
# INPUT
# 
# %%
import pandas as pd
from pathlib import Path
import os

# %%
def convert_country_names_to_isos(country_names, iso_spec):
    #print('!!! IMPORTANT: check the matches !!!')
    File = 'iso3_iso2_countrynames.csv'
    Data = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), 
                            File)).astype(str)
    Data.loc[Data.ISO3 == 'NAM', 'ISO2'] = 'NA'
    Data.index = Data.loc[:, iso_spec]
    if type(country_names) == str:
        country_names = [country_names]
    #
    ISOs = pd.DataFrame(index = range(0, len(country_names)), 
                        columns=[iso_spec, 'country_name_input', 'country_name_chosen'])
    ISOs.country_name_input = country_names
    country_names = [xx.upper() for xx in country_names]
    Remove_Words = ['THE', 'AND', 'OF']
    row = 0
    for name in country_names:
        data_act = pd.Series(index=ISOs.columns)
        data_act['country_name_input'] = name
        if 'UNIT' in name:
            if 'TANZANIA' in name:
                data_act[iso_spec] = 'TZA'
            elif 'KINGDOM' in name:
                data_act[iso_spec] = 'GBR'
            elif 'STATES' in name:
                data_act[iso_spec] = 'USA'
            elif ('EMIRATES' in name) or ('ARAB' in name):
                data_act[iso_spec] = 'ARE'
        elif name == 'SWAZILAND':
            data_act[iso_spec] = 'SWZ'
        elif 'ZEALAND' in name:
            data_act[iso_spec] = 'NZL'
        elif 'RUSSIA' in name:
            data_act[iso_spec] = 'RUS'
        elif ('SOUTH' in name and 'AFRICA' in name):
            data_act[iso_spec] = 'ZAF'
        elif ('COSTA' in name and 'RICA' in name):
            data_act[iso_spec] = 'CRI'
        elif (name == 'EU') or (name == 'EU28'):
            data_act[iso_spec] = 'EU28'
        elif name == 'UAE':
            data_act[iso_spec] = 'ARE'
        elif 'CONGO' in name:
            if 'REP' in name:
                if 'DEMO' not in name:
                    data_act[iso_spec] = 'COG'
                else:
                    data_act[iso_spec] = 'COD'
        elif 'GUINEA' in name:
            if 'BISSAU' in name:
                data_act[iso_spec] = 'GNB'
            elif 'EQ' in name:
                data_act[iso_spec] = 'GNQ'
            elif 'PAP' in name:
                data_act[iso_spec] = 'PNG'
            else:
                data_act[iso_spec] = 'GIN'
        elif 'ARAB' in name:
            if 'EGYPT' in name:
                data_act[iso_spec] = 'EGY'
            elif 'SAUDI' in name:
                data_act[iso_spec] = 'SAU'
            elif 'SYRIA' in name:
                data_act[iso_spec] = 'SYR'
            elif 'EMIRATES' in name:
                data_act[iso_spec] = 'ARE'
            elif 'LIBYA' in name:
                data_act[iso_spec] = 'LBY'
        elif 'LIBYA' in name:
            data_act[iso_spec] = 'LBY'
        elif 'SUDAN' in name:
            if 'SOUTH' in name:
                data_act[iso_spec] = 'SSD'
            else:
                data_act[iso_spec] = 'SDN'
        elif 'VIRGIN' in name:
            if 'BRIT' in name:
                data_act[iso_spec] = 'VGB'
            elif 'U' in name:
                data_act[iso_spec] = 'VIR'
        elif 'KOREA' in name:
            if ('DEMO' in name) or ('NORTH' in name):
                data_act[iso_spec] = 'PRK'
            elif ('REP' in name) or ('SOUTH' in name):
                data_act[iso_spec] = 'KOR'
        elif ('ISL' in name) and ('MAN' in name):
            data_act[iso_spec] = 'IMN'
        elif 'SAMOA' in name:
            if 'AME' in name:
                data_act[iso_spec] = 'ASM'
            else:
                data_act[iso_spec] = 'WSM'
        elif 'SOLOMON' in name:
            data_act[iso_spec] = 'SLB'
        elif 'BARTHELEM' in name:
            data_act[iso_spec] = 'BLM'
        elif ('TIMOR' in name) or ('LESTE' in name):
            data_act[iso_spec] = 'TLS'
        elif 'VIET' in name:
            data_act[iso_spec] = 'VNM'
        else:
            nameSplit = name.split()
            for Remove in Remove_Words:
                if Remove in nameSplit:
                    nameSplit.remove(Remove)
            Search = []
            Search2 = []
            for ISO_Act in Data.index:
                country_Act = Data.loc[ISO_Act, ['ShortName', 'LongName']]
                country_Act = ' '.join(country_Act).upper().split()
                for Remove in Remove_Words:
                    if Remove in country_Act:
                        country_Act.remove(Remove)
                for Act in country_Act:
                    if Act in nameSplit:
                        Search.append(ISO_Act)
                        Search2.append(sum([1 for xx in nameSplit if xx in Data.loc[ISO_Act, 'ShortName'].upper()]))
            if len(Search2) > 0:
                Max = max(Search2)
                ISO_Act = list(set([Search[xx] for xx in range(0, len(Search)) if Search2[xx] == Max]))
                if len(ISO_Act) == 1:
                    data_act[iso_spec] = ISO_Act[0]
                else:
                    print('No ISO for ' + name)
        if type(data_act[iso_spec]) == str:
            data_act['country_name_chosen'] = Data.loc[data_act[iso_spec], 'ShortName']
        # endif
        ISOs.loc[row, :] = data_act
        row = row + 1
    #print('!!! IMPORTANT: check the matches !!!')
    print(ISOs.values)
    return list(ISOs.loc[:, iso_spec])
# %%

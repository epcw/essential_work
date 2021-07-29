import requests
import json
import pandas as pd

#ROOTBEER = '/home/ubuntu/housing_equity/sandbox-singlepage/' #production
ROOTBEER = '' #local

headers = {'Content-type': 'application/json'}
#serieslist = [''] #use to build this list through testing individual series source - https://data.bls.gov/timeseries/MLUMS53NN0001003?data_tool=XGtable
serieslist = ['SMU53426440700000001','LAUMT534266000000003','MLUMS53NN0001003'] #the real thing
start = '2011'
end = '2021'
data = json.dumps({"seriesid": serieslist,"startyear": str(start), "endyear": str(end),"registrationkey":"6a473b245bd04b109db93bb35f6b36ef" })
#data = json.dumps({"seriesid": serieslist,"registrationkey":"6a473b245bd04b109db93bb35f6b36ef" })
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
df = pd.DataFrame()
for series in json_data['Results']['series']:
    for item in series['data']:
        item['seriesID'] = series['seriesID'] #add seriesID as an item in the dict (needed because of the nesting in the json)
        df = df.append(item, True) #add dict as a row in the df
df['seriesName'] = ['StateAreaUnemployment(Sea-Bell-EverMSA)-ServiceSector(in_thous)' if i == 'SMU53426440700000001'
                    else 'LocalAreaUnemployment(Sea-Tac-BelMSA)' if i == 'LAUMT534266000000003'
                    else 'MassLayoffEvents(WA-definedas50UIfilingsin5wks)' if i == 'MLUMS53NN0001003'
                    else '' for i in df['seriesID']]

print(df) #for debugging
filename = ROOTBEER + 'data/bls-data.csv'
df.to_csv(filename,index=False) #comment out when testing unless you want to overwrite your datafile every time
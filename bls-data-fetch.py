import requests
import json
import pandas as pd

#ROOTBEER = '/home/ubuntu/housing_equity/sandbox-singlepage/' #production
ROOTBEER = '' #local

headers = {'Content-type': 'application/json'}
#serieslist = ['SMU53426440000000001'] #use to build this list through testing individual series
# individual series source exmaple https://data.bls.gov/timeseries/MLUMS53NN0001003?data_tool=XGtable
# list of series - https://www.bls.gov/sae/additional-resources/list-of-published-state-and-metropolitan-area-series/washington.htm
serieslist = ['SMU53426600000000001',
              'LAUMT534266000000003',
              'MLUMS53NN0001003',
              'SMU53426600500000001',
              'SMU53426600500000002',
              'SMU53426600500000003',
              'SMU53426600500000011',
              'SMU53426600600000001',
              'SMU53426600700000001',
              'SMU53426600800000001',
              'SMU53426601000000001',
              'SMU53426602000000001',
              'SMU53426602023800001',
              'SMU53426603000000001',
              'SMU53426604000000001',
              'SMU53426604100000001',
              'SMU53426604200000001',
              'SMU53426604244500001',
              'SMU53426604245200001',
              'SMU53426604300000001',
              'SMU53426605000000001',
              'SMU53426605500000001',
              'SMU53426606000000001',
              'SMU53426606056000001',
              'SMU53426606056100001',
              'SMU53426606500000001',
              'SMU53426606562100001',
              'SMU53426606562100001',
              'SMU53426606562200001',
              'SMU53426607000000001',
              'SMU53426607072200001',
              'SMU53426609000000001',
              'SMU53426608000000001',
              'SMU53426609091000001',
              'SMU53426609092000001',
              'SMU53426609092161101',
              'SMU53426609093000001',
              'SMU53426609093161101'] #the real thing
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
df['seriesName'] = ['Employment(Sea-Tac-BelMSA)-ServiceSector(in_thous)' if i == 'SMU53426600700000001'
                    else 'LocalAreaUnemployment(Sea-Tac-BelMSA)' if i == 'LAUMT534266000000003'
                    else 'MassLayoffEvents(WA-definedas50UIfilingsin5wks)' if i == 'MLUMS53NN0001003'
                    else 'Employment(Sea-Tac-BelMSA)-TotalNonFarm(in_thous)' if i == 'SMU53426600000000001'
                    else 'Employment(Sea-Tac-BelMSA)-TotalPrivate(in_thous)' if i == 'SMU53426600500000001'
                    else 'Employment(Sea-Tac-BelMSA)-TotalPrivate(avg_weekly_hours)' if i == 'SMU53426600500000002'
                    else 'Employment(Sea-Tac-BelMSA)-TotalPrivate(avg_hourly_$)' if i == 'SMU53426600500000003'
                    else 'Employment(Sea-Tac-BelMSA)-TotalPrivate(avg_weekly_$)' if i == 'SMU53426600500000011'
                    else 'Employment(Sea-Tac-BelMSA)-Goods-Producing(in_thous)' if i == 'SMU53426600600000001'
                    else 'Employment(Sea-Tac-BelMSA)-Services-Private(in_thous)' if i == 'SMU53426600800000001'
                    else 'Employment(Sea-Tac-BelMSA)-Mining+Logging(in_thous)' if i == 'SMU53426601000000001'
                    else 'Employment(Sea-Tac-BelMSA)-Construction(in_thous)' if i == 'SMU53426602000000001'
                    else 'Employment(Sea-Tac-BelMSA)-Manufacturing(in_thous)' if i == 'SMU53426603000000001'
                    else 'Employment(Sea-Tac-BelMSA)-SpecialtyTradeContractors(in_thous)' if i == 'SMU53426602023800001'
                    else 'Employment(Sea-Tac-BelMSA)-Trade+Transportation+Utilities(in_thous)' if i == 'SMU53426604000000001'
                    else 'Employment(Sea-Tac-BelMSA)-WholesaleTrade(in_thous)' if i == 'SMU53426604100000001'
                    else 'Employment(Sea-Tac-BelMSA)-RetailTrade(in_thous)' if i == 'SMU53426604200000001'
                    else 'Employment(Sea-Tac-BelMSA)-FoodandBeverageStores(in_thous)' if i == 'SMU53426604244500001'
                    else 'Employment(Sea-Tac-BelMSA)-GenStores(in_thous)' if i == 'SMU53426604245200001'
                    else 'Employment(Sea-Tac-BelMSA)-Transport+Warehousing(in_thous)' if i == 'SMU53426604300000001'
                    else 'Employment(Sea-Tac-BelMSA)-Information(in_thous)' if i == 'SMU53426605000000001'
                    else 'Employment(Sea-Tac-BelMSA)-Professional+businessservices(in_thous)' if i == 'SMU53426606000000001'
                    else 'Employment(Sea-Tac-BelMSA)-Admin+Support+WasteManagement+Remediation(in_thous)' if i == 'SMU53426606056000001' #maybe kill this one if it'encompassess all of the below
                    else 'Employment(Sea-Tac-BelMSA)-Admin+Support(in_thous)' if i == 'SMU53426606056100001'
                    else 'Employment(Sea-Tac-BelMSA)-Education+HealthServices(in_thous)' if i == 'SMU53426606500000001'
                    else 'Employment(Sea-Tac-BelMSA)-AmbulatoryHealthCare(in_thous)' if i == 'SMU53426606562100001'
                    else 'Employment(Sea-Tac-BelMSA)-Hospitals(in_thous)' if i == 'SMU53426606562200001'
                    else 'Employment(Sea-Tac-BelMSA)-Leisure+Hospitality(in_thous)' if i == 'SMU53426607000000001'
                    else 'Employment(Sea-Tac-BelMSA)-FoodDrinkingPlaces(in_thous)' if i == 'SMU53426607072200001'
                    else 'Employment(Sea-Tac-BelMSA)-OtherServices(in_thous)' if i == 'SMU53426608000000001'
                    else 'Employment(Sea-Tac-BelMSA)-Government(in_thous)' if i == 'SMU53426609000000001'
                    else 'Employment(Sea-Tac-BelMSA)-FederalGovt(in_thous)' if i == 'SMU53426609091000001'
                    else 'Employment(Sea-Tac-BelMSA)-StateGovt(in_thous)' if i == 'SMU53426609092000001'
                    else 'Employment(Sea-Tac-BelMSA)-StateGovtEducational(in_thous)' if i == 'SMU53426609092161101'
                    else 'Employment(Sea-Tac-BelMSA)-LocalGovt(in_thous)' if i == 'SMU53426609093000001'
                    else 'Employment(Sea-Tac-BelMSA)-LocalGovtEducational(in_thous)' if i == 'SMU53426609093161101'
                    else '' for i in df['seriesID']]

#print(df) #for debugging
filename = ROOTBEER + 'data/bls-data.csv'
df.to_csv(filename,index=False) #comment out when testing unless you want to overwrite your datafile every time
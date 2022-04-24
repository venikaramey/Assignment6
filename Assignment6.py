import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis',  'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

###1
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
###2
temp = pd.DataFrame(df['From_To'])
# print(temp)
temp['Source'] = temp.From_To.str.split('_').str[0]
temp['Destination'] = temp.From_To.str.split('_').str[1]
temp.drop('From_To',axis=1,inplace=True)
# print(temp)

####3
temp['Source'] =temp['Source'].str.capitalize()
temp['Destination'] =temp['Destination'].str.capitalize()
# print(temp)

###4
df.drop('From_To',axis=1,inplace=True)
df =pd.concat([df,temp],axis=1)
# print(df)

###5
delays =pd.DataFrame(df['RecentDelays'].to_list(),columns=['delay_1','delay_2','delay_3'])
# print(delays)
df.drop('RecentDelays',axis=1,inplace=True)
df =pd.concat([df,delays],axis=1)
print(df)


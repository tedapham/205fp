
"""#python script to paste together files
import wget
import numpy as np
import pandas as pd
import os

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def create_data(state):
    url='https://waterservices.usgs.gov/nwis/site/?STATECD='+state+'&siteOutput=expanded'
    statefile=wget.download(url)
    datalist=[]
    with open(statefile,'r') as file:
        for line in file:
            if line[0]!='#':
                x=line.split('\t')
                datalist.append(x)
    os.remove(statefile)
    state_df=pd.DataFrame(datalist[2:],columns=datalist[0])
    return state_df

df_list=[]
for state in states:
    df_list.append(create_data(state))
print df_list

#create raw dataframe with all the state data
raw_df=pd.concat(df_list)

site_type_df=pd.read_csv('USGSSitetypes.csv',header=None,names=['Site_cd','Site_Type','Type_Description'])
statecounty_lookup=pd.read_csv('USGSCountyStateCode.csv')
statecounty_lookup['County']=statecounty_lookup['County'].str.replace(' Parish','')
statecounty_lookup['County']=statecounty_lookup['County'].str.replace(' County','')

df=raw_df[['site_no','station_nm','site_tp_cd','dec_lat_va','dec_long_va','state_cd','county_cd','dec_coord_datum_cd',
       'drain_area_va','nat_aqfr_cd','well_depth_va']]

df.columns=['site_no','station_nm','Site_cd','Latitude','Longitude','State_CD','County_CD','dec_coord_datum_cd',
       'drain_area_va','nat_aqfr_cd','well_depth_va']

df['State_CD']=pd.to_numeric(df['State_CD'])
df['County_CD']=pd.to_numeric(df['County_CD'])

df=pd.merge(df,site_type_df,how='left',on='Site_cd')

df=pd.merge(df,statecounty_lookup,how='left',on=['State_CD','County_CD'])

df=df.set_index('site_no')

df.to_csv('water_data.csv',header=False)

#df.to_csv('sites.csv')
"""
#python script to paste together files
import wget
import numpy as np
import pandas as pd
import os

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def create_data(state):
    url='https://waterservices.usgs.gov/nwis/site/?STATECD='+state+'&siteOutput=expanded'
    statefile=wget.download(url)
    datalist=[]
    with open(statefile,'r') as file:
        for line in file:
            if line[0]!='#':
                x=line.split('\t')
                datalist.append(x)
    os.remove(statefile)
    state_df=pd.DataFrame(datalist[2:],columns=datalist[0])
    return state_df

df_list=[]
for state in states:
    df_list.append(create_data(state))
print df_list

#create raw dataframe with all the state data
raw_df=pd.concat(df_list)

site_type_df=pd.read_csv('USGSSitetypes.csv',header=None,names=['Site_cd','Site_Type','Type_Description'])
statecounty_lookup=pd.read_csv('USGSCountyStateCode.csv')
statecounty_lookup['County']=statecounty_lookup['County'].str.replace(' Parish','')
statecounty_lookup['County']=statecounty_lookup['County'].str.replace(' County','')

df=raw_df[['site_no','station_nm','site_tp_cd','dec_lat_va','dec_long_va','state_cd','county_cd','dec_coord_datum_cd',
       'drain_area_va','nat_aqfr_cd','well_depth_va']]

df.columns=['site_no','station_nm','Site_cd','Latitude','Longitude','State_CD','County_CD','dec_coord_datum_cd',
       'drain_area_va','nat_aqfr_cd','well_depth_va']

df['State_CD']=pd.to_numeric(df['State_CD'])
df['County_CD']=pd.to_numeric(df['County_CD'])

df=pd.merge(df,site_type_df,how='left',on='Site_cd')

df=pd.merge(df,statecounty_lookup,how='left',on=['State_CD','County_CD'])

df=df.set_index('site_no')
df['station_nm'] = df['station_nm'].str.replace(',',' ')

df2=df[['station_nm','Latitude','Longitude','dec_coord_datum_cd','drain_area_va',
    'nat_aqfr_cd','well_depth_va','Site_Type','State','County','Size']]

df2.to_csv('water_data2.csv',header = False)

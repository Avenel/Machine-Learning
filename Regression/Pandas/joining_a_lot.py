import quandl
import pickle
import pandas as pd
api_key = open('./quandlapikey.txt', 'r').read()

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]
    

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': abbv}, inplace=True)
        print(query)
        df[abbv] = (df[abbv]-df[abbv][0]) / df[abbv][0] * 100.0
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={'Value': 'United States'}, inplace=True)
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    df.rename(columns={'United States': 'US_HPI'}, inplace=True)
    return df

def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start = '1975-01-01', auhtoken = api_key)
    df['Value'] = (df['Value']-df['Value'][0]) / df['Value'][0] * 100.0
    df.rename(columns={'Value': 'MTG'}, inplace=True)
    df = df.resample('M').mean()
    return df


def big_mac_index_data():
    df = quandl.get("ECONOMIST/BIGMAC_USA", trim_start="1975-01-01", authtoken=api_key)
    print(df.head())
    df["dollar_price"] = (df["dollar_price"]-df["dollar_price"][0]) / df["dollar_price"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'dollar_price':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df

# grab_initial_state_data()
HPI_data = pd.read_pickle('fiddy_states3.pickle')
m30 = mortgage_30y()
big_mac_index = big_mac_index_data()
gdp = gdp_data()
HPI_Bench = HPI_Benchmark()
# unemployment = us_unemployment()

HPI = HPI_data.join([HPI_Bench, m30, gdp, big_mac_index])
pd.to_pickle(HPI, 'HPI_data.pickle')

print(HPI.tail())
# print(HPI.corr())

# us_m30_corr = HPI.corr()
# print(us_m30_corr)

# state_HPI_M30 = HPI_data.join(m30)
# print(state_HPI_M30.corr()['M30'].describe())
import quandl
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# (byte) data serialization and deserialization
import pickle

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

api_key = open('./quandlapikey.txt', 'r').read()

# Get all State Abbreviations
def state_list(): 
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        print('FMAC/HPI_' + str(abbv))
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': abbv}, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    # pandas:
    main_df.to_pickle('fiddy_states_percent_change_to_origin.pickle')

# eigene ladefunktion
def load_state_data_from_pickle():
    pickle_in = open('fiddy_states.pickle', 'rb')
    HPI_data = pickle.load(pickle_in)
    print(HPI_data)

# plot HPI_data and HPI_Benchmark
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)

HPI_data = pd.read_pickle('../fiddy_states.pickle')

# rollender avg
# HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)

# standardabweichung
# HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)

# rolling korrelation
TX_AK_12corr = pd.rolling_corr(HPI_data['TX'], HPI_data['AK'], 12)

# print(HPI_data[['TX', 'TX12MA']])

HPI_data['TX'].plot(ax=ax1)
HPI_data['AK'].plot(ax = ax1)
TX_AK_12corr.plot(ax = ax2)

plt.legend().remove()
plt.show()

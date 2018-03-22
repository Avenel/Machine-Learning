import quandl
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# (byte) data serialization and deserialization
import pickle

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
        
        # Berechnet prozentual die Veränderung zum Vorwert
        # df = df.pct_change()

        # Wir wollen die Veränderung prozentual zum Start berechnen
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    # eigene funktion zum speichern
    #pickle_out = open('fiddy_states.pickle', 'wb')
    #pickle.dump(main_df, pickle_out)
    #pickle_out.close()

    # pandas:
    main_df.to_pickle('fiddy_states_percent_change_to_origin.pickle')

# eigene ladefunktion
def load_state_data_from_pickle():
    pickle_in = open('fiddy_states.pickle', 'rb')
    HPI_data = pickle.load(pickle_in)
    print(HPI_data)

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    print(df.head())
    df.rename(columns={'Value': 'United States'}, inplace=True)
    df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0
    return df


# grab_initial_state_data()

# pandas ladefunktion

# plot HPI_data and HPI_Benchmark
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('fiddy_states_percent_change_to_origin.pickle')
benchmark = HPI_Benchmark()

HPI_data.plot(ax = ax1)
benchmark.plot(color='k', ax=ax1, linewidth=10)

plt.legend().remove()
plt.show()

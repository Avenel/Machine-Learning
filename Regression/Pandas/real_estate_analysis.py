import quandl
import pandas as pd

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
        df = quandl.get('FMAC/HPI_TX', authtoken=api_key)
        df.rename(columns={'Value': abbv}, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    # eigene funktion zum speichern
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

    # pandas:
    # main_df.to_pickle('fiddy_states.pickle')

# grab_initial_state_data()

# eigene ladefunktion
def load_state_data_from_pickle():
    pickle_in = open('fiddy_states.pickle', 'rb')
    HPI_data = pickle.load(pickle_in)
    print(HPI_data)

# pandas ladefunktion
HPI_data = pd.read_pickle('fiddy_states.pickle')
print(HPI_data)
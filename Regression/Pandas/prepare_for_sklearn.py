import quandl
import pickle
import pandas as pd
api_key = open('./quandlapikey.txt', 'r').read()

HPI_data = pd.read_pickle('HPI_data.pickle')

# add future price
HPI_data['Future_US_HPI'] = HPI_data['US_HPI'].shift(-1)

# method for calc label
def calc_label(curr_HPI, fut_HPI):
    if fut_HPI > curr_HPI:
        return 1
    else:
        return 0

HPI_data['label'] = list(map(calc_label, HPI_data['US_HPI'], HPI_data['Future_US_HPI']))
HPI_data.dropna(inplace=True)
print(HPI_data)

pd.to_pickle(HPI_data, 'HPI_sklearn_ready.pickle')
import pandas_datareader as web
import datetime

def update_graph(user_input):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2018, 3, 23)
    df = web.DataReader(user_input, 'google', start, end)
    print(df.head())

update_graph('TSLA')

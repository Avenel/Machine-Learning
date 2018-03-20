import pandas as pd
import datetime
import quandl
import matplotlib.pyplot as plt
from matplotlib import style

df = quandl.get('WIKI/GOOGL')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = quandl.get('WIKI/GOOGL')
print(df.head())

style.use('fivethirtyeight')
df['Adj. Open'].plot()
plt.legend()
plt.show()
import pandas as pd

df = pd.read_csv('ZILLOW-N4480_ZRIMFRR.csv', names = ['Date', 'House_Prices'], index_col=0)
#df.set_index('Date', inplace=True)

print(df.head())

df.rename(columns={'House_Prices': 'Prices'}, inplace=True)
df.to_csv('newcsv2.csv')
df.to_html('example.html')
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight') 

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)

# rollende Standardabweichung
df['STD'] = df['meters'].rolling(2).std()

# df standardabweichung
df_std = df.describe()
df_meters_std = df_std['meters']['std']
print(df_meters_std)

# lösche alle messwerte, die über der allgemeinen std liegen
df = df[ (df['STD'] < df_meters_std) ]


df['meters'].plot()
plt.show()
#joining and merging dfs
# merge -> Join on shared columns: pd.merge(x, y, on='', how='')
# join -> Join on index: df1.join(df2, how='')
# left, outer, right, inner -> like sql joins

import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(df1)
print(df2)
print(df3)

print('-- MERGE ---')
d4 = pd.merge(df1, df3, on='HPI')
d4.set_index('HPI', inplace=True)
print(d4)

print(pd.merge(df1,df2, on=['HPI', 'Int_rate']))

# join
print('-- JOIN ---')
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
print(joined)


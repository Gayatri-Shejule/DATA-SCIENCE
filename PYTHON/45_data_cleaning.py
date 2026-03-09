import pandas as pd

df = pd.read_csv('45_data.csv')

print(df)

new_df = df.dropna()

print(new_df.to_string())

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())

df.drop_duplicates(inplace = True)

print(df.to_string())

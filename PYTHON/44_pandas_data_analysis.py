import pandas as pd

df = pd.read_csv('44_data.csv')

print(df.head(10))

print(df.head())

print(df.tail(8))

print(df.tail())

print(df.info())
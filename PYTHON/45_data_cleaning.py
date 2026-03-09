import pandas as pd

df = pd.read_csv('45_data.csv')

print(df)

new_df = df.dropna()

print(new_df.to_string())
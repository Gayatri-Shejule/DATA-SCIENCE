import pandas as pd

df = pd.read_csv('42_data.csv')

print(df) 

print(df.to_string()) 

print(pd.options.display.max_rows) 

pd.options.display.max_rows = 9999
print(df)
print(pd.options.display.max_rows) 
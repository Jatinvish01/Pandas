import pandas as pd

#  .head()  .tail()

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print('Display the first 5 rows of first: ')
print(df.head())
print('Display the first 5 rows of last:')
print(df.tail())
'''
Same common arregation functions
1- sum()
2- mean()
3- count()
4- min()
5- max()
6- std()
'''

import pandas as pd

data = {
      "Name": ["Robert", "John", "Michael", "Sarah", "Jessica"],
      "Age": [28, 30, 29, 28, 30],
      "Salary": [50000, 60000, 55000, 45000, 70000],
      "Department": ["HR", "IT", "Finance", "Marketing", "Sales"]
}

df = pd.DataFrame(data)
print(df)

# Grouping data
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

'''
df.groupby("Age")
age = 28 [50000, 45000]
age = 30 [60000, 70000]
age = 29 > [55000]

["Salary"].sum()
age = 28 [50000, 45000] = 95000
age = 30 [60000, 70000] = 130000
age = 29 > [55000] = 55000
'''


# Grouping data with multiple columns
df = pd.DataFrame(data)
print(df)

# Grouping data
grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print("\n After grouping Age and Name\n",grouped)
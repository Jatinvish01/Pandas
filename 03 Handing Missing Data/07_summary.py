'''
df["column_name"].mean()
df["column_name"].sum()
df["column_name"].max()
df["column_name"].min()
'''

import pandas as pd


data = {
      "Name": ["Robert", "John", "Michael", "Sarah", "Jessica"],
      "Age": [28, 34, 29, 25, 30],
      "Salary": [50000, 60000, 55000, 45000, 70000],
      "Department": ["HR", "IT", "Finance", "Marketing", "Sales"]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print(avg_salary)
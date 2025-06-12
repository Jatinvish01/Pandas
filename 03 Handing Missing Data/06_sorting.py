'''
sorting data
SORTING DATA 1 column sort_value()
df.sort_values(by="columns_name", True/False, implace = True)
'''

import pandas as pd

data = {
      "Name": ["Robert", "John", "Michael", "Sarah", "Jessica"],
      "Age": [28, 34, 29, 25, 30],
      "Salary": [50000, 60000, 55000, 45000, 70000],
      "Department": ["HR", "IT", "Finance", "Marketing", "Sales"]
}

df = pd.DataFrame(data)
print(df)

# sortig the Age column in ascending order
df.sort_values(by="Age", ascending=True, impalce=True)
print("\nDataFrame after sorting by Age in ascending order:\n", df)

df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print("\nDataFrame after sorting by Age and Salary in descending order:\n", df)
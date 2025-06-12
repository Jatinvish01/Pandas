'''
vertically (row-wse)
horizontally (column-wise)

pd.concate[df1, df2], axis=0, ignore_index=True)
'''

# Vertically (row-wise)
import pandas as pd

df_Region1 = pd.DataFrame({
      "CustomerID": [1, 2, 3, 4],
      "Name": ["Gopal", "Raju", "Ravi", "Raj"]
})

df_Region2 = pd.DataFrame({
      "CustomerID": [5, 6, 7, 8],
      "Name": ["Ramesh", "Suresh", "Mahesh", "Rajesh"]
})

df_concate = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print(df_concate)

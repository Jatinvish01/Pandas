'''
There is a two option to handle missing values
1. ya to us values ko remove krdo
2. ya to unhe kisi value se replace krdo
3. ya to unhe kisi value se fill krdo

The dropna() method in Pandas is used to remove missing (NaN) values from a DataFrame or Series.
It can drop rows or columns that contain any or all NaN values.

🔹 Common Parameters:
axis=0 → drop rows (default)

axis=1 → drop columns

how='any' → drop if any NaN

how='all' → drop if all values are NaN

inplace=True → modify the original DataFrame directly
'''

import pandas as pd

data = data = {
      "Name": [None, 'Rocky', 'Sultan', 'Micheal','Harry','Jatin'],
      "Age": [None, 45, 34, 40,99,78],
      "City": [None, 'Los Angeles', 'Chicago', 'Houston','Delhi','Mumbai'],
      "Salary": [70000, None, 60000, 90000, 66900,58900]
}
 
df = pd.DataFrame(data)
print(df)

# Drop rows with any NaN values

df.dropna( inplace=True)
print("\n",df)

# Output:
#        Name   Age     City   Salary
# 2   Sultan  34.0  Chicago  60000.0
# 3  Micheal  40.0  Houston  90000.0
# 4    Harry  99.0    Delhi  66900.0
# 5    Jatin  78.0   Mumbai  58900.0
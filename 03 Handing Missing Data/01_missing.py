import pandas as pd

data = data = {
      "Name": [None, 'Rocky', 'Sultan', 'Micheal','Harry','Jatin'],
      "Age": [None, 45, 34, 40,99,78],
      "City": [None, 'Los Angeles', 'Chicago', 'Houston','Delhi','Mumbai'],
      "Salary": [70000, None, 60000, 90000, 66900,58900]
}
 
df = pd.DataFrame(data)
print(df)

# isnull() method
print(df.isnull())


print(df.isnull().sum()) # gives the count of missing values in each column

# Output: 
# Name      1
# Age       1
# City      1
# Salary    1
# dtype: int64
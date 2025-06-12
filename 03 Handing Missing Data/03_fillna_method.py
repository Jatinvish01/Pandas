import pandas as pd

data = data = {
      "Name": [None, 'Rocky', 'Sultan', 'Micheal','Harry','Jatin'],
      "Age": [None, 45, 34, 40,99,78],
      "City": [None, 'Los Angeles', 'Chicago', 'Houston','Delhi','Mumbai'],
      "Salary": [70000, None, 60000, 90000, 66900,58900]
}
 
df = pd.DataFrame(data)
print(df)

# Fill NaN values with a specified value
# .fillma(value, inplace=True) method is used to fill NaN values with a specified value

# df.fillna(0, inplace=True)
# print("\n",df)

# Fill NaN values with the mean of the column

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print("\n",df) 
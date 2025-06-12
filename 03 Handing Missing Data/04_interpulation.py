import pandas as pd

data = data = {
      "Name": ['lilly', 'Rocky', 'Sultan', 'Micheal','Harry','Jatin'],
      "Age": [None, 45, 34, 40,99,78],
      "City": [None, 'Los Angeles', 'Chicago', 'Houston','Delhi','Mumbai'],
      "Salary": [70000, None, 60000, 90000, 66900,58900]
}
 
df = pd.DataFrame(data)
print(df)

# linear, polynomail, time 
df.interpolate(method="linear", axis=0, inplace=True)
print(df)
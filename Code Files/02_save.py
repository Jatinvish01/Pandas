import pandas as pd
import openpyxl as open

data = {
      "Name": ['John', 'Rocky', 'Sultan', 'Micheal'],
      "Age": [23, 45, 34, 29],
      "City": ['New York', 'Los Angeles', 'Chicago', 'Houston'],
      "Salary": [70000, 80000, 60000, 90000]
}

df = pd.DataFrame(data)
print(df)

# Save the DataFrame to a CSV file

df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
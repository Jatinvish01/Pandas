import pandas as pd


# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

data = {
      "Name": ['John', 'Rocky', 'Sultan', 'Micheal'],
      "Age": [23, 45, 34, 29],
      "City": ['New York', 'Los Angeles', 'Chicago', 'Houston'],
      "Salary": [70000, 80000, 60000, 90000]
}

df = pd.DataFrame(data)

print("Displaying the info of the data set: ")
print(df.info())
import pandas as pd

data = {
      "Time": [1,2,3,4,5,6],
      "Value": [10, None, 30,40, None, 60]
}

df = pd.DataFrame(data)
print("Before Interpolation:\n",df)

df["Value"] = df["Value"].interpolate(method="linear")
print("\nAfter Interpolation:\n",df)


'''
When use interpolate() method
1- timer series data
2- numeric data with trends
3- avoid dropping rows
4- charaacteristics values ke saath nhi kr skte h
'''
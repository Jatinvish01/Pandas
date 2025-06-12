import pandas as pd

# pd.merge(df1, df2 , on="column_name", how="type of join")

df_customer = pd.DataFrame({
      "CustomerID": [1, 2, 3, 4],
      "Name": ["Ramesh", "Suresh", "Mahesh", "Rajesh"]
})

df_orders = pd.DataFrame({
      "CustomerID": [1, 2, 4, 5],
      "Order Amount": [456,256,854,236]
})

# Mergeing the two dataframes on CustomerID
df_merged = pd.merge(df_customer, df_orders, on="CustomerID", how="inner")
print(df_merged)

df_merged = pd.merge(df_customer, df_orders, on="CustomerID", how="outer")
print("\n Outer joining\n", df_merged) # Value match nahi hoge toh use NaN se fill karega

df_merged = pd.merge(df_customer, df_orders, on="CustomerID", how="left")
print("\n Left joining\n", df_merged) # Left side ki value match nahi hui toh use NaN se fill karega

df_merged = pd.merge(df_customer, df_orders, on="CustomerID", how="right")
print("\n Right joining\n", df_merged) # Right side ki value match nahi hui toh use NaN se fill karega


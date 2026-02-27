import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dubai_real_estate.csv")

print("First 5 rows:")
print(df.head())

print("\nAverage price by location:")
print(df.groupby("location")["price"].mean())

df["price_per_sqft"] = df["price"] / df["sqft"]

print("\nAverage price per sqft:")
print(df.groupby("location")["price_per_sqft"].mean())

df.groupby("location")["price"].mean().plot(kind="bar")
plt.title("Average Property Price by Location")
plt.xticks(rotation=45)
plt.show()

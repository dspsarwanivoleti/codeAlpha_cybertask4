import pandas as pd

data = pd.read_csv("attack_log.csv")

print("Columns found:")
print(data.columns)

print("\nData:")
print(data.head())
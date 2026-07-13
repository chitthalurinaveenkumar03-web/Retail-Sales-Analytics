import pandas as pd

# Read CSV
df = pd.read_csv("data/customers.csv")

print("========== ORIGINAL DATA ==========")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing age
df = df.dropna(subset=["age"])

# Keep only valid ages
df = df[df["age"] >= 0]

print("\n========== CLEANED DATA ==========")
print(df)
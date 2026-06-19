import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

print("\nPayment type counts:")
print(df['payment_type'].value_counts())

print("\nPassenger count distribution:")
print(df['passenger_count'].value_counts())

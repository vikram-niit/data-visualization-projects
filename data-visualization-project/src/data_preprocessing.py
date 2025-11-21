import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")

df.dropna(inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.to_csv("data/processed/cleaned_dataset.csv", index=False)

print("Preprocessing complete!")

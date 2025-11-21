import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_dataset.csv")

sns.lineplot(x="date", y="value", data=df)
plt.title("Value Over Time")
plt.savefig("reports/figures/value_over_time.png")

print("Visualization saved!")

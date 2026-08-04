import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")

plt.figure(figsize=(8,5))

plt.bar(df["Query"], df["Average (ms)"])

plt.title("Average Query Latency")

plt.ylabel("Milliseconds")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("charts/average_latency.png")

print("Chart created successfully.")
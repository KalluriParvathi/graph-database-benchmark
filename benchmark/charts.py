import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

# ----------------------------
# Chart 1: Average Latency
# ----------------------------
results = pd.read_csv("results/results.csv")

plt.figure(figsize=(8, 5))
plt.bar(results["Query"], results["Average (ms)"])
plt.title("Average Query Latency")
plt.ylabel("Milliseconds")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/average_latency.png")
plt.close()

# ----------------------------
# Chart 2: Database Comparison
# ----------------------------
comparison = pd.read_csv("results/comparison.csv")

pivot = comparison.pivot(
    index="Query",
    columns="Database",
    values="Average (ms)"
)

pivot.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("CognoDB vs Neo4j Aura")
plt.ylabel("Average Latency (ms)")
plt.xticks(rotation=20)
plt.legend(title="Database")
plt.tight_layout()
plt.savefig("charts/comparison.png")
plt.close()

print("Charts created successfully.")
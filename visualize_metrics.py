import pandas as pd
import matplotlib.pyplot as plt

# Load metrics data
df = pd.read_csv("metrics.csv")
if df.empty:
    print("No data found in metrics.csv — run some deployments first!")
    exit()

# Parse timestamps
df["deploy_timestamp"] = pd.to_datetime(df["deploy_timestamp"])
df["week"] = df["deploy_timestamp"].dt.isocalendar().week

# Group by week
weekly_counts = df.groupby("week").size()

# Plot Deployment Frequency
plt.figure(figsize=(7,4))
plt.plot(weekly_counts.index, weekly_counts.values, marker='o', color='blue')
plt.title("Deployment Frequency per Week")
plt.xlabel("Week Number")
plt.ylabel("Number of Deployments")
plt.grid(True)
plt.tight_layout()
plt.savefig("deployment_frequency_chart.png")
plt.show()

print("✅ Graph saved as deployment_frequency_chart.png")

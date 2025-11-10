import pandas as pd
from datetime import datetime

def parse_ts(s):
    try:
        return pd.to_datetime(s, utc=True)
    except Exception:
        return pd.NaT

df = pd.read_csv('metrics.csv')
if df.empty:
    print("metrics.csv is empty. Push a few commits to generate data.")
    raise SystemExit(0)

# Parse timestamps
df['commit_timestamp'] = df['commit_timestamp'].apply(parse_ts)
df['deploy_timestamp'] = df['deploy_timestamp'].apply(parse_ts)

# Sort by deploy time
df = df.sort_values('deploy_timestamp').reset_index(drop=True)

# Deployment Frequency (per week, average over observed weeks)
df['week'] = df['deploy_timestamp'].dt.isocalendar().week
deploys_per_week = df.groupby('week').size()
deployment_frequency = deploys_per_week.mean()

# Lead Time for Changes = deploy_ts - commit_ts (minutes)
lead_times = (df['deploy_timestamp'] - df['commit_timestamp']).dt.total_seconds() / 60.0
lead_time_avg = lead_times.mean()

# Change Failure Rate = failed / total
total_deploys = len(df)
failed_deploys = (df['status'] == 'failed').sum()
cfr = (failed_deploys / total_deploys) * 100.0

# MTTR: for each failed deploy, find next succeeding successful deploy and compute delta
mttr_list = []
for i, row in df.iterrows():
    if row['status'] != 'failed':
        continue
    # find next success after this index
    after = df.iloc[i+1:]
    next_success = after[after['status'] == 'success']
    if not next_success.empty:
        recover_time = (next_success.iloc[0]['deploy_timestamp'] - row['deploy_timestamp']).total_seconds() / 60.0
        if recover_time >= 0:
            mttr_list.append(recover_time)

mttr = sum(mttr_list)/len(mttr_list) if mttr_list else 0.0

report = [
    "=== DORA METRICS REPORT ===",
    f"Deployment Frequency (avg/week): {deployment_frequency:.2f}",
    f"Lead Time for Changes (avg minutes): {lead_time_avg:.2f}",
    f"Change Failure Rate: {cfr:.2f}%",
    f"Mean Time To Recovery (minutes): {mttr:.2f}",
    "",
    "Observations:",
    f"- Total deployments observed: {total_deploys}",
    f"- Failures observed: {failed_deploys}",
]

print("\n".join(report))

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("Saved report to report.txt")

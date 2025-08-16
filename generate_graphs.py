import json
import os
import matplotlib.pyplot as plt

output_dir = "outputs"

# Load data
with open(os.path.join(output_dir, "traffic_data.json")) as f:
    lane_counts = json.load(f)

# Generate vehicle count graph
plt.figure(figsize=(8, 5))
plt.bar(lane_counts.keys(), lane_counts.values(), color='green')
plt.xlabel("Lane")
plt.ylabel("Vehicle Count")
plt.title("Total Vehicles per Lane")
plt.savefig(os.path.join(output_dir, "vehicle_count.png"))
print("Vehicle count graph saved.")

# Generate anomaly graph (Mock data)
anomaly_counts = {lane: count * 0.1 for lane, count in lane_counts.items()}  # Mock anomalies

plt.figure(figsize=(8, 5))
plt.bar(anomaly_counts.keys(), anomaly_counts.values(), color='red')
plt.xlabel("Lane")
plt.ylabel("Anomalies")
plt.title("Traffic Anomalies per Lane")
plt.savefig(os.path.join(output_dir, "anomalies.png"))
print("Anomaly graph saved.")

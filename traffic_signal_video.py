import json
import time
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')


output_dir = "outputs"

# Load traffic data
with open(os.path.join(output_dir, "traffic_data.json")) as f:
    lane_counts = json.load(f)

# Decide signal order (more traffic → longer green time)
sorted_lanes = sorted(lane_counts.items(), key=lambda x: x[1], reverse=True)

print("🚦 Simulating Traffic Signals...")
for lane, count in sorted_lanes:
    print(f"🟢 {lane} gets green light for {count} seconds")
    time.sleep(min(count, 30))  # Simulate green time
    print(f"🔴 {lane} red light\n")

print("✅ Traffic signal simulation completed.")

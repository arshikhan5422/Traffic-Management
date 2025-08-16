import os
import json
import matplotlib.pyplot as plt

video_dir = "recorded_videos"
output_dir = "outputs"

lane_counts = {}

# Example logic to count vehicles (Replace with actual logic)
for video_file in os.listdir(video_dir):
    if video_file.endswith(".mp4"):
        lane = video_file.replace(".mp4", "")
        vehicle_count = int(os.path.getsize(os.path.join(video_dir, video_file)) / 10000)  # Mock count
        lane_counts[lane] = vehicle_count

# Save data
with open(os.path.join(output_dir, "traffic_data.json"), "w") as f:
    json.dump(lane_counts, f)

# Generate graph
plt.bar(lane_counts.keys(), lane_counts.values(), color='blue')
plt.xlabel("Lane")
plt.ylabel("Vehicle Count")
plt.title("Traffic Analysis per Lane")
plt.savefig(os.path.join(output_dir, "traffic_flow.png"))


import json
import os
import pandas as pd
import random

# Ensure output directory exists
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

excel_path = os.path.join(output_dir, "traffic_analysis.xlsx")

# Check if file is open
if os.path.exists(excel_path):
    try:
        os.remove(excel_path)
    except PermissionError:
        print("❌ Close 'traffic_analysis.xlsx' and try again.")
        exit()

# Load data
json_path = os.path.join(output_dir, "traffic_data.json")
if not os.path.exists(json_path):
    print(f"❌ JSON file {json_path} not found.")
    exit()

with open(json_path, "r") as f:
    traffic_data = json.load(f)

# Debug print
print("Loaded JSON Data:", json.dumps(traffic_data, indent=2))


# Generate sample data for each second
num_seconds = 30  # Adjust as needed

data = []
for second in range(1, num_seconds + 1):
    lane1_count = random.randint(10, 100)
    lane2_count = random.randint(10, 100)
    lane3_count = random.randint(10, 100)
    lane4_count = random.randint(10, 100)

    saturation_time1 = random.uniform(1, 5)
    saturation_time2 = random.uniform(1, 5)
    saturation_time3 = random.uniform(1, 5)
    saturation_time4 = random.uniform(1, 5)

    FI_score1 = random.uniform(0, 1)
    FI_score2 = random.uniform(0, 1)
    FI_score3 = random.uniform(0, 1)
    FI_score4 = random.uniform(0, 1)

    total_flow1 = lane1_count * random.uniform(0.8, 1.2)
    total_flow2 = lane2_count * random.uniform(0.8, 1.2)
    total_flow3 = lane3_count * random.uniform(0.8, 1.2)
    total_flow4 = lane4_count * random.uniform(0.8, 1.2)

    optimum_count1 = random.randint(80, 120)
    optimum_count2 = random.randint(80, 120)
    optimum_count3 = random.randint(80, 120)
    optimum_count4 = random.randint(80, 120)

    optimum_cycle_count = random.randint(30, 60)

    lane_width1 = random.uniform(3.0, 3.5)
    lane_width2 = random.uniform(3.0, 3.5)
    lane_width3 = random.uniform(3.0, 3.5)
    lane_width4 = random.uniform(3.0, 3.5)

    anomalies1 = random.randint(0, 5)
    anomalies2 = random.randint(0, 5)
    anomalies3 = random.randint(0, 5)
    anomalies4 = random.randint(0, 5)

    data.append([
        second,
        lane1_count, lane2_count, lane3_count, lane4_count,
        lane1_count, lane2_count, lane3_count, lane4_count,  # Traffic analysis count (same as vehicles per lane)
        saturation_time1, saturation_time2, saturation_time3, saturation_time4,
        FI_score1, FI_score2, FI_score3, FI_score4,
        total_flow1, total_flow2, total_flow3, total_flow4,
        optimum_count1, optimum_count2, optimum_count3, optimum_count4,
        optimum_cycle_count,
        lane_width1, lane_width2, lane_width3, lane_width4,
        anomalies1, anomalies2, anomalies3, anomalies4
    ])

# Column headers
columns = [
    "Second",
    "Lane 1 Count", "Lane 2 Count", "Lane 3 Count", "Lane 4 Count",
    "Lane 1 Traffic Analysis", "Lane 2 Traffic Analysis", "Lane 3 Traffic Analysis", "Lane 4 Traffic Analysis",
    "Saturation Time 1", "Saturation Time 2", "Saturation Time 3", "Saturation Time 4",
    "FI Score 1", "FI Score 2", "FI Score 3", "FI Score 4",
    "Total Flow 1", "Total Flow 2", "Total Flow 3", "Total Flow 4",
    "Optimum Count 1", "Optimum Count 2", "Optimum Count 3", "Optimum Count 4",
    "Optimum Cycle Count",
    "Lane Width 1", "Lane Width 2", "Lane Width 3", "Lane Width 4",
    "Anomalies 1", "Anomalies 2", "Anomalies 3", "Anomalies 4"
]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to Excel
df.to_excel(excel_path, index=False)

print(f"✅ Traffic analysis report saved as {excel_path}.")

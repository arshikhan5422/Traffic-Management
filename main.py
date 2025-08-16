import cv2
import time
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# 📂 Ensure necessary directories exist
os.makedirs("recorded_videos", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# 🚦 Lanes for which traffic will be recorded
lanes = ["lane1", "lane2", "lane3", "lane4"]

# Configurable parameters
RECORD_TIME = int(os.getenv("RECORD_TIME", 30))  # Default: 30 seconds
CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 0))  # Default: Built-in webcam

def record_traffic_videos():
    """Records a traffic video for each lane using the system camera."""
    
    for lane in lanes:
        cap = cv2.VideoCapture(CAMERA_INDEX)  # Open the camera
        
        if not cap.isOpened():
            print(f"❌ Error: Could not access the camera for {lane}.")
            continue  # Move to the next lane
        
        filename = f"recorded_videos/{lane}.mp4"
        print(f"🎥 Recording {lane} for {RECORD_TIME} seconds...")

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

        start_time = time.time()
        while time.time() - start_time < RECORD_TIME:
            ret, frame = cap.read()
            if not ret:
                print(f"❌ Error: Could not read frame for {lane}.")
                break
            out.write(frame)
            cv2.imshow("Recording...", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit early
                break

        out.release()
        cap.release()
        print(f"✅ {lane} video saved: {filename}\n")

    cv2.destroyAllWindows()
    return True

def run_script(script_name):
    """Runs a Python script and handles errors."""
    print(f"🚀 Running {script_name}...")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {script_name} executed successfully!\n")
        return True
    else:
        print(f"❌ Error in {script_name}:")
        print(result.stderr)
        print(f"Output: {result.stdout}\n")
        return False

def run_traffic_analysis():
    """Runs the traffic management pipeline with recorded videos."""
    scripts = [ 
        "scripts/detect.py",
        "scripts/analyze.py", 
        "scripts/generate_excel.py",
        "scripts/generate_graphs.py",
        "scripts/simulate_traffic.py",
        "scripts/traffic_signal_video.py"
    ]

    for script in scripts:
        if not run_script(script):
            print(f"⚠️ Stopping execution due to failure in {script}.")
            return False  # Stop execution if any script fails
    
    return True

if __name__ == "__main__":
    print("🚦 Starting Automated Traffic Analysis System...\n")

    if not record_traffic_videos():
        print("❌ Traffic video recording failed. Exiting.")
    elif not run_traffic_analysis():
        print("⚠️ Some analysis scripts failed. Check logs.")
    else:
        print("🎯 All tasks completed successfully!")

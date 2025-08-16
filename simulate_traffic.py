import cv2
import numpy as np
import time

# Video settings
width, height = 400, 600
fps = 1  # One frame per second (slow transition for visibility)
duration = 9  # Total duration of the video in seconds
frames = duration * fps

# Traffic light colors
colors = [(0, 255, 0), (0, 165, 255), (0, 0, 255)]  # Green, Orange, Red
labels = ["GO", "WAIT", "STOP"]

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('traffic_signal_simulation.mp4', fourcc, fps, (width, height))

for i in range(frames):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(img, (150, 100), (250, 500), (50, 50, 50), -1)  # Traffic light box

    color_idx = (i // 3) % 3  # Cycle through colors every 3 seconds
    for j in range(3):
        color = colors[j] if j == color_idx else (30, 30, 30)  # Dim inactive lights
        center = (200, 200 + j * 120)
        radius = 40
        cv2.circle(img, center, radius, color, -1)

    # Display text label
    cv2.putText(img, labels[color_idx], (160, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    out.write(img)
    time.sleep(1)  # Simulate real-time change

out.release()
cv2.destroyAllWindows()

print("Traffic signal simulation video generated: traffic_signal_simulation.mp4")

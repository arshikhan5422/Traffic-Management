import os
import torch
import cv2
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
yolov5_path = os.path.join(os.path.dirname(__file__), '../yolov5')
sys.path.insert(0, yolov5_path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'venv', 'Lib', 'site-packages')))

from yolov5.models.common import DetectMultiBackend
from yolov5.utils.torch_utils import select_device
from yolov5.utils.general import non_max_suppression, scale_boxes as scale_coords
import numpy as np

# Paths
video_dir = "recorded_videos"
output_dir = "outputs"
model_weights = "yolov5s.pt"  # Ensure you have YOLOv5 trained weights

os.makedirs(output_dir, exist_ok=True)

# Load YOLOv5 model
device = select_device('')
model = DetectMultiBackend(model_weights, device=device)
stride, names, pt = model.stride, model.names, model.pt

def detect_objects(video_path):
    cap = cv2.VideoCapture(video_path)
    output_video_path = os.path.join(output_dir, os.path.basename(video_path))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        img = torch.from_numpy(frame).float().to(device) / 255.0
        img = img.permute(2, 0, 1).unsqueeze(0)  # Convert to model format

        # YOLO Inference
        pred = model(img, augment=False)
        pred = non_max_suppression(pred, 0.25, 0.45, None, False)

        # Draw detections
        for det in pred:
            if len(det):
                for *xyxy, conf, cls in det:
                    label = f"{names[int(cls)]} {conf:.2f}"
                    cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        out.write(frame)
        cv2.imshow("Detection", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"✅ Processed {video_path} and saved output to {output_video_path}")

# Run detection on all recorded videos
for video_file in os.listdir(video_dir):
    if video_file.endswith(".mp4"):
        detect_objects(os.path.join(video_dir, video_file))


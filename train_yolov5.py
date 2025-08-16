# train_yolov5.py
import sys
import os
import subprocess

# Insert the YOLOv5 directory into the Python path
yolov5_path = os.path.join(os.path.dirname(__file__), '../yolov5')  # Adjust this path if needed
sys.path.insert(0, yolov5_path)

def train_yolov5():
    """
    Function to train YOLOv5 model using the 'train.py' script from the YOLOv5 repository.
    """
    train_script = os.path.join(yolov5_path, 'train.py')  # Path to YOLOv5's train.py script
    data_config = './datasets/yolo/traffic.yaml'  # Path to your dataset config file
    weights = ''  # Use empty string for training from scratch or specify path to pretrained weights
    
    # Subprocess to run the YOLOv5 train script
    subprocess.run([
        sys.executable,  # Use the current Python interpreter
        train_script,  # YOLOv5's train.py script
        '--data', data_config,  # Dataset configuration
        '--weights', weights,  # Initial weights
        '--epochs', '50',  # Number of training epochs
        '--img-size', '640',  # Image size
        '--batch-size', '16',  # Batch size
        '--project', 'results',  # Output project directory
        '--name', 'yolov5_traffic',  # Name for the training run
        '--exist-ok'  # Allow overwriting of results
    ])

if __name__ == '__main__':
    train_yolov5()

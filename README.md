# 🚦 Smart Traffic Management through Anomaly Detection and Load Balancing  

This project presents an intelligent traffic management system designed to **optimize urban traffic flow** by detecting anomalies in real-time and efficiently distributing vehicle load across available routes. The system leverages **YOLOv5** for real-time object detection and **MobileNet** for lightweight classification, enabling high accuracy with reduced latency.  

---

## 📌 Features
- **Real-Time Vehicle Detection** using YOLOv5  
- **Anomaly Detection** (accidents, congestion, unusual patterns)  
- **Load Balancing** by rerouting vehicles to alternate roads  
- **Lightweight Model Integration** with MobileNet for efficiency  
- **Scalability for Smart Cities** – adaptable to IoT and VANETs  
- **Improved Emergency Response** with faster detection of critical events  

---

## 🏗️ System Architecture
1. **Input** – Real-time video feed or traffic camera footage  
2. **Detection** – YOLOv5 detects vehicles and anomalies  
3. **Classification** – MobileNet classifies detected anomalies  
4. **Load Balancing** – Intelligent routing distributes traffic flow  
5. **Output** – Real-time traffic insights, alerts, and optimized routes  

---

## ⚙️ Tech Stack
- **Languages:** Python  
- **Deep Learning Frameworks:** PyTorch, TensorFlow/Keras  
- **Models:** YOLOv5, MobileNet  
- **Computer Vision:** OpenCV  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Streamlit / Flask (optional)  

---

## 📊 Performance Metrics
- **Accuracy of Vehicle Detection:** XX% (replace with your result)  
- **Latency for Real-Time Processing:** XX ms/frame  
- **Response Time Improvement for Emergency Vehicles:** XX%  

---

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/USERNAME/Smart-Traffic-Management.git
cd Smart-Traffic-Management

---

### 2. Create Environment & Install Dependencies
```bash
pip install -r requirements.txt

---

### 3. Training the Model
```bash
python yolov5/train.py --img 640 --batch 16 --epochs 50 --data traffic.yaml --weights yolov5s.pt
---

### 4. Run Detection
```bash
python yolov5/detect.py --weights runs/train/exp/weights/best.pt --img 640 --source data/test_images
---

### 5.Integrating MobileNet
```bash
python src/mobilenet_classifier.py

---

## 🔮 Future Enhancements
Integration with real-world IoT/VANET systems

Cloud-based scalable deployment for city-wide monitoring

Reinforcement learning for dynamic route optimization

Dashboard for live visualization of traffic anomalies






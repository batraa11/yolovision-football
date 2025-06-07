# Football Player Detection using YOLOv11l

This project demonstrates a custom-trained YOLOv11l model for football player detection in match footage. The model was trained locally using a dataset annotated and exported from Roboflow. It detects players in video frames and can be extended for speed tracking, tactical overlays, and other analytics.

## 🏗️ What I Did

- Collected and annotated football match images using Roboflow.  
- Exported the dataset in **YOLOv5-compatible format** (i.e., `images/`, `labels/`, plus a `data.yaml` manifest), fully supported by Ultralytics YOLOv8/YOLOv11.  
- Trained the YOLOv11l model locally via Ultralytics’ CLI.  
- Evaluated detection performance on sample videos and visualized results.

## 🛠️ Replication Steps

1. **Clone Ultralytics YOLO**  
   git clone https://github.com/ultralytics/ultralytics.git  
   cd ultralytics  
   pip install -e .

2. **Prepare your dataset**  
   - Annotate on Roboflow, export as `YOLOv5 PyTorch`.  
   - Organize in `datasets/football/` as:  
     
       datasets/football/  
       ├── images/  
       │   ├── train/  
       │   └── val/  
       ├── labels/  
       │   ├── train/  
       │   └── val/  
       └── data.yaml  
     
   - In `data.yaml`, set `path`, `train`, `val`, and `names`.

3. **Train the model**  
   yolo task=detect mode=train \
     model=yolov11l.pt \
     data=datasets/football/data.yaml \
     epochs=80 \
     imgsz=640

4. **Run inference**  
   yolo task=detect mode=predict \
     model=runs/detect/train/weights/best.pt \
     source=path/to/your/video.mp4

5. **View outputs**  
   Results will be saved under `runs/detect/predict/`.

## 🧠 Model Info

- **Architecture:** YOLOv11l (Ultralytics)  
- **Dataset:** Custom football player annotations from Roboflow  
- **Training:** Local GPU recommended  

## 🚀 Improvements Over Default YOLOv11

- Significantly improved player detection accuracy, especially in crowded scenes and motion-heavy frames  
- Vastly enhanced ball detection performance, even during fast movement and partial occlusion  
- Improved ability to distinguish referees from players using spatial awareness (e.g., referees outside pitch boundaries are no longer misclassified as players)


## 📜 License

This project is licensed under the MIT License. See `LICENSE`.

## ✍️ Author

**Aarohan Batra**

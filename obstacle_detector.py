from ultralytics import YOLO

# Load a pre-trained YOLOv8 model (first time only, it will download)
model = YOLO('yolov8n.pt')
# you can use 'yolov8s.pt' or 'yolov8m.pt' for better accuracy


def detect_obstacles(image_path):
    results = model(image_path)
    detections = []

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])
            if conf > 0.5:
                detections.append({
                    "label": label,
                    "confidence": round(conf, 2),
                    "box": box.xyxy[0].tolist()  # [x1, y1, x2, y2]
                })

    return {
        "obstacles_detected": len(detections),
        "detections": detections
    }

from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

def detect_objects(frame):
    results = model.track(frame, persist=True)[0]

    objects = []

    for box in results.boxes:
        cls = int(box.cls[0])
        name = model.names[cls]

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        area = (x2 - x1) * (y2 - y1)

        # رسم Box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, name, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        objects.append((name, area, x1, x2))

    return objects, frame











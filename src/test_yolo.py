from ultralytics import YOLO

model = YOLO("yolov8n.pt")
print("YOLO loaded successfully")

from ultralytics import YOLO

model = YOLO("yolov8n.pt")
print("YOLO loaded successfully")

results = model("https://ultralytics.com/images/bus.jpg")

results[0].show()

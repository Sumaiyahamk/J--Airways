from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("frame.jpg")

for r in results:
    print(r.boxes)
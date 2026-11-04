from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("frame.jpg")

for r in results:
    annotated = r.plot()
    import cv2
    cv2.imshow("Detection", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
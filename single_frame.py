from pysimverse import Drone
import cv2

drone = Drone()
drone.connect()

frame, success = drone.get_frame()

print("Success:", success)

if success:
    cv2.imwrite("frame.jpg", frame)
    print("Saved frame.jpg")
else:
    print("No frame received")
from pysimverse import Drone
import cv2

drone = Drone()
drone.connect()

while True:
    frame = drone.get_frame()

    if frame is None:
        continue

    cv2.imshow("PySimverse Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
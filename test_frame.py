from pysimverse import Drone

drone = Drone()
drone.connect()

frame = drone.get_frame()

print(type(frame))
print(frame)
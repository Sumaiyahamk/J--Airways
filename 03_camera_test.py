from pysimverse import Drone 
import cv2          
       # Image decoding and display. 
import numpy as np  
       # Convert JPEG bytes to an array. 
import zmq          
       # ZeroMQ timeout exception. 
import time 
drone = Drone() 
drone.connect() 
socket = drone.video_socket  # PySimverse video stream (SUB socket). 
socket.setsockopt(zmq.RCVTIMEO, 3000)  # Max 3 s wait for a frame.
cv2.namedWindow("Camera check", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Camera check", 1000, 650) 
  
try: 
    drone.streamon()       # Ask simulator to start sending camera frames. 
    time.sleep(2)          # Allow stream initialization. 
  
    while True: 
        try: 
            message = socket.recv()  # Receive a JPEG message. 
        except zmq.Again:            # No frame arrived before timeout. 
            print("No video frame received") 
            break 
  
        array = np.frombuffer(message, dtype=np.uint8) 
        frame = cv2.imdecode(array, cv2.IMREAD_COLOR) 
        if frame is not None:       # Only display successfully decoded frames. 
            cv2.imshow("Camera check", frame) 
        if cv2.waitKey(1) & 0xFF == ord("q"): 
            break                  # Q ends the viewing loop. 
finally: 
    drone.streamoff()              # Disable the video stream. 
    cv2.destroyAllWindows()        # Close OpenCV windows. 
import sys
sys.path.append('/Users/User/Desktop/lessons/Frame_in_Live_Stream_Video/venv/Lib/site-packages')

import cv2

# Create an object to hold reference to camera video capturing
camera_id = 0   # to access webcam enter 0, otherwise enter an rtsp connection
vidcap = cv2.VideoCapture(camera_id)

# check if connection with camera is successfully
if vidcap.isOpened():
   # continue to display window until 'q' is pressed
    print('Accessed the camera')
# print error if the connection with camera is unsuccessful
else:
    print('Cannot open camera')

vidcap.release()
cv2.destroyAllWindows()
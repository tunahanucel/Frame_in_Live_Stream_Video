import os
import sys
sys.path.append('/Users/User/Desktop/lessons/Frame_in_Live_Stream_Video/venv/Lib/site-packages')

import cv2

from datetime import datetime
now = datetime.now()
print(now)
FREQUENCY = 5
DURATION_SECOND = 5
trigger = now.minute % FREQUENCY

if trigger == 0:
    print('Triggered')
    date = now.strftime("%m-%d-%Y")
    time = now.strftime('%H-%M-%S')
    parent_dir = "/Users/User/Desktop/lessons/Frame_in_Live_Stream_Video/Frames"
    dir = date + '__' + time
    path = os.path.join(parent_dir, dir)
    os.makedirs(path)

    vidcap = cv2.VideoCapture(0)
    currentframe = 0
    frame_trigger = True
    # check if connection with camera is successfully
    if vidcap.isOpened():
        while frame_trigger:
            ret, frame = vidcap.read()  # capture a frame from live video

            cv2.imshow('Output', frame)
            filename = 'frame' + str(currentframe) + '.jpg'
            filepath = os.path.join(path, filename)
            cv2.imwrite(filepath, frame)  # store captured frame
            currentframe += 1

            end = datetime.now()
            spent_time = (end - now).seconds
            if spent_time <= DURATION_SECOND:
                pass
            else:
                frame_trigger = False
    # print error if the connection with camera is unsuccessful
    else:
        print('Cannot open camera')

    vidcap.release()
    cv2.destroyAllWindows()
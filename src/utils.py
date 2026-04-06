import cv2
import time
import os

def save_frame(frame):
    if not os.path.exists("captures"):
        os.makedirs("captures")

    filename = f"captures/frame_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
'''
python录屏
pip install opencv-python numpy pyautogui pynput
'''
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from pynput import keyboard
from datetime import datetime
import threading

fps = 30
screen_size = (640, 480)
output = datetime.now().strftime("%Y%m%d%H%M%S") + ".avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")

screenshot = pyautogui.screenshot()
screen_size = screenshot.size

out = cv2.VideoWriter(output, fourcc, fps, screen_size)
print("开始录屏...")
while True:
    # img = pyautogui.screenshot()
    img = ImageGrab.grab()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()

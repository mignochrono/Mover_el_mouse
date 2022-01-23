import pyautogui
import time

print ('starting...')
banana = 1000
while banana > 1:
    mouse=pyautogui.position()
    print('the mouse its on this place')
    print(mouse)
    banana= banana - 1
    time.sleep(1)

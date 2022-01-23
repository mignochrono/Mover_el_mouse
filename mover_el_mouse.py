import pyautogui #import pyautogui
import time #import time because if not it goes too fast

print ('starting...') #marcador de que el programa inicio bien
banana = 1000 # a variable so we can limit the time
while banana > 1: #simple while loop
    mouse=pyautogui.position() #function to find the position of the mouse on the screen
    print('the mouse its on this place')
    print(mouse)
    banana= banana - 1
    time.sleep(1)

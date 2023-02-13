import pyautogui as pag 
import random
import time

while True:
    x = random.randint(400, 700)
    y = random.randint(200, 750)
    pag.moveTo(x,y, 0.5)
    time.sleep(2)



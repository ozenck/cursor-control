import pyautogui
from random import randint
from time import sleep

size = pyautogui.size()
width=size[0]
height=size[1]
print(f"width={width}, height={height}")

while True:
    x = randint(400, width-600)
    y = randint(500, height-100)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click(x,y)
    sleep(5)

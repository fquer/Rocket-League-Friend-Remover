from time import sleep
from cv2 import exp
import pyautogui
import winsound
import os
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def remover(file):
    x, y = pyautogui.locateCenterOnScreen('images\\' + file + '.PNG', confidence = 0.9)
    pyautogui.moveTo()
    sleep(0.5)
    pyautogui.click(x, y)
    sleep(0.25)
        
os.system('cls')


while True:
    try:
        remover('friend')
        remover('remove')
        remover('accept')

    except:
        try:
            remover('friend_offline')
            remover('remove')
            remover('accept')
        except:
            pass
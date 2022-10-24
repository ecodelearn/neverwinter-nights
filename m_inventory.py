import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

## Resolution (1280 x 960) in a UltraWide Monitor with Resolution (2560 x 1080)

# Map key inventory
I = 0x17

def inventory_slots():
  #1
  pyautogui.moveTo(345, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(350, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(345, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(350, 290)
  pyautogui.mouseUp()

  # 2
  pyautogui.moveTo(310, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(350, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(310, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(350, 290)
  pyautogui.mouseUp()

  # 3
  pyautogui.moveTo(275, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(275, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(280, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(275, 290)
  pyautogui.mouseUp()

  # 4
  pyautogui.moveTo(240, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(275, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(240, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(275, 290)
  pyautogui.mouseUp()

  # 5
  pyautogui.moveTo(200, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(200, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(200, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(200, 290)
  pyautogui.mouseUp()

  # 6
  pyautogui.moveTo(165, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(165, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(175, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(175, 290)
  pyautogui.mouseUp()

  # 7
  pyautogui.moveTo(130, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(130, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(130, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(130, 290)
  pyautogui.mouseUp()

  # 8
  pyautogui.moveTo(95, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(95, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(95, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(95, 290)
  pyautogui.mouseUp()

  # 9
  pyautogui.moveTo(60, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(60, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(60, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(60, 290)
  pyautogui.mouseUp()

  # 10
  pyautogui.moveTo(25, 360)
  pyautogui.mouseDown()
  pyautogui.moveTo(25, 290)
  pyautogui.mouseUp()
  time.sleep(0.3)
  pyautogui.moveTo(25, 430)
  pyautogui.mouseDown()
  pyautogui.moveTo(25, 290)
  pyautogui.mouseUp()


#select GameWindow
pyautogui.moveTo(560, 25)
pyautogui.click()
time.sleep(0.2)

PressKey(I) # Open Inventory
ReleaseKey(I)
time.sleep(0.2)

# move 2nd session of inventory
pyautogui.moveTo(380, 330)
pyautogui.click()

## Inicia Move ##

inventory_slots()

# move 3rd session of inventory
pyautogui.moveTo(375, 360)
pyautogui.mouseDown()
pyautogui.mouseUp()

inventory_slots()

# move 4th session of inventory
pyautogui.moveTo(375, 400)
pyautogui.mouseDown()
pyautogui.mouseUp()

inventory_slots()

# move 5th session of inventory
pyautogui.moveTo(375, 435)
pyautogui.mouseDown()
pyautogui.mouseUp()

inventory_slots()

# move 6th session of inventory
pyautogui.moveTo(375, 475)
pyautogui.mouseDown()
pyautogui.mouseUp()

inventory_slots()
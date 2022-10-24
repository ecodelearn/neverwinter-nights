import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

# Numeric Keys

n0 = 0x0B
n1 = 0x02
n2 = 0x03
n3 = 0x04
n4 = 0x05
n5 = 0x06
n6 = 0x07
n7 = 0x08
n8 = 0x09
n9 = 0x0A

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

pyautogui.moveTo(44, 78)
pyautogui.click()
time.sleep(0.2)

count = 0
while (count < 34):   
  count = count + 1
  PressKey(n1) # Select poiton options Percy Benzor
  ReleaseKey(n1)
  time.sleep(4.5)
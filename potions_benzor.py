import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

# Define variaveis zeradas.

bark = int(input('Quantas pocoes de Barkskin ? '))
cure = int(input('Quantas pocoes de cura ? '))


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

pyautogui.moveTo(51, 86)
pyautogui.click()
time.sleep(0.2)

PressKey(n2) # Select poiton options Percy Benzor
ReleaseKey(n2)

time.sleep(0.3)

# Compra Barkskin
count = 0
while (count < bark):   
  count = count + 1
  pyautogui.moveTo(103, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(567, 563)
  pyautogui.click()
  time.sleep(0.2)

# Compra Cure Serious Wounds

count = 0
while (count < cure):   
  count = count + 1
  pyautogui.moveTo(68, 465)
  time.sleep(0.2)
  pyautogui.click()
  
  pyautogui.moveTo(567, 563)
  time.sleep(0.2)
  pyautogui.click()
  

  
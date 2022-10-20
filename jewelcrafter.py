import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

pyautogui.FAILSAFE = True
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

x = int(0)

x = int(input("Quantas pedras vc quer comprar malachitas e ametistas ? : "))


pyautogui.moveTo(47, 96, duration = 0.5)
pyautogui.click()
PressKey(n3) # Select poiton options Percy Benzor
ReleaseKey(n3)
pyautogui.moveTo(341, 86, duration = 0.5)
pyautogui.click()
time.sleep(1)


count = 0
while (count < x):   
  count = count + 1

  pyautogui.moveTo(31, 470, duration = 0.2)
  pyautogui.click()

  pyautogui.moveTo(539, 558, duration = 0.2)
  pyautogui.click() 

  pyautogui.moveTo(71, 470, duration = 0.2)
  pyautogui.click()

  pyautogui.moveTo(539, 558, duration = 0.2)
  pyautogui.click() 
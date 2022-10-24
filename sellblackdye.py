import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

# Define variaveis zeradas.

quantidade = int(input('Quantos BlackDyes Quer Vender ? '))



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

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

pyautogui.moveTo(51, 86)
pyautogui.click()
time.sleep(0.2)

PressKey(n2) # Select BlackDye Option
ReleaseKey(n2)
time.sleep(1)
PressKey(n7) # Select BlackDye Option
ReleaseKey(n7)
time.sleep(1)
count = 0
while (count < 11):
  time.sleep(1)   
  count = count + 1
  PressKey(n8) # Select BlackDye Option
  ReleaseKey(n8)

time.sleep(1)
count = 0
while (count < quantidade):
  time.sleep(1)   
  count = count + 1
  PressKey(n5) # Select BlackDye Option
  ReleaseKey(n5)
  time.sleep(0.5)
  PressKey(n1) # Select BlackDye Option
  ReleaseKey(n1)

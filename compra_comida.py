import pyautogui
import time

pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.3

pyautogui.moveTo(36, 60, duration = 0.5)
pyautogui.click()
pyautogui.typewrite(['1'], interval=0.5)
pyautogui.moveTo(314, 80, duration = 0.5)
pyautogui.click()
time.sleep(0.5)

count = 0
while (count < 25):   
  count = count + 1
  #Chila
  # pyautogui.moveTo(203, 439, duration = 0.2)
  #Gnome Food Merchant
  pyautogui.moveTo(159, 439, duration = 0.2)
  pyautogui.click()
  pyautogui.moveTo(582, 569, duration = 0.2)
  pyautogui.click() 


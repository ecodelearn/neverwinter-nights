import pyautogui
import time

pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.3

#NWN DIAMOND
# pyautogui.moveTo(36, 60, duration = 0.5)
# pyautogui.click()
# pyautogui.typewrite(['1'], interval=0.5)
# pyautogui.moveTo(314, 80, duration = 0.5)
# pyautogui.click()
# time.sleep(0.5)

pyautogui.moveTo(50, 160, duration = 0.5)
pyautogui.click()
pyautogui.typewrite(['1'], interval=0.5)
pyautogui.moveTo(336, 69, duration = 0.5)
pyautogui.click()
time.sleep(1)

count = 0
while (count < 30):   
  count = count + 1
  #Chila BENZOR
  pyautogui.moveTo(220, 472, duration = 0.2)
  pyautogui.click()

  #Gnome Food Merchant GNOME VILLAGE
  # pyautogui.moveTo(183, 473, duration = 0.2)
  # pyautogui.click()
  pyautogui.moveTo(596, 548, duration = 0.2)
  pyautogui.click() 


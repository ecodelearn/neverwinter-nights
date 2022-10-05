import pyautogui
import time

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

pyautogui.moveTo(1246, 895)
pyautogui.click()
pyautogui.typewrite(['r'])
time.sleep(20)

pyautogui.hotkey('shift', 'f2')  

pyautogui.hotkey('shift', 'f1')  
pyautogui.click()
pyautogui.hotkey('ctrl', 'f3')  
pyautogui.click()
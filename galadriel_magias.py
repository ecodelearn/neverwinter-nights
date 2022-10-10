import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

# Map of Direc Input Keyboard

ctrl = 0x1D
shift = 0x2A

f1 = 0x3B
f2 = 0x3C
f3 = 0x3D
f4 = 0x3E
f5 = 0x3F
f6 = 0x40
f7 = 0x41
f8 = 0x42
f9 = 0x43
f10 = 0x44
f11 = 0x57
f12 = 0x58

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True


pyautogui.moveTo(1249, 116)
pyautogui.doubleClick()


# All Shift Buffs Setup

PressKey(shift)

time.sleep(0.3)
PressKey(f12)
ReleaseKey(f12)
time.sleep(0.3)
# PressKey(shift)
time.sleep(0.3)
PressKey(f11)
ReleaseKey(f11)
time.sleep(0.3)
# PressKey(shift)
time.sleep(0.3)
PressKey(f10)
ReleaseKey(f10)
time.sleep(0.3)
# PressKey(shift)
time.sleep(0.3)
PressKey(f9)
ReleaseKey(f9)
pyautogui.click()
time.sleep(0.3)
PressKey(f8)
ReleaseKey(f8)
pyautogui.moveTo(1225, 272) 
time.sleep(0.3)
pyautogui.click()
time.sleep(0.3)
PressKey(f6)
ReleaseKey(f6)
pyautogui.click()
time.sleep(0.3)
PressKey(f5)
ReleaseKey(f5)
pyautogui.click()
time.sleep(0.3)
ReleaseKey(shift)

time.sleep(0.3)

PressKey(ctrl)
PressKey(f11)
ReleaseKey(f11)
pyautogui.click()
ReleaseKey(ctrl)

PressKey(shift)
pyautogui.moveTo(1225, 80)
time.sleep(0.3)
PressKey(f6)
ReleaseKey(f6)
pyautogui.click()
time.sleep(0.3)
PressKey(f5)
ReleaseKey(f5)
pyautogui.click()
time.sleep(0.3)
PressKey(f4)
ReleaseKey(f4)
pyautogui.click()
time.sleep(0.3)
PressKey(f3)
ReleaseKey(f3)
# pyautogui.click()
time.sleep(0.3)
PressKey(f2)
ReleaseKey(f2)
time.sleep(0.3)

ReleaseKey(shift)

# All Control Buffs Setup
PressKey(ctrl)

time.sleep(0.3)
PressKey(f10)
ReleaseKey(f10)
pyautogui.click()
time.sleep(0.3)
PressKey(f9)
ReleaseKey(f9)
pyautogui.click()
time.sleep(0.3)
PressKey(f8)
ReleaseKey(f8)
time.sleep(0.3)
PressKey(f7)
ReleaseKey(f7)
time.sleep(0.3)
PressKey(f3)
ReleaseKey(f3)
time.sleep(0.3)
pyautogui.click()

ReleaseKey(ctrl)

# End of Script!


# pyautogui.hotkey('shift', 'f12')
# time.sleep(4)
# pyautogui.click
# pyautogui.hotkey('shift', 'f12')
# # pyautogui.press('f10')
# pyautogui.leftClick()
# pyautogui.keyUp('shift')
#time.sleep(1)
# # pyautogui.click()
# pyautogui.hotkey('shift', 'f11')  
# # pyautogui.click()
# pyautogui.hotkey('shift', 'f10')  
# # pyautogui.click()
# pyautogui.hotkey('shift', 'f9')  
# pyautogui.click()
# pyautogui.hotkey('shift', 'f8')
# pyautogui.moveTo(1225, 272)  
# time.sleep(0.3)
# pyautogui.click()
# pyautogui.hotkey('shift', 'f5')
# pyautogui.click()
# pyautogui.moveTo(1225, 80)
# time.sleep(0.3)
# pyautogui.hotkey('shift', 'f5')
# pyautogui.click()
# pyautogui.hotkey('shift', 'f4')
# pyautogui.click()
# pyautogui.hotkey('shift', 'f3')
# # pyautogui.click()
# pyautogui.hotkey('shift', 'f2')

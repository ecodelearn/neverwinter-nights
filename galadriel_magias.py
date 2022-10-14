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
pyautogui.click()
time.sleep(0.5)
pyautogui.click()


# All Shift Buffs Setup

PressKey(shift)

time.sleep(0.5)
PressKey(f12) # summons familiar
ReleaseKey(f12)
time.sleep(0.5)
# PressKey(shift)
time.sleep(0.5)
PressKey(f11) # uses Rod of the Ghost
ReleaseKey(f11)
time.sleep(0.5)
# PressKey(shift)
time.sleep(0.5)
PressKey(f10) # casting Energy Buffer
ReleaseKey(f10)
time.sleep(0.5)
# PressKey(shift)
time.sleep(0.5)
PressKey(f9) # casting Improved Invisibility
ReleaseKey(f9)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(1225, 272) # move Mouse to familiar
time.sleep(0.5) 
PressKey(f8) # casting Stoneskin
ReleaseKey(f8)
pyautogui.click()
time.sleep(0.5)
PressKey(f6) # casting Greater Magic Weapon
ReleaseKey(f6)
pyautogui.click()
time.sleep(0.5)
PressKey(f5) #casting Flame Weapon
ReleaseKey(f5)
pyautogui.click()
time.sleep(0.5)
ReleaseKey(shift) # Release Shift Key
time.sleep(0.5)
PressKey(ctrl) # Press Control Key
time.sleep(0.5)
PressKey(f11) # casting Endure Elements
ReleaseKey(f11)
pyautogui.click()
ReleaseKey(ctrl) # Release Control Key
time.sleep(0.5)
pyautogui.moveTo(1225, 80) # Move Back to Charter
time.sleep(0.5)
PressKey(shift) # Press Shift Key
time.sleep(0.5)
PressKey(f6) # casting Greater Magic Weapon
ReleaseKey(f6)
pyautogui.click()
time.sleep(0.5)
PressKey(f5) # casting Flame Weapon
ReleaseKey(f5)
pyautogui.click()
time.sleep(0.5)
PressKey(f4) # casting Magic Circle against Evil
ReleaseKey(f4)
pyautogui.click()
time.sleep(0.5)
PressKey(f3) # casting Shield
ReleaseKey(f3)
# pyautogui.click()
time.sleep(0.5)
PressKey(f2) # casting Greater Stoneskin
ReleaseKey(f2)
time.sleep(0.5)

ReleaseKey(shift) # Release Shift Key

# All Control Buffs Setup
PressKey(ctrl) # Press Control Key

time.sleep(0.5)
PressKey(f10) # casting Premonition
ReleaseKey(f10)
# pyautogui.click()
time.sleep(0.5)
PressKey(f9) # casting Lesser Mind Blank
ReleaseKey(f9)
pyautogui.click()
time.sleep(0.5)
PressKey(f8) # casting Shadow Shield
ReleaseKey(f8)
time.sleep(0.5)
PressKey(f7) # casting Spell Mantle
ReleaseKey(f7)
time.sleep(0.5)
PressKey(f3) # casting True Seeing
ReleaseKey(f3)
time.sleep(0.5)
pyautogui.click()

ReleaseKey(ctrl) # Release Control Key

# End of Script!
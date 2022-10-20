import ctypes
import pyautogui
import time

from directkeys import PressKey, ReleaseKey

SendInput = ctypes.windll.user32.SendInput

# Define variaveis zeradas.

BAS = int(input('Quantos Basic Arrow Shaft ? '))
BAH = int(input('Quantas Basic Arrow Head ? '))
HAH = int(input('Quantas Hooked Arrow Head ? '))
BAD = int(input('Quantas Bladed Arrow Head ? '))
AAH = int(input('Quantas Advanced Arrow Head ? '))
BAF = int(input('Quantos Basic Arrow Fletch ? '))
AAF = int(input('Quantos Advanced Arrow Fletch ? '))
EOF = int(input('Quantas Pocoes de Fogo ? '))
EOE = int(input('Quantas Pocoes de Eletricidade ? '))
EOA = int(input('Quantas Pocoes de Acido ? '))
EOC = int(input('Quantas Pocoes de Gelo ? '))



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


PressKey(n3) # Select poiton options Fletcher
ReleaseKey(n3)
time.sleep(0.2)

pyautogui.moveTo(338, 72)
pyautogui.click()
time.sleep(0.2)

# Compra Basic Arrow Shaft
count = 0
while (count < BAS):   
  count = count + 1
  pyautogui.moveTo(140, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

# Compra Basic Arrow Head
count = 0
while (count < BAH):   
  count = count + 1
  pyautogui.moveTo(29, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

    # Compra Bladed Arrow Head
count = 0
while (count < BAD):   
  count = count + 1
  pyautogui.moveTo(138, 435)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

    # Compra Hooked Arrow Head
count = 0
while (count < HAH):   
  count = count + 1
  pyautogui.moveTo(358, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

    # Compra Advanced Arrow Head
count = 0
while (count < AAH):   
  count = count + 1
  pyautogui.moveTo(170, 435)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

  # Compra Basic Arrow Fletch
count = 0
while (count < BAF):   
  count = count + 1
  pyautogui.moveTo(65, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

  # Compra Advanced Arrow Fletch
count = 0
while (count < AAF):   
  count = count + 1
  pyautogui.moveTo(206, 435)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)


pyautogui.moveTo(190, 70)
pyautogui.click()
time.sleep(0.2)

  # Compra Poção Fogo
count = 0
while (count < EOF):   
  count = count + 1
  pyautogui.moveTo(30, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

  # Compra Poção Eletricidade
count = 0
while (count < EOE):   
  count = count + 1
  pyautogui.moveTo(65, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)

  # Compra Poção Ácido
count = 0
while (count < EOA):   
  count = count + 1
  pyautogui.moveTo(100, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)


  # Compra Poção Gelo
count = 0
while (count < EOC):   
  count = count + 1
  pyautogui.moveTo(135, 465)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(550, 550)
  pyautogui.click()
  time.sleep(0.1)
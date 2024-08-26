

import pyautogui
import time

pyautogui.FAILSAFE = False 

# Espera 2 segundos para dar tempo de ver o mouse se movendo
time.sleep(2)

# Move o mouse para uma posição inicial, por exemplo (100, 100)
pyautogui.moveTo(100, 100, duration=1)

# Move o mouse 10 pixels para baixo, um pixel por vez
for i in range(10):
    pyautogui.moveRel(0, 1, duration=0.1)  # Move 1 pixel para baixo com um pequeno delay

# Função para mover o mouse a cada 3 segundos
def prevent_sleep():
    try:
        while True:
            pyautogui.moveRel(0,80)  # Move o mouse 1 pixel para baixo
            pyautogui.moveRel(0,-80) # Move o mouse 1 pixel para cima, retornando à posição original
            pyautogui.press('ctrl')  # Pressiona a tecla ctrl
            time.sleep(3)            # Espera 3 segundos antes de repetir
    except KeyboardInterrupt:
        print("Interrompido pelo usuário")

# Iniciar a função
prevent_sleep()

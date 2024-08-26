# Localiza o botão usando uma imagem do botão de download
button_location = pyautogui.locateOnScreen('botao.png')

if button_location:
    pyautogui.click(button_location)
else:
    print("Botão não encontrado.")

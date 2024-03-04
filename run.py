# passo a passo do projeto

# Passo 1: Entrar na base de dados da empresa
from time import sleep
import pyautogui as auto

auto.PAUSE = 1

# Pyautogui.click -> clicar em algum lugar
# Pyautogui.write -> Escrever textos
# Pyautogui.click -> Apertar 1 tecla
# Pyautogui.hotkey -> combinação de teclas

# Abrir o navegador (Edge)
auto.press('win')
auto.write('edge')
auto.press('enter')

# Entrar no site
LINK = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
auto.write(LINK)
auto.press('enter')

# Dar uma pausa um pouco maior
sleep(5)

# Passo: 2 Fazer Login
auto.click(x=719, y=442)
auto.write('pythonimpressionador@gmail.com')
auto.press('tab')
auto.write('sua senha aqui')
auto.press('tab')
auto.press('enter')

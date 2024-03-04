# passo a passo do projeto
# Passo 1: Entrar na base de dados da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

from time import sleep
import pyautogui as auto

auto.PAUSE = 0.5

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

# Escrever a senha
auto.press('tab')
auto.write('sua senha aqui')

# Clicar em login
auto.press('tab')
auto.press('enter')

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
# leitor de pdf tabula

import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)


# Passo 4: Cadastrar 1 Produto
# Passo 5: Repetir o processo de cadastro até acabar

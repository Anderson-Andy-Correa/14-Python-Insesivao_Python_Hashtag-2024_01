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
sleep(6)

# Passo: 2 Fazer Login
auto.press('tab')
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
tabela = pandas.read_csv('documentos/produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 Produto
# Para cada linha da minha tabela

colunas = tuple(tabela.columns)
for linha in tabela.index:
    # Clicar no 1º campo
    auto.click(x=724, y=339)

    for coluna in colunas:
        campo = tabela.loc[linha, coluna]
        if not pandas.isna(campo):
            auto.write(str(campo))
        auto.press('tab')
        
    # Enviar
    auto.press('enter')

    # Voltar ao início
    auto.press('home')

# Passo 5: Repetir o processo de cadastro até acabar

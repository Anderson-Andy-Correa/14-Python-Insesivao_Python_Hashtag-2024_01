import pyautogui as auto

auto.PAUSE = 1

auto.press('win')
auto.write('edge')
auto.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
auto.write(link)
auto.click('enter')

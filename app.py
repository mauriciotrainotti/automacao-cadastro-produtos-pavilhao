import pyautogui
from time import sleep

#clicar em produtos
pyautogui.click(61,216, duration=2)
#clicar em produtos novamente
pyautogui.click(53,248,)
#clicar no botao de novo 
pyautogui.click(1260,210, duration=3)
#clicar no gtin
pyautogui.click(208,328, duration=1)
#digitar gtin
pyautogui.write("000")
#clicar no cod. original
pyautogui.press('tab')
#digitar cod. original
pyautogui.write('000')
#clicar no SKU
pyautogui.press('tab')
#digitar SKU
pyautogui.write('000')
#clicar em categoria
pyautogui.press('tab')
pyautogui.press('tab')
#digitar categoria
pyautogui.write('Brindes Empresariais')
pyautogui.press('enter') 
#clicar em nome
pyautogui.press('tab')
#digitar nome  
pyautogui.write('Teste cadastro produto 1')
#clicar em preço/estoque
pyautogui.click(237,241,)
#clicar em unidade de medida
pyautogui.click(131,325, duration=1)
#digitar unidade
pyautogui.write('UN')
pyautogui.press('enter')
#clicar em estoque disponivel
pyautogui.click(673,327, duration=2)
#digitar estoque disponivel
pyautogui.write('1')
#clicar em preço de custo
pyautogui.click(124,452, duration=2)
#digitar preço de custo
pyautogui.write('6,50')
#clicar em preço de venda
pyautogui.press('tab')
#digitar preço de venda
pyautogui.write('10,00')
#clicar em descrição/complemento

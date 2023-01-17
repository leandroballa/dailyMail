import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
link = 'https://github.com/leandroballa/dailyMail/blob/main/Vendas%20-%20Dez.xlsx'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=1208, y=521)
time.sleep(10)
pyautogui.hotkey('alt', 'f4')
df = pd.read_excel(r'C:\Users\leand\Downloads\Vendas - Dez.xlsx')
#print(df)
fat = df['Valor Final'].sum()
qtde = df['Quantidade'].sum()
print(
    f'O faturamento foi de R$ {fat:.2f}\n'
    f'A quantidade de produtos vendidos foi de {qtde}'
)
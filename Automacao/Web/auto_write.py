from time import sleep
import pyautogui

# coding = utf-8
sleep(2)

message = ("""Hoje nós da Do Lixo Ao Luxo lançamos nosso maior projeto, a lab Dll 🔥 https://www.instagram.com/labdll_ofc/""")

#message_trans = message.decode('utf-8')
#final = message_trans.encode('cp1250')

pyautogui.typewrite(message, interval=0.05)
pyautogui.press('enter')


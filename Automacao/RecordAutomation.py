"""
O codigo é iniciado a partir das teclas no teclado
Ele grava em um arquivo grava.txt 
Os comando no mouse e teclado no padrao da biblioteca pynput
O objetivo é utilizar essa saida para automatizar qualquer tipo de processo mais rapidamente
"""

from pynput.mouse import Button, Listener
from pynput.keyboard import Key,Controller

arq = open('grava.txt','w')
texto = """ Teste de gravacao em arquivo """

lista = []


def Click(x,y, button, pressed):
    print (x,y,button,pressed)
    if not pressed: 
        return False

def Move(x,y):
    print (x,y)

with Listener(on_click=Click, on_move=Move) as listener:
    texto = listener.join()
    

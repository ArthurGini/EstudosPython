from pynput.keyboard import Key,Controller

key = Controller()
key.press('1')
key.release('1')

key.type('Vai se fuder')

key.press(Key.cmd)
key.release(Key.cmd)

#Salva automaticamente o projeto
with key.pressed(Key.ctrl):
    key.press('s')
    key.release('s')

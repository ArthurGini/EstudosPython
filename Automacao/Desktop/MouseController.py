from pynput.mouse import Button, Controller

mouse = Controller()

#print (mouse.position)

mouse.positon = (0,600)
mouse.move(150,0)
mouse.click(Button.left, 2)
#clicka no mouse e fica 
mouse.press(Button)
mouse.release(Button.left)


mouse.scroll()
from pynput.mouse import Button, Listener

def Click(x,y, button, pressed):
    print (x,y,button,pressed)
    if not pressed: 
        return False

def Move(x,y):
    print (x,y)

#listener = Listener(on_click=Click, on_move=Move, on_scroll=Scroll)
#listener.start()
#listener.join()
#listener.stop()

with Listener(on_click=Click, on_move=Move) as listener:
    listener.join()

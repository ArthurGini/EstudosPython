from pynput.keyboard import Listener, Key

def press(Key):
    print (Key)

def release(key):
    if key == Key.ctrl:
        return False

with Listener(on_pressed=press, on_release=release) as listener:
    listener.join()


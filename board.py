import keyboard
def activateKeys():
    keyboard.remap_key('e', 'w')
    keyboard.remap_key('s', 'a')
    keyboard.remap_key('d', 's')
    keyboard.remap_key('f', 'd')

def deactivateKeys():
    keyboard.unhook_all()

if __name__ == '__main__':
    while True:
        activateKeys()
        keyboard.wait('f8', suppress=True)
        deactivateKeys()
        keyboard.wait('f8', suppress=True)

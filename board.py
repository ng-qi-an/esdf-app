import keyboard
from store import loadConfig
from state import state
from PIL import Image
from resourcePath import resource_path

hooks = []

def activateKeys():
    global hooks
    config = loadConfig()
    preset = [x for x in config['presets'] if x['active']] 
    if len(preset) == 0:
        return
    deactivateKeys()
    for key in preset[0]['keys']:
        if key['src'] and key['dst']:
            hooks.append(keyboard.remap_key(key['src'].lower(), key['dst'].lower()))

    state.icon.icon = Image.open(resource_path('public/esdfEnabled.ico'))
    print("[BOARD] Key mappings activated")

def deactivateKeys():
    global hooks
    print("[BOARD] Key mappings deactivated")
    for hook in hooks:
        keyboard.unhook(hook)
    hooks = []
    state.icon.icon = Image.open(resource_path('public/esdfDisabled.ico'))

def registerHotkeys():
    def toggleKeys():
        if state.enabledWhen == "always":
            deactivateKeys()
            state.enabled = False
            state.enabledWhen = "never"
        elif state.enabledWhen == "never":
            state.enabledWhen = "always"
            activateKeys()
            state.enabled = True
        elif state.enabledWhen == "selectedGames":
            if state.enabled:
                deactivateKeys()
                state.enabled = False
            else:
                activateKeys()
                state.enabled = True
    keyboard.add_hotkey('f8', toggleKeys, suppress=True)

if __name__ == '__main__':
    while True:
        activateKeys()
        keyboard.wait('f8', suppress=True)
        deactivateKeys()
        keyboard.wait('f8', suppress=True)

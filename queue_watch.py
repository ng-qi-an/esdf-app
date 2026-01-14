from state import state
from board import deactivateKeys, activateKeys
def watch_queue(queue):
    while True:
        try:
            cmd = queue.get(timeout=0.5)  # Non-blocking with timeout
            
            if cmd["action"] == "saved_settings":
                state.selectedGames = cmd["settings"]['selectedGames']
                state.enabledWhen = cmd['settings']['enabledWhen']
                if state.enabledWhen == "always":
                    activateKeys()
                elif state.enabledWhen == "never":
                    deactivateKeys()
                elif state.enabledWhen == "selectedGames":
                    deactivateKeys()
                print("[QUEUE] Reloaded settings and keybinds")
        except:
            pass  # No message, continue
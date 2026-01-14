import time
import win32.win32gui as win32gui
import win32.win32process as win32process
import psutil
from state import state
from board import activateKeys, deactivateKeys

def get_foreground_exe():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return psutil.Process(pid).name()
    except:
        return None

def watch():    
    print("[WATCH] Game watcher started")
    print(f"[WATCH] Selected games: {state.selectedGames}")
    timeElapsed = 0
    isEnabledNow = False
    while True:
        if state.enabledWhen == "selectedGames":
            exe = get_foreground_exe()
            if exe in state.selectedGames:
                if not state.enabled and isEnabledNow == False:
                    print("[WATCH] Activating keybinds...")
                    state.enabled = True
                    isEnabledNow = True
                    activateKeys()
            else:
                isEnabledNow = False
                if state.enabled:
                    print("[WATCH] Deactivating keybinds...")
                    state.enabled = False
                    deactivateKeys()
        time.sleep(0.2)
        timeElapsed += 0.2

if __name__ == "__main__":
    state.enabled = True
    watch()

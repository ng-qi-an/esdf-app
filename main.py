import multiprocessing
import sys
import threading
from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem
import webview
from api import API
from monitor import beginMonitor
from store import checkConfig
from board import activateKeys, registerHotkeys
from state import state
from game_watch import watch
from queue_watch import watch_queue
from pathlib import Path
from resourcePath import resource_path



# Adapted from pywebview pystray example
if sys.platform == 'darwin':
    ctx = multiprocessing.get_context('spawn')
    Process = ctx.Process
    Queue = ctx.Queue
else:
    Process = multiprocessing.Process
    Queue = multiprocessing.Queue

action_queue = None  # Will be initialized in main

def create_settings(queue):
    api = API(queue)
    window = webview.create_window(
        title='ESDF Settings', 
        url=resource_path('index.html'),
        width=900,
        height=600,
        min_size=(400, 400),
        background_color='#000000',
        js_api=api
    )
    webview.start()


webview_process = None

def on_open():
    global webview_process, action_queue
    if not webview_process or not webview_process.is_alive():
        webview_process = Process(target=create_settings, args=(action_queue,))
        webview_process.start()

def on_exit(icon, item):
    icon.stop()

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Must be first line in __main__ for PyInstaller
    action_queue = Queue()  # Initialize queue only in main process
    #threading.Thread(name="monitor", target=beginMonitor, daemon=True).start() # Activates the activity monitor
    menu = Menu(MenuItem('Open settings', on_open), MenuItem('Quit', on_exit))
    image = Image.open(resource_path('public/esdfDisabled.ico'))
    icon = Icon("ESDF", title='ESDF', icon=image, menu=menu)
    state.icon = icon

    config = checkConfig()
    print(f"[MAIN] Enabled: {config['enabledWhen']}")
    state.enabledWhen = config['enabledWhen']
    if config['enabledWhen'] == "always":
        state.enabled = True
        icon.icon = Image.open(resource_path('public/esdfEnabled.ico'))
        activateKeys()
    registerHotkeys()
    print("[MAIN] Hotkeys registered")
    state.selectedGames = config.get("selectedGames", [])
    threading.Thread(name="game_watch", target=watch, daemon=True).start() # Activates game watch monitor
    threading.Thread(name="queue_watch", target=watch_queue, args=(action_queue,), daemon=True).start() # Activates queue watch monitor
    
    icon.run()
    print("[MAIN] Closing application!")
    if webview_process and webview_process.is_alive():
        webview_process.terminate()
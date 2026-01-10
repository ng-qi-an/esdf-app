import multiprocessing
import sys
from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem
import webview
from api import API

# Adapted from pywebview pystray example
if sys.platform == 'darwin':
    ctx = multiprocessing.get_context('spawn')
    Process = ctx.Process
    Queue = ctx.Queue
else:
    Process = multiprocessing.Process
    Queue = multiprocessing.Queue

def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)
    return image

def create_settings():
    window = webview.create_window(
        title='ESDF Settings', 
        url='index.html',
        width=900,
        height=600,
        min_size=(400, 400),
        background_color='#000000',
        js_api=API()
    )
    webview.start(debug=True)


webview_process = None
def on_open():
    global webview_process
    webview_process = Process(target=create_settings)
    if not webview_process.is_alive():
        webview_process.start()

def on_exit(icon, item):
    icon.stop()

if __name__ == '__main__':
    menu = Menu(MenuItem('Open settings', on_open), MenuItem('Quit', on_exit))
    icon = Icon('ESDF', create_image(64, 64, 'black', 'white'), menu=menu)
    icon.run()
    webview_process.terminate()
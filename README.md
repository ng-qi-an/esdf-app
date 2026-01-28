<img width="3780" height="1890" alt="Add a heading" src="https://github.com/user-attachments/assets/e349d4eb-379c-4be5-8d54-2a66e07acf19" />

# How to use
1. Download the latest exe from [Github Releases](https://github.com/ng-qi-an/esdf-app/releases)
2. Double-click it to open. Dismiss any security prompts if required
3. Open the system tray and pin it to the taskbar
   - Click the arrow on the bottom right that is facing up
   - A menu should open, containing a black ESDF icon
   - Drag the ESDF icon to the taskbar
4. Right-click the icon to quit the app or configure settings at any time.
5. `F8` can be used to toggle on and off states, reflected by the red or green outline around the esdf icon.
6. ESDF will launch automatically on boot by default in the background. No action is needed on restart unless otherwise configured.

# Technologies
ESDF was made with **Python** and **Web technologies**. It uses pystray and the keyboard library to deliver core functionally, such as key supression and remaps. The settings panel was made with PyWebview, opening a html file like a native app that offers bridging between JS and Python APIs.

This approach allowed me to speed up development time significantly, but may come at a minimal cost of performance or polish. Web apps are typically more resource-intensive and do not feel as smooth as native UIs. However, learning a widget library like Tkinter or PyQT would take much longer. Perhaps in the future, ESDF will be revised for native UIs.

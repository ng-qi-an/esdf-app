import sys
from store import addStartup, removeStartup, saveConfig, loadConfig
class API():
    def __init__(self):
        print("API initialized")
        
    def version(self):
        response = {'message': f'Hello from Python {sys.version}'}
        return response
    
    def getConfig(self):
        print("[API] getConfig called")
        config = loadConfig()
        return config
    
    def saveSettings(self, settings):
        print(f"[API] saveSettings called with {settings}")
        config = loadConfig()
        config.update(settings)
        saveConfig(config)
        return {'status': 'success', 'settings': settings}
    
    def setStartup(self, runOnStartup):
        print(f"[API] setStartup called with {runOnStartup}")
        if runOnStartup:
            addStartup()
        else:
            removeStartup()
        return {'status': 'success', 'runOnStartup': runOnStartup}
import os
from pathlib import Path
import json
import sys

# Get app config directory
appdata = os.getenv("APPDATA")
config_dir = Path(appdata, "esdf")
config_dir.mkdir(parents=True, exist_ok=True)
config_file = Path(config_dir, "settings.json")

# Meant for adding and removing startup files
exe_location = os.path.dirname(sys.executable)
startup_dir = Path(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
bat_path = Path(startup_dir, "ESDF.bat")

def addStartup():
    if not bat_path.exists():
        with open(bat_path, 'w') as f:
            f.write(f'@echo off\nstart "" "{exe_location}"')

def removeStartup():
    if bat_path.exists():
        bat_path.unlink()

def saveConfig(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

def loadConfig():
    if config_file.exists():
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        return {}

def checkConfig():
    print("[STORE] Checking config file")
    if not config_file.exists():
        print("[STORE] Creating default config file")
        default_config = {
            "runOnStartup": True,
            "enabled": "selectedGames",
            "selectedGames": [],
            "presets": [
            ]
        }
        saveConfig(default_config)
    
    config = loadConfig()
    if config.get("runOnStartup", False):
        addStartup()
    else:
        removeStartup()
    print("[STORE] Config check complete!")

if __name__ == '__main__':
    config = loadConfig()
    print(config)
    if config.get("runOnStartup", False):
        addStartup()
    else:
        removeStartup()
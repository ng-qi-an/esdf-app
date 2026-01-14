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
exe_path = sys.executable
startup_dir = Path(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
bat_path = Path(startup_dir, "ESDF.bat")

def addStartup():
    with open(bat_path, 'w') as f:
        f.write(f'@echo off\nstart "" "{exe_path}"')

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
            "enabledWhen": "never",
            "selectedGames": [],
            "presets": [{
                "name": "ESDF",
                "active": True,
                "keys": [
                    {
                        "src": "E",
                        "dst": "W"
                    },
                    {
                        "src": "S",
                        "dst": "A"
                    },
                    {
                        "src": "D",
                        "dst": "S"
                    },
                    {
                        "src": "F",
                        "dst": "D"
                    },
                    {
                        "src": "R",
                        "dst": "E"
                    },
                    {
                        "src": "T",
                        "dst": "R"
                    },
                    {
                        "src": "Y",
                        "dst": "T"
                    },
                    {
                        "src": "W",
                        "dst": "Q"
                    }
                ]
            }]
        }
        addStartup()
        saveConfig(default_config)
        return default_config
    
    config = loadConfig()
    if config.get("runOnStartup", False):
        addStartup()
    else:
        removeStartup()
    print("[STORE] Config check complete!")
    return config

if __name__ == '__main__':
    config = loadConfig()
    print(config)
    if config.get("runOnStartup", False):
        addStartup()
    else:
        removeStartup()
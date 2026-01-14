# Shared state across modules
class State:
    def __init__(self):
        self.forceDisabled = False
        self.enabled = False
        self.icon = None
        self.enabledWhen = "manually"
        self.selectedGames = []

# Single instance shared by all modules
state = State()

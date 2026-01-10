import sys
class API():
    def __init__(self):
        print("API initialized")
        
    def version(self):
        response = {'message': f'Hello from Python {sys.version}'}
        return response
    
    
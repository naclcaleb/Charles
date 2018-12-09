from events import Registry
class Driver:
    def __init__(self, name):
        self.name = name
    def add_event_listener(self,event, function):
        Registry.add(self.name, event, function)
    def remove_event_listener(self, event):
        Registry.remove(self.name,event)
    def send(self, data):
        pass
    def get(self,data=[]):
        pass
    
        
    

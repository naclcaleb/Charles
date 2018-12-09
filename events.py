class Event:
    def __init__(self, name):
        self.name = name
    def trigger(self):
        try:
            dispatch(self.name)
            return True
        else:
            return False
class Registry:
    def __init__(self):
        pass
    def add(self,device, event, function):
        handler.add_listener(device, event, function)
    def remove(self, device,event):
        handler.remove_listener(device,event)
class Handler:
    def __init__(self):
        self.listeners = []
    def add_listener(device, event, callback):
        self.listeners.append({"device":device,"event":event,"callback":callback})
    def remove_listener(device,event):
        self.listeners = [ x for x in self.listeners if (x.device != device) or (x.event != event) ]
    def handle(self,event):
        for i in self.listeners:
            if i.event == event:
                i.callback()
        
          


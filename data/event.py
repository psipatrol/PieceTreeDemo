class EventDispatcher:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def trigger(self, event):
        for listener in self.listeners:
            listener.trigger(event)
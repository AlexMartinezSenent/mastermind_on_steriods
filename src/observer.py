class Observer:
    observers = []

    def __init__(self):
        Observer.observers.append(self)
        self.observables = {}

    def observe(self, event_name, callback):
        self.observables[event_name] = callback
from observer import Observer
from event import Event

# from main import guess_number

class Guess(Observer):
    max_length = 8
    
    def __init__(self):
        # self.try_number = try_number
        self.number = []
        Observer.__init__(self)
        self.observe("key_pressed",self.callback)


    def callback(self, data):
        global guess_number
        if data == "enter":
            # TODO send number to slot
            if not self.number:
                pass
            elif len(self.number) > self.max_length:
                print(int("".join(self.number[:self.max_length])))
                Event("new_guess",self)
                
            else:
                print(int("".join(self.number)))
                Event("new_guess",self)
                
            self.number = []
        elif data == "delete":
            if not self.number:
                pass
            else:
                self.number.pop()
        else:
            if len(self.number) >= 8:
                pass
            else:
                self.number.append(data)
        Event("number_update",self.number)

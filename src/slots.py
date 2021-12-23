import pygame
from observer import Observer
from event import Event


class Slot():
    def __init__(self, guess, try_number, passcode):
        self.guess = guess
        self.try_number = try_number
        self.bulbs = self.get_bulbs(passcode)

    def get_bulbs(self,passcode):
        bulbs = [0,0,0,0,0,0,0,0]
        for ind, val in enumerate(self.guess):
            if val == passcode[ind]:
                bulbs[ind] = 2
        for ind, val in enumerate(self.guess):
            if not bulbs[ind] == 2:
                if val in passcode:
                    bulbs[ind] = 1
                    if self.guess.count(val) >= passcode.count(val):
                        indeces_pass = [i for i, x in enumerate(passcode) if x == val]
                        indeces_guess = [j for j, y in enumerate(self.guess[:ind]) if y == val]
                        if sum(bulbs[ii] for ii in indeces_pass)+sum(bulbs[jj] for jj in indeces_guess)*2 >= passcode.count(val)*2:
                            bulbs[ind] = 0
                    if val in self.guess[:ind] and self.guess[:ind].count(val) >= passcode.count(val):
                        bulbs[ind] = 0
        if sum(bulbs) == len(bulbs)*2:
            Event("solved",bulbs)
        return bulbs

class Slots(Observer):

    def __init__(self, screen, passcode):
        self.slot_pos = 0
        self.max_slots = 6
        self.screen = screen
        self.passcode = passcode
        self.try_number = 1
        self.try_font = pygame.font.Font(None, 32)
        self.guess_font = pygame.font.Font(None, 60)
        self.try_location = (53,218)
        self.try_y_spacing = 80
        self.guess_location = (96,218)
        self.guess_x_spacing = 46
        self.guess_y_spacing = 79
        self.bulb_location = (466,225)
        self.bulb_x_spacing = 33.5
        self.bulb_y_spacing = 81
        self.bulb_radius = 11
        self.init_slots()
        Observer.__init__(self)
        self.observe("new_guess", self.callback)

    def callback(self, data):
        self.slots[self.slot_pos] = Slot(data.number, self.try_number, self.passcode)
        self.try_number += 1
        self.update_slot_head()

    def init_slots(self):
        self.slots = [None,None,None,None,None,None]
    
    def update_slot_head(self):
        self.slot_pos += 1
        if self.slot_pos >= self.max_slots:
            self.slot_pos = 0
    
    def draw_slots(self):
        for i, slot in enumerate(self.slots):
            if not slot == None:
                self.draw_try(slot,i)
                self.draw_number(slot,i)
                self.draw_bulbs(slot,i)

    def draw_try(self, slot, h):
        if slot.try_number < 10:
            try_number_str = "0"+str(slot.try_number)
        else: try_number_str = str(slot.try_number)
        rend = self.try_font.render(try_number_str, True, (10,10,10))
        self.screen.blit(rend,(self.try_location[0],self.try_location[1]+self.try_y_spacing*h))

    def draw_number(self, slot, h):
        for j, number in enumerate(slot.guess):
            rend = self.guess_font.render(str(number), True, (10,10,10))
            self.screen.blit(rend,(self.guess_location[0]+self.guess_x_spacing*j,self.guess_location[1]+self.guess_y_spacing*h))

    def draw_bulbs(self, slot, h):
        for k,state in enumerate(slot.bulbs):
            if state == 1:
                pygame.draw.circle(self.screen, (255,0,0), (self.bulb_location[0]+self.bulb_x_spacing*k,self.bulb_location[1]+self.bulb_y_spacing*h), self.bulb_radius, 0)
            elif state == 2:
                pygame.draw.circle(self.screen, (255,255,255), (self.bulb_location[0]+self.bulb_x_spacing*k,self.bulb_location[1]+self.bulb_y_spacing*h), self.bulb_radius, 0)

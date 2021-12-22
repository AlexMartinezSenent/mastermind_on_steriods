import pygame 
# from main import screen
from observer import Observer

class LCD(Observer):

    def __init__(self, screen):
        Observer.__init__(self)
        self.observe("number_update", self.callback)
        self.font = pygame.font.Font(None, 80)
        self.location = (740,200)
        self.number = []
        self.screen = screen


    def callback(self, data):
        self.number = data
        self.draw_number()
        
    def draw_number(self):
        global screen
        if not self.number:
            pass
        else:
            self.rend = self.font.render("".join(self.number), True, (0,70,0))
            self.screen.blit(self.rend, self.location)
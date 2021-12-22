import pygame
from observer import Observer
import random 

class Passcode(Observer):
    def __init__(self,screen):
        decimal = round(random.random(),8)
        self.passcode_string = str(decimal)[2:]
        self.passcode = list(self.passcode_string)
        self.font = pygame.font.Font(None, 100)
        self.location = (94,92)
        self.spacing = 76
        self.screen = screen
        

    def draw_question_marks(self):
        global screen
        self.rend = self.font.render("?", True, (225,255,210))
        for i in range(len(self.passcode_string)):
            self.screen.blit(self.rend, (self.location[0]+self.spacing*i,self.location[1]))

    def draw_passcode(self):
        global screen
        for index, number in enumerate(self.passcode):
            self.rend = self.font.render(str(number), True, (225,255,210))
            self.screen.blit(self.rend, (self.location[0]+self.spacing*index,self.location[1]))

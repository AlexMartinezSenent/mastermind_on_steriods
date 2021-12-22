import pygame

import numpy as np
import random 
import time
import keyboard
from guess import Guess
from display import LCD

pygame.init()


background = pygame.image.load('visuals/background.png')
pygame.display.set_caption("MasterNumber")
screen = pygame.display.set_mode((1080, 720))

menu_font = pygame.font.Font(None, 72)
# icon = pygame.image.load('elephant_icon.png')
# pygame.display.set_icon(icon)
keys = keyboard.keyboard_init(screen)
guess_number = 1
Guess(guess_number)
lcd = LCD(screen)

running = True
while running:
    screen.blit(background,(0,0))
    # pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for key in keys:
        key.update_key()
    lcd.draw_number()
    pygame.display.update()
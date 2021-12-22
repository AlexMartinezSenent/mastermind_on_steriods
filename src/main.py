import pygame
import numpy as np
import random 
import time
import keyboard
from guess import Guess

pygame.init()

screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('visuals/background.png')
pygame.display.set_caption("MasterNumber")

menu_font = pygame.font.Font(None, 72)
# icon = pygame.image.load('elephant_icon.png')
# pygame.display.set_icon(icon)
keys = keyboard.keyboard_init(screen)
Guess(1)

running = True
while running:
    screen.blit(background,(0,0))
    # pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for key in keys:
        key.update_key()
    pygame.display.update()
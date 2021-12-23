import pygame
import numpy as np
import random 
import time
import keyboard
from guess import Guess
from display import LCD
from passcode import Passcode
from slots import Slots


pygame.init()


background = pygame.image.load('visuals/background.png')
win_overlay = pygame.image.load('visuals/win_overlay.png')
pygame.display.set_caption("MasterNumber")
screen = pygame.display.set_mode((1080, 720))

menu_font = pygame.font.Font(None, 72)
# icon = pygame.image.load('elephant_icon.png')
# pygame.display.set_icon(icon)
keys = keyboard.keyboard_init(screen)
passcode = Passcode(screen)
slots = Slots(screen,passcode.passcode)

Guess()

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
    if passcode.solved:
        passcode.draw_passcode()
        screen.blit(win_overlay,(0,0))
    else:
        passcode.draw_question_marks()
    slots.draw_slots()
    pygame.display.update()
import pygame


def keyboard_init(screen):
    keys = [Key("0",(838,720-80-61),screen),
            Key("1",(743,720-80-156),screen),
            Key("2",(838,720-80-156),screen),
            Key("3",(933,720-80-156),screen),
            Key("4",(743,720-80-251),screen),
            Key("5",(838,720-80-251),screen),
            Key("6",(933,720-80-251),screen),
            Key("7",(743,720-80-346),screen),
            Key("8",(838,720-80-346),screen),
            Key("9",(933,720-80-346),screen),
            Key("enter",(933,720-80-61),screen),
            Key("delete",(743,720-80-61),screen)
            ]
    return keys



class Key:
    def __init__(self, value, position, screen):
        self.value = value
        self.position = position
        self.screen = screen
        self.image_rest_location = "visuals/key_"+ self.value + ".png"
        self.image_pressed_location = "visuals/key_"+ self.value + "_pressed.png"
        self.image_rest = pygame.image.load(self.image_rest_location)
        self.image_pressed = pygame.image.load(self.image_pressed_location)
        self.image_to_display = self.image_rest
        self.rect = self.image_to_display.get_rect()
        self.rect.topleft = self.position
        self.antibounce = False
        self.update_key()

    def is_pressed(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            # TODO Event goes here
            self.antibounce = True
            return True
        else: 
            self.antibounce = False
            return False

    def get_image(self):
        if self.is_pressed():
            self.image_to_display = self.image_pressed
        else:
            self.image_to_display = self.image_rest
        
    def update_key(self):
        self.get_image()
        self.screen.blit(self.image_to_display,self.position)

